num_1 = input("Please input first number: ")
num_2 = input("Please input second number: ")
num_3 = input("Please input third number: ")

print("First Number: {}" .format(num_1))
print("Second Number: {}" .format(num_2))
print("Third Number: {}" .format(num_3))

if num_1 >= num_2 and num_1>=num_3:
    print("Highest Number: {}" .format(num_1))
elif num_2 >= num_1 and num_2>num_3:
    print("Highest Number: {}".format(num_2))
else:
    print("Highest Number: {}".format(num_3))