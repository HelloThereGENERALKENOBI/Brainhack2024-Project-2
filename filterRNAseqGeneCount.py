import pandas as pd



def remove_useless_data(filename) -> pd.DataFrame:
    try:
        geneExpressionFile = pd.read_table(filename, sep='\t', header=1)
        geneExpressionFile = geneExpressionFile.iloc[4:]
    except Exception as error:
        print("There was an error loading gene expression quantity data")

    # geneExpressionFile.get(["gene_name", "unstranded"]).to_csv('unfilteredData.csv', index=False)

    return geneExpressionFile.get(["gene_name", "unstranded"])

def remove_unused_genes(data: pd.DataFrame) -> pd.DataFrame:
    gene_names = pd.read_csv("all_genes.txt", delimiter=" ", header=None, names=["gene_name"])
    data = data[data['gene_name'].isin(gene_names['gene_name'])]
    data.reset_index(drop=True, inplace=True)
    return data

def rescore(data: pd.DataFrame) -> tuple:
    def normalization(x):
        smallest = data["unstranded"].min()
        greatest = data["unstranded"].max()
        return (x - smallest) / (greatest - smallest)

    data["unstranded"] = data["unstranded"].apply(normalization)
    tuple_list = list(data.to_records(index=False))
    return tuple_list

#old version
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
    # new_file = open("entryData.csv", "w")
    # for i in range(len(z_scores)):
    #     new_file.write(geneNames[i])
    #     new_file.write(";")
    #     new_file.write(str(z_scores[i]))
    #     new_file.write('\n')
    # NOTE below 2 lines is debugging and info
    # for i in range(len(z_scores)):
    #     print(f'{geneNames[i]}; {str(z_scores[i])} \n')
    output = []
    for i in range(len(z_scores)):
        output.append((geneNames[i], float(z_scores[i])))
        

    return output

def run(path):
    # print('got here')
    # for file in os.listdir(path):
    # remove_useless_data(path)             # NOTE already done, REMEMBER TO USE THAT IN final implementation
    with open("unfilteredData.csv") as file:
        full_gene_names = []
        unstranded = []
        flag = True
        for line in file:
            if flag == True:
                flag = False
                continue
            new_line = line.split(",")
            full_gene_names.append(new_line[0])
            unstranded.append(int(new_line[1]))
    # gene_names=gene_names[1::]
    # unstranded=unstranded[1::]
    matches = matchData(full_gene_names, unstranded)
    gene_names = []
    gene_data = []
    for match in matches:
        gene_names.append(match[0])
        gene_data.append(match[1])

    normalized = normalize_data(gene_data)

    return formatDataForCNN(gene_names, normalized)


if __name__ == "__main__":
    filename = 'patientOne.tsv'
    # remove_useless_data -> remove_unused_genes -> rescore-> output: data.scv
    print(rescore(remove_unused_genes(remove_useless_data(filename))))
