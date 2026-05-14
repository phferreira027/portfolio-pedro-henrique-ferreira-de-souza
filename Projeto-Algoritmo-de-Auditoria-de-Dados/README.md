# 📊 Sistema de Análise de Segurança de Vendas

## 📝 Descrição do Projeto
Este projeto consiste em um script de automação para análise de dados transacionais e detecção de anomalias em vendas. O objetivo principal é monitorar o desempenho financeiro e garantir a integridade dos dados através de uma política de segurança rigorosa, prevenindo erros de entrada ou discrepâncias significativas que possam comprometer o fluxo de caixa.

[cite_start]Desenvolvido para fins de **Monitoramento e Segurança Operacional**, o sistema processa entradas manuais de vendas, calcula métricas estatísticas (média e mediana) e aplica gatilhos de alerta baseados em um limite de segurança pré-estabelecido de R$ 10.000,00[cite: 1, 3]. [cite_start]O diferencial desta versão é o uso da mediana para identificar vendas que fogem drasticamente do padrão, ignorando distorções causadas por valores extremos isolados[cite: 17, 30].


## 🚀 Tecnologias Utilizadas
* [cite_start]**Linguagem:** Python 3.x [cite: 2]
* [cite_start]**Paradigma:** Programação Procedural com tratamento de exceções [cite: 9, 13]
* [cite_start]**Recursos Core:** Manipulação de listas, funções globais e iterações [cite: 3, 4, 6]

## 📊 Principais Funcionalidades
O sistema implementa uma lógica de verificação em duas camadas para garantir a segurança dos dados:

* [cite_start]**Cálculo de Métricas:** Gera automaticamente a média simples e a mediana das vendas inseridas[cite: 16, 20].
* [cite_start]**Quarentena de Sistema:** Se a média das vendas ultrapassar o **LIMITE_SEGURANCA** (R$ 10.000,00), o sistema emite um alerta de "Quarentena"[cite: 25, 26].
* **Detecção de Discrepância:** Identifica e sinaliza qualquer venda individual que seja igual ou superior a 3 vezes o valor da mediana[cite: 30, 31].
* [cite_start]**Validação de Dados:** Utiliza blocos `try-except` para garantir que apenas valores numéricos (float) sejam aceitos durante a entrada de dados[cite: 9, 13, 14].

## 🔧 Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou copie o código fonte.
3. Execute o script diretamente no terminal:
   ```bash
   python nome_do_arquivo.py