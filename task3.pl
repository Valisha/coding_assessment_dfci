#!/usr/bin/perl

use strict;
use warnings;
use LWP::UserAgent;
use JSON;

# Function to fetch variant information from Ensembl API
sub fetch_variant_info {
    my ($variant_id) = @_;

    my $url = "https://rest.ensembl.org/variation/human/$variant_id";
    my $ua = LWP::UserAgent->new;
    my $response = $ua->get($url);

    if ($response->is_success) {
        my $variant_info = decode_json($response->content);
        return $variant_info;
    } else {
        print "HTTP Error: " . $response->status_line . "\n";
        return;
    }
}

# Example variant ID
my $variant_id = "rs56116432";

# Fetch variant information
my $variant_info = fetch_variant_info($variant_id);

if ($variant_info) {
    # Parse the JSON response to extract required information
    my $alleles = $variant_info->{alleles};
    my $location = $variant_info->{mappings}->[0]->{location};
    my $effects = $variant_info->{evidence}->{consequence_types};
    my $genes = $variant_info->{transcript_consequences};

    print "Alleles: $alleles\n";
    print "Location: $location\n";
    print "Effects: @$effects\n";
    print "Genes containing the transcripts:\n";
    foreach my $gene (@$genes) {
        print "- Gene: $gene->{gene_id} Transcript: $gene->{transcript_id}\n";
    }
}

