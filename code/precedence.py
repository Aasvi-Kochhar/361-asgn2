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
    Finds the index of the token within expression corresponding to the end of 
    the parenthetical expression in front of a :not: or an :and: operator.
    Translation: finds matching closing parenthesis ")" after the first "(" it finds
    '''

    assert type(expression) == list
    depth = 0
    for i in range(len(expression)):

        if expression[i] == "(":
            depth += 1

            # Search for mathing closing ")"
            for j in range(i+1, len(expression)):
                if expression[j] == "(":
                    depth += 1
                elif expression[j] == ")":
                    depth -= 1

                    # Check to see if we are back at depth = 0 now which means we found matching ")"
                    if depth == 0:
                        return j
                    
    print("Error: invalid query expression!")
    exit(1)
    

def find_par_exp_backward(expression):
    '''
    Finds the index of the token within expression correspondin to the start of 
    the parenthetical expression behind an :and: operator.
    Translation: starting at the last item, go backwards and find a matching "(" for the first ")" it finds
    '''
    assert type(expression) == list
    depth = 0

    for i in range(len(expression) - 1, -1, -1):
        if expression[i] == ")":
            depth += 1
            
            # Start at the end and go backwards
            for j in range(i - 1, -1, -1):
                if expression[j] == ")":
                    depth += 1
                elif expression[j] == "(":
                    depth -= 1

                    # Check to see if we are back at depth = 0 now which means we found matching "("
                    if depth == 0:
                        return j
                    
    print("Error: invalid query expression!")
    exit(1)

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