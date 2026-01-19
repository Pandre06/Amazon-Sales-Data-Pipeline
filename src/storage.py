"""
Data Storage Module
Handles saving processed data and generating reports.
"""

import pandas as pd
from pathlib import Path


def save_processed_data(df: pd.DataFrame, filepath: str) -> None:
    """
    Save processed data to CSV file.
    
    Args:
        df: DataFrame to save
        filepath: Path where the file will be saved
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")


def get_top_products(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Get top N products by revenue estimate.
    
    Args:
        df: Input DataFrame
        n: Number of top products to return
        
    Returns:
        Series with top products and their revenue
    """
    top_products = (
        df.groupby('product_name')['revenue_estimate']
          .sum()
          .sort_values(ascending=False)
          .head(n)
    )
    return top_products


def get_category_revenue(df: pd.DataFrame) -> pd.Series:
    """
    Get revenue aggregated by category.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Series with category-wise revenue
    """
    category_revenue = (
        df.groupby('category')['revenue_estimate']
          .sum()
          .sort_values(ascending=False)
    )
    return category_revenue


def print_top_products(df: pd.DataFrame, n: int = 10) -> None:
    """
    Print top N products by revenue.
    
    Args:
        df: Input DataFrame
        n: Number of top products to display
    """
    top_products = get_top_products(df, n)
    print(f"\nTop {n} Products by Revenue Estimate:")
    print(top_products)
