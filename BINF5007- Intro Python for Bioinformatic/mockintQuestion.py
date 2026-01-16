genesDic = {}
gene_symbols = ["TP53", "EGFR", "BRCA1", "KRAS", "TP53", "MYC", "PTEN", "EGFR", "KIT", "PDCD1", "BRAF", "KRAS", "CTLA4", "APC", "TP53", "ALK", "JUN", "BRCA2", "KRAS", "PTEN"]
for genes in gene_symbols:
    if (genes in genesDic):
        genesDic[genes] += 1
    else :
        genesDic[genes] = 1
maxVal = max(genesDic.values())
print(genesDic)
print(list(genesDic.keys())[list(genesDic.values()).index(maxVal)])
