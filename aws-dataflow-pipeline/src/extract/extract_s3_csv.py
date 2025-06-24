from pathlib import Path
import pandas as pd

def extract_csv_local(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dados extraídos do CSV local:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Erro ao ler CSV local: {e}")

if __name__ == "__main__":
    path = Path(__file__).parent.parent.parent / 'data' / 'data_clientes.csv'
    extract_csv_local(path)

