subjects={
    "maths":21,
    "ATCD":22,
    "DS":19,
    "m1":18,
    "java":25
}
for key,value in subjects.items():
    print(key,"-->",value)
    #highest_marks
highest_marks=max(subjects,key=subjects.get)
print("highest_marks = ", highest_marks)
