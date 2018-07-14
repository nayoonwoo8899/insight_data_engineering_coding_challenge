#!/bin/env python -B

"""
Python script for counting cost and subscription of drugs.
Usage:
    pharmacy_counting.py [input file] [output file]
Author: Nayoon Woo (nayoonwoo8899@gmail.com)
"""


import csv
import os
import sys
from collections import OrderedDict
from collections import defaultdict


def collect_stats(input_file):
    """
    Python function to read statistics from prescription input CSV file into a dictionary
    """
    
    outputdict = {}
    dnamerecord = defaultdict(set)
    
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = row['drug_name']
            if d in outputdict.keys():
            
                if (row['prescriber_first_name'], row['prescriber_last_name']) not in dnamerecord[d]:
                    outputdict[d]['num_prescriber'] += 1
                    dnamerecord[d].add((row['prescriber_first_name'], row['prescriber_last_name']))

                float_drug_cost = float(row['drug_cost'])
                float_total_cost = float(outputdict[d]['total_cost'])
                outputdict[d]['total_cost'] = float_drug_cost + float_total_cost           
        
            else:
                outputdict[d] = {'num_prescriber' : 1, 'total_cost' : row['drug_cost']}
                dnamerecord[d].add((row['prescriber_first_name'], row['prescriber_last_name']))
    return outputdict
    
    
def dump_stats(output_dict, output_file):
    """
    Python function to dump the statistics in dictionary to CSV file
    """

    ordered_output = OrderedDict(sorted(output_dict.items(), key=lambda x: (-float(x[1]['total_cost']), x[0])))
    with open(output_file, 'w') as w:
        thewriter = csv.writer(w)
        thewriter.writerow(['drug_name', 'num_prescriber', 'total_cost'])
        for medicine in ordered_output:
            thewriter.writerow([medicine, ordered_output[medicine]['num_prescriber'], ordered_output[medicine]['total_cost']])     
            

def count(input_file, output_file):
    """
    Python function to read prescription data from input file and dump statistics to output file
    """
    stats = collect_stats(input_file)
    dump_stats(stats, output_file)
    
     
def main():
    
    # read arguments
    args = sys.argv
    print(args)
    if len(args) < 3:
        print(__doc__)
        sys.exit(1)
        
    # parse files
    input_file = args[1]
    output_file = args[2]
    
    # process data
    count(input_file, output_file)
    
        
if __name__ == '__main__':
    main()