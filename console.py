#!/usr/bin/python3
"""
This module provides a python command line interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Provides methods that ensure proper functioning of the interpreter
    """
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def do_EOF(self, arg):
        """(Ctrl + D) to force exit the program"""
        return True
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel, Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg in globals() and isinstance(globals()[arg], type):
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                instance_id = args[1]

                if class_name in globals() and isinstance(globals()[class_name], type):
                    all_objs = storage.all()
                    instance_found = False
                    for obj_id, obj in all_objs.items():
                        if obj.id == instance_id:
                            print(str(obj))
                            instance_found = True
                            break
                    
                    if not instance_found:
                        print("** no instance found **")

                else:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Commend"""
        pass
    
    def do_all(self, arg):
        """Commend"""
        pass
    
    def do_update(self, arg):
        """Commend"""
        pass
    
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    