test_genes=['BRCA1','TP53','EFGR','CFTR','TNF'] #LIST
print(test_genes)
test_genes.append("MLH1")

temp = ['ABL1','KMT2A','RB1']
test_genes.extend(temp) #note List is mutible, append/extend changes the 'test_genes' list, original is lost

#Indexing, Slicing and Insertion of Lists
sub_list = test_genes [1:4] #slice values from index 1 to length 4 (index 3)
sliced_list = test_genes [::2] #slice every other item in list 'test_genes'
print(sub_list)
print(sliced_list)
test_genes[1:1]=["BRCA2"] #insert 'BRCA2' between 'BRCA1' and 'TP53'
print(test_genes)

test_genes = "BRCA1,TP53,EFGR,CFTR,TNF"
first_char = test_genes[0]
sub_string = test_genes[6:10] #slicing and indexing works on strings as well, however, recall strings are immutable
print(first_char)
print(sub_string)

#Combining two lists
new_listConcatination1 = sub_list+sliced_list #concatination, can only concatinate list type values
print(new_listConcatination1)                 #note this preserves the original 'sub-list' and 'sliced_list'

new_listConcatination2 = sub_list
new_listAppended = sub_list
new_listExtend = sub_list

new_listConcatination2+=sliced_list #same as concatinate, *note* this changes 'new_listConcatination2' like append
                                    #and extend

new_listAppended.append(sliced_list) #appends item to end of list 'sub_list', argument not exclusive to list
                                                #note, item added to last index, and results in nested list
new_listExtend.extend(sliced_list) #Extend item(s) to end of list, extends the last index to the 
                                              #lenght of added (extended) list, argument not exclusive to list
print(new_listConcatination2)
print(new_listAppended)
print(new_listExtend)

#other useful methods
test_genes = "BRCA1,TP53,EFGR,CFTR,TNF" #stored as a tuple
test_genes = test_genes.split(",") #'split' will convert a immutable type string into a list and preserve original
                                   #string variable
sentence = "What a cool sentence"
words = sentence.split() #default argument is space/blank
print(words)
print(test_genes)

test_genes = ",".join(test_genes) #opposite of split method, converts list type into string
print(test_genes)