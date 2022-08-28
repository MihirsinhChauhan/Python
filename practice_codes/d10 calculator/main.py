from art import logo
print(logo)
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():
    num1= float(input("What's the first number "))
    
    
    for operation in operations:
        print(operation)
    
    operation_sym = input("Pick a operation from the line above ")
    num2 = float(input("What's the second number "))
    function = operations[operation_sym]
    ans = function(num1,num2)
    print(f"{num1} {operation_sym} {num2} = {ans}")
    
    flag = True
    while flag:
        con = input("Dou yoy want to continue , Type y for yes and n for no ")
        if con == "y":
            operation_sym = input("Pick another operation ")
            next_num = float(input("What's the next number "))
            function = operations[operation_sym]
            pre_num = ans
            ans = function(pre_num,next_num)
            print(f"{pre_num} {operation_sym} {next_num} = {ans}")
        else:
            flag = False
            calculator()

calculator()