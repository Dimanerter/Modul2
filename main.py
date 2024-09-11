strok = input(">>>")
number_of_space = 0
number_of_char = 0

for i in strok:
    if i == " ":
        number_of_space += 1
    else:
        number_of_char += 1

print(number_of_char)
print(number_of_space)