
from ipaddress import v6_int_to_packed
import math

operators = ["=", "+", "-", "*", "/", ">", "<", ">=", "<=", "==", "!=", "++"]
keywords = ["class", "if", "else", "switch", "return", "static", "void", "public", "private"]
loops = ["while", "for"]
datatypes = ["int", "float", "long", "double", "boolean", "String", "char"]

def isOp(v):
    for i in range(len(operators)):
        if operators[i] == v:
            return True
    return False


def isNum(v):
    return not math.isnan(float(v)) and math.isfinite(v)


def isDigit(str):
    return str >= "0" and str <= "9"


def isAlpha(str):
    return (str >= "a" and str <= "z") or (str >= "A" and str <= "Z") or str == "_"


def isAlphaNumeric(str):
    return isAlpha(str) or isDigit(str)


def isLoop(l):
    for i in range(len(loops)):
        if loops[i] == l:
            return True
    return False


def isKeyword(v):
    for i in range(len(keywords)):
        if keywords[i] == v:
            return True
    return False

def isDataType(v):
    for i in range(len(datatypes)):
        if datatypes[i] == v:
            return True
    return False
