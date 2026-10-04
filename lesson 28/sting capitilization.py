class capital():
    def __init__(self):
        self.nothing=""
    def get_input (self):
        self.nothing=(input("enter words or sentences for capitalization"))
    def something(self):
        print("result:",self.nothing.upper())

nothing=capital()
nothing.get_input()
nothing.something()