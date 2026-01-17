# echo "Executing pipeline..."
# # echo "Downloading Refseq fasta file"
# # efetch -db nucleotide -id NC_000017.11 -format fasta > NC_000017.fasta
# # echo "Downloading Disease seq file"
# # prefetch  SRR35529488
# # echo "converting fastq to fasta file"
# # fastq-dump SRR35529488
# # REFERENCE_ACCESSION="AF086833"
# # DISEASE_ACCESSION="SRR1972739"

# # echo "Downloading Reference Data"
# # efetch -db nucleotide -id $REFERENCE_ACCESSION -format fasta > $REFERENCE_ACCESSION.fasta

# # echo "Downloading Disease Data"
# # prefetch $DISEASE_ACCESSION

# # echo "Converting SRA file into FASTQ file"
# # fastq-dump $DISEASE_ACCESSION

# # echo "Cleaning Disease Data set"
# # fastp -i SRR1972739.fastq -o SRR1972739_fastp.fastq -h fastp.html

# # echo "index fasta file for alignment"
# # bwa index $REFERENCE_ACCESSION.fasta

# # echo "Fastq file"
# # bwa mem $REFERENCE_ACCESSION.fasta $DISEASE_ACCESSION.fastq > output.sam


# '''
# BAM files are the binary version of a SAM file
# -SAM file is human readable text file
# -BAM file is machine readable and needs special software to open (binary
#      file)

# prefetch = .sra file (binary) = nucleotide data
# fastq file (human readable) = nucleotide data

# BAM file is more effecient and smaller storage size with faster computation
# than SAM files

# Text files = human readable, easy for us to read and modify

# SAM tools-like SRA tools
# -more significant for BAM files
# SAMTOOLS VIEW -> changes SAM file to BAM file and vice versa
# '''
# # samtools view -b output.sam > output.bam

# #View contents of SAM and BAM file
# # cat output.sam | head -n 5
# # cat output.bam | head -n 5 # will output non-human readable format
# # samtools view output.bam | head -n 5 # will return first 5 lines in human readable format

# # echo "Pipeline executed successfully"

# # REFERENCE_ACCESSION="AF086833"
# # DISEASE_ACCESSION="SRR1972739"

# # echo "Starting Pipeline..."

# # echo "Downloading Reference Data"
# # efetch -db nucleotide -id $REFERENCE_ACCESSION -format fasta > $REFERENCE_ACCESSION.fasta

# # echo "Downloading Disease Data"
# # prefetch $DISEASE_ACCESSION

# # echo "Converting SRA file into FASTQ file"
# # fastq-dump -X 1000 $DISEASE_ACCESSION

# # echo "Quality Control and data cleaning"
# # # # cleaning using fastp (REPLACE WITH ACTUAL FASTP COMMAND)

# # echo "Index FASTA file for alignment"
# # bwa index $REFERENCE_ACCESSION.fasta

# # echo "Align FASTQ file with FASTA file"
# # bwa mem $REFERENCE_ACCESSION.fasta $DISEASE_ACCESSION.fastq > output.sam


# # echo "Convert SAM file to BAM File"
# # samtools view -b output.sam > output.bam

# # echo "Sort and File"
# # samtools sort output.bam > sorted.bam #we can use the -o to output as a file instead of using '>'

# '''
# sorting sorts reads based on base pair number (in context of gene/genome) instead of fastq read number
# this is useful for downstream processes
# '''

# # echo "Index BAM file for faster later analysis"
# # samtools index sorted.bam

# # echo "Index FASTA file for faster later analysis"
# #faidx -> Creates an index file (.fai) for random access to sequences
# # samtools faidx $REFERENCE_ACCESSION.fasta

# #SAMTOOLS FLAGSTAT -> gives us quality statistics of how well our alignment performed

# #samtools tview sorted.bam AF086833.fasta #used to show visualization of reads against the refrence sequence

# # echo "Post alignment Processing"
# # gatk ValidateSamFile -I sorted.bam - MODE SUMMARY

