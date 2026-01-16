print("Hello World") #print values in perenthesis in a console/terminal window
dna_seq= "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #a string variable named 'dna_seq'
print(dna_seq.lower()) #'lower' - an example of a function that takes a immutable string and changes all characters to lower case
print(len(dna_seq)) #'len' a method (think of it as a pre-defined function) that outputs the lenght of a string
print(round(len(dna_seq)/4)) #round method will round values to nearest whole number by default

# ignore following code
# nucA=0
# nucT=0

# for x in dna_seq:
#     if (x=='A'):
#         nucA+=1
#     if (x=='T'):
#         nucT+=1
# print(nucA,nucT)


tup = ("item 1", "item 2", "item 3") #an tuple variable named 'tup' with only strings: "item 1", "item 2", "item 3"
tup1 = ("item 1", 1) #changes the variable 'tup' to contain different variable types : "item 1", 1
print(type(tup[1]))#'type' method gives the type of a variable -> outputs "str"
print(tup1)