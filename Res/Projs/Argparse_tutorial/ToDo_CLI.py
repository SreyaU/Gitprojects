'''
TO_DO CLI
============
Goal: CLI to manage a simple to-do list stored in a file (todo.txt).
Subcommands: add, list, remove

Requirements:
    add:
        Positional argument task (string).
        Optional priority -p/--priority (choices: low, medium, high, default=medium).
    list:
        Optional flag --all to list all tasks.
    remove:
        Positional argument index (int) to remove a task by its index.
        Store tasks in todo.txt (append/read/remove lines).

Hints:
    Use add_subparsers for add, list, remove.
    Use set_defaults(func=...) for each subcommand.
    Access subcommand via args.func(args).

Example usage:

$ python todo.py add "Buy milk" --priority high
Task added: Buy milk (high)

$ python todo.py list
1. Buy milk (high)

$ python todo.py remove 1
Task removed: Buy milk

'''