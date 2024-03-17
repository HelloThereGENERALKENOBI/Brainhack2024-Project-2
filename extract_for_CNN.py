import json

# Opening JSON file
f = open("final_output_v2_floated.json")

classes = {"Oligodendroglioma": 1, "Astrocytoma": 2, "Mixed": 3}
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
data_points = []
names_vals = []
for i in data:
    data_points.append(data[i])

dataset = []
for i in range(len(data_points)):
    # print(data_points[0]["gene_info"])
    dataset.append(data_points[i]["gene_info"])
    dataset[i].append(classes[data_points[0]["glioma_name"]])


print(dataset[0])

f.close()
