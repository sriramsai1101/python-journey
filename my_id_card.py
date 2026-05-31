print('------my college idcard-------')
student={
    "name":"sriram",
    "college":"avanthi",
    "roll no":"24Pt1A6610",
    "branch":"AI&ML",
    "year":"3rd year"
}
student["city"]="hyderabad"
student["fav sub"]="python"
for key,value in student.items():
    print(key,"=",value)