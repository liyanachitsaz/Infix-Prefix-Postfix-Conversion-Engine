class node : 

    def __init__(self , data = None , link = None) : 

        self.data = data 

        self.link = link
        
class Stack : # use stack to keep the items

    def __init__(self) :

        self.top = node()

        self.top.link = None 

    def Push(self,item_stack) :

        new_stack = node()

        new_stack.data = item_stack

        new_stack.link = self.top.link

        self.top.link = new_stack

    def Pop(self) :

        if  self.top.link :

            data = self.top.link.data

            self.top.link = self.top.link.link

            return data
        
        else :
            
            return None 

def IcpOperator(char) :

    if char == '(' :

        icp = 0 # most significant in icp

    elif char == '+' or char == '-' :

        icp = 2 # least significant in icp

    elif char == '*' or char == '/' :

        icp = 1

    return icp 

def IspOperator(char) :

    if char == '(' :

        isp = 3 # least significant in isp

    elif char == '+' or char == '-' :

        isp = 2

    elif char == '*' or char == '/' :

        isp = 1 # most significant in isp

    return isp 

def InfixToPrefix() : # reverse infix at first , then we do the same operations that we do in InfixToPostfix() and in the end we reverse the postfix to make prefix 

    operator = Stack()

    operator.Push("#") # to know stack is empty

    prefix = ''

    infix = input("Enter your infix format : ")

    R_infix = '' # short cut for reverse of infix

    for char in infix : # make the reverse of infix format

        if char == ')' : # when we reverse the infix format ,parenthesis should be reversed too 

            char = '('

            R_infix = char + R_infix 

        elif char == '(' :

            char =')'

            R_infix = char + R_infix

        else :

            R_infix = char + R_infix


    for char in R_infix : 

        if char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data == '#' :

                operator.Push(char) 

            else :

                if char == ')' :

                    op = operator.Pop()

                    while op != '(' : 

                        prefix += op

                        op = operator.Pop()

                elif IcpOperator(char) < IspOperator(operator.top.link.data) :

                    operator.Push(char)

                elif IcpOperator(char) >= IspOperator(operator.top.link.data) :

                    prefix += operator.Pop()

                    operator.Push(char)
                   

        else :

            prefix += char

    while operator.top.link.data != '#' :

        prefix += operator.Pop()

    print("Prefix format is :",prefix[::-1]) 

def InfixToPostfix() :

    operator = Stack()

    operator.Push("#")

    postfix = ''

    infix = input("Enter your infix format : ")

    for char in infix : 

        if char in [ '+' , '-' , '*' , '/' , '(' , ')' ] : 

            if operator.top.link.data == '#' : # just push operators in the stack

                operator.Push(char) 

            else :

                if char == ')' :

                    op = operator.Pop()

                    while op != '(' : # poping operators from the stack and add them to the postfix format

                        postfix += op

                        op = operator.Pop()

                elif IcpOperator(char) < IspOperator(operator.top.link.data) : # if icp is more significant than isp 

                    operator.Push(char)

                elif IcpOperator(char) >= IspOperator(operator.top.link.data) : # if isp == icp or isp is more significant than icp

                    postfix += operator.Pop() # poping the last operator in the stack and add it to postfix format 

                    operator.Push(char) 
                   

        else :

            postfix += char 

    while operator.top.link.data != '#' :

        postfix += operator.Pop() # poping all the operators that are in the stack and add them to the postfix format

    print("Postfix format is :",postfix) 

def PrefixToInfix() : # at first reverse the prefix , then do the same thing that we do in PostixToInfix() , reverse the infix

    operator = Stack()

    operator.Push("#")

    infix = ''

    R_infix = ''

    x = 0

    prefix = input("Enter your prefix format : ")

    prefix = prefix[::-1] # reverse of prefix == postfix of reverse infix

    for char in prefix : # prefix as postfix entered

        if char not in [ '+' , '-' , '*' , '/' ] :

            operator.Push(char) 

        elif char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data != '#' and operator.top.link.link.data != '#' :

                x = operator.Pop()

                infix = "(" + operator.Pop() + char +  x + ")" # poping the last two items was pushed in the stack , we add them with the operator to infix

                operator.Push(infix) # push the new infix format to the stack 

    for char in infix : #reverse of infix which we have the postfix of it

        if char == ')' :

            char = '('

            R_infix = char + R_infix

        elif char == '(' :

            char =')'

            R_infix = char + R_infix

        else :

            R_infix = char + R_infix


    print("Infix format is :",R_infix)

