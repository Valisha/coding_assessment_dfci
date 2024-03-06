#! /usr/local/bin/python3

import os
import argparse

def count_nucleotides(line):
    """
    This function is to make sure that we only count the A, T, G and Cs in the string.
    Input is the parsed line, defined inside the count_long_sequences function
    """
    return sum(1 for nucleotide in line if nucleotide in ['A', 'T', 'G', 'C'])

def count_long_sequences(file_path):
    """
    This function takes each line as an input, and checks if its the starting of a new line, then calculates the length of the sequences. By using the count_nucleotides function
    """
    long_sequences = 0
    total_sequences = 0
    with open(file_path, "r") as file:
        in_sequence = False
        for line in file:
            if line.startswith("@"):  # Check for new sequence entry
                in_sequence = True
                total_sequences += 1
            elif in_sequence:
                sequence_length = count_nucleotides(line.strip())
                if sequence_length > 30:
                    long_sequences += 1
                in_sequence = False  # Set to False after processing the sequence
    if total_sequences == 0:
        return 0
    else:
        return (long_sequences / total_sequences) * 100

def find_fastq_files(directory):
    """
    This function for finding all the possible fastqs in the directory, containing multiple sub directories
    """
    fastq_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fastq"):
                fastq_files.append(os.path.join(root, file))
    return fastq_files

def main():
    parser = argparse.ArgumentParser(description="Count long sequences in FASTQ files.") 
    parser.add_argument("directory", help="Directory path to search for FASTQ files.")
    args = parser.parse_args()
    fastq_files = find_fastq_files(args.directory)
    for file_path in fastq_files:
        percent_long_sequences = count_long_sequences(file_path)
        print(f"File: {file_path}, Percent long sequences: {percent_long_sequences:.2f}%")

if __name__ == "__main__":
    main()

