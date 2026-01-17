#Curl command used to download data over the internet (other than NCBI)
#NCBI has it's own set of API commands

efetch -db nucleotide -id KJ946236.1 -format fasta > KJ946236.fasta