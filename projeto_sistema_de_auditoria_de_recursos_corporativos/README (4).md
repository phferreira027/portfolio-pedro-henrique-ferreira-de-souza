# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programação Backend do curso de Análise e Desenvolvimento de Sistemas. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi construída utilizando conceitos importantes da linguagem Python, com foco em recursividade, reutilização de código e flexibilidade na passagem de parâmetros.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na execução.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes conceitos:
 
* **Funções Recursivas (Recursion):** Utilizadas para percorrer toda a estrutura de dados hierárquica, independentemente da profundidade.
* **Decorators:** Implementação do `@auditor` para adicionar funcionalidades como log e medição de tempo sem alterar a lógica principal do cálculo.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados para permitir maior flexibilidade na função, possibilitando ignorar departamentos dinamicamente e aplicar taxa de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/AlexandreNogueiraDev/portfolio-alexandre-almeida-de-jesus-nogueira.git

2. Acesse a pasta do projeto:
   ```bash
   cd portfolio-alexandre-almeida-de-jesus-nogueira/projeto_sistema_de_auditoria_de_recursos_coporativos
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
* A lógica principal do projeto foi baseada em recursão, já que a estrutura da empresa é representada como um dicionário aninhado (uma árvore). A função percorre cada nível verificando se o valor ainda é um dicionário ou um valor final. Caso seja um dicionário, a função chama a si mesma; caso contrário, soma o valor ao total.

  O decorator foi utilizado para separar responsabilidades. Em vez de misturar lógica de cálculo com auditoria, foi criada uma função externa (@auditor) que intercepta a execução da função principal, registra os parâmetros recebidos e mede o tempo de execução. Isso torna o código mais organizado e reutilizável.
* **Dados:** Os dados simulados da empresa foram estruturados em um dicionário hierárquico, onde cada chave representa um setor ou subsetor, e os valores podem ser outros dicionários (subníveis) ou valores numéricos (orçamento final daquele setor).
 
## 👤 Autor
 
* **Alexandre Almeida de Jesus Nogueira**
* LinkedIn: https://www.linkedin.com/in/alexandre-almeida-de-jesus-nogueira-70b077366/
* E-mail: alexandreajnbr@gmail.com
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
