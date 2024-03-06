#!/opt/anaconda3/bin/python3

import requests

# Function to fetch variant information from Ensembl API
def fetch_variant_info(variant_id):
    url = f"https://rest.ensembl.org/variation/human/{variant_id}"
    response = requests.get(url)
    try:
        response.raise_for_status()  # Check for HTTP errors
        variant_info = response.json()  # Parse JSON response
        return variant_info
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    return None

# Example variant ID
variant_id = "rs56116432"

# Fetch variant information
variant_info = fetch_variant_info(variant_id)

if variant_info:
    # Parse the JSON response to extract required information
    alleles = variant_info.get('alleles')
    location = variant_info.get('mappings')[0].get('location')
    effects = variant_info.get('evidence')['consequence_types']
    genes = variant_info.get('transcript_consequences')

    print("Alleles:", alleles)
    print("Location:", location)
    print("Effects:", effects)
    print("Genes containing the transcripts:")
    for gene in genes:
        print("- Gene:", gene.get('gene_id'), "Transcript:", gene.get('transcript_id'))

