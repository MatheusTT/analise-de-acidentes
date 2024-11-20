# Análise de Acidentes em Chicago

Este projeto tem como objetivo realizar a análise de dados sobre acidentes de trânsito que ocorreram em Chicago. Utilizando Python, exploramos e visualizamos os dados para identificar padrões, causas principais e outros insights relevantes.

## Pré-requisitos

Para executar o projeto, é necessário ter o Python instalado em sua máquina. Além disso, as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

### Configuração do Ambiente Virtual

Recomendamos o uso de um ambiente virtual (`venv`) para garantir que as dependências do projeto não interfiram em outros projetos na sua máquina.

Siga os passos abaixo para configurar e rodar o projeto:

1. Clone o repositório:
   ```bash
   git clone https://github.com/MatheusTT/analise-de-acidentes.git
   cd analise-de-acidentes
   ```

2. Crie e ative um ambiente virtual:
   - **Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

Após configurar o ambiente e instalar as dependências, você pode rodar os scripts disponíveis para análise. Certifique-se de consultar a documentação nos comentários dos scripts para entender como utilizá-los.

```bash
python nome_do_script.py
```

## Estrutura do Repositório

- `requirements.txt`: Lista das bibliotecas necessárias para rodar o projeto.
- **Pasta `data`**:
  - Deve conter o arquivo de input (um arquivo CSV baixado [deste link](https://catalog.data.gov/dataset/traffic-crashes-crashes)).
  - Contém também os arquivos XLSX que foram processados a partir do arquivo de input.
- **Script `reduce_data.py`**:
  - Reduz o arquivo de input em dois arquivos separados: `antigo.xlsx` e `recente.xlsx`.
- **Script `graph_generator.py`**:
  - Gera gráficos de barras e gráficos de pizza com base nas configurações definidas no arquivo `graph_settings.json`.
- **JSON `graph_settings.json`**:
  - Arquivo de configuração contendo:
    - Coluna utilizada para os dados do gráfico.
    - Título do gráfico
    - Informações adicionais como `xlabel`, `ylabel` e a cor das barras.
- **Script `hotspot_analysis.py`**:
  - Gera dois mapas de hotspots com base nos dados de acidentes:
    - Um mapa tradicional.
    - Um heatmap mostrando a concentração de acidentes nas coordenadas das batidas em Chicago.

## Contribuindo

Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias ou corrigir problemas.

---

Projeto desenvolvido como parte das atividades do curso de Engenharia de Software no UniSenai.
