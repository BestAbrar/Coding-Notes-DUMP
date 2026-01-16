print("Hello World")
dna_seq= "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_seq.lower())
print(len(dna_seq))
print(round(len(dna_seq)/4))
nucA=0
nucT=0

for x in dna_seq:
    if (x=='A'):
        nucA+=1
    if (x=='T'):
        nucT+=1
print(nucA,nucT)

print(str(0/0))