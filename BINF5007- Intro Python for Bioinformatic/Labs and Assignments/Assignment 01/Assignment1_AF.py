#2.
DNA_Seqs = ["ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC",
            "ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT",
            "ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC",
            "ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA",
            "ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA"]
for index, seq in enumerate(DNA_Seqs):
    DNA_Seqs[index] = seq[14:]
    print("Cleaned Seq: "+DNA_Seqs[index])
    print("Cleaned Seq length: "+ str(len(DNA_Seqs[index])))

import random
#3.
random_DNA_String = ""
nucleotides = ["A","T","G","C"]
counter = {"A":0,"T":0,"G":0,"C":0}
for base in range (0,1001):
    nuc = nucleotides[random.randint(0,3)]
    random_DNA_String += nuc
    counter[nuc]+=1
print(random_DNA_String)
for key in counter:
    print("The nucleotide \'"+key+"\' is "+ str(round(counter[key]/1001*100, 2))+"% of the sequence")
#no the random_DNA_String is not the same after each run



