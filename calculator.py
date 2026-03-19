
print("welcome to calculator")
def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
while True:
    print("menu")
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    operation=input("enter the operation: ")
    if operation=="5":
        print("exiting program...")
        break
    if operation not in ["1","2","3","4","5"]:
        print("not valid")
        continue

    num1=int(input("enter the number1: "))
    num2=int(input("enter the number2:"))

    if operation=="1":
        result=addition(num1,num2)
        print("result:",result)
    elif operation=="2":
        result=subraction(num1,num2)
        print("result:",result)
    elif operation=="3":
        result=multiplication(num1,num2)
        print("result:",result)
    elif operation=="4":
        if num2==0:
            print("zero is not allowed")
            continue
        result=division(num1,num2)
        print("result:",result)
    choice=input("do you want to continue (y/n):").lower()
    if choice=="n":
        print("good bye!!")
        break
    else:
        continue


    
    
        