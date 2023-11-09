#!/usr/bin/python3
"""
This module provides a python command line interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Provides methods that ensure proper functioning of the interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Prevents the previous command from being executed again if
        no command is given.
        """
        pass

    def precmd(self, line):
        """
        Add an empty line before executing command in non-interactive
        mode (only) so that the output mimics that of the interactive
        mode
        """
        if not sys.stdin.isatty():
            print()
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
