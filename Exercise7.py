firstName = input("Enter first Name:\n")
secondName = input("Enter Second Name:\n")
names = firstName + secondName
love = "TrueLove"
love = love.lower()
names = names.lower()
tracked_names = set()
count = 0


for i in range(len(love)):
    for j in range(len(names)):
        # print(names[i])
        if love[i] == names[j]:
            tracked_names.add(love[i])

percent = len(tracked_names) / len(love) * 100
print(tracked_names)
print(len(tracked_names))
print(len(love))
print(f"{percent}%")


# firstName = input("Enter first Name:\n")

# secondName = input("Enter Second Name:\n")
# names = firstName + secondName
# love = "TrueLove"

# # Convert both strings to lowercase
# love = love.lower()
# names = names.lower()

# count = 0

# # Compare each character in `love` with each character in `names`
# for i in range(len(love)):
#     for j in range(len(names)):
#         if love[i] == names[j]:
#             count += 1
#             # Once a match is found, mark that character as processed
#             names = names[:j] + "_" + names[j + 1 :]
#             break

# # Calculate the percentage
# percent = (count / len(love)) * 100 if len(love) > 0 else 0

# print(f"Count of matches: {count}")
# print(f"Percentage of characters in 'love' found in 'names': {percent:.2f}%")
