import os 

def load_to_s3(df, ano, mes):
    try:
        dir_path = f"s3_simulado/ano={ano}/mes={mes}"
        os.makedirs(dir_path, exist_ok=True)

        output_path = os.path.join(dir_path, "dataset_final.csv")
        df.to_csv(output_path, index=False)

        print(f"Arquivo salvo em: {output_path}")

    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')