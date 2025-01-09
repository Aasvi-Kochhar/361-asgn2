'''

Reads in a collection and a Boolean query and prints to STDOUT
the IDs of documents in the collection satisfying the query expression.

The program will be run from the root of the repository.

'''

import sys
import preprocessing # implements tokenize and normalize text
import precedence # implements the functions to fix precedece

'''
Below are the implementation of the basic boolean operators on bit vectors
'''
def term_vector(term):
    assert term in matrix and len(matrix[term]) == matrix['_M_']
    return matrix[term]

def AND(vector1, vector2):
    assert len(vector1) == matrix['_M_'] and len(vector2) == matrix['_M_']
    # TODO: fill in the rest

def OR(vector1, vector2):
    assert len(vector1) == matrix['_M_'] and len(vector2) == matrix['_M_']
    # TODO: fill in the rest

def NOT(vector):
    assert len(vector) == matrix['_M_']
    # TODO: fill in the rest

'''
Below are the other key functions for the assignment.
'''

def read_matrix(collection):
    '''
    Reads a term-document incidence matrix (inside the 'processed' folder).
    '''
    queries_file = './processed/' + collection + extension

    # TODO: fill in the rest
    return matrix

def document_ids(vector):
    '''
    Returns a list with the IDs of documents corresponding to non-zero entries 
    in the matrix.
    '''
    assert len(vector) == matrix['_M_']

    # TODO: fill in the rest

def solve_expression(stack):
    '''
    Returns the result of the expression at the top of the stack 
    (as discussed in class)
    '''
    assert type(stack) == list

    # TODO: fill in the rest
    # TODO: check for errors -- like operators out of place or missing terms


def answer(tokenized_query):
    '''
    Implements the algorithm for solving expressions discussed in class.
    Must call solveExpression(...) eventually.
    '''
    assert type(tokenized_query) == list
    
    stack = [] # start with empty stack

    # TODO: fill in the rest

    answer_vector = stack.pop()
    assert len(answer_vector) == matrix['_M_']
    return document_ids(answer_vector)


def tokenize_and_answer(query_expression):
    '''
    Takes a query expression (string), tokenizes it, calls fix_precedence to
    add parenthesis as discussed in class, and calls answer to solve the
    query and return the ids.
    '''
    assert type(query_expression) == str

    fixed_precedence = fix_precedence(query_expression.split())
    tokenized_query = []

    reserved = set(['(', ')', ':and:', ':or:', ':not:'])

    for token in fixed_precedence:
        if token in reserved:
            tokenized_query.append(token)
        else:
            # note: tokenize/normalize work with lists but we expect a single word here
            terms = normalize(tokenize(token))
            assert len(terms) == 1
            tokenized_query.append(terms[0])

    return answer(['('] + tokenized_query + [')'])


matrix = {}

if __name__ == "__main__":
    '''
    "main()" function goes here
    '''
    # TODO: read the collection name from command line
    # TODO: read query expression from command line
    # TODO: check for invalid parameters
        
    matrix = read_matrix()
    assert type(matrix) == dict  # matrix must be as in the specs

    # print the IDs of the documents satisfying the query, one per line
    for docID in tokenize_and_answer(query_expression):
        print(docID)

    exit(0)