"""
Data Optimization Module
Handles data type optimization and memory efficiency.
"""

import pandas as pd


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize data types to reduce memory usage.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with optimized data types
    """
    df = df.copy()
    
    print(f"Before optimization: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    # Convert categorical columns
    if 'category' in df.columns:
        df['category'] = df['category'].astype('category')
    
    if 'product_id' in df.columns:
        df['product_id'] = df['product_id'].astype('category')
    
    print(f"After optimization: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    return df


def get_memory_usage(df: pd.DataFrame) -> float:
    """
    Get current memory usage of the DataFrame in MB.
    
    Args:
        df: DataFrame to analyze
        
    Returns:
        Memory usage in MB
    """
    return df.memory_usage(deep=True).sum() / 1024**2
