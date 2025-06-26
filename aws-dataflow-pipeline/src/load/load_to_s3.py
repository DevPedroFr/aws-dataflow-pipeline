import pandas as pd
from pathlib import Path

def load_to_s3(df, ano, mes):
    try:
        path = Path(f"s3_simulado/vendas/ano={ano}/mes={mes}")
        path.mkdir(parents=True, exist_ok=True)

        if df is not None:
            df.to_csv(path / 'dataset_final.csv', index=False)
            print(f' Arquivo salvo em: {path / "dataset_final.csv"}')
        else:
            print(' DataFrame fornecido é None. Nenhum arquivo foi salvo.')

    except Exception as e:
        print(f' Erro ao salvar arquivo simulado no S3: {e}')

        
