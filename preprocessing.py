import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path)

    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df

if __name__ == "__main__":
    df = load_and_clean_data("data/raw_dataset_final.xlsx")
    print(df.head())