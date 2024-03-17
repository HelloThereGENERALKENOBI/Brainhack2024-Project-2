import os
from os import listdir, path

# print(listdir("RawData"))
patient_files = []
patient_dirs = listdir("RawData")
# print(len(patient_dirs))
for inner_dit in patient_dirs:
    f = list(listdir(os.path.join("RawData", inner_dit)))
    f = [x for x in f if "tsv" in x]
    patient_files.append(f)

f = open("files_for_excel.xls", "w")
for el in patient_files:
    f.write(str(el[0]))
    f.write("\n")
