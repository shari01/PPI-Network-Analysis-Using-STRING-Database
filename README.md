<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPI Network Analysis Using STRING Database</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 20px 30px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: disc;
            margin: 10px 0 10px 20px;
        }
        li {
            margin-bottom: 8px;
        }
        strong {
            color: #2c3e50;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.9em;
            color: #7f8c8d;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PPI Network Analysis Using STRING Database</h1>
        <p>
            This project enables researchers to analyze <strong>Protein-Protein Interaction (PPI)</strong> networks using the 
            <strong>STRING database</strong>. The script processes a list of genes, retrieves interaction data, builds a network, 
            and identifies important genes based on their <strong>connectivity (node degree)</strong>. It is particularly useful for identifying 
            <strong>hub genes</strong> that play a crucial role in biological networks.
        </p>

        <h2>Features</h2>
        <ul>
            <li><strong>Batch Querying</strong>: Efficiently queries the <strong>STRING database</strong> for large gene lists in batches.</li>
            <li><strong>Network Visualization</strong>: Builds a <strong>PPI network</strong> using the <strong>NetworkX</strong> library.</li>
            <li><strong>Customizable Threshold</strong>: Allows users to adjust the <strong>interaction score threshold</strong> to capture relevant interactions.</li>
            <li><strong>Hub Gene Identification</strong>: Computes <strong>node degrees</strong> and identifies the top 20 genes with the highest connectivity.</li>
            <li><strong>Output Files</strong>: Saves <strong>full node degree data</strong> and the <strong>top 20 most connected genes</strong> to CSV files.</li>
        </ul>
    </div>
    <footer>
        Created by <strong>Your Name</strong> | <a href="https://github.com/YourUsername">GitHub Profile</a>
    </footer>
</body>
</html>
