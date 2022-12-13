import sys

with open(sys.argv[1], 'r') as input_file:
    data = input_file.readlines()

matching_rows = {}

for row in data:
    values = row.strip().split()

    if values[0] in matching_rows:
        matching_rows[values[0]].append(values[1])
    else:
        matching_rows[values[0]] = [values[1]]

for key in matching_rows:
    print(key + "," + ",".join(matching_rows[key]))
