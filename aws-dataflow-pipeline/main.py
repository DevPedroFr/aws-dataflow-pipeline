from src.extract.extract_postgres import extract_data_from_postgres
from src.extract.extract_api import extract_users_from_api
from src.extract.extract_s3_csv import extract_csv_local
from src.transform.transform_data import transform_data
from src.load.load_to_s3 import load_to_s3

def run_pipeline():
    print("\n==== Etapa 1: Extração ====")
    df_vendas = extract_data_from_postgres()
    df_clientes = extract_csv_local('data/data_clientes.csv')
    df_api = extract_users_from_api()

    print("\n==== Etapa 2: Transformação ====")
    df_final = transform_data(df_vendas, df_clientes, df_api)

    print("\n==== Etapa 3: Carga ====")
    load_to_s3(df_final, ano=2024, mes="06")

    print("\n Pipeline executado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
