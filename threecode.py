#!/usr/bin/env python
# coding: utf-8

# In[3]:


def findMinusBracket(listOfExpression):
    minuses = [i for i, x in enumerate(listOfExpression) if x == "-" ]
    for minusIndex in minuses:
        if listOfExpression[minusIndex + 1] == "(":
            return minusIndex
    return False

def findBracket(listOfExpression):
    brackets = [i for i, x in enumerate(listOfExpression) if x == "(" ]
    for minusIndex in brackets:
        return minusIndex
    return False

def findMinuses(listOfExpression):
    minuses = [i for i, x in enumerate(listOfExpression) if x == "-"]
    pattern = re.compile("[A-Za-z0-9]+")
    for minusIndex in minuses:
        if pattern.fullmatch(listOfExpression[minusIndex + 1]):
            return minusIndex
    return False
        
def findPluses(listOfExpression):
    pluses = [i for i, x in enumerate(listOfExpression) if x == "+"]
    pattern = re.compile("[A-Za-z0-9]+")
    for plusIndex in pluses:
        if (
            pattern.fullmatch(listOfExpression[plusIndex - 1])
            and
            pattern.fullmatch(listOfExpression[plusIndex + 1])
        ):
            return plusIndex
    return False

def findMultiply(listOfExpression):
    multiplies = [i for i, x in enumerate(listOfExpression) if x == "*"]
    pattern = re.compile("[A-Za-z0-9]+")
    for multiplyIndex in multiplies:
        if (
            pattern.fullmatch(listOfExpression[multiplyIndex - 1])
            and
            pattern.fullmatch(listOfExpression[multiplyIndex + 1])
        ):
            return multiplyIndex
    return False

def findDivide(listOfExpression):
    divides = [i for i, x in enumerate(listOfExpression) if x == "/"]
    pattern = re.compile("[A-Za-z0-9]+")
    for divideIndex in divides:
        if (
            pattern.fullmatch(listOfExpression[divideIndex - 1])
            and
            pattern.fullmatch(listOfExpression[divideIndex + 1])
        ):
            return divideIndex
    return False
    
def engine(expression):
    listOfExpresion = expression.split()
    counter = 1
    while True:
        brackets = findBracket(listOfExpresion)
        if type(brackets) == int:
            sring = str("T" + str(counter))
            print(sring 
                  + 
                  " = " 
                  + 
                  str(listOfExpresion[brackets]) 
                  +
                  " "
                  + 
                  str(listOfExpresion[brackets+1])
                  +
                  " "
                  + 
                  str(listOfExpresion[brackets+2])
                  +
                  " "
                  + 
                  str(listOfExpresion[brackets+3])
                  +
                  " "
                  + 
                  str(listOfExpresion[brackets+4]))
            listOfExpresion[brackets]  = sring
            listOfExpresion.pop(brackets+1)
            listOfExpresion.pop(brackets+ 1)
            listOfExpresion.pop(brackets +1)
            listOfExpresion.pop(brackets + 1)
            counter += 1
            print(" ".join(listOfExpresion))
        else:
            break
            
    while True:
        minuses = findMinuses(listOfExpresion)
        if type(minuses) == int:
            sring = str("T" + str(counter))
            print(sring + " = " + str(listOfExpresion[minuses]) + str(listOfExpresion[minuses+1]))
            listOfExpresion[minuses]  = sring
            listOfExpresion.pop(minuses + 1)
            counter += 1
            print(" ".join(listOfExpresion))
        else:
            break
    
    while True:
        multiplies = findMultiply(listOfExpresion)
        if type(multiplies) == int:
            sring = str("T" + str(counter))
            print(sring + " = " + str(listOfExpresion[multiplies - 1]) +" "+ str(listOfExpresion[multiplies]) +" "+ str(listOfExpresion[multiplies+1]))
            listOfExpresion[multiplies - 1]  = sring
            listOfExpresion.pop(multiplies + 1)
            listOfExpresion.pop(multiplies)
            counter += 1
            print(" ".join(listOfExpresion))
        else:
            break
            
    while True:
        divides = findDivide(listOfExpresion)
        if type(divides) == int:
            sring = str("T" + str(counter))
            print(sring + " = " + str(listOfExpresion[divides - 1]) +" "+ str(listOfExpresion[divides]) +" "+ str(listOfExpresion[divides+1]))
            listOfExpresion[divides - 1]  = sring
            listOfExpresion.pop(divides + 1)
            listOfExpresion.pop(divides)
            counter += 1
            print(" ".join(listOfExpresion))
        else:
            break
            
    while True:
        pluses = findPluses(listOfExpresion)
        if type(pluses) == int:
            sring = str("T" + str(counter))
            print(sring + " = " + str(listOfExpresion[pluses - 1]) +" "+ str(listOfExpresion[pluses]) +" "+ str(listOfExpresion[pluses+1]))
            listOfExpresion[pluses - 1]  = sring
            listOfExpresion.pop(pluses + 1)
            listOfExpresion.pop(pluses)
            counter += 1
            print(" ".join(listOfExpresion))
        else:
            break
    return listOfExpresion

import re
expression = str(input("Please Enter the expression you would like to change to Three Address Code:"))
engine(expression)


# In[ ]:




