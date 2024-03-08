import cmd

class HBNBCmd(cmd.Cmd):
    prompt = 'HBNB> '  # Prompt displayed to the user

    def do_hello(self, arg):
        """Prints a greeting message."""
        print("Hello, world!")

    def do_quit(self, arg):
        """Exit the program."""
        print("Quitting...")
        return True  # This will exit the command loop

if __name__ == '__main__':
    HBNBCmd().cmdloop()
