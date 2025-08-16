A = int(input("Enter 1st Num: "))
B= int (input("Enter 2nd Num: "))
        
print("What u wanna do? (+,-,*,/)")
op = input("Enter the operator: ")
if(op=='+'):
    sum=A+B
    print("Sum: ",sum)
elif(op=='-'):
    sub=A-B
    print("Sub: ",sub)
elif(op=='*'):
    mul=A*B
    print("Mul: ",mul)
elif(op=='/'):
    if B!=0:
        div=A/B
        print("Div: ",div)
    else:
        print("ERROR! : Division by Zero!")
else:
    print("U entered Rong Operator. Try Again")
            
