from src.extract.extract_postgres import extract_data_from_postgres
from src.extract.extract_s3_csv import extract_csv_local
from src.transform.transform_data import transform_data
from src.load.load_to_s3 import load_to_s3_simulado

df_vendas = extract_data_from_postgres()
df_clientes = extract_csv_local('data/data_clientes.csv')

df_final = transform_data(df_vendas, df_clientes)

load_to_s3_simulado(df_final, ano=2024, mes='06')
