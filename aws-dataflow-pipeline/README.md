Projeto: AWS DataFlow Pipeline (ETL com múltiplas fontes de dados)
Objetivo
Este projeto tem como objetivo a construção de um pipeline de dados utilizando Python, que integra informações de diferentes fontes (banco de dados PostgreSQL, API REST e arquivos CSV externos) e realiza um processo completo de ETL (Extract, Transform, Load).

O pipeline está preparado para trabalhar com a AWS, realizando armazenamento dos dados tratados no Amazon S3 e consultas via Amazon Athena. Neste momento, por questões de custo e acessibilidade, a extração de dados da camada S3 está sendo simulada com arquivos CSV locais, mantendo toda a estrutura de código pronta para uma futura integração com um bucket real na AWS.

Tecnologias utilizadas
Python 3.x

Pandas

Psycopg2

Requests

Boto3 (estruturado, mas simulado no momento)

PostgreSQL

Docker (para ambiente local do PostgreSQL)

Git

Estrutura do Projeto
css
Copiar código
aws-dataflow-pipeline/
├── src/
│   ├── extract/
│   │   ├── extract_postgres.py
│   │   ├── extract_api.py
│   │   └── extract_s3_csv.py
│   ├── transform/
│   │   └── transform_data.py
│   ├── load/
│   │   ├── load_to_s3.py
│   │   └── load_to_athena.py
│   └── aws_utils/
│       └── helpers.py
├── data/
│   └── data_clientes.csv
├── tests/
│   └── test_transform.py
├── docs/
│   └── pipeline_diagram.png
├── requirements.txt
├── .gitignore
└── README.md
Funcionalidades Implementadas
Extração de dados de um banco PostgreSQL

Extração de dados de uma API REST pública

Extração de dados simulada de arquivos CSV externos (em substituição ao S3)

Transformações nos dados utilizando pandas

Estruturação de código para futura carga em S3 e consultas via Athena

Estrutura modular seguindo boas práticas de Engenharia de Dados

Execução do Projeto
Pré-requisitos
Python 3.x

Docker (opcional, para subir o PostgreSQL local)

Conta AWS (opcional, para uso futuro com S3 e Athena)

Instalação de dependências
bash
Copiar código
pip install -r requirements.txt
Extração de Dados
PostgreSQL:
Edite e execute o arquivo src/extract/extract_postgres.py

API REST:
Execute o arquivo src/extract/extract_api.py

CSV Local (simulação do S3):
Execute o arquivo src/extract/extract_s3_csv.py

Transformação dos Dados
Execute:

bash
Copiar código
python src/transform/transform_data.py
Carga (simulada no momento)
Os scripts de carga load_to_s3.py e load_to_athena.py estão estruturados para futura integração, mas podem ser ajustados conforme necessidade.

Observações sobre a AWS
Toda a arquitetura de código foi desenvolvida com a AWS em mente, utilizando a biblioteca boto3 e preparando a camada de carga para interações com o S3 e Athena.

Por questões de custo, as operações com AWS estão simuladas localmente no momento.
Para adaptação futura, basta ajustar as configurações de boto3 e credenciais AWS.

Próximos passos (Evoluções futuras)
Implementação real da carga no S3

Criação automática de tabelas externas no Athena

Integração com AWS Lambda para automação do pipeline

Versionamento de dados

Monitoramento de execução

Contato
Pedro França
Desenvolvedor Python focado em Engenharia de Dados e soluções em Cloud.