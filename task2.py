#! /usr/local/bin/python3

import argparse

## 1. Read the file line by line 
## 2. Parse the relevant columns (%gc and mean_target_coverage)
## 3. Calculate the GC% bins for each entry 
## 4. Group the entries by GC% bins 
## 5. Calculate the mean target coverage for each bins 
## 6. Output the results 

def parse_intervals_file(file_path):
   gc_coverage_data = {}
   with open(file_path, 'r') as file:
        next(file) ## Skipping the header 
        for line in file:
            parts = line.strip().split('\t')
            if parts[5] and parts[6]:
                gc_percentage = float(parts[5])*100 ## Converting the GC rage from 0-1 to percentage 
                mean_coverage = float(parts[6])
                gc_bin = int(gc_percentage // 10) * 10 ## Calculating gc bin 
                gc_coverage_data.setdefault(gc_bin, []).append(mean_coverage)
            else:
                gc_coverage_data.setdefault(gc_bin, []).append(0)
   return gc_coverage_data

def calculate_mean_coverage(gc_coverage_data):
    mean_coverage_by_bin = {}
    for gc_bin, coverages in gc_coverage_data.items():
        mean_coverage = sum(coverages) / len(coverages)
        mean_coverage_by_bin[gc_bin] = mean_coverage
    return mean_coverage_by_bin

def main():
    parser = argparse.ArgumentParser(description="Calculate the mean target coverage for each GC bin")
    parser.add_argument("file_path", help="path to the file")
    args = parser.parse_args()
    gc_coverage_data = parse_intervals_file(args.file_path)
    mean_coverage_by_bin = calculate_mean_coverage(gc_coverage_data)

    print("Mean target coverage by GC% bins: ")
    for gc_bin, mean_coverage in sorted(mean_coverage_by_bin.items()):
        print(f"GC% Bin: {gc_bin}-{gc_bin+10}, Mean Coverage: {mean_coverage:.2f}")

if __name__ == "__main__":
    main()




 