# # echo "Pipeline Completed Successfully!"

# REFERENCE_ACCESSION="AF086833"
# DISEASE_ACCESSION="SRR1972739"
# RESULTS_FOLDER=results
# SNPEFF_DIR=${RESULTS_FOLDER}/snpEff
# SNPEFF_DATA_DIR=${SNPEFF_DIR}/data/reference_db


# # #echo "Starting Pipeline..."

# # echo "Downloading Reference Data"
# # efetch -db nucleotide -id $REFERENCE_ACCESSION -format fasta > $REFERENCE_ACCESSION.fasta

# # echo "Downloading Disease Data"
# # prefetch $DISEASE_ACCESSION

# # echo "Converting SRA file into FASTQ file"
# # fastq-dump -X 1000 $DISEASE_ACCESSION

# # echo "Quality Control and data cleaning"
# # # # cleaning using fastp (REPLACE WITH ACTUAL FASTP COMMAND)

# # echo "Index FASTA file for alignment"
# # bwa index $REFERENCE_ACCESSION.fasta

# # echo "Align FASTQ file with FASTA file"
# # bwa mem -R '@RG\tID:1\tLB:lib1\tPL:illumina\tPU:unit1\tSM:sample1' $REFERENCE_ACCESSION.fasta $DISEASE_ACCESSION.fastq > output.sam


# # echo "Convert SAM file to BAM File"
# # samtools view -b output.sam > output.bam

# # echo "Sort BAM File for faster later analysis"
# # samtools sort output.bam > sorted.bam

# # echo "Index BAM file for faster later analysis"
# # samtools index sorted.bam

# # echo "Index FASTA file for faster later analysis"
# # samtools faidx $REFERENCE_ACCESSION.fasta


# # echo "Post Alignment Processing"
# # gatk ValidateSamFile -I sorted.bam -MODE SUMMARY

# # echo "Mark Duplicates"
# # gatk MarkDuplicates -I sorted.bam -O sorted_dedup.bam -M dedup_metrics.txt

# # echo "Create Sequence Dictionary"
# # gatk CreateSequenceDictionary -R $REFERENCE_ACCESSION.fasta -O $REFERENCE_ACCESSION.dict

# # echo "Index BAM file for faster later analysis"
# # samtools index sorted_dedup.bam

# # echo "Extract Variants into VCF file"
# # gatk HaplotypeCaller -R $REFERENCE_ACCESSION.fasta -I sorted_dedup.bam -O variants.vcf

# # echo "Variant Filtering"
# # gatk VariantFiltration -R $REFERENCE_ACCESSION.fasta -V variants.vcf -O filtered_variants.vcf --filter-expression "QD < 2.0 || FS > 60.0 || MQ < 40.0" --filter-name "BasicFilter"
# #gatk SelectVariants -R $REFERENCE_ACCESSION.fasta -V filtered_variants.vcf --select-type INDEL -O selected_indels.vcf
# '''
# vcf files are human readable files that show the variants present when compared to the reference sequence
# '''

# # echo "Annotation"

# # rm -r results/snpEff
# # mkdir -p results/snpEff/data/reference_db

# # echo Downloading reference GenBank file for snpEff...
# # efetch -db nucleotide -id $REFERENCE_ACCESSION -format genbank > $SNPEFF_DATA_DIR/genes.gbk

# # echo Downloaded GenBank file for snpEff!

# echo Building snpEff database...
# snpEff build -c $SNPEFF_DIR/snpEff.config -genbank -v -noCheckProtein reference_db 
# echo Built snpEff database!

# echo Exporting snpEff database...
# snpEff dump -c $SNPEFF_DIR/snpEff.config reference_db > $SNPEFF_DIR/snpEff_reference_db.txt 
# echo Exported snpEff database!

# echo Annotating variants with snpEff...
# snpEff -c $SNPEFF_DIR/snpEff.config -stats $SNPEFF_DIR/snpEff.html reference_db filtered_variants.vcf > annotated_variants.vcf
# echo Annotated variants with snpEff!

