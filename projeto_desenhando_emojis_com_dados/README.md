# 🛡️ Algoritmo de Auditoria e Segurança de Vendas

## 📝 Descrição do Projeto
Este projeto consiste num script de auditoria automatizada desenvolvido em Python para monitorizar transações comerciais e identificar comportamentos anómalos. O sistema atua como uma camada de segurança de dados, processando lotes de vendas para detetar discrepâncias estatísticas e garantir que os limites operacionais sejam respeitados.

[cite_start]O algoritmo foca na deteção de **outliers** (valores fora do padrão) e na gestão dinâmica de limites de segurança, oferecendo um protocolo de resposta rápida para transações suspeitas[cite: 5].

## ⚙️ Funcionalidades Principais
* [cite_start]**Análise Estatística de Desvio:** O sistema calcula médias parciais e identifica se qualquer venda individual é 5 vezes superior à média das restantes, disparando um alerta de **REVISÃO MANUAL**[cite: 5].
* [cite_start]**Gestão Dinâmica de Limites:** Monitoriza se as vendas ultrapassam o `LIMITE_SEGURANCA` global (padrão: R$ 10.000,00)[cite: 5].
* [cite_start]**Protocolo de Quarentena:** Se a média total do lote de vendas exceder o limite de segurança, o sistema entra automaticamente em estado de **SISTEMA EM QUARENTENA**[cite: 5].
* [cite_start]**Interface de Auditor:** Permite a atualização em tempo real do limite de segurança caso uma venda alta seja validada como legítima pelo utilizador[cite: 5].

## 🚀 Estrutura de Lógica
O script utiliza conceitos avançados de lógica de programação:
* [cite_start]**Escopo Global:** Uso de `global LIMITE_SEGURANCA` para permitir que funções modifiquem parâmetros de configuração do sistema[cite: 5].
* [cite_start]**Tratamento de Exceções:** Implementação de blocos `try/except` para validar a entrada de novos limites e prevenir falhas por dados inválidos[cite: 5].
* [cite_start]**Validação de Tipagem:** Monitorização rigorosa dos tipos de dados (`float`, `type`) para garantir precisão nos cálculos financeiros[cite: 5].

## 📊 Regras de Negócio
| Condição | Ação do Sistema |
| :--- | :--- |
| Venda ≥ 5x a média das outras | Alerta de Revisão Manual |
| Venda > Limite de Segurança | Solicitação de validação e opção de novo limite |
| Média do Lote > Limite | Ativação de Quarentena |

## 🔧 Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Descarregue o ficheiro `projeto_algoritmo_de_auditoria_de_dados.py`.
3. Execute no terminal:
   ```bash
   python projeto_algoritmo_de_auditoria_de_dados.py
