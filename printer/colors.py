class Colors:
    
    def __init__(self):
        self.color_dict = {
            "ERROR": ';'.join([str(7), str(31), str(47)]),
            "WARN": ';'.join([str(7), str(33), str(40)]),
            "INFO": ';'.join([str(7), str(32), str(40)]),
            "GEN": ';'.join([str(7), str(34), str(47)])
        }

    def get_cformat(self, message_type):
        return self.color_dict[message_type]