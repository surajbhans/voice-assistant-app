class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, function):
        self.commands[command_name] = function

    def handle_command(self, command):
        if command in self.commands:
            return self.commands[command]()
        else:
            return "Command not recognized."