def PostfixToInfix() :

    operator = Stack()

    operator.Push("#")

    infix = ''

    x = 0

    postfix = input("Enter your postfix format : ")

    for char in postfix : 

        if char not in [ '+' , '-' , '*' , '/' ] :

            operator.Push(char) 

        elif char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data != '#' and operator.top.link.link.data != '#' :

                x = operator.Pop()

                infix = "(" + operator.Pop() + char +  x + ")"

                operator.Push(infix)

    print("Infix format is :",operator.Pop())

def PrefixToPostfix() :

    operator = Stack()

    operator.Push("#")

    infix = ''

    R_infix = ''

    x = 0

    prefix = input("Enter your prefix format : ")

    prefix = prefix[::-1] #reverse of prefix -> postfix

    for char in prefix : #prefix as postfix entered

        if char not in [ '+' , '-' , '*' , '/' ] :

            operator.Push(char) 

        elif char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data != '#' and operator.top.link.link.data != '#' :

                x = operator.Pop()

                infix = "(" + operator.Pop() + char +  x + ")"

                operator.Push(infix)

    for char in infix : #reverse of infix which we have the postfix of it

        if char == ')' :

            char = '('

            R_infix = char + R_infix

        elif char == '(' :

            char =')'

            R_infix = char + R_infix

        else :

            R_infix = char + R_infix

    operator = Stack()

    operator.Push("#")

    postfix = ''

    for char in R_infix : 

        if char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data == '#' :

                operator.Push(char) 

            else :

                if char == ')' :

                    op = operator.Pop()

                    while op != '(' : 

                        postfix += op

                        op = operator.Pop()

                elif IcpOperator(char) < IspOperator(operator.top.link.data) :

                    operator.Push(char)

                elif IcpOperator(char) >= IspOperator(operator.top.link.data) :

                    postfix += operator.Pop()

                    operator.Push(char)
                   

        else :

            postfix += char

    while operator.top.link.data != '#' :

        postfix += operator.Pop()

    print("Postfix format is :",postfix) 

def PostfixToPrefix() :

    operator = Stack()

    operator.Push("#")

    infix = ''

    x = 0

    postfix = input("Enter your postfix format : ")

    for char in postfix : 

        if char not in [ '+' , '-' , '*' , '/' ] :

            operator.Push(char) 

        elif char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data != '#' and operator.top.link.link.data != '#' :

                x = operator.Pop()

                infix = "(" + operator.Pop() + char +  x + ")"

                operator.Push(infix)

    newinfix = operator.Pop()

    operator = Stack()

    operator.Push("#")

    prefix = ''

    R_infix = ''

    for char in newinfix :

        if char == ')' :

            char = '('

            R_infix = char + R_infix

        elif char == '(' :

            char =')'

            R_infix = char + R_infix

        else :

            R_infix = char + R_infix


    for char in R_infix : 

        if char in [ '+' , '-' , '*' , '/' , '(' , ')' ] :

            if operator.top.link.data == '#' :

                operator.Push(char) 

            else :

                if char == ')' :

                    op = operator.Pop()

                    while op != '(' : 

                        prefix += op

                        op = operator.Pop()

                elif IcpOperator(char) < IspOperator(operator.top.link.data) :

                    operator.Push(char)

                elif IcpOperator(char) >= IspOperator(operator.top.link.data) :

                    prefix += operator.Pop()

                    operator.Push(char)
                   

        else :

            prefix += char

    while operator.top.link.data != '#' :

        prefix += operator.Pop()

    print("Prefix format is :",prefix[::-1]) 


number = 0 

while number != -1 :

    print("Which format do you want to enter ?")

    print("Press (1) if you want to change your phrase from infix format to prefix format ")

    print("Press (2) if you want to change your phrase from infix format to postfix format ")

    print("Press (3) if you want to change your phrase from prefix format to infix format ")

    print("Press (4) if you want to change your phrase from postfix format to infix format ")

    print("Press (5) if you want to change your phrase from prefix format to postfix format ")

    print("Press (6) if you want to change your phrase from postfix format to prefix format ")

    print("Press (-1) to exit")

    number = int(input())

    if number == 1 :

        InfixToPrefix()

    elif number == 2 :

        InfixToPostfix()

    elif number == 3 :

        PrefixToInfix()

    elif number == 4 :

        PostfixToInfix()

    elif number == 5 : 

        PrefixToPostfix()

    elif number == 6 :

        PostfixToPrefix()

    elif number == -1 :

        break 

    else :

        print("Entered number is not correct !")





