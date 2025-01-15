This project enables researchers to analyze protein-protein interaction (PPI) networks using the STRING database. The script processes a list of genes, retrieves interaction data, builds a network, and identifies important genes based on their connectivity (node degree). It is particularly useful for identifying hub genes that play a crucial role in biological networks.

#Features
Batch Querying: Efficiently queries the STRING database for large gene lists in batches.
Network Visualization: Builds a PPI network using the NetworkX library.
Customizable Threshold: Allows users to adjust the interaction score threshold to capture relevant interactions.
Hub Gene Identification: Computes node degrees and identifies the top 20 genes with the highest connectivity.
Output Files: Saves full node degree data and the top 20 most connected genes to CSV files.
