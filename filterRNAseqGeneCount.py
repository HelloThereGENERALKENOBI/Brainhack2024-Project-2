import pandas as pd
import os


def filterData(filename):
    try:
        geneExpressionFile = pd.read_table(filename, sep='\t', header=1)
        geneExpressionFile = geneExpressionFile.iloc[4:]
    except Exception as error:
        print("There was an error loading gene expression quantity data")

    geneExpressionFile.get(["gene_name", "unstranded"]).to_csv('unfilteredData.csv', index=False)


def matchData(filename):

    found_genes = []
    good_genes = []

    with open("all_genes_methy.txt") as ent_data:
        for line in ent_data:
            line = line.strip("\n")
            good_genes.append(line)

    with open(filename) as file:
        for line in file:
            proc_line = line.split()
            for el in proc_line:
                if el in good_genes:
                    found_genes.append(proc_line)

    f = open("found_genes_unstranded.txt", "a")
    for el in found_genes:
        f.write(el[1])
        f.write(";")
        f.write(el[3])
        f.write("\n")


filename = 'patientZero.tsv'
filterData('patientZero.tsv')
matchData('unfilteredData.csv')
