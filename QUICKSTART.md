# Quick Start Guide

This guide will help you get started with LLM Cluster Analysis in 5 minutes.

## Step 1: Install Dependencies (2 minutes)

```bash
# Clone the repository
git clone https://github.com/devesh23/llm_cluster_analysis.git
cd llm_cluster_analysis

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Azure AI (1 minute)

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Azure AI credentials:
```env
AZURE_AI_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
AZURE_AI_KEY=your-api-key-here
AZURE_AI_MODEL_NAME=text-embedding-ada-002
AZURE_AI_CHAT_MODEL=gpt-4
```

### Getting Azure AI Credentials

If you don't have Azure AI credentials:

1. Go to [Azure Portal](https://portal.azure.com)
2. Create or navigate to your Azure AI Foundry resource
3. Under "Keys and Endpoint", copy:
   - Endpoint URL → `AZURE_AI_ENDPOINT`
   - Key 1 or Key 2 → `AZURE_AI_KEY`
4. Note the model deployment names for embeddings and chat

## Step 3: Run the Notebook (2 minutes)

```bash
# Launch Jupyter Notebook
jupyter notebook cluster_analysis.ipynb
```

In the notebook:
1. Run all cells (Cell → Run All)
2. The notebook will use `sample_data.csv` by default
3. View the results: clusters, titles, and visualizations

## Using Your Own Data

Replace `sample_data.csv` with your data file. Required format:

```csv
sequence_uuid,semantic_data
uuid_1,Your first text entry
uuid_1,Related text for same uuid
uuid_2,Different text entry
```

**Important**: Multiple rows with the same `sequence_uuid` will be combined into a single semantic unit.

## Customizing Clusters

In the notebook, modify these settings in the Configuration cell:

```python
NUM_CLUSTERS = 5          # Number of clusters
CLUSTERING_METHOD = 'llm' # Options: 'llm', 'kmeans', 'dbscan'
```

### Clustering Method Guide:
- **'llm'** (Recommended): AI intelligently groups data for best semantic accuracy
  - Pros: Superior semantic understanding, automatic theme identification
  - Cons: Slower, uses more API calls
- **'kmeans'**: Fast traditional clustering
  - Pros: Very fast, efficient
  - Cons: Requires known cluster count, less semantic awareness
- **'dbscan'**: Automatic cluster detection
  - Pros: Finds clusters automatically, handles noise
  - Cons: May need parameter tuning

## Expected Output

1. **Console Output**: Progress messages and cluster statistics
2. **Visualization**: 2D scatter plot showing clusters
3. **Summary Report**: Detailed breakdown of each cluster
4. **CSV File**: `clustered_results.csv` with all results

## Example Cluster Output

```
CLUSTER 0: Delivery and Shipping Issues
Size: 3 items
Sample entries:
  1. [seq_001] Customer complained about slow delivery times...
  2. [seq_008] Delivery was faster than expected...

CLUSTER 1: Technical Problems  
Size: 4 items
Sample entries:
  1. [seq_002] Website was down during peak hours...
  2. [seq_007] Mobile app crashes on startup...
```

## Troubleshooting

### "Missing credentials" error
- Ensure `.env` file exists and contains valid credentials
- Restart Jupyter kernel after updating `.env`

### "Module not found" error
- Run: `pip install -r requirements.txt`
- Restart Jupyter kernel

### Poor clustering results
- Try different clustering methods: 'llm' for best semantic accuracy
- For LLM method: Adjust `NUM_CLUSTERS` (try 3-10 for best results)
- For K-means: Increase/decrease `NUM_CLUSTERS`
- Try `CLUSTERING_METHOD = 'dbscan'` for automatic cluster detection
- Ensure your data has meaningful semantic differences

## Next Steps

- Adjust clustering parameters for better results
- Export results for further analysis
- Integrate with your data pipeline
- Customize visualization styles

## Support

- Check the main [README.md](README.md) for detailed documentation
- Open an issue on GitHub for bugs or questions
- Review the notebook comments for implementation details
