# ==================================== INFIX => POSTFIX ====================================

def infixToPostfix(infixStack):
    
    operators = ['+', '-', '/', '*', '$', '(', ')']
    operatorStack = []  
    outputStack = [] # resulting postfix expression
    weights = {'$': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1} # assigning weights to each operator for correct precendence 

    for element in infixStack:
        if element not in operators:  # is an operand
            outputStack.append(element)

        elif element == '(':
            operatorStack.append(element)

        elif element == ')':
            while operatorStack[-1] != '(':  # transfer from operatorStack to outputStack until '(' is found
                outputStack.append(operatorStack.pop())
            operatorStack.pop()  # discards the '('
    
        else:  # is and operator
            while (operatorStack and operatorStack[-1] != '(' and ((weights[operatorStack[-1]] > weights[element]) or (weights[operatorStack[-1]] == weights[element] and element != '$'))):    
                outputStack.append(operatorStack.pop())
            operatorStack.append(element)

    # empties the rest of the operatorStack
    while operatorStack:
        outputStack.append(operatorStack.pop())

    return outputStack



# ==================================== INFIX => PREFIX ====================================

def infixToPrefix(infixStack):
    
    operators = ['+', '-', '/', '*', '$', '(', ')']

    # inverts the expression and flips the parentheses 
    inverseInfixStack = []
    for element in infixStack[::-1]:
        if element == '(':
            inverseInfixStack.append(')')
        elif element == ')':
            inverseInfixStack.append('(')
        else:
           inverseInfixStack.append(element)

    # logic similar to postfix conversion
    operatorsStack = []
    outputStack = []
    weights = {'$': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}

    for element in inverseInfixStack:
        if element not in operators:
            outputStack.append(element)
        elif element == '(':
            operatorsStack.append(element)
        elif element == ')':
            while operatorsStack and operatorsStack[-1] != '(':
                outputStack.append(operatorsStack.pop())
            operatorsStack.pop()
        else:
            while (operatorsStack and operatorsStack[-1] != '(' and ((weights[operatorsStack[-1]] > weights[element]) or (weights[operatorsStack[-1]] == weights[element] and element == '$'))):
                outputStack.append(operatorsStack.pop())
            operatorsStack.append(element)

    while operatorsStack:
        outputStack.append(operatorsStack.pop())

    # inverting the output
    prefixOutput = outputStack[::-1]
   
    return prefixOutput



# ==================================== CALCULATION OF NUMERIC RESULT ====================================

def calculate(infixStack):
    postfixStack = infixToPostfix(infixStack)
    valueStack = []
    operators = ['+', '-', '*', '/', '$']

    for element in postfixStack:
        if element not in operators:  # is a number
            valueStack.append(int(element)) # converts string to number
        else:
            op2 = valueStack.pop()
            op1 = valueStack.pop()

            if element == '+':
                result = op1 + op2
            elif element == '-':
                result = op1 - op2
            elif element == '*':
                result = op1 * op2
            elif element == '/':
                if op2 == 0:
                    raise ZeroDivisionError('Division by zero')
                result = op1 / op2
            elif element == '$':
                result = op1 ** op2

            valueStack.append(float(result))

    return valueStack[0]








# ==================================== TEST ====================================

testExpression = ['2','+','5','+','8','*','3','+','(','4','$','2','$','3','*','2',')','-','5','$','3']
postfixOutput = infixToPostfix(testExpression)
prefixOutput = infixToPrefix(testExpression)
valueOutput = calculate(testExpression)

print('')
print('===============================================')
print('')
print(f"Infix Expression: {testExpression}")
print('')
print(f" - Postfix Output: {postfixOutput}")
print('')
print(f" - Prefix Output: {prefixOutput}")
print('')
print(f" - Numeric Result: {valueOutput}")
print('')
print('===============================================')
print('')