from os import listdir, path
import os
from pprint import pprint

# hardcoded rn
basic_genes = ['CBWD6','C1orf116','DIO2','LRRC37A2','MAEL','SPATA22','HRH1','RASA4','LRP5L', 'ZNF404']
# or from file 
def get_interesting_genes(path: str="all_genes.txt"):
    good_genes = []
    with open(path) as ent_data:
        for line in ent_data:
            line = line.strip("\n")
            good_genes.append(line)
    return good_genes

def get_all_data(path: str) -> None:
    all_files = listdir(path)
    interesting_gen = get_interesting_genes()
    for file_that_is_a_dir in all_files:
        f = list(listdir(os.path.join(path, file_that_is_a_dir)))[0]     # file is in a directory, so we move to the first file inside (assuing there's only one there)
        # if os.path.isfile(os.path.join(path, f)):  # NOTE stuff below needs to go to separate func
        found_genes = []
        full_path = os.path.join(path, file_that_is_a_dir, f)
        with open(full_path) as patient_file:
            for line in patient_file:
                proc_line = line.split()
                for el in proc_line:
                    if el in interesting_gen:
                        found_genes.append(proc_line)
        for record in found_genes:
            print(record[1], record[3])
        # else:
        #     print(f'WARNING found something thats not a file: {f}')

if __name__ == '__main__':
    path = r'RawData\\'
    get_all_data(path)