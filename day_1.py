# STACK APPLICATIONS 
# EVOLUTION ARITHMETIC EXPRESSION
# PREFIX : +ab -->operator appears in the beggining
# INFIX : a+b -->operator appears in the middle
# POSTFIX : ab+ -->operator appears in the last


# POSTFIX EXPRESSION EVOLUTION :
# ===============================
# STEP 1: read symbols from left to right.
# STEP 2: if the symbol is a number (operand) , push it onto the stack.
# STEP 3: if the symbol is an operator (+,-,*,/):
        # - Pop two numbers from the stack (operand 1 and operand 2)
        # - Perform the opaeration : operand 1 operator operand 2
        # - Push the result back onto the stack
# STEP 4: after reading all symbols , pop the final value from the stack -- this is the result.
# Examples:
# 1. 432 *+ 5-         ----> Ans: 5
# 2. 53 + 62 /* 35 *+  ----> Ans: 39
# Scanned Symbol         Stack          Output
# --------------         -----          ------
# 5                       5             push 5
# 3                       5,3           push 3
# +                       8             pop 3, 5 and find 3+5 = 8
#                                       push 8
# 6                       8,6           push 6
# 2                       8,6,2         push 2
# /                       8,3           pop 2,6 and find 6/2
#                                       push 3
# *                       24            pop 3,8 and find 3*8 = 24
#                                       push 24
# 3                       24,3          push 3
# 5                       24,3,5        push 5
# *                       24,15         pop 5,3 and find 5*3 = 15
#                                       push 15
# +                       39            pop 15,24 and find 15+24 = 39

# 1. 432 *+ 5-         ----> Ans: 5
# Scanned Symbol         Stack          Output
# --------------         -----          ------
# 4                       4              push 4
# 3                       4,3            push 3
# 2                       4,3,2          Push 2   
# *                       4,6            pop 2, 3 and find 2 * 3
#                                        push 6
# +                       10             pop 4, 6 and find 4 + 6
#                                        push 10
# 5                       10,5           push 5
# -                       5              pop 5,10 and find 10-5
#                                        push 5
'''
#CODE
stack = []
expression = "432*+5-"
for i in expression:
    if i.isdigit():
        stack.append(int(i))
    else:
        b=stack.pop()
        a=stack.pop()
        if i == "+":
            c=a+b
        elif i == "-":
            c=a-b
        elif i == "*":
            c=a*b
        elif i == "/":
            c=a/b
        stack.append(c)
print(stack[0])
print(stack.pop())
#by using functions

class postfixEvaluator:
    def __init__(self, postfix):
        self.postfix_exp=postfix
        self.stack = []
    def evaluate(self):
        for symbol in self.postfix_exp:
            if symbol.isdigit():
                self.stack.append(int(symbol))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if symbol == "+":
                    res=a+b

                elif symbol =="-":
                    res = a-b
                elif symbol =="*":
                    res = a*b
                elif symbol =="/":
                    res = a/b
                self.stack.append(res)
        return self.stack[0]
postfix = "432*+5-"
ob = postfixEvaluator(postfix)
print("postfix expression",postfix)
print("result:",ob.evaluate())


#INFIX TO POSTFIX CONVERSION
#STEP1:READ SYMBOLS FROM LEFT TO RIGHT
STEP2:IF SYMBOL IS OPERAND(NUM OR VAR),PRINT IT TO RES
STEP3:IF SYMBOL IS '(' , PUSH IT ONTO STACK
STEP4:IF SYMBOL IS ')' , POP AND PRINT ALL OPERATORS FROM STACK UNTIL '(' IS FOUND, THEN DISCARD '('
STEP5: IF SYMBOL IF (+,-,*,/)"
    - POP AND PRINT HIGHER OR EQUAL PRECEDENCE OPERATOR FROM STACK
    - PUSH THE CURRENT OPEARTOR ONTO THE STACK
STEP6: AFTER READING ALL SYMBOLS, POP AND PRINT ANY REMAINING OPERATORS FROM THE STACK
# EXAMPLES:
# 1.A^B*C/(D*E-F) ------->  ANS:AB^C*DE*F-/
# 2.A+B*C-D/E     ------->  ANS:ABC*+DE/-

1.A^B*C/(D*E-F) ------->  ANS:AB^C*DE*F-/
SCANNED SYMBOL            STACK            OUTPUT
------------              -------          ---------
A                         -----            A
^                         ^                A
B                         ^                AB
*                         *                AB^  [PRE(^)>=pre(*),pop ^ and add to result,push*]
C                         *                AB^C
/                         /                AB^C* [pre(*)==pre(/),pop ^ and add to result, push *]
(                         /,(              AB^C*
D                         /,(              AB^C*D
*                         /,(,*            AB^C*D
E                         /,(,*            AB^C*DE  [pre()>=pre(*), pop ^ and add to result , push *]
-                         /,(,-            AB^C*DE*
F                         /,(,-            AB^C*DE*F
)                         /                AB^C*DE*F-
2.A+B*C-D/E     ------->  ANS:ABC*+DE/-
SCANNED SYMBOL            STACK            OUTPUT
------------              -------          ---------
A                         -----            A
+                          +               A
B                          +               AB
*                          +,*             AB
C                          +,*             ABC
-                          -               ABC*+
D                          -               ABC*+D
/                          -,/             ABD*+D
E                           -,/            ABC*+DE
---                         ----           ABC*+DE/-
'''
#CODE
def infix_to_postfix(infix):
    stack = []
    output = []
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    for symbol in infix:
        if symbol.isalnum():
            output.append(symbol)
        elif symbol == '(':
            output.append(symbol)
        elif symbol == ')':
            while stack and stack[-1]!='(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!='(' and precedence[symbol]<=precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(symbol)
    while stack:
        output.append(stack.pop())
    return "".join(output)
print(infix_to_postfix('A+B*C-D/E'))
        







        
