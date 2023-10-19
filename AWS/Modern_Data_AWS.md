# Contents

- [Contents](#contents)
- [Contato do palestrante: AWS Modern Data Architectures](#contato-do-palestrante-aws-modern-data-architectures)
- [O porquê de uma arquitetura moderna](#o-porquê-de-uma-arquitetura-moderna)
- [Uma visão da arquitetura moderna na AWS](#uma-visão-da-arquitetura-moderna-na-aws)
- [Princípios](#princípios)
- [Arquetura Moderna na Prática](#arquetura-moderna-na-prática)
  - [Data Lakes Escaláveis - um caminho comum](#data-lakes-escaláveis---um-caminho-comum)
    - [Amazon S3 - armazenamento](#amazon-s3---armazenamento)
    - [AWS Glue Catalog - integração](#aws-glue-catalog---integração)
    - [AWS Lake Formation - acesso](#aws-lake-formation---acesso)
    - [Querying the Data Lake - acesso](#querying-the-data-lake---acesso)
    - [Movimentação de dados](#movimentação-de-dados)
      - [AWS DMS Database Migration Service](#aws-dms-database-migration-service)
      - [AWS Amazon Kinesis](#aws-amazon-kinesis)
      - [AWS AppFlow Integration for Third-Party Apps (No code)](#aws-appflow-integration-for-third-party-apps-no-code)
    - [AWS Simple Schema](#aws-simple-schema)
    - [Redshift](#redshift)
    - [AWS ML Stack](#aws-ml-stack)
    - [AWS Analytics](#aws-analytics)

# Contato do palestrante: AWS Modern Data Architectures

- Edir Santana (AWS): https://www.linkedin.com/in/edir-cabral-santana-4642952a/

[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# O porquê de uma arquitetura moderna

![1](/AWS/images/1.png)

[Uma documentação interessante sobre as diferenças entre os modelos de desenvolvimento aqui.](https://aws.amazon.com/pt/compare/the-difference-between-a-data-warehouse-data-lake-and-data-mart/)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Uma visão da arquitetura moderna na AWS
![3](/AWS/images/3.png)

[Uma documentação na AWS sobre a arquitetura moderna aqui.](https://aws.amazon.com/pt/big-data/datalakes-and-analytics/modern-data-architecture/)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Princípios

![4](/AWS/images/4.png)

- **Data Lake Escalável**: repositório centralizado que armazena todas as estruturas de dados
- **Serviços de propósito específico**: modelo democrático que contempla diferentes perfis e acessos ao dado
- **Movimentação de dados**: fluxos de dados constantes que entram e saem do Data Lake
- **Performance e custo-benefício**: serviços desacoplados da infraestrutura, pagamento conforme o consumo e alta performance em serviços de propósito específico 
- **Governança unificada**: modelo de governança abrangente que consiga controlar o ambiente e mantê-lo sustentável

[Uma documentação na AWS sobre os pilares aqui.](https://wa.aws.amazon.com/wat.pillars.wa-pillars.pt_BR.html)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

# Arquetura Moderna na Prática

![5](/AWS/images/5.png)

- Nomenclaturas importantes na plataforma AWS:
  - **Camada de entrada**: dados brutos
  - **Camada de consolidação**: dados transformados
  - **Camada de disponibilização**: dados prontos para consumo


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

## Data Lakes Escaláveis - um caminho comum

![6](/AWS/images/6.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Amazon S3 - armazenamento

![7](/AWS/images/7.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### AWS Glue Catalog - integração

![23](/AWS/images/23.png)

![8](/AWS/images/8.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### AWS Lake Formation - acesso

- [Lake Formation Workshop]()

![9](/AWS/images/9.png)

- Nomenclaturas importantes na plataforma AWS:
  - **Principal**: quem usa, exemplos de principals abaixo

![10](/AWS/images/10.png)

- Permissões efetivas são aquelas que combinam métodos em databases, tabelas, colunas ou filtros e as tags

![11](/AWS/images/11.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Querying the Data Lake - acesso

![12](/AWS/images/12.png)

- Acessa Delta, Iceberg e Hudi
- Custo no Athena: organizar o dado para obter a melhor relação
  - Tipo parquet são colunares: consulta é mais barata no Athena
  - Se tiver filtros na restrição de acesso: criar partição
  - É possível fazer transformações dentro do Athena


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Movimentação de dados

![13](/AWS/images/13.png)

- **Inside Out**: dados gerados de dentro do Data Lake para fora do ambiente
- **Outside In**: dado de fora do ambiente para dentro do Data Lake, como dos logs para o centro do Data Lake
- **Around the perimeter**: um exemplo é aquelas geradas por um modelo de Machine Learning que vai abastecer o perímetro ao redor do Data Lake

![14](/AWS/images/14.png)

- Exemplos de **padrões para movimentação** de dados

![14](/AWS/images/15.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

#### AWS DMS Database Migration Service

![16](/AWS/images/16.png)

- Replica
- Distribui (Fan Out)

![17](/AWS/images/17.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

#### AWS Amazon Kinesis

- Decisões importantes a considerar

![24](/AWS/images/24.png)

- Permite MongoDb, DMS não.

![18](/AWS/images/18.png)

- Senders e Consumers

![19](/AWS/images/19.png)

- Diferenças entre Kinesis e MSK

![22](/AWS/images/22.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

#### AWS AppFlow Integration for Third-Party Apps (No code)

![20](/AWS/images/20.png)

![21](/AWS/images/21.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### AWS Simple Schema

![25](/AWS/images/25.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### Redshift

![26](/AWS/images/26.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### AWS ML Stack

![27](/AWS/images/27.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)

### AWS Analytics

![28](/AWS/images/29.png)


[Get back to the main repo](/README.md)

[Get back to this contents](#contents)