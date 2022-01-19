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

with open("step3.txt", 'r') as inputfile:
    text_line = inputfile.read()
    text_line = text_line.splitlines()
   
overallresult = 0
for values in text_line:
    temp = values[5]
    print(temp)
    if temp == 'c':
        check, calc, operator, num1, num2 = values.split()
        print ("GOTO Calc: "+ text_line)
    elif temp.isnumeric() == 'True':
        print("GOTO LineNumber: "+ text_line)
    else:
        print("false")
    #index = [x for x in range(len(text_line)) if 'text_line' in text_line[x].lower()]
    #print (index)
#    result = calculator(Operation = operator, Number1 = int(num1), Number2 = int(num2))
#   temp1 = result
#    overallresult +=  temp1
#print("Answer: " + str(overallresult))