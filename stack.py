def create():
    stack=[]
    return stack
def check(stack):
    if(len(stack)==0):
        return True
    else:
        return False
def push(s):
    s.append(input())
    print("Added",s)
def pop(s):
    if(len(s)==0):
        print("Stack is Empty")
    else:
        print("REmoved Value is",s.pop())
s=create()
# if(check(s)):
#     print("OK")
push(s)
pop(s)