import tkinter as tk
from tkinter import messagebox

def agendar_servicos():
    clientes = []
    
    try:
        num_clientes = int(entry_num_clientes.get())
        
        for i in range(num_clientes):
            nome = entry_nomes[i].get()
            inicio = int(entry_horarios_inicio[i].get())
            fim = int(entry_horarios_fim[i].get())
            clientes.append((inicio, fim, nome))
        
        # Ordenar os clientes pelo horário de término em ordem crescente
        agenda = sorted(clientes, key=lambda x: x[1])
        
        # Agendamento dos serviços usando o algoritmo de Interval Scheduling
        horario_disponivel = 0
        agendados = []
        
        for cliente in agenda:
            inicio = cliente[0]
            fim = cliente[1]
            
            if inicio >= horario_disponivel:
                # Agendar o cliente
                agendados.append(cliente)
                horario_disponivel = fim
        
        # Exibir o agendamento final
        mensagem = ""
        for cliente in agendados:
            mensagem += f"Nome: {cliente[2]}, Início: {cliente[0]}h, Término: {cliente[1]}h\n"
        
        messagebox.showinfo("Agendamento Final", mensagem)
        
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para os horários.")

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Agendamento de Manicure")

# Frame para os campos de entrada
frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=20, pady=20)

# Campo de entrada para o número de clientes
label_num_clientes = tk.Label(frame_inputs, text="Número de clientes:")
label_num_clientes.grid(row=0, column=0, sticky="e")

entry_num_clientes = tk.Entry(frame_inputs)
entry_num_clientes.grid(row=0, column=1, padx=5, pady=5)

# Campos de entrada para nome, horário de início e horário de término de cada cliente
entry_nomes = []
entry_horarios_inicio = []
entry_horarios_fim = []

def criar_campos_entrada():
    num_clientes = int(entry_num_clientes.get())

    for i in range(num_clientes):
        label_nome = tk.Label(frame_inputs, text=f"Nome do cliente {i+1}:")
        label_nome.grid(row=i+1, column=0, sticky="e")

        entry_nome = tk.Entry(frame_inputs)
        entry_nome.grid(row=i+1, column=1, padx=5, pady=5)
        entry_nomes.append(entry_nome)

        label_inicio = tk.Label(frame_inputs, text=f"Início do serviço (cliente {i+1}):")
        label_inicio.grid(row=i+1, column=2, sticky="e")

        entry_inicio = tk.Entry(frame_inputs)
        entry_inicio.grid(row=i+1, column=3, padx=5, pady=5)
        entry_horarios_inicio.append(entry_inicio)

        label_fim = tk.Label(frame_inputs, text=f"Término do serviço (cliente {i+1}):")
        label_fim.grid(row=i+1, column=4, sticky="e")

        entry_fim = tk.Entry(frame_inputs)
        entry_fim.grid(row=i+1, column=5, padx=5, pady=5)
        entry_horarios_fim.append(entry_fim)

# Botão para criar os campos de entrada
btn_criar_campos = tk.Button(frame_inputs, text="Criar campos", command=criar_campos_entrada)
btn_criar_campos.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

# Botão para agendar os serviços
btn_agendar = tk.Button(root, text="Agendar", command=agendar_servicos)
btn_agendar.pack(pady=10)

# Execução da janela principal
root.mainloop()
