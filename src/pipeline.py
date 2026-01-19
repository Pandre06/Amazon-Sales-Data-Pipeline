"""
Main Pipeline Module
Orchestrates the entire data processing pipeline.
"""

import pandas as pd
from pathlib import Path
from . import ingestion, cleaning, transformation, optimization, storage


def run_pipeline(raw_data_path: str, output_path: str) -> pd.DataFrame:
    """
    Execute the complete data processing pipeline.
    
    Args:
        raw_data_path: Path to raw CSV file
        output_path: Path where cleaned data will be saved
        
    Returns:
        Processed and cleaned DataFrame
    """
    print("=" * 60)
    print("AMAZON SALES DATA PIPELINE")
    print("=" * 60)
    
    # Step 1: Ingestion
    print("\n[1/6] Loading data...")
    df = ingestion.load_data(raw_data_path)
    ingestion.inspect_data(df)
    
    # Step 2: Cleaning
    print("\n[2/6] Handling missing values...")
    df = cleaning.handle_missing_values(df)
    
    print("\n[3/6] Removing duplicates...")
    df = cleaning.remove_duplicates(df)
    
    print("\n[4/6] Cleaning text columns...")
    df = cleaning.clean_text_columns(df)
    df = cleaning.remove_unnecessary_columns(df)
    
    # Step 3: Transformation
    print("\n[5/6] Transforming data...")
    df = transformation.clean_price_columns(df)
    df = transformation.clean_discount_percentage(df)
    df = transformation.clean_ratings_and_counts(df)
    df = transformation.create_derived_features(df)
    
    # Step 4: Optimization
    print("\n[6/6] Optimizing data types...")
    df = optimization.optimize_dtypes(df)
    
    # Step 5: Storage
    print("\nSaving processed data...")
    storage.save_processed_data(df, output_path)
    
    # Generate reports
    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY REPORTS")
    print("=" * 60)
    storage.print_top_products(df)
    
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)
    
    return df


if __name__ == "__main__":
    # Define paths
    raw_data_path = Path(__file__).parent.parent / "data" / "raw" / "amazon.csv"
    output_path = Path(__file__).parent.parent / "data" / "processed" / "cleaned_amazon_sales.csv"
    
    # Run pipeline
    df = run_pipeline(str(raw_data_path), str(output_path))
