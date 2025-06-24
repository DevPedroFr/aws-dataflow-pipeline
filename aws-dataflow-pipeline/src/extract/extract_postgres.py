import psycopg2
import pandas as pd

def extract_data_from_postgres():
    try:
        #configurações de conexão
        conn = psycopg2.connect(
            host ="localhost",
            port ="5432",
            database ="meubanco",
            user ="postgres",
            password ="123456"    
            )
        
        query = "SELECT * FROM vendas;"
        df = pd.read_sql_query(query, conn)

        print("Dados extraídos com sucesso")
        print(df)

        df.to_csv('vendas.csv', index=False)

        conn.close()
    except Exception as e:
        print(f"Erro ao conectar ou extrair dados: {e}")

if __name__ == "__main__":
    extract_data_from_postgres()

        