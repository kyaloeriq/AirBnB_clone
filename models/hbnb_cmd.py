#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = 'HBNB> '  # Prompt displayed to the user

    def do_hello(self, arg):
        """Prints a greeting message."""
        print("Hello, world!")

    def do_quit(self, arg):
        """Exit the program."""
        print("Quitting...")
        return True  # Exits the command loop
