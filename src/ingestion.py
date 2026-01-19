"""
Data Ingestion Module
Handles loading and initial inspection of raw data.
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data from the given filepath.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        pandas DataFrame with loaded data
    """
    df = pd.read_csv(filepath)
    return df


def inspect_data(df: pd.DataFrame) -> None:
    """
    Perform basic inspection of the dataset.
    
    Args:
        df: DataFrame to inspect
    """
    print(f"Dataset Shape: {df.shape}")
    print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"\nFirst few rows:\n{df.head()}")
    print(f"\nData Types:\n{df.info()}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
