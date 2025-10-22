import tkinter as tk
from tkinter import Toplevel

# Create the main application window
def create_main_window():
    global root
    root = tk.Tk()
    root.title("Iperf3 GUI")
    root.geometry("500x350")  # Set window size (width x height)


    # Add a label
    label = tk.Label(root, text="Welcome to GUI", font=("Arial", 14))
    label.pack(anchor="w",pady=20)  # Add padding around the label

    Tools = ["Ping", "Traceroute", "Iperf"]

    label = tk.Label(
        root,
        text=f"Selected Tool: {Tools[0]}",
    )
    label.pack(anchor="w", padx=10, pady=10)

    def selection():
        label.config(text=f"Selected: {variable.get()}")

    variable = tk.StringVar(root, f"{Tools[0]}")
    # global selected_tool
    # selected_tool = variable.get()

    for tool in Tools:
        tk.Radiobutton(
            root,
            text=tool,
            variable=variable,
            value=tool,
            command=selection,
        ).pack(anchor="w", padx=10, pady=5)

    # Button to open tool window
    tk.Button(root, text="Proceed>>", command=open_tool_window).pack(pady=40)
    root.mainloop()

def open_tool_window():
    #close the main window
    # root.destroy()
    root.withdraw()
    # Create the new window for selected tool
    tool_window = Toplevel(root)
    tool_window.title("new window")
    tool_window.geometry("400x300")
    tool_window.protocol("WM_DELETE_WINDOW", lambda: [tool_window.destroy(), root.deiconify()])
    
    # Disable main window interaction
    tool_window.grab_set()
    
    # Optional: place it centered relative to root
    tool_window.transient(root)

    # Add content
    tk.Label(tool_window, text="This is a modal window").pack(pady=20)
    tk.Button(tool_window, text="Close", command=tool_window.destroy).pack(pady=10)
    # tk.Button(tool_window, text="Run", command=tool_window.destroy).pack(pady=10)

    # Make sure the window is focused
    tool_window.focus_set()
    tool_window.wait_window()  # Wait until closed


    # Button to return to the main window
    def back_to_main():
        tool_window.destroy()
        create_main_window()

    tk.Button(tool_window, text="<<Previous", command=back_to_main).pack(pady=20)

    tool_window.mainloop()

create_main_window()


