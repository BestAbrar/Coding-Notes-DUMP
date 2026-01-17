echo "Executing pipeline..."
# echo "Downloading Refseq fasta file"
# efetch -db nucleotide -id NC_000017.11 -format fasta > NC_000017.fasta
# echo "Downloading Disease seq file"
# prefetch  SRR35529488
# echo "converting fastq to fasta file"
# fastq-dump SRR35529488
REFERENCE_ACCESSION="AF086833"
DISEASE_ACCESSION="SRR1972739"

echo "Downloading Reference Data"
efetch -db nucleotide -id $REFERENCE_ACCESSION -format fasta > $REFERENCE_ACCESSION.fasta

# echo "Downloading Disease Data"
# prefetch $DISEASE_ACCESSION

# echo "Converting SRA file into FASTQ file"
# fastq-dump $DISEASE_ACCESSION

# echo "Cleaning Disease Data set"
# fastp -i SRR1972739.fastq -o SRR1972739_fastp.fastq -h fastp.html

# echo "index fasta file for alignment"
# bwa index $REFERENCE_ACCESSION.fasta

echo "Fastq file"
bwa mem $REFERENCE_ACCESSION.fasta $DISEASE_ACCESSION.fastq > output.sam

echo "Pipeline executed successfully"