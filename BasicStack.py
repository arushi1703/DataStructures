def push(e):
    stk.append(e)

def pop():
    if isEmpty():
        print("Stack is empty")
        return
    e=top()
    del stk[-1]
    return e

def isEmpty():
    if stk:
        return False
    return True

def top():
    if isEmpty():
        return
    return stk[-1]

def display():
    print(stk)

def checkPar(expr):
    lefty="({["
    righty=")}]"
    for c in expr:
        if c in lefty:
            push(c)
        elif c in righty:
            if isEmpty():
                return Fasle
            if righty.index(c)!=lefty.index(pop()):
                return False
    return isEmpty()

def infix_postfix(infix):
    postfix=""
    operators=["^","*","/","+","-"]
    precedence={"^":3,"*":2,"/":2,"+":1,"-":1}

    if not checkPar(infix):
        print("Brackets have not been matched")
        return

    for token in infix:
        if token.isalnum():
            postfix+=token
        elif token=="(":
            push(token)
        elif token==")":
            while top()!="(":
                postfix+=pop()
            pop()
        elif token in operators:
            if top() in operators and precedence[top()]>=precedence[token]:
                postfix+=pop()
                push(token)
            else:
                push(token)

    while not isEmpty():
        postfix+=pop()
    return postfix

def postfix_evaluation(expr):
    operators=["^","*","/","+","-"]
    for token in expr:
        if token.isdigit():
            push(token)
        elif token in operators:
            b=int(pop())
            a=int(pop())
            if token=="^":
                push(a^b)
            elif token=="*":
                push(a*b)
            elif token=="/":
                push(a/b)
            elif token=="+":
                push(a+b)
            elif token=="^":
                push(a-b)
    return pop()

stk=[]
infix=input("enter infix experssion:")
print("Postfix:",infix_postfix(infix))
postfix=input("enter postfix expression:")
print("The expression is evaluated to give:",postfix_evaluation(postfix))
