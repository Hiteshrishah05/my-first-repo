#grade stimulator 
print("marksheet of class A:")
students={"alice":98,
          "nandini":90,
          "ravi":50,
          "omkar":60,
          "atharva":70,
          "tanvi":80,}
for name,marks in students.items():
    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70-60:
        grade="C"
    elif marks>=50:
        grade="D"
    elif marks>=35:
        grade="E"
    else:
        grade="F"
    print(f"{name}:{marks}mks = Grade{grade}")