'''

Reads all documents in the collection file into memory and writes
term-document incidence matrix to the processed folder.

The program will be run from the root of the repository.

'''

import sys
import json
import preprocessing # implements tokenize and normalize text
import os


def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''

    assert type(collection) == str
    extension = "_bool.ALL"
    file = './collections/' + collection + extension
    documents = {}

    # From A1
    with open(file, "r") as file:
        current_id = 0
        content = ""
        previous_line = None

        while True:
            line = file.readline()
            # If unstripped line is empty, it is the end of the file 
            if not line:
                break
            line = line.strip()
            # Skip empty lines
            if not line:  
                continue
            # If line starts with ".I ", we are onto a new document
            if line.startswith(".I"):
                # if len(documents) == 3:  # Stop after 4 documents
                #     break
                #  Next line needs to start with .W
                if not file.readline().strip().startswith(".W"):
                    raise Exception("ERROR: Missing .W!")
                # Add any content to the dictionary if we have any
                if len(content.strip()) > 0:
                    documents[current_id] = content.strip()
                    content = ""
                # Get the ID after the ".I " 
                current_id = int(line[len(".I "):])
                previous_line = line
            # If line starts with ".W ", start reading the words/content
            elif line.startswith(".W"):
                if not previous_line.startswith(".I"):
                    raise Exception("ERROR: Missing .I!")
                else:
                    previous_line = line
                continue
            # Content of the document
            else:
                # Add a space between lines to avoid concatenation issues
                content += line + " "
                previous_line = line
        # Add remaining content if there's any
        if len(content.strip()) > 0:
            documents[current_id] = content.strip()

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
    
    for docID, text in documents.items():
       #original_text = documents[docID]
        tokenized[docID] = preprocessing.normalize(preprocessing.tokenize(text))
    
    matrix['_M_'] = len(documents) 

    # Create a row for each term and have the length be the number of documents
    for docID, tokens in tokenized.items():
        for term in tokens:
            if term not in matrix:
                matrix[term] = [0] * matrix['_M_']
    
    # Now we count the number of times a term appears in each document
    for docID, tokens in tokenized.items():
        for term in tokens:
            matrix[term][docID - 1] += 1

    return matrix


def write_matrix(collection, matrix):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(matrix) == dict
    matrix_file = './processed/' + collection + '.matrix.json'
    
    # Checking if the output file already exists in the processed folder
    if os.path.exists(matrix_file):
        raise Exception("Error, this output file already exists!")
    
    # Dumping matrix into a new json file
    with open(matrix_file, "w") as output_file:
        json.dump(matrix, output_file, indent=3)

def test_tokenize():
    s = "I take a trip to the candy store to go and buy some treats."
    print(preprocessing.normalize(preprocessing.tokenize(s)))

def main():
    try:
        collection_name = sys.argv[1]

        # throw an exception if if there are no files inside ./collections/ corresponding to the collection name provided
        split_collections = [os.path.splitext(i) for i in os.listdir("collections")]
        collections = [i[0] for i in split_collections if i[1] != ".md"]  # ignore readme file
        if collection_name + "_bool" not in collections:
            print("Error: no files corresponding to the collection name provided!")
            exit(1)

        documents = read_documents(collection_name)
        matrix = build_incidence_matrix(documents)
        write_matrix(collection_name, matrix)
        # print(matrix)
        # print(len(matrix))
    except Exception as e:
        print(e)
    else:
        print("SUCCESS")

if __name__ == "__main__":
    main()
    exit(0)