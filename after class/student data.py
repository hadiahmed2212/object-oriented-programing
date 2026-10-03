student_data ={"st1": {"name": "hadi", "class": "5.1", "subject": "english, math, technology"},
"st2": {"name": "Hafi", "class": "2.2", "subject": "english,hass, science"},
 "st3": {"name": "dude", "class": "7", "subject": "english, math, science"},
"st4": {"name": "dude2", "class": "2.1", "subject": "english, coding, math"}}
 
print("Student Records:")
print(student_data)
print("st1:")
print(student_data.get("st1", ".."))
print("st5:")
print(student_data.get("st5", ".."))

student_data["st5"] = {"name": "67 kid","class": "6","subject": "english, art, science"}
 

print("st5 +:")
print(student_data)
 
student_data["st2"]["subject"] = "english, math, coding"
print("After st2 subjrcts updated:")
print(student_data["st2"])

cleaned_data = {}
seen_records = []
 
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details 
student_data = cleaned_data
print("After removing duplicate records:")
print(student_data)
rmved_std = student_data.pop("id4", ".....")
print("Removed student:")
print(rmved_std)
print("Total student records left:", len(student_data))
