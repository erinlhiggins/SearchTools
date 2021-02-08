'''
This code can be used to export the IDs for all papers that acknowledge
this grant ID in their acknowledgements.
'''

# Import the Entrez tool to connect to PubMed
from Bio import Entrez
# Provide an email address for PubMed to track usage
Entrez.email = "elh108@pitt.edu"
# Provide which database should be accessed as well as the grant ID to search
handle = Entrez.esearch(db="pubmed", term="InputGrantNumHere[Grant Number]", idtype="acc")
# Generate and print the record, can be printed and save in any format
record = Entrez.read(handle)
print(record)
# Close the PubMed connection
handle.close()
