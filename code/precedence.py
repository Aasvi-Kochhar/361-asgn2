'''

Implements the functions to "fix" the precendence of operators in the 
query expression provided by the user by "wrapping" higher precedence
subexpressions in parenthesis, making sure that:

1. parenthesis provided by the user are left untouched.
2. :not: operators are "fixed" first.
3. :and: expressions are "fixed" next.

'''

def find_par_exp_forward(expression):
    '''
    Finds the index of the token within expression correspondin to the end of 
    the parenthetical expression in front of a :not: or an :and: operator.
    '''
    assert type(expression) == list
    depth = 0
    

def find_par_exp_backward(expression):
    '''
    Finds the index of the token within expression correspondin to the start of 
    the parenthetical expression behind an :and: operator.
    '''
    assert type(expression) == list
    depth = 0

def fix_precedence_NOT(expression):
    '''
    Finds and "wraps" all :not: exp in the query expression as discussed in class.
    '''
    assert type(expression) == list

def fix_precedence_AND(expression, start=0):
    '''
    Finds and "wraps" all exp1 :and: exp2 in the query expression as discussed in class.
    '''
    assert type(expression) == list

def fix_precedence(expression):
    '''
    Fixes the precedence of an entire expression
    '''
    
    assert type(expression) == list
    step1 = fix_precedence_NOT(expression)
    step2 = fix_precedence_AND(step1)
    
    return step2