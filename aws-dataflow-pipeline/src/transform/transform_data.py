import pandas as pd

def transform_data(df_vendas, df_clientes, df_api):
    try:
        # Renomeia a coluna para fazer o merge com df_clientes
        df_vendas = df_vendas.rename(columns={"cliente": "nome"})

        # Merge com dados de clientes (usando nome)
        df_merged = pd.merge(df_vendas, df_clientes, on="nome", how="left")

        # Padroniza nomes das colunas
        df_merged.columns = [col.lower().strip() for col in df_merged.columns]

        # Preenche e-mails faltantes
        df_merged['email'] = df_merged['email'].fillna('nao_informado@example.com')

        def faixa_preco(valor):
            if valor <500:
                return 'baixo'
            elif valor <= 2000:
                return 'medio'
            else:
                return 'alto'
            
        df_merged['faixa_preco'] = df_merged['valor'].apply(faixa_preco)

        df_api = df_api.rename(columns={"name": "nome", "city": "cidade"})

        df_merged = pd.merge(df_merged, df_api[['email', 'cidade']], on='email', how='left')

        print('Dados transformados:')
        print(df_merged.head())

        df_merged.to_csv('data/dataset_final.csv', index=False)

        return df_merged
    
    except Exception as e:
        print(f' Erro ao transformar os dados: {e}')
        return None