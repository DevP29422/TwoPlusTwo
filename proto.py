#BAD PROTOTYPE FOR THE PROJECT
#CURRENT LOOP ERROR
#Bad Bad
#Prev Ver had Debbuging statements


num1 = 0
num2 = 0

def funAdd(parm1, param2):
    return param2 + parm1

def funSub(param1, param2):
    return param1 - param2

def funMul(param1, param2):
    return param1 * param2

def funDiv(param1, param2):
    return int(param1 / param2)




num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opr = input("Enter oprator: ")
listOpr = {'+':funAdd(num1, num2), '-':funSub(num1, num2), 
        'x':funMul(num1, num2), '/':funDiv(num1, num2)}
return listOpr[opr]

