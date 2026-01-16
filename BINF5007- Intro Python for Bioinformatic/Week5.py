#if, elif and else statments
statment1 = True
statment2 = True
if (statment1): # if statment is true than will exicute code in block
    print("code inside if statment")
elif (statment2): #secondary if statment will only execute code in block when 'if' statment is not true
    print("code inside elif statment")
else: # will execute code only if the corrisponding 'if' statment or additional elif statments are false
    print("code inside else statment")

"""
OPERATORS and their oposites
== | !=
!= | ==
>  | <=
<  | >=

we can use 'and' and 'or' to combine conditional statments, not to get the opposite bool value of condition
"""
#Defining Methods, note python compiles line by line, so it's important to define the 
#functions before you run/call them (unlike java which is better IMO)
# def method name (parameters:parameter datatype)->return datatype:
def mymethod (myparameter:str)->dict:
    """
    Here is a discription of what 'mymethod' does,
    Good programming etiquit dictates that you include the following:
    1. Breif discription of the purpose of function (use case)
    2. Argument data type, sometimes with discription of purpose
    3. Return Data type
    4. Example of how to use the method
    5. Assumptions/Caution for values that will break the function
    """
    mydictionary = {'A':0,'T':0,'G':0,'C':0}
    for base in myparameter:
        mydictionary[base]+=1
    return mydictionary
def mymethod_v2 (myparameter:str)->str:
    """
    python only makes references of immutable values, what happens
    inside the function will not change the value of immutable variable outside the 
    function
    """
    myparameter += ", I can't change the parameter of this string outside this function"
    print("This is inside the function: ", myparameter)
    return myparameter
def mymethod_v3 (myparameter:list)->list:
    """
    However, python doesn't make reference to mutable values, it will change the value
    both inside and outside the function, PROCEED WITH CAUTION
    """
    myparameter += ["Imma mess up your list, hehe"]
    return myparameter

#Main code
argument = "ACGTAGATCGATCCCGGGGAGATAGC"
mymethod(argument)
print(argument)
argument_str = "This is my original string"
print("This is my string BEFORE calling the function",argument_str)
mymethod_v2(argument_str)
print("This is my string AFTER calling the function",argument_str)
argument_list = ["This is my original list"]
print("This is my list BEFORE calling the function",argument_list)
mymethod_v3(argument_list)
print("This is my list AFTER calling the function", argument_list)
"""
coincidentally after some testing, this only seems to work with concatination, if I try to assign a new
value to the parameter, it doesn't change the variable outside the function regardless if it's mutable
or not

"""