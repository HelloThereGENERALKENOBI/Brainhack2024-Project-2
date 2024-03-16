import pandas as pd
import os


def run(path):
    # for file in os.listdir(path):
    # print(path)
    filter_data(path)
    with open("unfilteredData.csv") as file:
        gene_names = []
        unstranded = []
        flag = True
        for line in file:
            if flag == True:
                flag = False
                continue
            new_line = line.split(",")
            gene_names.append(new_line[0])
            unstranded.append(int(new_line[1]))

    # gene_names=gene_names[1::]
    # unstranded=unstranded[1::]
    matches = matchData(gene_names, unstranded)
    kurwa =[]
    for match in matches:
        kurwa.append(match[1])

    normalized = normalize_data(kurwa)
    print(normalized)



    # print(gene_expression_file)
    # gene_length_list = gene_expression_file.get(["unstranded"])
    # z_score = normalize_data(gene_length_list)
    # print(z_score)


def normalize_data(arr: list) -> list:
    smallest = min(arr)
    greatest = max(arr)
    new_arr = []
    for el in arr:
        new_el = (el - smallest) / (greatest - smallest)
        new_arr.append(new_el)
    return new_arr


def formatDataForCNN(geneNames: list, z_scores: list) -> None:
    if len(geneNames) != len(z_scores):
        return
    new_file = open("entryData.csv", "w")
    for i in range(len(z_scores)):
        new_file.write(geneNames[i])
        new_file.write(";")
        new_file.write(z_scores[i])
        new_file.write('\n')


def filter_data(filename):
    try:
        geneExpressionFile = pd.read_table(filename, sep='\t', header=1)
        geneExpressionFile = geneExpressionFile.iloc[4:]
    except Exception as error:
        print("There was an error loading gene expression quantity data")

    geneExpressionFile.get(["gene_name", "unstranded"]).to_csv('unfilteredData.csv', index=False)


# def matchData(filename):
#     found_genes = []
#     good_genes = []
#
#     with open("all_genes_methy.txt") as ent_data:
#         for line in ent_data:
#             line = line.strip("\n")
#             good_genes.append(line)
#
#     with open(filename) as file:
#         for line in file:
#             proc_line = line.split()
#             for el in proc_line:
#                 if el in good_genes:
#                     found_genes.append(proc_line)
#
#     f = open("found_genes_unstranded.txt", "a")
#     for el in found_genes:
#         f.write(el[1])
#         f.write(";")
#         f.write(el[3])
#         f.write("\n")

def matchData(geneNames, z_scores):
    possible_matches = []
    true_matches = []
    with open("all_genes.txt") as ent_data:
        for line in ent_data:
            line = line.strip("\n")
            possible_matches.append(line)

    for el in geneNames:
        if el in possible_matches:
            true_matches.append([el, z_scores[geneNames.index(el)]])
    true_matches.sort(key=lambda x: x[1],reverse=True)
    return true_matches


if __name__ == "__main__":
    # dupa = filter_data('patientZero.tsv')
    print(run('patientOne.tsv'))
    # run("C:\\Users\\mmalk\\OneDrive - Politechnika Warszawska\\Programowanie\\Python\\Brainhack2024-Project-2\\RawData")
    # run('ass')
    # filename = 'patientZero.tsv'
    # filterData('patientZero.tsv')
    # matchData('unfilteredData.csv')
