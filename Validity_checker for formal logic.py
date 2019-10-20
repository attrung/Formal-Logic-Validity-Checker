# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:18:46 2019

@author: John Nguyen
"""

def process_premises(premise):
    """
    This function change a premise from a string to a list
    Input: String of premise
    Output: List of each characters
    
    Example: 
    process_premises('a^b')
    return ['a', '^', 'b']
    """
    processed_premise = []
    for char in premise:
        processed_premise.append(char)
    return processed_premise

def implication(a,b):
    """
    Input: atomic sentence a and b
    output: the implication a → b
    """
    return not a or b

def process_truth_value_premise(premise, dict_atomic):
    """
    This function changes all the atomic sentences ('a', 'b', 'c', 'd', etc.) into its true/false value for certain row
    of the truth table.
    
    Input: the premise and the dictionary showing the truth value of the atomic sentence
    Output: The premise after applying the truth value
    
    Example: 
    Input: process_truth_value_premise(['a', '^', 'b'], {'a': True, 'b': False})
    Output: [True, '^', False]
    
    """
    processed_truth_value_premise = []
    for char in premise:
        if char in dict_atomic.keys():
            processed_truth_value_premise.append(dict_atomic[char])
        else:
            processed_truth_value_premise.append(char)
    return processed_truth_value_premise

def parenthesis(processed_truth_value_premise):
    """
    This function deals with the parenthesis in a premise. What is in the parenthesis is returned as a list. This allows
    for an easier analyzation as we pass the premise through truthvalue(). If there is double parenthesis, a new list is created
    in the previous list.
    
    Input: The premise after process_truth_value_premise()
    Output: Premise where things in parenthesis is in list
    
    Example: 
    Input: [True, '/', '(', False, '^', True, ')']
    Output: [True, '/', [False, '^', True]]
    
    """
    i = 0
    while i < len(processed_truth_value_premise):
        if processed_truth_value_premise[i] == '(':
            list1 = []
            x = 0
            step = 0
            for j in range(i,len(processed_truth_value_premise)):
                list1.append(processed_truth_value_premise[j])
                step += 1
                if processed_truth_value_premise[j] == '(':
                    x += 1
                elif processed_truth_value_premise[j] == ')':
                    x -= 1
                if x == 0:
                    break
            list1 = parenthesis(list1[1:(len(list1)-1)])
            for index in range(i+1, j+1):
                processed_truth_value_premise.pop(i+1)
            processed_truth_value_premise[i] = list1
            i+= 1
        else:
            i += 1
    return processed_truth_value_premise

def truth_value(a):
    """ 
    This function takes in the premise processed by parenthesis() and return its truth value. 
    
    Some simple rules I used: 
    Recursion if an element is a list
    return the corresponding rule with symbols including ¬ (not), ^ (and), / (or), → (imply), and ↔ (if and only if)
    
    Input: Premise
    Output: Truth value of premise
    
    Example:
    Input: [True, '/', [False, '^', True]]
    Output: True
    
    """
    while len(a) != 1:
        for i in range(0, len(a)): #all the list (thing in parenthesis), must be solved first
            if type(a[i]) == list:
                a[i] = truth_value(a[i])
                
        for i in range(0, len(a)): #all the negation must be solved first
            if a[i] == '¬':
                a[i] = not a[i+1]
                a.pop(i+1)
            if i >= len(a) - 1: #avoid list out of index range error
                break
                
        for i in range(0,len(a)): #the 'and' and 'or' is solved next
            if a[i] == '^':
                a[i] = a[i-1] and a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            elif a[i] == '/':
                a[i] = a[i-1] or a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            if i >= len(a) - 1:
                break

        for i in range(0,len(a)): #the implication goes next
            if a[i] == '→':
                a[i] = implication(a[i-1], a[i+1])
                a.pop(i+1)
                a.pop(i-1)
            if i >= len(a) - 1:
                break
        
        for i in range(0,len(a)): #if and only if goes last
            if a[i] == '↔':
                a[i] = (a[i-1] == a[i+1])
                a.pop(i+1)
                a.pop(i-1)
            if i >= len(a) - 1:
                break
            
    return a[0]
    
def user_input():
    """ 
    This function allows users to input the premises.
    
    Requirements for input:
    Using connectives as followed: ^ (and), / (or), → (imply), ¬ (not), ↔ (if and only if), and () as parenthesis
    No space allowed 
    
    """
    num_premise = int(input("Number of premises: "))
    num_atomic = int(input("Number of atomic sentences: "))
    list_variable = []
    for i in range(0,num_atomic):
        list_variable.append(input("Atomic sentence number " + str(i+1) +": "))
    print('The allowed symbol for connectives are: ^ (and), / (or), → (imply), ¬ (not), ↔ (if and only if), and () (parentheses).')
    print('You can copy/paste the symbol from the line above to use for your input of premises')
    list_premises = []
    for i in range(0, num_premise):
        list_premises.append(input("Premise number " + str(i+1) +": "))
    conclusion = input("Conclusion is: ")
    conclusion = process_premises(conclusion)
    list_processed_premises = []
    for premise in list_premises:
        list_processed_premises.append(process_premises(premise))
    return list_variable, list_processed_premises, conclusion, list_premises

def valid_checker(a_list):
    """
    This takes in the argument from user_input and return the validity of the argument. 
    """
    list_variable = a_list[0]
    list_processed_premises = a_list[1]
    conclusion = a_list[2]
    print_premises = a_list[3]
    print(list_variable, print_premises, conclusion)
    k = False #there exist a situation where all premises are true and the conclusion is true
    m = True #there exist no situations where all the premises are true, but the conclusion is false
    n = len(list_variable)
    for i in range(0, 2**n): #considering all truth values that atomic sentences can have
        dict_atomic = {}
        for j in range(0, n):
            if (i//2**(n-j-1))%2 == 0: #different line of the truth table print out a different situation for the truth value of the atomic sentences
                dict_atomic[list_variable[j]] = True
            else:
                dict_atomic[list_variable[j]] = False
        for j in range(0, n):
            truth_value_premises = []
            for premise in list_processed_premises:
                processed_truth_value_premise = process_truth_value_premise(premise, dict_atomic)
                processed_truth_value_premise = parenthesis(processed_truth_value_premise)
                truth_value_premises.append(truth_value(processed_truth_value_premise))
            truth_value_conclusion = truth_value(process_truth_value_premise(conclusion, dict_atomic))
            if False not in truth_value_premises and truth_value_conclusion == True:
                k = True
            elif False not in truth_value_premises and truth_value_conclusion == False:
                m = False
        print(list(dict_atomic.values()), truth_value_premises, truth_value_conclusion)
    if k == m == True: 
        print('Valid')
    else: 
        print('Invalid')
        
valid_checker(user_input())