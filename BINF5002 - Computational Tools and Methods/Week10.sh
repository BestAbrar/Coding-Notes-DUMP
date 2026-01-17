#efetch -db sra -id SRR31123153 -format fastq > SRR31123153sra.fastq
#fasterq-dump SRR31123153 --concatenate-reads -p
prefetch SRR1972739 #download acession as a folder with SRA file
fastq-dump -X 10000 ./SRR1972739

#understanding fastq files
#line one refers to read ID
#line two is the read sequence
#line 3 is a spacer
#line 4 is Phred score indicating the confidence of each base call in
#ascii values (each ascii value has a corresponding quality score)

#refines fastq file to get rid of any potential artifacts + adaptor seqs
fastp -i SRR1972739.fastq -o SRR1972739_fastp.fastq -h fastp.html

#python3 -m http.server  443 #used to run a html server to visualize html
#files

