'''
This script is to be run second.
It uses the list of IDs from the previous step to generate a list of
appropriate papers.
The IDs from the last step are to be inputted as identified below.
'''

# Connect to the database again with the IDs inputted
# Can change the return mode from XML if another format is desired
handle = Entrez.esummary(db="pubmed", id="Enter List of IDs Here", retmode="xml")
# Parse the records according to the type of file
records = Entrez.parse(handle)
# Print each of the generated records
for record in records:
     # Each record is a Python dictionary or list.
    print(record['Title'])
# Close the connection
handle.close()
