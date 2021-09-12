class Printer:
    
    def __init__(self) -> None:
        self.color_format = "color_format"
        self.message_type = message_type

    def log_error(self, color_format, message_type):
        self.__str__(color_format, message_type)

    def __str__(self) -> str:
        return f"\x1b[{self.color_format}m {self.message_type} \x1b[0m: This is an {self.message_type}, are you sure you ok?"
        
    


