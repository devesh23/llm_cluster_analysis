# LLM Cluster Analysis

A Jupyter notebook for performing semantic cluster analysis using Azure AI Foundry APIs. This tool groups multi-line semantic data by sequence identifiers, clusters them based on semantic similarity, and automatically generates descriptive titles for each cluster.

## Features

- **Multi-line Data Handling**: Automatically groups semantic data by `sequence_uuid`, treating multiple lines as a single semantic unit
- **Azure AI Integration**: Uses Azure AI Foundry APIs for embeddings and LLM-based cluster naming
- **Flexible Clustering**: Supports three clustering methods:
  - **LLM-based clustering** (Recommended): AI intelligently groups data based on semantic meaning
  - **K-means**: Traditional fast clustering for well-separated data
  - **DBSCAN**: Density-based clustering with automatic cluster detection
- **Automatic Cluster Naming**: Generates descriptive titles for clusters using LLM
- **Visualization**: PCA-based 2D visualization of semantic clusters
- **Export Functionality**: Saves clustered results to CSV for further analysis

## Prerequisites

- Python 3.8 or higher
- Azure AI Foundry account with API access
- API credentials for:
  - Embeddings model (e.g., text-embedding-ada-002)
  - Chat completion model (e.g., GPT-4)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/devesh23/llm_cluster_analysis.git
cd llm_cluster_analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Azure AI credentials:
```bash
cp .env.example .env
# Edit .env with your Azure AI credentials
```

## Configuration

Update the `.env` file with your Azure AI credentials:

```env
AZURE_AI_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
AZURE_AI_KEY=your-api-key-here
AZURE_AI_MODEL_NAME=text-embedding-ada-002
AZURE_AI_CHAT_MODEL=gpt-4
```

## Data Format

Your input CSV file should have the following structure:

| sequence_uuid | semantic_data |
|---------------|---------------|
| seq_001 | First line of semantic data |
| seq_001 | Second line related to seq_001 |
| seq_002 | Different semantic data |

### Key Points:
- **sequence_uuid**: Unique identifier for grouping related semantic entries
- **semantic_data**: The text content to be analyzed
- Multiple rows with the same `sequence_uuid` will be combined into a single semantic unit

## Usage

1. Launch Jupyter Notebook:
```bash
jupyter notebook cluster_analysis.ipynb
```

2. Follow the notebook workflow:
   - **Configuration**: Set clustering parameters (number of clusters, method)
   - **Data Loading**: Load and group your semantic data
   - **Embedding Generation**: Create embeddings using Azure AI
   - **Clustering**: Apply clustering algorithm
   - **Title Generation**: Generate descriptive cluster titles
   - **Visualization**: View cluster distribution
   - **Export**: Save results to CSV

3. The notebook includes a sample dataset (`sample_data.csv`) for testing

## Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[Clustering Methods Comparison](CLUSTERING_COMPARISON.md)** - Detailed comparison of LLM, K-means, and DBSCAN
- **[LLM Clustering Implementation Guide](LLM_CLUSTERING_GUIDE.md)** - Deep dive into how LLM clustering works

## Sample Output

The notebook produces:
- **Clustered DataFrame**: Original data with cluster assignments and titles
- **Visualization**: 2D PCA plot showing cluster distribution
- **Summary Report**: Detailed breakdown of each cluster with sample entries
- **CSV Export**: File containing all results (`clustered_results.csv`)

## Customization

### Clustering Parameters

In the notebook's Configuration cell, you can adjust:

```python
NUM_CLUSTERS = 5  # Number of clusters for K-means and LLM methods
CLUSTERING_METHOD = 'llm'  # Options: 'llm', 'kmeans', 'dbscan'
```

### Clustering Methods

- **LLM (Recommended)**: Uses AI to intelligently group data based on semantic meaning
  - Best semantic understanding and accuracy
  - Automatically identifies meaningful cluster themes
  - Slower and uses more API calls
  - Ideal for: Complex semantic data, when accuracy is more important than speed
  
- **K-means**: Traditional clustering algorithm
  - Fast and efficient
  - Good for well-separated, spherical clusters
  - Requires knowing the number of clusters
  - Ideal for: Large datasets, when speed is important
  
- **DBSCAN**: Density-based clustering
  - Automatically detects number of clusters
  - Better for arbitrary shapes
  - May identify outliers/noise
  - Ideal for: Unknown number of clusters, irregular cluster shapes

### Method Comparison

| Method | Speed | Semantic Accuracy | API Usage | Best Use Case |
|--------|-------|-------------------|-----------|---------------|
| LLM | Slow | Highest | High | Semantic analysis, complex themes |
| K-means | Fast | Medium | Low | Large datasets, simple clustering |
| DBSCAN | Medium | Medium | Low | Automatic cluster detection |

### Advanced Options

- **Batch Size**: Modify `batch_size` in `get_embeddings()` to control API request sizes
- **Sample Size**: Adjust how many examples are sent to LLM for title generation
- **Visualization**: Customize colors, plot size, and styling in `visualize_clusters()`

## Architecture

```
┌─────────────────┐
│   Input CSV     │
│  (with UUIDs)   │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Group by UUID   │
│ Combine Lines   │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Azure AI        │
│ Embeddings API  │
└────────┬────────┘
         │
         v
┌─────────────────────────────────────────┐
│        Clustering Method Selection      │
├─────────────┬─────────────┬─────────────┤
│ LLM-based   │  K-means    │   DBSCAN    │
│ (AI Groups) │ (Fast)      │ (Auto)      │
└──────┬──────┴──────┬──────┴──────┬──────┘
       │             │             │
       └─────────────┴─────────────┘
                     │
                     v
         ┌─────────────────────┐
         │  LLM Clustering     │
         │  1. Identify Themes │
         │  2. Assign Items    │
         └──────────┬──────────┘
                    │
                    v
         ┌─────────────────────┐
         │ Azure AI LLM        │
         │ Title Generation    │
         │ (or use LLM themes) │
         └──────────┬──────────┘
                    │
                    v
         ┌─────────────────────┐
         │ Results Export      │
         │ & Visualization     │
         └─────────────────────┘
```

## Troubleshooting

### Common Issues

1. **Missing credentials error**:
   - Ensure `.env` file exists and contains valid Azure AI credentials
   - Check that environment variables are loaded properly

2. **API rate limits**:
   - Reduce `batch_size` in embedding generation
   - Add delays between API calls if needed

3. **Poor clustering results**:
   - Try different clustering methods (K-means vs DBSCAN)
   - Adjust number of clusters
   - Check data quality and preprocessing

4. **Import errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Use Python 3.8 or higher

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the GitHub repository.
