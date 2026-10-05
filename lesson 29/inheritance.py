class fammem:
    def __init__(self,eyeclr,heightcm):
        self.eyeclr=eyeclr
        self.heightcm=heightcm
    def swtr(self):
        print("stats (height)",self.heightcm)
        print("stats (eye colour)",self.eyeclr)
class kid(fammem):
    def __init__(self,name,age,eyeclr,heightcm ):
        self.name= name
        self.age= age
        super().__init__(eyeclr,heightcm)
    def swtr(self):
        print("name",self.name)
        print("age",self.age)
        super().swtr()
    def favhob (self,hobby):
        print(self.name,"loves to:",hobby)
child= kid("Hadi",10,"brown",165)
child.swtr()
child.favhob("technology")
print("are they even related?",issubclass(kid,fammem))

