def is_armstrong_number(number):
    #breakpoint()
    numOne = int(number)
    sum = 0
    numLen = len(str(numOne))
    if numLen == 1:
        return (numOne ** 1) == number
    
    while numOne != 0:
        digit = numOne % 10
        numOne = numOne // 10 # new number
        sum += digit ** numLen
    
    return number == sum
    
    
#print(is_armstrong_number(153))        
        
        
'''Notes:
I realized too late that I needed to compare the sum to the
original number and had to do some sketchy stuff to fix the 
issue.

the breakpoint is commented in only because I was trying to debug 
the program and the debugger wouldn't autopause.

the print statement is only for testing purposes as well.

'''