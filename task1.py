#! /usr/local/bin/python3 

import os
def count_long_sequences(file_path):
    """
    This function takes the file_path as an input. Reads the file, and then goes through it line by line to calcualate the total number of sequences and total number of long sequences. 
    """
    long_sequences = 0
    total_sequences = 0
    with open(file_path, "r") as file:
        line_number = 0
        for line in file:
            print(line[1:10])
            line_number += 1
            if line_number % 4 == 2: # Check for only sequence lines
                sequence = line.strip()
                if len(sequence) > 30:
                    long_sequences += 1
                total_sequences += 1
    if total_sequences == 0:
        return 0
    else:
        return (long_sequences/total_sequences) * 100
def find_fastq_files(directory):
    """
    This function goes through a directory and finds all the fastqs in any subdirectory and gives the fastq path as an output
    """
    fastq_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fastq"):
                fastq_files.append(os.path.join(root, file))
    return fastq_files
def main():
    directory = input("Enter the directory path to search for FASTQ files: ")
    directory = directory.strip('"')
    fastq_files = find_fastq_files(directory)
    for file_path in fastq_files:
        percent_long_sequences = count_long_sequences(file_path)
        print(f"File: {file_path}, Percent long sequences: {percent_long_sequences:.2f}%")

if __name__ == "__main__":
    main()
