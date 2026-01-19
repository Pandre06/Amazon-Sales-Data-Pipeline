"""
Data Cleaning Module
Handles missing values, duplicates, and basic data cleaning.
"""

import pandas as pd
import numpy as np


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values by filling numerical columns with median
    and categorical columns with 'Unknown'.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with missing values handled
    """
    df = df.copy()
    
    # Fill missing numerical values with median
    num_cols = df.select_dtypes(include=np.number).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    # Fill missing categorical values
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")
    
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the dataset.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with duplicates removed
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    
    print(f"Removed {before - after} duplicate rows")
    return df


def remove_unnecessary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns that are not needed for analysis.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with unnecessary columns removed
    """
    cols_to_drop = ['img_link', 'product_link']
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    
    if existing_cols:
        df = df.drop(columns=existing_cols)
        print(f"Dropped columns: {existing_cols}")
    
    return df


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize text columns.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with cleaned text columns
    """
    df = df.copy()
    
    if 'category' in df.columns:
        df['category'] = df['category'].str.strip().str.title()
    
    if 'product_name' in df.columns:
        df['product_name'] = df['product_name'].str.strip()
    
    return df
