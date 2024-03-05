#! /usr/local/bin/python3


## Read the GTF file and extract gene annotations, store them in a dictionary.
## Read the annotation text file and store the coordinates to annotate.
## For each coordinate, find overlapping gene annotations from the GTF file and output them.

import argparse

def load_gtf_annotations(gtf_file):
    annotations = {}
    with open(gtf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            chromosome = parts[0]
            start = int(parts[3])
            end = int(parts[4])
            gene_name = parts[8].split(';')[4].split('"')[1]  # Extract gene name from GTF format
            annotations.setdefault(chromosome, []).append((start, end, gene_name))
    return annotations

def load_coordinates_to_annotate(coordinates_file):
    coordinates = []
    with open(coordinates_file, 'r') as file:
         for line in file:
             parts = line.strip().split("\t")
             chromosome = parts[0]
             position = int(parts[1])
             coordinates.append((chromosome, position))
    return coordinates

def annotate_coordinates(gtf_annotations, coordinates):
    annotated_genes = set()
    for chromosome, position in coordinates:
        if chromosome in gtf_annotations:
            for start, end, gene_name in gtf_annotations[chromosome]:
                if start <= position <= end:
                    annotated_genes.add((chromosome, start, end, gene_name))
    return annotated_genes

def main():
    parser = argparse.ArgumentParser(description="Annotate a file with chromosome and positions, using a GTF annotations file")
    parser.add_argument("gtf_file", help="Path to the GTF annotations_file")
    parser.add_argument("file_to_annotate", help="Path to the file to annotate")
    args = parser.parse_args()
    gtf_annotations = load_gtf_annotations(args.gtf_file)
    coordinates = load_coordinates_to_annotate(args.file_to_annotate)
    annotated_genes = annotate_coordinates(gtf_annotations, coordinates)
    
    with open('annotated_genes.txt', 'w') as output_file:
         output_file.write(f"{'CHR'}\t{'START'}\t{'END'}\t{'GENE_NAME'}\n")
         for chromosome, start, end, gene_name in annotated_genes:
            output_file.write(f"{chromosome}\t{start}\t{end}\t{gene_name}\n")


if __name__ == "__main__":
    main()




