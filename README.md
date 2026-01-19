# Amazon Sales Data Pipeline

A comprehensive ETL (Extract, Transform, Load) pipeline for processing and analyzing Amazon sales data.

## Project Structure

```
Amazon-Sales-Data-Pipeline/
│
├── data/
│   ├── raw/                      # Raw data files
│   │   └── amazon.csv
│   └── processed/                # Cleaned and processed data
│       └── cleaned_amazon_sales.csv
│
├── src/                          # Main pipeline modules
│   ├── __init__.py
│   ├── ingestion.py             # Data loading and inspection
│   ├── cleaning.py              # Missing values, duplicates handling
│   ├── transformation.py         # Data type conversion and feature engineering
│   ├── optimization.py           # Memory optimization
│   ├── storage.py               # Data saving and reporting
│   └── pipeline.py              # Main orchestration
│
│
└── README.md
```

## Features

### Data Ingestion
- Load CSV data efficiently
- Automatic data inspection and basic statistics

### Data Cleaning
- Handle missing values (median for numerical, 'Unknown' for categorical)
- Remove duplicate records
- Clean text columns (strip whitespace, standardize case)
- Remove unnecessary columns (img_link, product_link)

### Data Transformation
- Clean price columns (remove currency symbols and commas)
- Parse discount percentages
- Convert ratings to numeric values
- Create derived features:
  - `discount_amount`: Difference between actual and discounted price
  - `revenue_estimate`: Estimated revenue from sales

### Data Optimization
- Convert categorical columns to category type for memory efficiency
- Track memory usage before and after optimization

### Data Storage & Reporting
- Save processed data to CSV
- Generate top products by revenue
- Calculate category-wise revenue

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Amazon-Sales-Data-Pipeline
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Pipeline

```python
from src.pipeline import run_pipeline

# Run the complete pipeline
df = run_pipeline(
    raw_data_path='data/raw/amazon.csv',
    output_path='data/processed/cleaned_amazon_sales.csv'
)
```

### Use Individual Modules

```python
from src import ingestion, cleaning, transformation, optimization, storage

# Load data
df = ingestion.load_data('data/raw/amazon.csv')

# Clean data
df = cleaning.handle_missing_values(df)
df = cleaning.remove_duplicates(df)

# Transform data
df = transformation.clean_price_columns(df)
df = transformation.create_derived_features(df)

# Optimize
df = optimization.optimize_dtypes(df)

# Save
storage.save_processed_data(df, 'data/processed/cleaned_amazon_sales.csv')
```

## Data Processing Steps

1. **Ingestion**: Load CSV and perform initial inspection
2. **Cleaning**: Handle missing values, remove duplicates, clean text
3. **Transformation**: Parse prices, standardize formats, create features
4. **Optimization**: Optimize data types for memory efficiency
5. **Storage**: Save processed data and generate reports

## Key Metrics

The pipeline generates the following metrics:

- **Top Products**: Top 10 products by revenue estimate
- **Category Revenue**: Total revenue aggregated by product category
- **Data Quality**: Memory usage before and after optimization
- **Duplicate Records**: Number of duplicate rows removed

<!--  [futher need to be added]
## Analysis Notebook

The `notebooks/analysis.ipynb` notebook provides:
- Exploratory Data Analysis (EDA)
- Visualizations of key metrics
- Statistical analysis
- Business insights
-->

## Data Dictionary

| Column | Description |
|--------|-------------|
| product_name | Name of the product |
| category | Product category |
| discounted_price | Current selling price (₹) |
| actual_price | Original price (₹) |
| discount_percentage | Discount as percentage |
| rating | Product rating (0-5) |
| rating_count | Number of ratings received |
| product_id | Unique product identifier |
| discount_amount | Actual discount in rupees |
| revenue_estimate | Estimated revenue (discounted_price × rating_count) |

## Requirements

- Python 3.8+
- pandas
- numpy
<!-- - matplotlib -->
<!-- - jupyter -->