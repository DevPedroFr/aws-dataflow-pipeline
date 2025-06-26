import pandas as pd

def transform_data(df_vendas, df_clientes):
    try:
        if df_vendas is None:
            raise ValueError("df_vendas is None")
        df_vendas = df_vendas.rename(columns={"cliente": "nome"})

        df_merged = pd.merge(df_vendas, df_clientes, on="nome", how="left")

        df_merged.columns = [col.lower().strip() for col in df_merged.columns]

        df_merged['email'] = df_merged['email'].fillna('nao_informado@example.com')

        def faixa_preco(valor):
            if valor < 500:
                return 'baixo'
            elif valor <= 2000:
                return 'médio'
            else:
                return 'alto'
            
        df_merged['faixa_preco'] = df_merged['valor'].apply(faixa_preco)

        print('Dados transformados:')
        print(df_merged.head())

        df_merged.to_csv('data/dataset_final.csv', index=False)

        return df_merged
    
    except Exception as e:
        print(f'Erro ao transformar os dados: {e}')
        return None
