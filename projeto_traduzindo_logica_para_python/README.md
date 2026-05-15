# 🐍 Coleção de Algoritmos: Traduzindo Lógica para Python

## 📝 Descrição do Projeto
Este repositório contém uma série de scripts desenvolvidos para exercitar a transição entre lógica de programação e a sintaxe da linguagem Python. Os algoritmos abordam problemas comuns do quotidiano, como gestão de vendas, análise climática, controlo académico e simulações financeiras.

O projeto foi estruturado de forma modular, onde cada função resolve um problema específico utilizando estruturas de repetição (`for`, `range`), condicionais compostas (`if`, `elif`, `else`) e manipulação de tipos de dados.

## ⚙️ Funcionalidades e Módulos

### 🛍️ 1. Processamento de Vendas (`processar_vendas`)
Sistema de checkout que calcula o total de uma compra com base em múltiplos produtos e aplica descontos progressivos:
* [cite_start]**Desconto de 10%:** Para compras acima de R$ 500,00. [cite: 2]
* [cite_start]**Desconto de 5%:** Para compras acima de R$ 200,00. [cite: 2]
* [cite_start]**Validação:** Identifica erros em preços ou quantidades negativas ou nulas. [cite: 2]

### 🌡️ 2. Análise de Clima (`analisar_clima`)
Monitoriza as temperaturas ao longo de uma semana (7 dias) e gera um relatório:
* [cite_start]**Média Semanal:** Calcula a média térmica do período. [cite: 2]
* [cite_start]**Contagem de Calor:** Identifica quantos dias registaram temperaturas acima de 35°C. [cite: 2]
* [cite_start]**Alertas Extremos:** Emite um aviso de segurança se a temperatura ultrapassar 45°C ou descer abaixo de -5°C. [cite: 2]

### 🎓 3. Sistema de Notas Escolar (`sistema_notas_turma`)
Gere o desempenho de uma turma de alunos:
* [cite_start]**Aprovação:** Média ≥ 7.0. [cite: 2]
* [cite_start]**Recuperação:** Média entre 5.0 e 6.9. [cite: 2]
* [cite_start]**Reprovação:** Média inferior a 5.0. [cite: 2]

### 💰 4. Simulador de Poupança e Investimento (`simulador_poupanca`)
Calcula a evolução de um capital com juros compostos e aportes mensais:
* [cite_start]**Metas de Investimento:** Notifica o utilizador assim que o saldo atinge a meta de R$ 10.000,00. [cite: 2]
* [cite_start]**Projeção Mensal:** Exibe o saldo atualizado mês a mês após juros e depósitos. [cite: 2]

## 🚀 Tecnologias Utilizadas
* [cite_start]**Linguagem:** Python 3.x [cite: 2]
* [cite_start]**Recursos de Lógica:** * Laços de repetição determinados (`for`). [cite: 2]
    * [cite_start]Operadores aritméticos e de comparação. [cite: 2]
    * [cite_start]Formatação de strings para relatórios financeiros (`f-strings`). [cite: 2]

## 🔧 Como Executar
1. Instale o Python 3 na sua máquina.
2. Descarregue o ficheiro `traduzindo-logica-para-python.py`.
3. Execute o script no seu terminal ou ambiente de desenvolvimento:
   ```bash
   python traduzindo-logica-para-python.py
