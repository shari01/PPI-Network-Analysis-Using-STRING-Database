import pandas as pd
import requests
import networkx as nx
import matplotlib.pyplot as plt

# Load the gene list from the CSV file
file_path = 'C:/Users/Sheryar Malik/Downloads/PPI_Network_Analysis-main/code/genes.csv'
gene_df = pd.read_csv(file_path)

# Check if the 'gene' column exists and is correctly named
if 'gene' not in gene_df.columns:
    raise ValueError("The input file does not contain a 'gene' column. Please check the column name.")

# Extract the gene names from the column, ensuring there are no NaN values
gene_list = gene_df['gene'].dropna().tolist()

# Function to query STRING database for PPI data in batches
def query_stringdb_batch(gene_list, batch_size=500):
    url = 'https://string-db.org/api/json/network?identifiers='
    ppi_data = []
    
    # Split the gene list into smaller batches and send multiple requests
    for i in range(0, len(gene_list), batch_size):
        genes_batch = gene_list[i:i + batch_size]
        genes_query = '%0D'.join(genes_batch)
        full_url = url + genes_query + "&species=9606"  # 9606 is the species ID for humans
        response = requests.get(full_url)
        
        if response.status_code == 200:
            ppi_data.extend(response.json())  # Add the results from the current batch
        else:
            print(f"Error querying STRING DB: {response.status_code}")
    
    return ppi_data

# Get PPI data for the provided gene list
ppi_data = query_stringdb_batch(gene_list)

# Check how many genes are mapped by STRING
mapped_genes = set()
for interaction in ppi_data:
    mapped_genes.add(interaction['preferredName_A'])
    mapped_genes.add(interaction['preferredName_B'])

print(f"Total genes in input: {len(gene_list)}")
print(f"Total mapped genes: {len(mapped_genes)}")

# Parse the PPI data to build a network
G = nx.Graph()

# Adjust interaction score threshold if needed
interaction_threshold = 0.15  # Lowering the score threshold to capture more interactions

for interaction in ppi_data:
    gene_a = interaction['preferredName_A']
    gene_b = interaction['preferredName_B']
    score = interaction['score']
    identifier_a = interaction['stringId_A']
    identifier_b = interaction['stringId_B']
    
    if score >= interaction_threshold:  # Adjusted threshold for capturing more interactions
        G.add_edge((gene_a, identifier_a), (gene_b, identifier_b), weight=score)

# Prepare the list for node degree along with identifiers
node_data = []
for node, degree in G.degree():
    gene_name = node[0]        # Extract gene name
    string_id = node[1]        # Extract STRING ID
    node_data.append([gene_name, string_id, degree])  # Append gene name, ID, and degree

# Convert the results to a DataFrame
node_degree_df = pd.DataFrame(node_data, columns=['node', 'identifier', 'node_degree'])

# Sort the genes by their node degree in descending order
node_degree_df_sorted = node_degree_df.sort_values(by='node_degree', ascending=False)

# Save the full results to a CSV file
output_file_full = 'C:/Users/Sheryar Malik/Downloads/PPI_Network_Analysis-main/code/node_degrees.csv'
node_degree_df_sorted.to_csv(output_file_full, index=False)

# Get the top 20 genes by node degree
top_20_genes_df = node_degree_df_sorted.head(20)

# Save the top 20 genes to a separate CSV file
output_file_top_20 = 'C:/Users/Sheryar Malik/Downloads/PPI_Network_Analysis-main/code/top_20_genes.csv'
top_20_genes_df.to_csv(output_file_top_20, index=False)

print(f'Node degree data saved to {output_file_full}')
print(f'Top 20 important genes saved to {output_file_top_20}')
