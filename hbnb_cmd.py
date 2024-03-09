#!/usr/bin/python3

import cmd
from models.user import User
from models import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB> '  # Prompt displayed to the user

    def do_show(self, arg):
        """Show command usage: show User <user_id>"""
        args = arg.split()
        if len(args) < 2:
            print("Usage: show User <user_id>")
            return
        user_id = args[1]
        user_key = "User." + user_id
        users = storage.all(User)
        if user_key in users:
            print(users[user_key])
        else:
            print("** no instance found **")

    def do_create(self, arg):
        """Create command usage: create User"""
        if arg == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)
        else:
            print("Usage: create User")

    def do_destroy(self, arg):
        """Destroy command usage: destroy User <user_id>"""
        args = arg.split()
        if len(args) < 2:
            print("Usage: destroy User <user_id>")
            return
        user_id = args[1]
        user_key = "User." + user_id
        users = storage.all(User)
        if user_key in users:
            del users[user_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Update cmd usage: update User <user_id> <attribute> "<value>"""
        args = arg.split()
        if len(args) < 4:
            print("Usage: update User <user_id> <attribute> <value>")
            return
        user_id = args[1]
        user_key = "User." + user_id
        users = storage.all(User)
        if user_key in users:
            user = users[user_key]
            setattr(user, args[2], args[3])
            user.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """All command usage: all User"""
        if arg == "User":
            users = storage.all(User)
            for user in users.values():
                print(user)
            else:
                print("Usage: all User")

    def do_quit(self, arg):
        """Exit the program"""
        print("Quitting...")
        return True  # Exits the command loop

    def do_EOF(self, arg):
        """Exit on EOF: Ctrl+D or Ctrl+Z"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
