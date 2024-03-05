#! /usr/local/bin/python3

import argparse
def parse_fasta(file_path):
    sequences = []
    with open(file_path, "r") as file:
        current_sequence = ""
        for line in file:
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line.strip()
        if current_sequence:  # For the last sequence in the file
            sequences.append(current_sequence)
    return sequences

def find_most_frequent_sequences(file_path):
    sequences = parse_fasta(file_path)
    sequence_counts = {}
    for sequence in sequences:
        if sequence in sequence_counts:
            sequence_counts[sequence] += 1
        else:
            sequence_counts[sequence] = 1
    sorted_sequences = sorted(sequence_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_sequences[:10]


def main():
    parser = argparse.ArgumentParser(description="10 most frequent sequences")
    parser.add_argument("directory", help="Directory path to the fasta file")
    args = parser.parse_args()
    most_frequent_sequences = find_most_frequent_sequences(args.directory)
    print("Top 10 most frequent sequences:")
    for sequence, count in most_frequent_sequences:
        print(f"Sequence: {sequence}, Count: {count}")

if __name__ == "__main__":
    main()

