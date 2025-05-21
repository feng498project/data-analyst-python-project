import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def analyze_data(df):
    print("\n--- Dataset Overview ---")
    print(df.info())
    print("\n--- Basic Statistics ---")
    print(df.describe())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

def top_categories(df, column, n=5):
    print(f"\n--- Top {n} {column} ---")
    print(df[column].value_counts().head(n))

if __name__ == "__main__":
    filepath = "data.csv"
    df = load_data(filepath)
    analyze_data(df)
    top_categories(df, column="category")
