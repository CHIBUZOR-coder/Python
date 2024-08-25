# Leap Year
year = int(input("Enter year"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("A Leap Year")
#         else:
#             print("Not A Leap Year")
# else:
#     print("Not A Leap Year")

if year % 400 == 0:
    print("A Leap Year")
elif year % 100 == 0:
    print("Not A Leap Year")
elif year % 4 == 0:
    print("A Leap Year")
else:
    print("Not A Leap Year")
