#!/opt/anaconda3/bin/python3

import requests

url = 'https://rest.ensembl.org/variation/homo_sapiens'
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
data = {"ids": ["rs56116432", "COSM476"]}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    data = response.json()
else:
    print("Error:", response.status_code)
    print("Response:")
    print(response.text)

variant_info = []

for variant_id, info in data.items():
    mappings = [{'Location': mapping.get('location', None),
                 'Allele String': mapping.get('allele_string', None),
                 'Ancestral Allele': mapping.get('ancestral_allele', None)} 
                for mapping in info.get('mappings', [])]
    
    variant = {
        'ID': variant_id,
        'Variant Class': info.get('var_class', None),
        'Most Severe Consequence': info.get('most_severe_consequence', None),
        'Minor Allele': info.get('minor_allele', None),
        'Mappings': mappings
    }
    
    variant_info.append(variant)

for variant in variant_info:
    print(f"ID: {variant['ID']}")
    print(f"Variant Class: {variant['Variant Class']}")
    print(f"Most Severe Consequence: {variant['Most Severe Consequence']}")
    print(f"Minor Allele: {variant['Minor Allele']}")
    print("Mappings:")
    for mapping in variant['Mappings']:
        print(f"\tLocation: {mapping['Location']}")
        print(f"\tAllele String: {mapping['Allele String']}")
        print(f"\tAncestral Allele: {mapping['Ancestral Allele']}")
        print()
    print()
