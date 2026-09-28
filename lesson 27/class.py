class student:
    grade=67
    print("i am in grade",grade)
ob=student()
print(ob)

#second activity:
class car:
    def __init__ (self,miliage,max_speed):
        self.max_speed= max_speed
        self.miliage= miliage
modelx= car(670,84)
print("modelx max speed",modelx.max_speed)
print("modelx odometer",modelx.miliage)