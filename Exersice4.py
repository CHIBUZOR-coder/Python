mass = input("Enter weight in kg")
height = input("Enter height in meter")

bmi = int(mass) / float(height) ** 2

print("bmi:" + str(int(bmi)) + "kg")

# print(type(bmi))

if bmi < 16:
    print("Severe Thiness")
    print("Please see a Medical personal ")
elif bmi >= 16 and bmi <= 16.9:
    print("Moderate Thinness")
    print("Please Improve in your Diet and see a Medical personal if needed")
elif bmi >= 17 and bmi <= 18:
    print("Mild Thinness")
    print("Please Improve in your Diet and take it seriously")
elif bmi >= 18.5 and bmi <= 24:
    print("Normal Thinnes")
    print("Please Improve in your Diet")
elif bmi >= 25 and bmi <= 29:
    print("Pre Obessed")
    print("Please watch your level of eating so you wont get obessed")
elif bmi <= 30 and bmi >= 34:
    print("ObessedI")
    print("Please watch your level of eating and do some exersice")
elif bmi >= 35 and bmi <= 39:
    print("ObessedII")
    print("Please reduce your eating habbit and take exercise seriouly")
elif bmi >= 40:
    print("ObessedIII")
    print("Please reduce your eating and enroll in a weight controll and diet class")

