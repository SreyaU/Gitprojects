"""
PyPerf - A Tkinter-based frontend for iperf3 (jPerf-style)
Author: sreya + ChatGPT Tech Support
Version: 1.1
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import queue
import time
import os
import signal

APP_TITLE = "PyPerf - iperf3 GUI"
APP_SIZE = "1000x700"


class PyPerfApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(APP_SIZE)
        self.minsize(900, 600)
        self.configure(bg="#f5f6f8")

        self.worker_q = queue.Queue()
        self.iperf_process = None

        self._create_style()
        self._create_widgets()
        self._layout_widgets()
        self._bind_shortcuts()
        self._poll_worker_queue()

    # ------------------------------------------------------------
    # Style
    # ------------------------------------------------------------
    def _create_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TLabel", background="#f5f6f8", font=("Segoe UI", 10))
        style.configure("TButton", padding=6)
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))

    # ------------------------------------------------------------
    # Widgets
    # ------------------------------------------------------------
    def _create_widgets(self):
        # Header
        self.header = ttk.Frame(self, padding=8)
        self.lbl_title = ttk.Label(self.header, text="PyPerf - Network Throughput Test", style="Header.TLabel")

        # Config panel
        self.config_frame = ttk.LabelFrame(self, text="Configuration", padding=8)
        self.mode = tk.StringVar(value="client")
        self.protocol = tk.StringVar(value="tcp")

        self.rb_client = ttk.Radiobutton(self.config_frame, text="Client", variable=self.mode, value="client", command=self._on_mode_change)
        self.rb_server = ttk.Radiobutton(self.config_frame, text="Server", variable=self.mode, value="server", command=self._on_mode_change)

        self.lbl_host = ttk.Label(self.config_frame, text="Server IP:")
        self.ent_host = ttk.Entry(self.config_frame)
        self.ent_host.insert(0, "127.0.0.1")

        self.lbl_port = ttk.Label(self.config_frame, text="Port:")
        self.ent_port = ttk.Entry(self.config_frame)
        self.ent_port.insert(0, "5201")

        self.lbl_protocol = ttk.Label(self.config_frame, text="Protocol:")
        self.rb_tcp = ttk.Radiobutton(self.config_frame, text="TCP", variable=self.protocol, value="tcp")
        self.rb_udp = ttk.Radiobutton(self.config_frame, text="UDP", variable=self.protocol, value="udp")

        self.lbl_duration = ttk.Label(self.config_frame, text="Duration (sec):")
        self.ent_duration = ttk.Entry(self.config_frame)
        self.ent_duration.insert(0, "10")

        self.lbl_parallel = ttk.Label(self.config_frame, text="Parallel Streams:")
        self.ent_parallel = ttk.Entry(self.config_frame)
        self.ent_parallel.insert(0, "1")

        self.btn_start = ttk.Button(self.config_frame, text="Start", command=self.on_start)
        self.btn_stop = ttk.Button(self.config_frame, text="Stop", command=self.on_stop, state="disabled")

        # Console output
        self.console_frame = ttk.LabelFrame(self, text="Console Output", padding=8)
        self.txt_console = scrolledtext.ScrolledText(
            self.console_frame, wrap="word", height=10, state="disabled", font=("Consolas", 10)
        )

        # Graph placeholder
        self.graph_frame = ttk.LabelFrame(self, text="Throughput Graph (Placeholder)", padding=8)
        self.graph_placeholder = ttk.Label(
            self.graph_frame, text="Graph area — to be replaced with matplotlib chart later.", foreground="gray"
        )

    # ------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------
    def _layout_widgets(self):
        self.header.pack(fill="x")
        self.lbl_title.pack(side="left", padx=4, pady=4)

        self.config_frame.pack(fill="x", padx=8, pady=8)
        f = self.config_frame

        self.rb_client.grid(row=0, column=0, padx=4, pady=4, sticky="w")
        self.rb_server.grid(row=0, column=1, padx=4, pady=4, sticky="w")

        self.lbl_host.grid(row=1, column=0, padx=4, pady=4, sticky="e")
        self.ent_host.grid(row=1, column=1, padx=4, pady=4, sticky="w")
        self.lbl_port.grid(row=1, column=2, padx=4, pady=4, sticky="e")
        self.ent_port.grid(row=1, column=3, padx=4, pady=4, sticky="w")

        self.lbl_protocol.grid(row=2, column=0, padx=4, pady=4, sticky="e")
        self.rb_tcp.grid(row=2, column=1, padx=4, pady=4, sticky="w")
        self.rb_udp.grid(row=2, column=2, padx=4, pady=4, sticky="w")

        self.lbl_duration.grid(row=3, column=0, padx=4, pady=4, sticky="e")
        self.ent_duration.grid(row=3, column=1, padx=4, pady=4, sticky="w")
        self.lbl_parallel.grid(row=3, column=2, padx=4, pady=4, sticky="e")
        self.ent_parallel.grid(row=3, column=3, padx=4, pady=4, sticky="w")

        self.btn_start.grid(row=4, column=0, padx=6, pady=6, sticky="w")
        self.btn_stop.grid(row=4, column=1, padx=6, pady=6, sticky="w")

        for i in range(4):
            f.grid_columnconfigure(i, weight=1)

        self.console_frame.pack(fill="both", expand=True, padx=8, pady=4)
        self.txt_console.pack(fill="both", expand=True)

        self.graph_frame.pack(fill="both", expand=True, padx=8, pady=4)
        self.graph_placeholder.pack(expand=True, fill="both")

    # ------------------------------------------------------------
    # Shortcuts
    # ------------------------------------------------------------
    def _bind_shortcuts(self):
        self.bind_all("<Control-q>", lambda e: self.destroy())

    # ------------------------------------------------------------
    # UI Mode Change Handler
    # ------------------------------------------------------------
    def _on_mode_change(self):
        """Enable/disable fields based on mode selection."""
        mode = self.mode.get()
        if mode == "server":
            self.ent_host.config(state="disabled")
            self.lbl_host.config(foreground="gray")
            self.ent_duration.config(state="disabled")
            self.lbl_duration.config(foreground="gray")
        else:
            self.ent_host.config(state="normal")
            self.lbl_host.config(foreground="black")
            self.ent_duration.config(state="normal")
            self.lbl_duration.config(foreground="black")

    # ------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------
    def log(self, msg):
        self.txt_console.config(state="normal")
        self.txt_console.insert(tk.END, msg + "\n")
        self.txt_console.see(tk.END)
        self.txt_console.config(state="disabled")

    # ------------------------------------------------------------
    # Start / Stop Handlers
    # ------------------------------------------------------------
    def on_start(self):
        mode = self.mode.get()
        host = self.ent_host.get()
        port = self.ent_port.get()
        proto = self.protocol.get()
        duration = self.ent_duration.get()
        parallel = self.ent_parallel.get()

        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.txt_console.config(state="normal")
        self.txt_console.delete("1.0", tk.END)
        self.txt_console.config(state="disabled")

        self.log(f"Mode: {mode.upper()} | Host: {host}:{port} | Protocol: {proto.upper()} | Duration: {duration}s | Streams: {parallel}")
        self.log("Starting iperf3 test...\n")

        thread = threading.Thread(
            target=self._run_iperf3, args=(mode, host, port, proto, duration, parallel), daemon=True
        )
        thread.start()

    def on_stop(self):
        if self.iperf_process:
            self.log("Stopping iperf3 process...")
            try:
                if os.name == "nt":
                    self.iperf_process.send_signal(signal.CTRL_BREAK_EVENT)
                else:
                    self.iperf_process.terminate()
            except Exception as e:
                self.log(f"Error stopping process: {e}")
            self.iperf_process = None
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")

    # ------------------------------------------------------------
    # Iperf3 Runner
    # ------------------------------------------------------------
    def _run_iperf3(self, mode, host, port, proto, duration, parallel):
        cmd = ["iperf3"]
        if mode == "server":
            cmd.append("-s")
        else:
            cmd += ["-c", host, "-p", port, "-t", duration, "-P", parallel]
            if proto.lower() == "udp":
                cmd.append("-u")

        self.log(f"Executing command: {' '.join(cmd)}\n")

        try:
            self.iperf_process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True
            )

            for line in self.iperf_process.stdout:
                self.worker_q.put(("log", line.strip()))

            self.iperf_process.wait()
            self.worker_q.put(("done", "iperf3 test finished."))

        except FileNotFoundError:
            self.worker_q.put(("log", "Error: iperf3 not found. Please install it and ensure it is in PATH."))
        except Exception as e:
            self.worker_q.put(("log", f"Error: {e}"))
        finally:
            self.iperf_process = None

    # ------------------------------------------------------------
    # Worker Queue
    # ------------------------------------------------------------
    def _poll_worker_queue(self):
        try:
            while True:
                typ, data = self.worker_q.get_nowait()
                if typ == "log":
                    self.log(data)
                elif typ == "done":
                    self.log(data)
                    self.btn_start.config(state="normal")
                    self.btn_stop.config(state="disabled")
        except queue.Empty:
            pass
        self.after(200, self._poll_worker_queue)


if __name__ == "__main__":
    app = PyPerfApp()
    app.mainloop()
