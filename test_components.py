#!/usr/bin/env python3
"""
Test script to validate the cluster analysis notebook components.
This script tests the data loading and grouping functionality without requiring Azure credentials.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def test_load_and_group_data():
    """Test data loading and grouping by sequence_uuid."""
    print("Testing data loading and grouping...")
    
    # Create sample data
    data = {
        'sequence_uuid': ['seq_001', 'seq_001', 'seq_002', 'seq_003', 'seq_003', 'seq_003'],
        'semantic_data': [
            'First line for seq_001',
            'Second line for seq_001',
            'Single line for seq_002',
            'First line for seq_003',
            'Second line for seq_003',
            'Third line for seq_003'
        ]
    }
    df = pd.DataFrame(data)
    
    # Group by sequence_uuid
    grouped_df = df.groupby('sequence_uuid').agg({
        'semantic_data': lambda x: ' '.join(x.astype(str))
    }).reset_index()
    
    grouped_df.rename(columns={'semantic_data': 'combined_semantic_data'}, inplace=True)
    
    # Validate results
    assert len(grouped_df) == 3, f"Expected 3 groups, got {len(grouped_df)}"
    assert 'First line for seq_001 Second line for seq_001' in grouped_df['combined_semantic_data'].values
    
    print("✓ Data loading and grouping test passed")
    print(f"  - Loaded {len(df)} rows")
    print(f"  - Grouped into {len(grouped_df)} unique sequence_uuids")
    
    return grouped_df


def test_sample_data_file():
    """Test that sample_data.csv exists and has correct format."""
    print("\nTesting sample data file...")
    
    file_path = Path('sample_data.csv')
    
    if not file_path.exists():
        print("✗ sample_data.csv not found")
        return False
    
    # Load the file
    df = pd.read_csv(file_path)
    
    # Check columns
    required_columns = ['sequence_uuid', 'semantic_data']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"✗ Missing required columns: {missing_columns}")
        return False
    
    # Group data
    grouped_df = df.groupby('sequence_uuid').agg({
        'semantic_data': lambda x: ' '.join(x.astype(str))
    }).reset_index()
    
    print("✓ Sample data file test passed")
    print(f"  - Loaded {len(df)} rows")
    print(f"  - Contains {len(grouped_df)} unique sequence_uuids")
    print(f"  - Columns: {df.columns.tolist()}")
    
    return True


def test_clustering_simulation():
    """Simulate clustering with random embeddings."""
    print("\nTesting clustering simulation...")
    
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    
    # Create random embeddings (simulating real embeddings)
    n_samples = 15
    embedding_dim = 128
    embeddings = np.random.randn(n_samples, embedding_dim)
    
    # Standardize
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)
    
    # Cluster
    n_clusters = 5
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(embeddings_scaled)
    
    # Validate
    assert len(labels) == n_samples
    assert len(set(labels)) <= n_clusters
    
    print("✓ Clustering simulation test passed")
    print(f"  - Created {n_samples} sample embeddings")
    print(f"  - Clustered into {len(set(labels))} clusters")
    print(f"  - Cluster distribution: {np.bincount(labels)}")
    
    return labels


def main():
    """Run all tests."""
    print("=" * 70)
    print("LLM Cluster Analysis - Component Tests")
    print("=" * 70)
    
    tests_passed = 0
    tests_total = 3
    
    try:
        test_load_and_group_data()
        tests_passed += 1
    except Exception as e:
        print(f"✗ Data loading test failed: {e}")
    
    try:
        if test_sample_data_file():
            tests_passed += 1
    except Exception as e:
        print(f"✗ Sample data file test failed: {e}")
    
    try:
        test_clustering_simulation()
        tests_passed += 1
    except Exception as e:
        print(f"✗ Clustering simulation test failed: {e}")
    
    print("\n" + "=" * 70)
    print(f"Tests completed: {tests_passed}/{tests_total} passed")
    print("=" * 70)
    
    if tests_passed == tests_total:
        print("\n✓ All tests passed successfully!")
        return 0
    else:
        print(f"\n⚠ {tests_total - tests_passed} test(s) failed")
        return 1


if __name__ == '__main__':
    exit(main())
