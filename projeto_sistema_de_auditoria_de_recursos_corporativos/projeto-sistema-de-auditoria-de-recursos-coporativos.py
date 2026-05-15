import time

empresa_data = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 50000,
                "Seguranca": 30000
            },
            "Desenvolvimento": {
                "Frontend": 20000,
                "Backend": 25000,
                "DevOps": 15000
            }
        },
        "RH": {
            "Recrutamento": 10000,
            "Treinamento": 12000
        },
        "Financeiro": 40000
    },
    "Filial": {
        "Comercial": {
            "Vendas": 15000,
            "Parcerias": 8000
        },
        "Suporte": {
            "HelpDesk": 7000
        }
    }
}

def auditor(funcao):
  def executar(*valores, **configuracao):
    print("--- INICIO DA AUDITORIA ---")
    print(f"Argumentos posicionais: {valores}")
    print(f"Argumentos nomeados: {configuracao}")

    inicio = time.perf_counter()

    resultado = funcao(*valores, **configuracao)

    fim = time.perf_counter()

    print(f"Tempo total de execução: {fim - inicio:.8f} segundos")
    print("--- FIM DA AUDITORIA---")

    print("Resultado final:", resultado)

    return resultado
  return executar


@auditor
def calcular_orcamento(dados_empresa, *departamentos_ignorados, **financeiro):
  taxa = financeiro.get("taxa_cambio", 1)
  ignorar = set(departamentos_ignorados)

  def calcular(parte):
      soma = 0
      for chave, valor in parte.items():
          if chave in ignorar:
              continue
          if isinstance(valor, dict):
              soma = soma + calcular(valor)
          else:
              soma = soma + valor
      return soma

  total = calcular(dados_empresa)

  moeda = financeiro.get("moeda_destino")
  if moeda:
      print("Moeda destino:", financeiro["moeda_destino"])

  total = total * taxa

  return total


resultado = calcular_orcamento(
    empresa_data,
    "Filial",
    taxa_cambio=5,
    moeda_destino="BRL"
)
