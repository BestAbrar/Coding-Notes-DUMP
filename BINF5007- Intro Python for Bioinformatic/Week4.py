#FOR loops and WHILE loops
#for loop using intiger values
for x in range(1,10):
    print(x)
#for loop using string/char values
string = "this is a string"
for x in string:
    print(x)
#for loop using string/char and int
for x, y in enumerate(string):
    if (string[x]=='a'):
        print(y)
#for loop using list values
mylist = [1 ,2 ,3 , 'A', 'B', 'C']
for x in mylist:
    print(x)
#while loop, perform iteration only while condition is 'TRUE'
x = 0
while x < len(string):
    print(x < len(string))
    x += 1
#'break' can be used to exit a loop when a condition is meet
x = 0
while x < len(string):
    if(x==4):
        print(string[x])
        break
    x += 1
