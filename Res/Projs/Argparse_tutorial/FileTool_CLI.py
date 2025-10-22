'''
CLI TOOL FOR FILE OPERATIONS
==================================================

Operations :
    - List line
    - Count words/ lines(default)
    - Find and replace word
Code structure :
    1) main() - cli parser logic #subcommands with its own arguments.
    2) function logic for operations part. # function --> cmd_list, cmd_count, cmd_replace

'''

import argparse

def cmd_list(args):
    '''list file contents'''
    with open (args.file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip())

def cmd_count(args):
    '''Count lines or words, depending on flag.'''
    with open (args.file, 'r', encoding='utf-8') as f:
        text = f.read()
        if args.words:
            n = len(text.split())
            print(f"Word count : {n}")
        else:
            n = text.count('\n') + 1
            print(f"Line count : {n}")

def cmd_replace(args):
    """Replace old substring with new in file; optionally write back."""
    with open (args.file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(args.old, args.new)
    if args.inplace:
        with open(args.file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(new_content)


def main():
    #parser
    parser = argparse.ArgumentParser(prog="myfileTool",description= "CLI tool for file operations")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Sub-commands to run")
    
    #list cmnd
    parser_list = subparsers.add_parser("list", help="Print file contents")
    parser_list.add_argument("file", type=str, help="path to file")
    parser_list.set_defaults(func=cmd_list)

    #count cmnd
    parser_count = subparsers.add_parser("count", help="Count lines or words in a file")
    parser_count.add_argument("file",type=str, help="path to file")
    parser_count.add_argument("-w","--words" , action="store_true", help="count words instead of lines")
    parser_count.set_defaults(func=cmd_count)

    #replace cmnd
    parser_replace = subparsers.add_parser("replace", help="Find and replace words in a file")
    parser_replace.add_argument("file", type=str, help="path to file")
    parser_replace.add_argument("old", type=str, help="old substring")
    parser_replace.add_argument("new", type=str, help="new substring")
    parser_replace.add_argument("-i","--inplace",action="store_true", help="modify inplace")
    parser_replace.set_defaults(func=cmd_replace)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()