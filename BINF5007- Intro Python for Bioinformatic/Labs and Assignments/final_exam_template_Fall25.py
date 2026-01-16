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

def calculate_protein_hydrophobicity(protein:str)->float:
    #TODO - Complete the function
    pass

def most_hydrophobic_protein(proteins:list)->tuple:
    #TODO - Complete the function
    pass

"""
Protein variant extraction with Regex
"""
import re
# TODO - Complete with the requested functionality

"""
Translation with BioPython
"""
import json
from Bio.Seq import Seq
# TODO - Complete with the requested functionality
