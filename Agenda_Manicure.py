def agendar_servicos(clientes):
    # Ordenar os clientes pelo horário de término em ordem crescente
    clientes.sort(key=lambda x: x[1])

    agenda = []
    horario_disponivel = 0

    for cliente in clientes:
        inicio = cliente[0]
        fim = cliente[1]

        if inicio >= horario_disponivel:
            # Agendar o cliente
            agenda.append(cliente)
            horario_disponivel = fim

    return agenda


# Exemplo de utilização
clientes = []
num_clientes = int(input("Digite o número de clientes: "))

for i in range(num_clientes):
    nome = input(f"Digite o nome do cliente {i+1}: ")
    inicio = int(input(f"Digite o horário de início do serviço para o cliente {nome} (em horas): "))
    fim = int(input(f"Digite o horário de término do serviço para o cliente {nome} (em horas): "))

    clientes.append((inicio, fim, nome))

agenda = agendar_servicos(clientes)

print("Agendamento Final:")
for cliente in agenda:
    print(f"Nome: {cliente[2]}, Início: {cliente[0]}h, Término: {cliente[1]}h")5