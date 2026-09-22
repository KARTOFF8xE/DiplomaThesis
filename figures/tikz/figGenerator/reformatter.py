import csv
import os
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(
    description="Reformat a CSV file containing latency differences by frequency and number of pairs."
)
parser.add_argument(
    "input_file",
    help="Path to the input CSV file (required)"
)

args = parser.parse_args()
input_file = args.input_file

if not os.path.isfile(input_file):
    print(f"[✘] File not found: {input_file}")
    exit(1)

output_file = os.path.splitext(input_file)[0] + '_reformatted.csv'

data = defaultdict(lambda: defaultdict(dict))
num_pairs_set = set()
value_keys = set()

with open(input_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        freq = row['frequency']
        num_pairs = row['num_pairs']
        num_pairs_set.add(num_pairs)

        for key, value in row.items():
            if key in ['frequency', 'num_pairs']:
                continue
            value_keys.add(key)
            data[freq][num_pairs][key] = value

num_pairs_list = sorted(num_pairs_set, key=lambda x: float(x))
value_keys = sorted(value_keys)

header = ['frequency']
for np in num_pairs_list:
    for key in value_keys:
        header.append(f'{np}/{key}')

with open(output_file, 'w', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(header)

    for freq in sorted(data.keys(), key=lambda x: float(x)):
        row = [freq]
        for np in num_pairs_list:
            for key in value_keys:
                row.append(data[freq].get(np, {}).get(key, ''))
        writer.writerow(row)

print(f'[✔] File "{output_file}" was successfully created.')
