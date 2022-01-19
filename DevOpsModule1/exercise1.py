def calculator():
    Number1=int(input("enter number 1: "))
    Number2=int(input("enter number 2: "))
    Operation=input("enter Operator: ")
    if Operation == '+' :
        return Number1 + Number2
    elif Operation == '-' :
        return Number1 - Number2
    elif Operation == '*' :
        return Number1 * Number2
    elif Operation == '/' :
        return Number1 / Number2
    else:
        return "Wrong Number/Operation, retry again"
    
#print (calculator(2,3,'/') )
result = calculator()
print (result)

#https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt



