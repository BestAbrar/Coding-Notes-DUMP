import pandas as pd
import seaborn as ses
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''Q1'''
#1.
df = pd.read_csv('elves_data.csv')
print(df.info())
print(df.describe())
#2.
for elf in df.iloc():
    print(elf)
#3.
ear_size = []
GC_content = []
for elf in df.iloc:
    if(elf["ear_length_cm"]>10):
        ear_size.append("Large")
    else:
        ear_size.append('Small')
    GC_only = len(elf["DNA_seq"].replace("A","").replace("T",""))
    GC_content.append(GC_only/len(elf["DNA_seq"]))

df["ear_size"] = ear_size
df["GC%"]=GC_content

print(df.info())
print(df.describe())
#4
df_new = df.loc[:, ["elf_ID","ear_size","GC%"]]
#5
df_short = df.loc[:, ["ear_size","GC%"]]
groups = df_short.groupby("ear_size")
print(groups.mean())
#6
df_GCOnly = df["GC%"]
df_GCOnly.to_csv("grangers_analysis.csv", header=False)

'''Q2'''
df = pd.read_csv("Mammal_lifehistories_v2.txt", sep="\t", na_values=['-999', '-999.00'])
df = df.loc[:, ["order","mass(g)","newborn(g)"]].dropna()
print(df.info())
print(df.describe())
#1.
ses.scatterplot(data=df, x="mass(g)", y="newborn(g)")
plt.title("adult mass vs. newborn mass")
plt.savefig("Q2_part1.png")
plt.close()
#2.
df["Log(mass(g))"]=np.log(df["mass(g)"])
df["Log(newborn(g))"]=np.log(df["newborn(g)"])
ses.scatterplot(data=df, x=("Log(mass(g))"), y="Log(newborn(g))")
plt.title("log (base 10) of adult mass vs. the log (base 10) of newborn mass")
plt.savefig("Q2_part2.png")
plt.close()
#3
df_Rodentia = df[df["order"]=="Rodentia"]
ses.scatterplot(data=df_Rodentia, x=("Log(mass(g))"), y="Log(newborn(g))")
plt.title("log (base 10) of adult mass vs. the log (base 10) of newborn mass \n for order Rodentia")
plt.savefig("Q2_part3.png")
plt.close()
#4
ses.scatterplot(data=df, x=("Log(mass(g))"), y="Log(newborn(g))",
                hue="order", alpha = 0.7)
plt.title("log (base 10) of adult mass vs. the log (base 10) of newborn mass \n by order")
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()
plt.savefig("Q2_part4.png")
plt.close()
#5
grouped = df.groupby("order")

fig, ax = plt.subplots(4, 4, figsize=(10, 7))

row=0
col=0
for g in grouped:
    if col<=3:
        ses.scatterplot(data = g[1], x=("Log(mass(g))"), y="Log(newborn(g))",ax=ax[row, col])
        ax[row,col].set_title(g[0])
        col += 1
    if col == 4:
        col=0
        row+=1
plt.tight_layout()
plt.savefig("Q2_part5.png", dpi=300, bbox_inches="tight")
plt.close()