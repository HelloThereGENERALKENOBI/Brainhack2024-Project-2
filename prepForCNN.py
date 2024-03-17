import pandas as pd

dupa = pd.read_json("final_output_v2_floated.json")
# a = dupa["915fa984-e320-4db8-85e8-1ed98435ec16.rna_seq.augmented_star_gene_counts.tsv"]["glioma_name"]
dupa.to_csv("dupa.csv")
print(dupa)
print("dupa")
a=dupa.index[0]
print(a)
b=dupa.columns[0]
print(b)
print("1")
print(dupa[b,a])
print('2')
# print(dupa.get_value(0,0))
# for filename, cancer_type in dupa.iterrows():
#     print(cancer_type)
#     print("pupa")
#     print(dupa[filename][cancer_type])
#     print("dupa")