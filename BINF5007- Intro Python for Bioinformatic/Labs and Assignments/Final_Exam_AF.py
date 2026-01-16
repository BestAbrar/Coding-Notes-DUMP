"""
Hydrophobicity
"""
def get_aa_hydrophobicity(amino_acid:str)->float:
    """
    Returns the hydrophobicity index of a given amino acid.
    :param amino_acid: A string that represents the amino acid.
    :return: hydrophobicity index of a given amino acid.
    """
    hydrophobicity_values = {
        'A': 1.8, 'C': 2.5, 'D': -3.5, 'E': -3.5, 'F': 2.8,
        'G': -0.4, 'H': -3.2, 'I': 4.5, 'K': -3.9, 'L': 3.8,
        'M': 1.9, 'N': -3.5, 'P': -1.6, 'Q': -3.5, 'R': -4.5,
        'S': -0.8, 'T': -0.7, 'V': 4.2, 'W': -0.9, 'Y': -1.3
    }

    return hydrophobicity_values[amino_acid]
'''
#1a)
def calculate_protein_hydrophobicity(protein:str)->float:
    index =0
    for amino in protein:
        index += get_aa_hydrophobicity(amino)   
    return index
'''
#1c)
def calculate_protein_hydrophobicity(protein:str)->float:
    index =0
    for amino in protein:
        try:
            index += get_aa_hydrophobicity(amino)
        except KeyError:
            continue
    return index
#1b)
def most_hydrophobic_protein(proteins:list)->tuple:
    indexes = []
    max = None
    for index in range(len(proteins)):
        indexes.append(calculate_protein_hydrophobicity(proteins[index]))
        if max==None or index > max:
            max = index
    return (proteins[max], indexes[max])

"""
Protein variant extraction with Regex
"""
import re
#2.
def find_prot_ins_variants(text:str)-> list:
    regex = "(NC_\d{6}\.\d{1,2}:p\.\d+_\d+ins[ACGT]+)"
    return re.findall(regex, text)

text = str(input("Please enter raw text: "))
variants = find_prot_ins_variants(text)
print("The protein insertion variants found in your text are:")
for variant in variants:
    print(variant)
"""
Translation with BioPython
"""
import json
from Bio.Seq import Seq
#3.
with open ("dna_seq.json") as genes_file:
    data = json.load(genes_file)
    seq_list = data["dna_sequences"]
    proteins = []
    for seq in seq_list:
        proteins.append(Seq(seq["sequence"]).translate())
with open ("output.txt", "w") as file:
    for protein in proteins:
        file.write(str(protein)+"\n")