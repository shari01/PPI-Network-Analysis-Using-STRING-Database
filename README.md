<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPI Network Analysis Using STRING Database</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0 15px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
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
        

        <h2>Features</h2>
        <ul>
            <li><strong>Batch Querying</strong>: Efficiently queries the <strong>STRING database</strong> for large gene lists in batches.</li>
            <li><strong>Network Visualization</strong>: Builds a <strong>PPI network</strong> using the <strong>NetworkX</strong> library.</li>
            <li><strong>Customizable Threshold</strong>: Allows users to adjust the <strong>interaction score threshold</strong> to capture relevant interactions.</li>
            <li><strong>Hub Gene Identification</strong>: Computes <strong>node degrees</strong> and identifies the top 20 genes with the highest connectivity.</li>
            <li><strong>Output Files</strong>: Saves <strong>full node degree data</strong> and the <strong>top 20 most connected genes</strong> to CSV files.</li>
        </ul>
    </div>
</body>
</html>
