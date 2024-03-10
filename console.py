#!/usr/bin/python3
"""
The Console Module that contains the entry point of the command interpreter
"""
import cmd
import json
from models.base_model import BaseModel
from models import Place, State, City, Amenity, Review
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Setting custom prompt

    def do_create(self, arg):
        """Creates a new instance of a specified class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance attributes missing **")
                return
            kwargs = {}
            for pair in args[1:]:
                key, value = pair.split("=")
                kwargs[key] = value.strip('"')
            obj = eval(class_name)(**kwargs)
            obj.save()
            print(obj.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
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
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
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
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj_dict = storage.all()
            obj = obj_dict.get(key)
            if not obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3].strip('"')
            setattr(obj, attr_name, attr_value)
            storage.save()
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg:
            try:
                obj_list = storage.all()
                filtered_objs = [str(obj) for obj in obj_list.values() if obj.__class__.__name__ == arg]
                print(filtered_objs)
            except Exception as e:
                print(e)
        else:
            try:
                obj_list = storage.all()
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
        """Help documentation for handling EOF"""
        print("Handles EOF signal to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
