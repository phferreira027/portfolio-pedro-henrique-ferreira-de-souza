# 🛒 Sistema de Caixa e Cálculo de Troco

## 📝 Descrição do Projeto
Este projeto consiste num sistema de automação para pontos de venda (PDV), focado no registo de produtos, processamento de pagamentos e cálculo otimizado de troco. O sistema utiliza uma lógica de decomposição de valores para determinar a menor quantidade de notas necessárias para o troco.

Desenvolvido como parte da disciplina de **Lógica de Programação**, o projeto inclui o mapeamento completo do fluxo de dados através de fluxogramas e a implementação da lógica em pseudocódigo.

## ⚙️ Funcionalidades Principais
* [cite_start]**Registo de Produtos:** Leitura contínua de produtos e acumulação do valor total da compra ($T = T + PROD$)[cite: 86].
* [cite_start]**Validação de Pagamento:** Verifica se o valor pago pelo cliente é suficiente para cobrir o total da compra[cite: 102, 109].
* [cite_start]**Cálculo de Troco:** Determina o valor exato a ser devolvido ($TROCO = PAG - T$)[cite: 118, 120].
* [cite_start]**Decomposição em Notas:** Algoritmo que calcula a distribuição do troco entre as notas disponíveis (ex: 100, 50, 20, 10, 5, 2) para minimizar o número de notas entregues[cite: 124, 184].

## 🚀 Estrutura do Algoritmo
O sistema está dividido em funções modulares para facilitar a manutenção:
* [cite_start]**`FUNCAO CAIXA`**: Gere a entrada de dados dos produtos e encerra a conta ao comando do utilizador[cite: 90, 97].
* [cite_start]**`FUNCAO CALC_TROCO`**: Realiza a operação aritmética básica de subtração entre pagamento e total[cite: 118].
* **`FUNCAO DECA_NOTAS`**: Executa a lógica de divisão inteira e resto para separar o troco por cédulas[cite: 177, 185].
* **`FUNCAO MOSTRAR`**: Apresenta o resumo final ao cliente, incluindo o total, valor pago e o detalhe das notas do troco[cite: 140, 146].

## 📊 Regras de Negócio
1. **Fluxo de Continuidade:** O caixa continua a ler produtos até que o botão "Continuar" (ou finalizar) seja acionado[cite: 86].
2. **Erro de Pagamento:** Se o valor pago for menor que o total, o sistema emite um alerta: "O valor deve ser maior ou igual ao total"[cite: 112, 169].
3. **Prioridade de Notas:** O troco começa sempre pelas notas de maior valor disponível no array `[100, 50, 20, 10, 5, 2]`.

## 🔧 Como Executar
O projeto está documentado em formato de algoritmos:
1. Consulte os **Fluxogramas** (Páginas 1, 4 e 5) para entender o comportamento visual do sistema[cite: 86, 124, 135].
2. O **Pseudocódigo** completo pode ser encontrado a partir da página 8, pronto para ser transcrito para linguagens como Portugal ou adaptado para Python/C[cite: 152, 156].

---
[Voltar ao início](https://github.com/AlexandreNogueiraDev/AlexandreNogueiraDev)
