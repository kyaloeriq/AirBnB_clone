#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
import shlex  # For parsing quoted strings
from models.base_model import BaseModel
from models import storage

storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """Class that contains the command interpreter"""
    prompt = "(hbnb) "  # Setting custom prompt

    def do_create(self, arg):
        """Creates a new instance of a specified class"""
        try:
            if not arg:
                raise ValueError("** class name missing **")

            class_name = arg
            if class_name not in ["BaseModel"]:
                raise ValueError("** class doesn't exist **")
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        try:
            args = shlex.split(arg)
            if not arg:
                raise ValueError("** class name missing **")

            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise ValueError("** class doesn't exist **")

            if len(args) < 2:
                raise ValueError("** instance id missing **")

            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        try:
            args = shlex.split(arg)
            if not args:
                raise ValueError("** class name missing **")

            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise ValueError("** class doesn't exist **")

            if len(args) < 2:
                raise ValueError("** instance id missing **")

            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if obj:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        try:
            args = shlex.split(arg)
            if not arg:
                raise ValueError("** class name missing **")

            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise ValueError("** class doesn't exist **")

            if len(args) < 2:
                raise ValueError("** instance id missing **")

            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if not obj:
                print("** no instance found **")
                return

            if len(args) < 3:
                raise ValueError("** attribute name missing **")

            if len(args) < 4:
                raise ValueError("** value missing **")

            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            storage.save()

        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        try:
            args = shlex.split(arg)
            if args and args[0] not in ["BaseModel"]:
                raise ValueError("** class doesn't exist **")
            obj_list = storage.all()
            if args:
                filtered_objs = [
                        str(obj)
                        for obj in obj_list.values()
                        if obj.__class__.__name__ == args[0]
                        ]
                print(filtered_objs)
            else:
                print([str(obj) for obj in obj_list.values()])

        except Exception as e:
            print(e)

    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        print()  # Add a newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass  # Do nothing, just return to prompt

    def help_quit(self):
        """Documentation for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Documentation for handling EOF"""
        print("Handles EOF signal to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
