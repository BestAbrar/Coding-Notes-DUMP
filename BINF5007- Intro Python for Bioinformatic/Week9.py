#REGEX
'''
in order to use regex, you must import the module into the python file
'.' (wild card character) used to match any character
'*' used to match 0 or more times
'+' used to match 1 or more times
'^' use to match only the first character of a line/string
'$' used to match the last character of a line/string
'\S' used to match all non-white space characters
'\s' used to match only white spaces
'?' lazy match modifier used to match shortest possible match
[] inclusive selection inside square bracket (select if an element inside bracket)
{} repetition
() capture only desired part of a match (refine extraction of regular expression)
'''
import re
dna_seq1 = "ACGTGATACATGTACGCA"
dna_seq2 = "ACGGCAACGGCAACGGCA"

regex1 = "ACG.*GCA" #match starting phrase 'ACG' and ending phrase 'GCA'
regex2 = "ACG[ATGC]*?GCA" #refers to match with only the following characters 'A','T','G','C' 0 or more times


print(re.search(regex1, dna_seq1))
print(re.search(regex2, dna_seq2)) #finds the largest match, only finds one match

match = re.search(regex2, dna_seq1)
print(match.start()) #print the starting index of the match
print(match.end()) #print the ending index of the match
print(match.span()) #print a tuple with the start and end of the match
print(match.string) #print the string matching the regex searched

print(re.findall(regex2, dna_seq1))
print(re.findall(regex2, dna_seq2)) #finds all the matches for regex in string as a list, starting with first occurance
