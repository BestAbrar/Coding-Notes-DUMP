'''
file_handle = open ("dna_strings.txt", "r")

#for line in file_handle:
#    print(line)
print(file_handle.read().split("\n"))
file_handle.close()
with open("dna_strings.txt", "r") as f:
    seq = f.read().replace("\n","")
baseCount = {'A':0,'T':0,'G':0,'C':0}
for base in seq:
    baseCount[base]+=1
#automatically closes file after block is executed
with open("dna_percentage.txt", "w") as f:
    f.write()
'''
import pandas as pd
'''
df = pd.DataFrame(
    {"Name":["Braun, Mr.Owen Harris", "Allen, Mr. William Henry","Bonnell, Miss Elizabeth"],
     "Age":[22,35,58],
     "Sex":["Male","Male","Female"]}
)
print(df)
'''
df = pd.read_csv('titanic.csv')
print(df.info())
print(df.describe())

print(df["Fare"])
print(df["Fare"].head())
print(df["Fare"].tail())

passangersWithKnownAge=df[df['Age'].notna()] #.notna filters out values that are missing or 'None'
passangersOld = passangersWithKnownAge[passangersWithKnownAge['Age']>25] #[] used to select rows
passangersYoungSurvived = passangersWithKnownAge[(passangersWithKnownAge['Age']<18) & (passangersWithKnownAge['Survived']==1)]
#when combining multiple filters, and = '&' and or = '|', ensure all conditionals are surrounded by paranthesis
print (len(passangersYoungSurvived)) #len function outputs number of rows in a dataframe
passangersYoungSurvived.to_csv("titanic_subset.csv", index = False)

subset_row_iloc = passangersYoungSurvived.iloc[9:22][["Name","Survived"]] #iloc used to select rows using index
print(subset_row_iloc)
subset_row_loc = passangersYoungSurvived.loc[9:22][["Name","Survived"]] #only prints line with labels between 9-22
print(subset_row_loc)
subset_rowcol_iloc = passangersYoungSurvived.iloc[9:22, 2:4] #selecting dataframe using both row and column (9:22 and 2:4 respectivily)
print(subset_rowcol_iloc)

groups = passangersYoungSurvived.groupby("Sex") #groups values by value into different sections
for g in groups:
    print(g)
print(groups["Age"].mean(),groups["Fare"].mean())#gives summary of the mean age in groups grouped by "Sex"
