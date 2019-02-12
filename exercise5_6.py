def converter(arg):
    cel = float((arg-32)*5/9)
    return cel

print("Please enter the temperature in Fahrenheit")
temp = float(input())
converted = converter(temp)
print("The converted value is {:.2f} C".format(converted))

# There is no exercise 6 in the assigments, it was skipped
