#!/usr/bin/python3
"""
The Console Module that contains the entry point of the command interpreter
"""
import cmd
from models.engine import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage = FileStorage()
storage.reload()

class HBNBCommand(cmd.Cmd):
    """inherits all the methods and attributes of the parent class cmd"""
    prompt = "(hbnb) "  # Setting custom prompt

    valid_classes = ["BaseModel", "Place", "State", "City", "Amenity", "Review"]

    def do_create(self, arg):
        """Creates a new instance of a specified class"""
        try:
            if not arg:
                raise ValueError("** class name missing **")

            class_name, *params = arg.split()
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                raise ValueError("** class doesn't exist **")

            if not params:
                raise ValueError("** instance attributes missing **")

            kwargs = {}
            for param in params:
                key, value = param.split("=")
                kwargs[key] = value.strip('"')
            
            new_instance = eval(class_name)(**kwargs)
            new_instance.save()
            print(new_instance.id)

        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        try:
            if not arg:
                raise ValueError("** class name missing **")

            class_name, obj_id = arg.split()
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                raise ValueError("** class doesn't exist **")

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
            if not arg:
                raise ValueError("** class name missing **")

            class_name, obj_id = arg.split()
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                raise ValueError("** class doesn't exist **")

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
            if not arg:
                raise ValueError("** class name missing **")

            args = arg.split()
            class_name, obj_id = args[0], args[1]
            if class_name not in ["Place", "State", "City", "Amenity", "Review"]:
                raise ValueError("** class doesn't exist **")

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

            attr_name, attr_value = args[2], args[3].strip('"')
            setattr(obj, attr_name, attr_value)
            storage.save()

        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        try:
            if arg:
                if arg not in self.valid_classes:
                    raise ValueError("** class doesn't exist **")
                
                obj_list = storage.all()
                filtered_objs = [str(obj) for obj in obj_list.values() if obj.__class__.__name__ == arg]
                print(filtered_objs)
            else:
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
