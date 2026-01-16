import pandas as pd
import re
#gnomAD data
genes = ["CTNNB1", "KCNA1", "KMT2D", "MYCN", "PRDM6", "TP53"]
variants = {"CTNNB1":[], "KCNA1":[], "KMT2D":[], "MYCN":[], "PRDM6":[], "TP53":[]}
for gene in genes:
    file = "variants/"+gene+"/"+gene+"_variants.vcf"
    with open (file, "r") as f:
        for line in f:
            #ANN=T|stop_gained
            regex = "ANN=.+|([^|]+)"
            #c.-48-8872T>G
            regex = "c\..\d*.\d+[^|]+"
            match = re.search(regex,line)
            
            if match != None:
                variants[gene].append(match.group(0))