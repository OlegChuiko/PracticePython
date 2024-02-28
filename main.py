def fun(a,b,c,d):
    result = (((a * (b ** 0.5)) - (c * (d ** 0.5))) ** 2) * (5.6 / (a + b + c))
    return result


val2 = input("Enter the second number: ")
val1 = input("Enter the first number: ")
val3 = input("Enter the third number: ")
val4 = input("Enter the fourth number: ")

print("Result = ",fun(int(val1),int(val2),int(val3),int(val4)))















