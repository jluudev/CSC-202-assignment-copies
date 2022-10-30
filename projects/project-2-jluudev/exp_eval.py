from stack_array import Stack
from typing import Union


# You should not change this Exception class!
class PostfixFormatException(Exception):
    """An excelption for when a postfix string is not well-formed"""
    pass


def calc(operand_1: Union[int, float], operand_2: Union[int, float], token: str) -> Union[int, float]:
    """Helper function to evaluate two operands by a token in a postfix expression"""
    '''Input argument: two operands that are either an int or float and either + - * / ** >> << as a token.
     Returns an int or float that is the evaluation of the two operands by the token
     Raises a PostfixFormatException if the token is invalid.
     '''

    if token == "+":
        return operand_2 + operand_1
    elif token == "-":
        return operand_2 - operand_1
    elif token == "*":
        return operand_2 * operand_1
    elif token == "/":
        if operand_1 == 0:
            raise ValueError("division by zero")
        return operand_2 / operand_1
    elif token == "**":
        return operand_2 ** operand_1
    elif token == "<<":
        if operand_1 < 0:
            # raise PostfixFormatException("negative shift count")
            raise PostfixFormatException("Illegal bit shift operand")
        elif isinstance(operand_1, float) or isinstance(operand_2, float):
            # raise PostfixFormatException("unsupported operand type(s) for >>")
            raise PostfixFormatException("Illegal bit shift operand")
        return operand_2 * (2 ** operand_1)
    elif token == ">>":
        if operand_1 < 0:
            # raise PostfixFormatException("negative shift count")
            raise PostfixFormatException("Illegal bit shift operand")
        elif isinstance(operand_1, float) or isinstance(operand_2, float):
            # raise PostfixFormatException("unsupported operand type(s) for >>")
            raise PostfixFormatException("Illegal bit shift operand")
        return operand_2 / (2 ** operand_1)

    raise PostfixFormatException("Invalid token")


def postfix_eval(input_str: str) -> Union[int, float]:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack = Stack(30)
    token_list = input_str.split(" ")
    operators = ("+", "-", "*", "/", "**", "<<", ">>")

    if len(input_str) == 0:
        raise PostfixFormatException("Insufficient operands")

    for token in token_list:
        try:
            x = int(token)
        except:
            try:
                y = float(token)
            except:
                if token not in operators:
                    raise PostfixFormatException("Invalid token")

    for token in token_list:
        if token not in operators:
            if "." in token:
                op = float(token)
            else:
                op = int(token)
            stack.push(op)
        else:
            if stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")

            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.push(calc(operand_1, operand_2, token))

    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")

    return stack.pop()


def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    stack = Stack(30)
    postfix_str_list = []
    token_list = input_str.split(" ")
    operators = ("+", "-", "*", "/", "**", "<<", ">>", "(", ")")
    operators_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "**": 3, "<<": 4, ">>": 4}

    if len(input_str) == 0:
        raise PostfixFormatException("Insufficient operands")


    for token in token_list:
        try:
            x = int(token)
        except:
            try:
                y = float(token)
            except:
                if token not in operators:
                    raise PostfixFormatException("Invalid token")


    for token in token_list:
        if token not in operators:
            postfix_str_list.append(token)
        elif token == "(":
            stack.push("(")
        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix_str_list.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != "(" and operators_precedence[token] <= operators_precedence[stack.peek()] and token != "**":
                postfix_str_list.append(stack.pop())
            stack.push(token)

    while stack.size() != 0:
        postfix_str_list.append(stack.pop())

    return " ".join(postfix_str_list)


def prefix_to_postfix(input_str: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""

    stack = Stack(30)
    token_list = input_str.split(" ")
    operators = ("+", "-", "*", "/", "**", "<<", ">>")
    # postfix_str_list = []

    if len(input_str) == 0:
        raise PostfixFormatException("Insufficient operands")


    for token in token_list:
        try:
            x = int(token)
        except:
            try:
                y = float(token)
            except:
                if token not in operators:
                    raise PostfixFormatException("Invalid token")


    reversed_list = [token_list[len(token_list) - i] for i in range(1, len(token_list) + 1)]
    for token in reversed_list:
        if token not in operators:
            stack.push(token)
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()

            # stack.push(token)
            # stack.push(operand_2)
            # stack.push(operand_1)

            postfix_str = operand_1 + " " + operand_2 + " " + token
            stack.push(postfix_str)

    # while stack.size() != 0:
    # postfix_str_list.append(stack.pop())

    # postfix_str = " ".join(postfix_str_list)
    postfix_str = stack.pop()
    return postfix_str

# print(int(-75.2))
