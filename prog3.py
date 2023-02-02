num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))

try:
    result=num1/num2
    print("Answer :",result)
except:
    print("Zero is not Allowed ! num2")

    num2=int(input("Enter Second Number :"))

    result=num1/num2
    print("Answer :",result)

finally:
    print("Hi world")