# echo "Pipeline Completed Successfully!"
 

REFERENCE_ACCESSION="AF086833"
DISEASE_ACCESSION="SRR1972739"
RESULTS_FOLDER=results
SNPEFF_DIR=${RESULTS_FOLDER}/snpEff
SNPEFF_DATA_DIR=${SNPEFF_DIR}/data/reference_db


echo "Starting Pipeline..."

echo "Downloading Reference Data"
efetch -db nucleotide -id $REFERENCE_ACCESSION -format fasta > $REFERENCE_ACCESSION.fasta

echo "Downloading Disease Data"
prefetch $DISEASE_ACCESSION

echo "Converting SRA file into FASTQ file"
fastq-dump -X 1000 $DISEASE_ACCESSION

echo "Quality Control and data cleaning"
fastp -i $DISEASE_ACCESSION.fastq -o $DISEASE_ACCESSION.fastq -h fastp.html

echo "Index FASTA file for alignment"
bwa index $REFERENCE_ACCESSION.fasta

echo "Align FASTQ file with FASTA file"
bwa mem $REFERENCE_ACCESSION.fasta $DISEASE_ACCESSION.fastq > output.sam

echo "Convert SAM file to BAM File"
samtools view -b output.sam > output.bam

echo "Sort BAM File for faster later analysis"
samtools sort output.bam > sorted.bam

echo "Index BAM file for faster later analysis"
samtools index sorted.bam

echo "Index FASTA file for faster later analysis"
samtools faidx $REFERENCE_ACCESSION.fasta


echo "Post Alignment Processing"

echo "Validate SAM File"
gatk ValidateSamFile -I sorted.bam -MODE SUMMARY

echo "Mark Duplicates"
gatk MarkDuplicates -I sorted.bam -O sorted_dedup.bam -M dedup_metrics.txt

echo "Create Sequence Dictionary"
gatk CreateSequenceDictionary -R $REFERENCE_ACCESSION.fasta -O $REFERENCE_ACCESSION.dict

echo "Index Sorted Dedup BAM file for faster later analysis"
samtools index sorted_dedup.bam

echo "Extract Variants into VCF file"
gatk HaplotypeCaller -R $REFERENCE_ACCESSION.fasta -I sorted_dedup.bam -O variants.vcf

echo "Variant Filtering"
gatk VariantFiltration -R $REFERENCE_ACCESSION.fasta -V variants.vcf -O filtered_variants.vcf --filter-expression "QD < 2.0 || FS > 10.0 || MQ < 40.0" --filter-name "BasicFilter"

echo "Annotation"

rm -r results/snpEff
mkdir -p results/snpEff/data/reference_db

echo Downloading reference GenBank file for snpEff...
efetch -db nucleotide -id $REFERENCE_ACCESSION -format genbank > $SNPEFF_DATA_DIR/genes.gbk
echo Downloaded GenBank file for snpEff!

echo Creating custom snpEff configuration file...
cat <<EOF > $SNPEFF_DIR/snpEff.config
# Custom snpEff config for reference_db
reference_db.genome : reference_db
reference_db.fa : $(readlink -f  $REFERENCE_ACCESSION)
reference_db.genbank : $(readlink -f $SNPEFF_DATA_DIR/genes.gbk)
EOF

echo Building snpEff database...
snpEff build -c $SNPEFF_DIR/snpEff.config -genbank -v -noCheckProtein reference_db 
echo Built snpEff database!

echo Exporting snpEff database...
snpEff dump -c $SNPEFF_DIR/snpEff.config reference_db > $SNPEFF_DIR/snpEff_reference_db.txt 
echo Exported snpEff database!

echo Annotating variants with snpEff...
snpEff -c $SNPEFF_DIR/snpEff.config -stats $SNPEFF_DIR/snpEff.html reference_db filtered_variants.vcf > annotated_variants.vcf
echo Annotated variants with snpEff!

echo "Pipeline Completed Successfully!"
 
 