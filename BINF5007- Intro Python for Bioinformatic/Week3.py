# import math
# #print(help(math)) #prints documentation of 'math' package
# input_numb = int(input("Enter number "))
# try:
#     print(math.sqrt(input_numb))
# except ValueError as err: #except catches only 'ValueError' type errors, and stores the error as a variable
#                           #'err'
#     print("Number is negative")

"""
try returns value only when all conditions are acceptable (no errors present)
except returns only when there is error in the 'try' statment
this tool is great for debuging or excluding certain edge cases that would cause errors
in the code
"""

"""
note the indent <TAB> after 'try:' and 'except:' this is important for python, ensure
<TAB> is equivlent to 4 spaces depending on the editor used
"""

#dictionaries
my_dic = {'John':1234567890, 'Jack': 1987654321}
#add a new item to dictionary
my_dic['Jill']=6887274899
#retrive an item 
number = my_dic['Jack']
#Delete item
del(my_dic['John'])
#Modify a vanlue
my_dic['Jill'] = 1234567890

print(my_dic)
print(len(my_dic))

#making nested dictionaries

myNestedDic = {"test1":{"subtest1":[1,'A'],
                        "subtest2":[2,'B'],
                        "subtest3":[3,'C']},
                "test2":{"subtest1":[1,'D'],
                        "subtest2":[2,'E'],
                        "subtest3":[3,'F']},
                "test3":{"subtest1":[1,'G'],
                        "subtest2":[2,'H'],
                        "subtest3":[3,'I']}
                }
print(len(myNestedDic["test1"])) #print length of nested dictionary key 'test1'
print(myNestedDic['test2']['subtest2'][1]) #print index 1 of the list in key 'subtest2' in key 'test2'
