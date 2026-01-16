import math
def convertable(num:str)-> bool:
    try:
        float(num)
        return True
    except:
        return False
def ValidNum (col:list) -> list:
    validCol = []
    for val in col:
        if(convertable(val) and val!="NaN" and type(val)!=None):
            validCol.append(float(val))
    return validCol
def Average(col:list) -> float:
    return sum(col)/len(col)
def Variance(col:list) -> float:
    if (len(col)==1):
        return 0
    mean = Average(col)
    total = 0
    for num in col:
        total += math.pow((num-mean),2)
    return total/(len(col)-1)
def Std_Dev(col:list) -> float:
    return math.sqrt(Variance(col))
def Median(col:list) -> float:
    col = sorted(col)
    if (len(col)%2==1):
        return col[int(len(col)/2)]
    else :
        return (col[len(col)//2]+col[len(col)//2-1])/2
def file_reader (file:str,col:int)->list:
    numbers = []
    try:
        with open (file, 'r') as infile:
            for line in infile:
                line = line.split("\t")
                if line[col] != None:
                    numbers.append(line[col])
                else:
                    numbers.append("NaN")
    except FileNotFoundError:
        print("The file:"+file+" has not been found")
        return None
    except IndexError:
        print("There is no valid 'list index' in column "+col+"in line 1 in file: "+file)
        return None
    return numbers
def col_stats (file:str,colNumb:int)->None:
    col = file_reader(file,column)
    try:
        valCol=ValidNum(col)
        if (len(valCol)!=0):
            stats = {"Count":len(col),
            "ValidNum":len(valCol),
            "Average":Average(valCol),
            "Maximum":max(valCol),
            "Minimum":min(valCol),
            "Variance":Variance(valCol),
            "Std Dev":Std_Dev(valCol),
            "Median":Median(valCol)}
            for metric in stats:
                print(metric+"="+str("{:.3f}".format(stats[metric])))
        else:
            print("There were no valid number(s) in column "+str(colNumb) +" in file: "+ file)
    except:
        print()


file = str(input("please enter data_file you wish to read from: "))
try:
    column = int(input("please enter column you wish to get stats for: "))
    if (type(column)==int):
        col_stats(file,column)
    else:
        print("Column is not a numerical value of type int")
except ValueError:
    print("Column is not a numerical value of type int")