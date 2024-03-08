#!/usr/bin/python3
import cmd
from hbnb_cmd import HBNBCommand  # Import the HBNBCommand class from another file

class MyCmd(cmd.Cmd):
    def do_hello(self, arg):
        print("Hello,", arg)

    def do_quit(self, arg):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
