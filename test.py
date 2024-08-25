# numbers = []

# counter = 1  # Start with 1

# for i in range(3):
#     for j in range(3):
#         numbers.append(counter)  # Move to the next line after each row
#         print(numbers[i * 3 + j], end=" ")
#         counter += 1
#     # Increment the counter by 1
#     print()
# print(numbers)

# a = [1, 4, 7, 4, 3]
# b = [5, 3, 1, 5, 7]
# c = []
# for i in range(5):
#     summ = a[i] + b[i]
#     c.append(summ)
# print(c)


# num = [[1, 3, 4], [4, 6, 3], [2, 7, 8]]
# changeA = int(input("Enter your save point:"))
# changeB = int(input("Enter your save point"))
# if 0 <= changeA < 3 and 0 <= changeB < 3:
#     num[changeA][changeB] = "X"
#     for i in range(3):
#         print(num[i])
# else:
#     print("Numbers must be between 0 and 3")


row1 = ["😎", "😎", "😎"]
row2 = ["😎", "😎", "😎"]
row3 = ["😎", "😎", "😎"]

print(f"{row1} \n{row2}\n{row3}")
matrix = [row1, row2, row3]

positionn = input("Enter positions")

row_num = int(positionn[0])
col_num = int(positionn[1])

row_select = matrix[row_num - 1]
row_select = matrix[col_num - 1] = "X"
print(f"{row1} \n{row2}\n{row3}")





