# Projeto de Análise de Reviews da Amazon

Este projeto foi desenvolvido no âmbito da unidade curricular de **Programação**.  
O objetivo é processar, analisar e visualizar dados de avaliações de produtos (**Amazon Fine Food Reviews**) **sem o uso da biblioteca Pandas**.

---

##  Grupo de Trabalho

- **Membro A :** Gabriel Salazar— Análise de Texto, Visualização e Integração  
- **Membro B:** Daniel Colavito— Estatísticas de Usuários  
- **Membro C:** Guilherme Cardoso — Análise Temporal e Estatísticas Gerais  

---

##  Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter instalado:

```bash
pip install matplotlib
```

### 2. Execução

Na pasta raiz do projeto, execute:

```bash
python main.py
```

 **Nota:**  
O projeto utiliza por defeito o ficheiro `data/Reviews_small.csv`.  
O código está preparado para aceitar datasets maiores como `data/Reviews.csv`.

---

##  Estrutura do Projeto

```
src/loader.py            → Carregamento de dados CSV
src/utils.py             → Sistema de logging (ficheiro e terminal)
src/analysis_general.py  → Estatísticas gerais e análise temporal (anos/meses)
src/analysis_users.py    → Identificação dos usuários mais ativos e úteis
src/analysis_products.py → Melhores produtos e pesquisa por palavra-chave
src/text_analysis.py     → Análise de frequência de palavras (stopwords)
src/visualization.py     → Geração de gráficos (Barras e Histograma)
```

---

##  Declaração de Uso de IA Generativa

De acordo com as normas do projeto, declaramos o uso de ferramentas de IA (Gemini/ChatGPT) para:

- **Estruturação do código:** apoio na organização dos módulos e conformidade PEP 8  
- **Depuração (debugging):** identificação de erros de sintaxe e lógica  
- **Otimização:** sugestões para loops mais eficientes e melhor manipulação de listas  

Todo o código foi **revisto, testado e compreendido** pelos membros do grupo.

---
