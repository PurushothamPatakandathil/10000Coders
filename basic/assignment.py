# Login page:
def login():
    username=input("Enter your username: ")
    savedPassword="123456"
    count=1
    while count<4:
        count+=1
        password=input("Enter your password here: ")
        if password==savedPassword:
            print("Login Successfull")
            break
        elif password!=savedPassword:
            print(f"Wrong Password, You have {4-count} more attempts left")
            if count==4:
                print("You have exhaused your login attempts. Revisit after 24hrs.")
        else:
            print("Something went wrong")
            break
login()


# Factorial program:
num = int(input())
factorial = 1
n = num
while n > 1:
    factorial *= n
    n -= 1
print(f"Factorial of {num} is {factorial}")




# Menu Driven Calculations
def menu():
    while True:
        arg=input("Enter [Square, cube or 1,2]/[+,-,/,*] and stop or .. to end" )
        res=0
        if arg in ['stop','..']:
            break
        elif arg in ['square','1','cube','2']:
            num=int(input("Enter a number: "))
            arg=arg.lower()
            if arg in ['square','1']:
                res=num**2
                print(f'{num} result: {res}')
            elif arg in ['cube','2']:
                res=num**3
                print(f'{num} result: {res}')
        elif arg in ['square','1','cube','2','+','add','-','sub','mul','*','div','/']:
            num1=int(input("Enter num 1: "))
            num2=int(input("Enter num 2: "))
            if arg in ['+','add']:
                res=num1+num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['-','sub']:
                res=num1-num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['*','mul']:
                res=num1*num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['/','div']:
                if num2!=0:
                    result=num1/num2
                    print(f'num1: {num1} num2: {num2} result: {res}')
                else:
                    print("division error by zero")
        else:
            print("Enter proper operator")
menu()



#divisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')