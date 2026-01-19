"""
Data Transformation Module
Handles data type conversions, parsing, and feature engineering.
"""

import pandas as pd


def clean_price(col: pd.Series) -> pd.Series:
    """
    Clean price columns by removing currency symbols and commas.
    
    Args:
        col: pandas Series containing price data
        
    Returns:
        Series with cleaned prices as floats
    """
    return (
        col.str.replace('₹', '', regex=False)
           .str.replace(',', '', regex=False)
           .astype(float)
    )


def clean_price_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean price-related columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with cleaned price columns
    """
    df = df.copy()
    
    if 'discounted_price' in df.columns:
        df['discounted_price'] = clean_price(df['discounted_price'])
    
    if 'actual_price' in df.columns:
        df['actual_price'] = clean_price(df['actual_price'])
    
    return df


def clean_discount_percentage(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean discount percentage column.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with cleaned discount percentage
    """
    df = df.copy()
    
    if 'discount_percentage' in df.columns:
        df['discount_percentage'] = (
            df['discount_percentage']
            .str.replace('%', '', regex=False)
            .astype(float)
        )
    
    return df


def clean_ratings_and_counts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean rating and rating_count columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with cleaned ratings and counts
    """
    df = df.copy()
    
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)
    
    if 'rating_count' in df.columns:
        df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce').fillna(0)
    
    return df


def create_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new derived features from existing columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with new derived features
    """
    df = df.copy()
    
    # Calculate discount amount
    if 'actual_price' in df.columns and 'discounted_price' in df.columns:
        df['discount_amount'] = df['actual_price'] - df['discounted_price']
    
    # Calculate revenue estimate
    if 'discounted_price' in df.columns and 'rating_count' in df.columns:
        df['revenue_estimate'] = df['discounted_price'] * df['rating_count']
    
    return df
