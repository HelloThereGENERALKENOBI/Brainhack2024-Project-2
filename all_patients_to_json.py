import os
from collections import defaultdict
from pprint import pprint

from filterRNAseqGeneCount import run as get_gene_run
import json_save

def last_man_standing(path):
    files = os.listdir(path)
    patient_genes = defaultdict(list)

    methylated_genes = ['CBWD6', 'C1orf116', 'DIO2', 'LRRC37A2','MAEL','SPATA22','HRH1','RASA4','LRP5L','ZNF404']

    for file in files:
        with open(os.path.join(path, file)) as f:
            for line in f:
                if line.split()[1] in methylated_genes:
                    patient_genes[file].append((line.split()[1], line.split()[3]))
                    # print(line.split()[1])
    return patient_genes


# def get_single_patient_gene_data(filename:str):
#     list_with_genes = get_gene_run(filename)

def get_all_data(path_with_gene_data:str):
    all_data = defaultdict(dict)
    with open('plikodgpt.csv') as files:
        gene_data = last_man_standing(path_with_gene_data)
        for line in files:
            line_split = line.split(',')
            all_data[line_split[0]]['glioma_name'] = line_split[1].strip(',\n')     #','.join(line_split[1]).strip(',\n')
            path_to_patient_genes = os.path.join(path_with_gene_data, line_split[0])

            # all_data[line_split[0]]['gene_info'] = get_gene_run(path_to_patient_genes)
            all_data[line_split[0]]['gene_info'] = gene_data[line_split[0]]
            # print(get_gene_run(path_to_patient_genes))
            # quit()

        # pprint(all_data)
        # quit()
        json_save.save_dict_to_json('nonnormalized_final_output.json', all_data)

if __name__=='__main__':
    path = 'RawDataAleBezFolderow'
    get_all_data(path)
    # last_man_standing(path)