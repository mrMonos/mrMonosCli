from colors import red
commands = dict()
PROMPT = "(CMD-3)"
__all__ = "CMD-3.0"
__name__ = ["CMD-3.0"]
class CMD():
    def __init__(self):
        self.prompt = PROMPT
        self.intro = """
        Welcome at CMD-3.0 \n
        ===========================
        """
        print(self.intro)
        commands.update({"help": self.intro2,})
    def __init_subclass__(cls):
        super().__init__(cls)
    def intro2(self,args):
        print(args[0]);
    def prase(self,line,commands):
        prasedline = line.split()
        try:
            self.command = prasedline[0]
        except:
            print(red("You have not given an order to execute"))
        del prasedline[0]
        self.args = prasedline
        try:
            return commands[self.command](self.args)
        except:
            return commands[self.command]()
    def cmdloop(self):
        line = "init" 
        while  line != "exit":
            line = input(self.prompt)
            if line != "exit":
                self.prase(line,commands)

