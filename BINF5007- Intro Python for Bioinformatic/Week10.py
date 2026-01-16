from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import seq3
from Bio.SeqRecord import SeqRecord

example = Seq('ACTCTACGACATCACGACTAC')
'''
print(type(example)) #type of example is now Bio.Seq.Seq not string
print(example)
print(example.complement()) #prints the compliment of example
print(example.reverse_complement()) #print the reverse compliment of example
print(example.transcribe()) #transcription of example


#slicing Seq objects
print(example[:6]) #prints the first 6 bases of sequence
#using operators of Seq objects
print(example*2)
'''
'''
#using seq3 to print protien using 3 letter code
protein = example.translate()
protein_3lc = seq3(protein)
print(protein_3lc)
#Adding a hyphin inbetween each aminoacid
temp = ""
for i in range(0,int(len(protein_3lc)/3)):
    temp += protein_3lc[i*3:(i+1)*3]+"-"
print(temp[:-1])

'''
'''
record_single = SeqIO.read("example_single.fasta","fasta")
print(record_single)#print a summary of all the data in fasta file
print(record_single.seq) #print only the sequence from file
seq = record_single.seq
print(seq.complement()) #print the compliment of the sequence
'''
'''
records_subset = []
for record in SeqIO.parse("example_multiple.fasta", "fasta"):
    print(record.description, len(record.seq))
    if(len(record.seq)<700):
        records_subset.append(record)
SeqIO.write(records_subset,"records_subset.mfa","fasta")
'''
'''
multiple_subset = SeqIO.parse("records_subset.mfa", "fasta")
for record in multiple_subset:
    print(record.description, len(record.seq))
'''