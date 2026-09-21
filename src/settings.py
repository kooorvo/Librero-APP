import json

class Param():
    def __init__(self, theme):
        self.theme = theme

    def to_dic(self):
        return{
            "theme":self.theme
        }

    @classmethod
    def from_dic(cls, settings):
        return cls(
            theme=settings["theme"],
        )