import sys
from sys import argv
import struct
from struct import *

# get encoded input file name from user
encoded_inputfile = sys.argv[1]  
# get input bit length from user
bit_length = sys.argv[2]  
bit_len = int(bit_length)
# create maximum table size from given input bit length
table_size = pow(2, bit_len)
# open encoded input file and read
file = open(encoded_inputfile, 'rb')
# empty string
s = ""
# array of compressed data
comp_data = []
nextcode = 256
dcomp_data = ""
# define dictionary 
dictionary_size = 256
dictionary = {i: chr(i) for i in range(dictionary_size)}   
                
# reading the encoded file.
while True:
    n = file.read(2)
    if len(n) != 2:
        break
    (data,) = unpack('>H', n)
    comp_data.append(data)

for code in comp_data:
    if not (code in dictionary):
        dictionary[code] = s + s[0]
    dcomp_data = dcomp_data + dictionary[code]
    if not (len(s) == 0):
        dictionary[nextcode] = s + (dictionary[code][0])
        nextcode = nextcode + 1
    s = dictionary[code]
    
# storing decoded data into output file name as "<input file name>_decode.txt"
outputfile = open(encoded_inputfile.split(".")[0] + "_decode.txt", "w")
for data in dcomp_data:
    outputfile.write(data)

outputfile.close()
file.close()
