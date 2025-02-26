# Análise de Dados de Redes

Este projeto tem como objetivo analisar dados de tráfego de rede, especificamente focando em pacotes ICMP e TCP. O código processa os dados, calcula estatísticas relevantes e gera visualizações para melhor compreensão dos fluxos de rede.

## Descrição do Código

O código é escrito em Python e utiliza várias bibliotecas populares para análise de dados e machine learning, como `pandas`, `numpy`, `matplotlib` e `seaborn`.

### Passos Principais

1. **Carregamento dos Dados**:
   - O código começa carregando os dados de um arquivo CSV chamado `dados.csv`.
   - As colunas desnecessárias (`No.` e `Info`) são removidas, e as colunas restantes são renomeadas para facilitar a compreensão.

2. **Filtragem e Ordenação**:
   - Os dados são filtrados para separar pacotes ICMP e TCP.
   - Os pacotes são ordenados por origem, destino, tamanho e tempo.

3. **Cálculo de Estatísticas**:
   - Para cada fluxo (grupo de pacotes com a mesma origem e destino), são calculadas várias estatísticas, como duração do fluxo, tempo máximo, tempo mínimo, tempo médio, tamanho total, tamanho máximo, tamanho mínimo, tamanho médio e taxa de bits.
   - Essas estatísticas são calculadas para ambos os tipos de pacotes (ICMP e TCP).

4. **Salvamento dos Resultados**:
   - As estatísticas calculadas são salvas em dois arquivos CSV: `FluxosICMP.csv` e `FluxosTCP.csv`.

5. **Visualização dos Dados**:
   - O código gera gráficos de pairplot usando a biblioteca `seaborn` para visualizar as relações entre as variáveis numéricas nos dados processados.

### Bibliotecas Utilizadas

- `pandas`: Para manipulação e análise de dados.
- `numpy`: Para operações numéricas.
- `matplotlib` e `seaborn`: Para visualização de dados.
