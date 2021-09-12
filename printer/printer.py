from colors import Colors

class Printer:

    colors = Colors()    

    def log_message(self, message_type, message, data=""):
        print(f"\x1b[{self.colors.get_cformat(message_type)}m {message_type} \x1b[0m: {message}\n")

        if data:
            if type(data) == "":



