import sys
from sys import argv
from struct import *

# get input file name from user
input_file = sys.argv[1]  
# get input bit length from user
bit_length = sys.argv[2]  
bit_len = int(bit_length)
# create maximum table size from given input bit length
table_size = pow(2, bit_len)
# open input file and read
file = open(input_file, 'r')
data = file.read()
# empty string
s = ""  
# array of compressed data
comp_data = []
# define dictionary 
dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}

# checking that input file is empty or not!
# if input file is empty then prompt message to user for provide non-empty file
while not data:
    print("Input file is empty...")
    input_file = input("\nPlease provide non-empty input file name : ")
    file = open(input_file, 'r')
    data = file.read()
    print('\nInput file data :' + data)
    print('==========================')

for symbol in data:
    str_symbol = s + symbol  
    if str_symbol in dictionary:
        s = str_symbol
    else:
        comp_data.append(dictionary[s])
        if (len(dictionary) <= table_size):
            dictionary[str_symbol] = dictionary_size
            dictionary_size = dictionary_size + 1
        s = symbol

if s :
    comp_data.append(dictionary[s])

# creating output file with the same as input file name with extension '.lzw'
outputfile = input_file.split(".")[0] + ".lzw"
print("Output file name : " + outputfile)
# open output file to write encoded text
open_outputfile = open(outputfile, "wb")
for data in comp_data:
    open_outputfile.write(pack('>H', int(data)))

open_outputfile.close()
file.close()
