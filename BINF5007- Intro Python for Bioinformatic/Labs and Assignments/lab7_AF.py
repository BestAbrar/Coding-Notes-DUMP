import re
genes = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455","xjhd53e", "45da", "de37dp"]
regexs= ["5","d.*e","d.e","d.*e|e.*d","d[arp]$"]

for regex in regexs:
    print ("accession names that satisfy the following regex expression: "+regex)
    for gene in genes:
        match = re.findall(regex,gene)
        if match!=[]:
            print(gene)
    