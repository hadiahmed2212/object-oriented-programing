class dailymsg:
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("Enter message: ")
 
    def print_message(self):
        print("uppercase:", self.message.upper())
 
 
daily_txt = dailymsg()
daily_txt.get_message()
daily_txt.print_message()
class helperses:
    def __init__(self):
        print("daily data helper session started")
    def __del__(self):
        print("daily data heelper session finished")
 
def create_session():
    session = helperses()
    return session
session_obj = create_session()
class prfir:
 def find_pr(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            needed_number = target - number
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index
        return None
del session_obj
print("THE END")