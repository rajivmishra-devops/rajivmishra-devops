#from exercise1 import calculator
def calculator(Operation, Number1, Number2):
    if Operation == '+' :
        return Number1 + Number2
    elif Operation == '-' :
        return Number1 - Number2
    elif Operation == 'x' :
        return Number1 * Number2
    elif Operation == '/' :
        return Number1 / Number2
    else:
        return "Wrong Number/Operation, retry again"

with open("textfile.txt", 'r') as inputfile:
    text_line = inputfile.read()
    text_line = text_line.splitlines()
   
overallresult = 0
for values in text_line:
    calc, operator, num1, num2 = values.split()
    result = calculator(Operation = operator, Number1 = int(num1), Number2 = int(num2))
    temp1 = result
    overallresult +=  temp1
print("Answer: " + str(overallresult))