from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import seq3
from Bio.SeqRecord import SeqRecord

def details (record:SeqRecord)->None:
    print(record.id, record.seq, len(record.seq))

#1
records = SeqIO.parse("ProteinFasta.fasta", "fasta")
fastalist = []
for record in records:
    fastalist.append(record)
    print(record.id, record.seq, len(record.seq))

#2
print("There are: "+str(len(fastalist))+" records in the fasta file ProteinFasta.fasta")

#3
details(fastalist[0]) #first record
details(fastalist[-1]) #last record

#4
total_len = 0
for record in fastalist:
    total_len += len(record.seq)
print("Total length of all sequences is: "+str(total_len))

#5
filtered_fasta = []
for record in fastalist:
    if len(record.seq)>10:
        filtered_fasta.append(record)
SeqIO.write(filtered_fasta,"ProteinFasta_filtered.mfa","fasta")
