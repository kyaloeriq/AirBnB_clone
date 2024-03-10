#!/usr/bin/python3
"""
The Console Module that contains the entry point of the command interpreter
"""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Setting custom prompt

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            all_objs = BaseModel.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            all_objs = BaseModel.all()
            if key in all_objs:
                del all_objs[key]
                BaseModel.save_to_file(all_objs)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg:
            try:
                obj_list = BaseModel.all()
                filtered_objs = [str(obj) for obj in obj_list.values() if obj.__class__.__name__ == arg]
                print(filtered_objs)
            except NameError:
                print("** class doesn't exist **")
        else:
            obj_list = BaseModel.all()
            print([str(obj) for obj in obj_list.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            all_objs = BaseModel.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) == 3:
                print("** value missing **")
                return
            attr_value = args[3]
            obj = all_objs[key]
            setattr(obj, attr_name, attr_value.strip('"'))  # Stripping double quotes
            obj.save()
        except NameError:
            print("** class doesn't exist **")

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
        """Help documentation for handling EOF"""
        print("Handles EOF signal to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
