import pandas as pd

my_types = {
        'Species' : 'string',
        'Kingdom' : 'string',
        'Class'   : 'string',
        'Assembly status' : 'string',
        'Number of genes' : 'Int64',
        'Number of proteins' : 'Int64'
    }

euk = pd.read_csv("eukaryotes.tsv", sep="\t", dtype = my_types, na_values=['-'])
#print (euk.info())
#A
euk_float = euk[euk['Size (Mb)']<4000].dropna()
print(euk_float.info())
#B
euk_filtered = euk.loc[(euk['Number of proteins']/euk['Number of genes'])>=1.1]
print(euk_filtered.info())
#C
euk_fungal = euk.loc[(euk['Kingdom']=="Fungi")&(euk['Size (Mb)']>100),"Species"]
print(euk_fungal.head)