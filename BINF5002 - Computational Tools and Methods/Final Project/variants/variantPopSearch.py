import pandas as pd
import re
#gnomAD data
genes = ["CTNNB1", "KCNA1", "KMT2D", "MYCN", "PRDM6", "TP53"]
df = {}
for gene in genes:
    file_path="gnomAD/"+gene+".csv"
    df[gene] = pd.read_csv(file_path)
# print(df["CTNNB1"].info())
variants = {"CTNNB1":[], "KCNA1":[], "KMT2D":[], "MYCN":[], "PRDM6":[], "TP53":[]}
for gene in genes:
    file = "variants/"+gene+"/"+gene+"_variants.vcf"
    with open (file, "r") as f:
        for line in f:
            #c.-48-8872T>G
            regex = "c\..\d*.\d+[^|]+"
            match = re.search(regex,line)
            if match != None:
                variants[gene].append(match.group(0))

df_found={}
df_unfound={"CTNNB1":[], "KCNA1":[], "KMT2D":[], "MYCN":[], "PRDM6":[], "TP53":[]}
for gene in variants:
    df_found[gene] = df[gene][df[gene]['HGVS Consequence'].isin(variants[gene])]
    for variant in variants[gene]:
        if variant not in df[gene]['HGVS Consequence']:
            df_unfound[gene].append(variant)
# print(df_unfound)
# for gene in df_unfound:
#     for variant in df_unfound[gene]:
#         print(variant)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(str(df_found))

# for gene in genes:
#     with open ("variants/"+gene+"/"+gene+"_observed_variants.txt","w") as file:
#         for variant in df_found[gene].iloc:
#             file.write(str(variant)+"\n") 
for gene in df_unfound:
    with open ("variants/"+gene+"/"+gene+"_unobserved_variants.txt","w") as file:
        for varaint in df_unfound[gene]:
            file.write(str(variant)+"\n")
with open ("observed_variants.txt","w") as file:
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        file.write(str(df_found))
with open ("unobserved_variants.txt","w") as file:
    for gene in df_unfound:
        file.write(gene+"\n")
        for variant in df_unfound[gene]:
            file.write(variant+"\n")
