import os
from collections import defaultdict
from pprint import pprint

from filterRNAseqGeneCount import run as get_gene_run
import json_save

def get_single_patient_gene_data(filename:str):
    list_with_genes = get_gene_run(filename)

def get_all_data(path_with_gene_data:str):
    all_data = defaultdict(dict)
    with open('plikodgpt.csv') as files:
        for line in files:
            line_split = line.split(',')
            all_data[line_split[0]]['glioma_name'] = line_split[1].strip(',\n')#','.join(line_split[1]).strip(',\n')
            path_to_patient_genes = os.path.join(path_with_gene_data, line_split[0])

            all_data[line_split[0]]['gene_info'] = get_gene_run(path_to_patient_genes)

        # pprint(all_data)
        json_save.save_dict_to_json('final_output_v2_floated.json', all_data)

if __name__=='__main__':
    path = 'RawDataAleBezFolderow'
    get_all_data(path)