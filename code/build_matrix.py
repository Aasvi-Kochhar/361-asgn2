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
    corpus_file = './collections/' + collection + extension
    documents = {}

    # From A1
    # with open(corpus_file, "r") as file:
    with open(os.path.join("ignore_this", "shortened.txt")) as file:
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
    
    for docID in documents:
        original_text = documents[docID]
        tokenized[docID] = preprocessing.normalize(preprocessing.tokenize(original_text))
    print(tokenized)

    # TODO: fill in the rest
    matrix["_M_"] = len(tokenized)
    print(matrix)
    # For each token found maybe count it? Idk

    return matrix


def write_matrix(collection, matrix):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(matrix) == dict
    matrix_file = './processed/' + collection + '.matrix.json'
    
    # Checking if the output file already exists in the processed folder
    if os.path.exists(matrix_file):
        print("Error, this output file already exists!")
        exit(1)
    
    # Dumping matrix into a new json file
    with open(matrix_file, "w") as output_file:
        json.dump(matrix, output_file, indent=3)

def test_tokenize():
    s = "I take a trip to the candy store to go and buy some treats."
    print(preprocessing.normalize(preprocessing.tokenize(s)))

def main():
    collection_name = sys.argv[1]
    documents = read_documents(collection_name)
    build_incidence_matrix(documents)

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well
    main()
    # test_tokenize()

    exit(0)