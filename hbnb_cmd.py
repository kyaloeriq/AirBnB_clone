#!/usr/bin/python3

import cmd
from models.user import User
from models import storage

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

    def do_hello(self, arg):
        """Prints a greeting message."""
        print("Hello, world!")

    def do_quit(self, arg):
        """Exit the program."""
        print("Quitting...")
        return True  # Exits the command loop
