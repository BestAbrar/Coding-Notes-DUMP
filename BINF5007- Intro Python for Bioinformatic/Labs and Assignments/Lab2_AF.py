patients = ["Jane Doe", "John Smith", "Emily White","Michael Brown"]
print(patients[1])
patients.append("Sarah Miller")
patients[2]="Emily Williams"
test = "Alejandro Ramirez, Chloe Mitchell, Sofia Vargas, Liam Sullivan"
new_pateints = ['Alejandro Ramirez', 'Chloe Mitchell', 'Sofia Vargas', 'Liam Sullivan']
patients += new_pateints
print(patients)

search = str(input("Enter Pateint Name: "))
print(search in patients)

pateint_input = str(input("Enter patient names (separated by commas)"))
patient_index = int(input("Enter desired index in patients list: "))
pateint_input = pateint_input.split(",")
patients [patient_index:patient_index]=pateint_input
print(patients)
