molecular_mass = float(input("Enter Molecular Mass (g/mol)"))
volume = float(input("Enter Volume (in ml)"))/1000
concentration = float(input("Enter Desired Concentration (molar M)"))

mass = concentration*volume*molecular_mass

print("The molecular mass you entered is: "+str(molecular_mass)+" g/mol")
print("The volume you entered is: "+str(volume*1000)+" ml")
print("The desired concentration you entered is: "+str(concentration)+" M")
print("Required mass is: "+str(mass))

dna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_seq=dna_seq.replace("A","t")
dna_seq=dna_seq.replace("C","g")
dna_seq=dna_seq.replace("T","a")
dna_seq=dna_seq.replace("G","c")

print(dna_seq.upper())