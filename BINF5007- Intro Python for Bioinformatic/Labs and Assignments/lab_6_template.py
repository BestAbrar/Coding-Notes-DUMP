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
print (euk.info())
