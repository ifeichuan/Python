tokens = ["3","-4","+"]

def evalRPN(tokens: list[str]):
    stack = []
    for str in tokens:
        if(abs(str)):
            stack.append(int(str))
        else:
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            stack.pop()
            if str=='-':
               stack.append(b-a) 
            elif str=='+':
               stack.append(b+a) 
            elif str=='*':
               stack.append(b*a) 
            elif str=='/':
               stack.append(int(b/a)) 
    return  stack[-1]

evalRPN(tokens)


