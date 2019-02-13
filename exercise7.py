# def wrap_text(arg1, arg2):
#     center = arg1
#     left = arg2[::-1]
#     right = arg2
#     return "{}{}{}".format(left,center,right)
#
# print("Enter your first string")
# inp1=input()
# print("Enter your second string")
# inp2=input()
#
# print(wrap_text(inp1,inp2))

#Interpreted the problem differently

def wrap_text(arg1, arg2):
    center = arg1
    left = arg2
    right = arg2
    return "{}{}{}".format(left,center,right)

print("Enter your first string")
inp1=input()
print("Enter your second string")
inp2=input()
print("Enter your third string")
inp3=input()
print("Enter your fourth string")
inp4=input()

combine = wrap_text(wrap_text(wrap_text(inp1,inp2),inp3),inp4)

print(combine)
