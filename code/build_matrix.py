'''

Reads all documents in the collection file into memory and writes
term-document incidence matrix to the processed folder.

The program will be run from the root of the repository.

'''

import sys
import json
import preprocessing # implements tokenize and normalize text


def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''

    assert type(collection) == str
    corpus_file = './collections/' + collection + extension

    documents = {}

    # TODO: fill in the rest and check for errors

    print(f'{len(documents)} documents read in total')
    return documents

def build_incidence_matrix(documents):
    '''
    Build term-document incidence matrix.
    Documents are given as mappings id -> text.
    '''

    assert type(documents) == dict

    matrix = {}
    tokenized = {}
    
    for docID in documents:
        original_text = documents[docID]
        tokenized[docID] = normalize(tokenize(original_text))

    # TODO: fill in the rest

    return matrix


def write_matrix(collection, matrix):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(matrix) == dict
    matrix_file = './processed/' + collection + '.matrix.json'
    
    # TODO: fill in the rest
    

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well

    exit(0)