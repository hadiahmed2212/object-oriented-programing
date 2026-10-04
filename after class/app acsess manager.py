CAMERA = 1    
MICROPHONE = 2   
STORAGE = 4   
LOCATION = 8     

approved_apps = ["coding app","tech app","scratch app","science app"]
student_name = input("Enter your name: ")
requested_app=input("enter the app youd like to acsess")
if type(student_name) is str:
    print("The student name is stored as text.")
if type(requested_app) is not int:
    print("requested app denied...")
if requested_app in approved_apps:
    print(requested_app, "approved")
else:
    print(requested_app, "not approved")
 
restricted_apps = ["gaming app","shopping app","social media app"]
if requested_app not in restricted_apps:
    print("not in restricted list.")
else:
    print("Access denied")
student_permissions = CAMERA | MICROPHONE | STORAGE
 
print("Permission value:", student_permissions)
print("Permission bits:", bin(student_permissions))
if student_permissions & CAMERA:
    print("permission: Enabled")
if student_permissions & MICROPHONE:
    print("permission: Enabled")
if student_permissions & STORAGE:
    print("permission: Enabled")
if student_permissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")
next_permission = CAMERA << 1
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))
previous_permission = STORAGE >> 1
print("storage bit:", bin(STORAGE))
print("after right shift:", bin(previous_permission))
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("denied to", requested_app)