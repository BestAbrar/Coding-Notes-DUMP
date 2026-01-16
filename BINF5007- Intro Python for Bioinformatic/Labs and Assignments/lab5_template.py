CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*',  # UAA is a STOP codon
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*',  # UGA is a STOP codon
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAG': '*'   # UAG is a STOP codon
}

def transcribe_dna_to_rna(dna_sequence: str) -> str:
    """
    Converts a DNA sequence to an RNA sequence.
    If the DNA has non-valid bases, the user is notified and
    None is returned.
    """
    try:
        rna_sequence = ""
        bases = {'A':'U','T':'A','G':'C','C':'G'}
        for index, base in enumerate(dna_sequence):
            rna_sequence += bases[base]
        return rna_sequence
    except KeyError:
        print(dna_sequence + " has an invalid base: \'"+base+"\' at index["+str(index)+"]")
        return None
    

def translate_rna_to_protein(rna_sequence: str, codon_table: dict = CODON_TABLE) -> str:
    """
    Translates an RNA sequence into a protein sequence using a codon table.
    If a codon cannot be mapped to an amino acid, the user is notified
    and None is returned
    """
    try:
        protien_sequence = ""
        for index in range (0,len(rna_sequence),3):
            protien_sequence+=codon_table[rna_sequence[index:index+3]]
            if codon_table[rna_sequence[index:index+3]] == '*':
                return protien_sequence
        return protien_sequence
    except KeyError:
        print("sequence: "+rna_sequence+" contains an incomplete codon: "+rna_sequence[index:index+3])
        return None

#Main Program Execution------------------------------
# Get a DNA sequence from the user, translate it to the corresponding protein
# and print it on screen

#Assertions---------------------------------
# Include test cases using assert to test your functions
DNA_seq1= "TACATGATCAGACCCATGTAGCAG"
DNA_seq2= "TACATGATGGGACCCATGTAGCAG"
DNA_seq3= "TACAPGATCAGACCCATGTAGCAG"
DNA_seq4= "TACATGATGGGACCCATGTAGCA"
print("The transcribed sequence for "+DNA_seq1 +" is:"+ transcribe_dna_to_rna(DNA_seq1))
print("The translated sequence for "+DNA_seq1 +" is:"+ translate_rna_to_protein(transcribe_dna_to_rna(DNA_seq1), CODON_TABLE))
print("The transcribed sequence for "+DNA_seq1 +" is:"+ transcribe_dna_to_rna(DNA_seq2))
print("The translated sequence for "+DNA_seq2 +" is:"+ translate_rna_to_protein(transcribe_dna_to_rna(DNA_seq2), CODON_TABLE))


assert transcribe_dna_to_rna(DNA_seq1)=="AUGUACUAGUCUGGGUACAUCGUC" #amino acid is truncated prematurely due to stop codon (transcribed correctly)
assert translate_rna_to_protein(transcribe_dna_to_rna(DNA_seq1), CODON_TABLE)=="MY*" #amino acid is truncated due to stop codon (translated correctly)
assert transcribe_dna_to_rna(DNA_seq2)=="AUGUACUACCCUGGGUACAUCGUC" #amino acid is not truncated prematurely due to stop codon (transcribed correctly)
assert translate_rna_to_protein(transcribe_dna_to_rna(DNA_seq2), CODON_TABLE)=="MYYPGYIV" #amino acid is not truncated prematurely due to stop codon (translated correcly)
assert transcribe_dna_to_rna(DNA_seq3)==None #sequence with invalid base 'P' and returns none
assert translate_rna_to_protein(transcribe_dna_to_rna(DNA_seq4))==None #sequence length isn't multiple of 3/incomplete codon not found in codon table and returns none
