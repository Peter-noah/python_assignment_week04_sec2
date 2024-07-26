grades = [55,70,65,40,90,85,50,77]
pass_with_bonus = [grade * 1.05 for grade in grades if grade >= 60]
print(pass_with_bonus)