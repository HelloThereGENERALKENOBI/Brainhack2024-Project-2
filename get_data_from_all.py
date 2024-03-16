from os import listdir, path

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
    for f in all_files:
        if path.isfile(f):  # NOTE stuff below needs to go to separate func
            found_genes = []
            with open(f) as patient_file:
                for line in patient_file:
                    proc_line = line.split()
                    for el in proc_line:
                        if el in good_genes:
                            found_genes.append(proc_line)
            print(found_genes)
        else:
            print(f'WARNING found something thats not a file: {f}')

if __name__ == '__main__':
    path = r''
    get_all_data(path)