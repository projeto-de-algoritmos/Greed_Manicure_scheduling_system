import tkinter as tk
from tkinter import messagebox
import customtkinter


def agendar_servicos():
    clientes = []
    
    try:
        num_clientes = int(entry_num_clientes.get())
        
        for i in range(num_clientes):
            nome = entry_nomes[i].get()
            inicio = int(entry_horarios_inicio[i].get())
            fim = int(entry_horarios_fim[i].get())
            clientes.append((inicio, fim, nome))
        
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
        
        janela_de_agendados = tk.Toplevel(root)
        janela_de_agendados.title("Agendamento Final")
        janela_de_agendados.geometry("400x500")
        janela_de_agendados.configure(bg="white")

        # Frame para exibir os dados
        frame_agenda = tk.Frame(janela_de_agendados, bg="white")
        frame_agenda.pack(padx=20, pady=20)

        # Rótulo de título
        label_titulo = tk.Label(frame_agenda, text="Agendamento Final", bg="white", font=("Helvetica", 16, "bold"))
        label_titulo.pack(pady=10)

        # Exibir os dados dos clientes agendados
        for i, cliente in enumerate(agendados):
            nome = cliente[2]
            inicio = cliente[0]
            fim = cliente[1]

            subtitulo = tk.Label(frame_agenda, text=f"Cliente {i+1}", font=("Helvetica", 14, "bold"), bg="#ffc1cc", padx=50, pady=13)
            subtitulo.pack(pady=5)

            tabela = tk.Label(frame_agenda, text=f"Nome: {nome}\nInício: {inicio} horas\nTérmino: {fim} horas", font=("Helvetica", 12), bg="white")
            tabela.pack(pady=5)
        
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para os horários.")


root = customtkinter.CTk()
root.geometry("1000x700")
root.title("Sistema de Agendamento de Manicure")
root.configure(fg_color="white")

# Frame para os campos de entrada
frame_inputs = customtkinter.CTkFrame(root,fg_color="white")
frame_inputs.pack(padx=20, pady=20, expand=True, fill="both", anchor="center")


# # Campo de entrada para o número de clientes
entry_num_clientes = customtkinter.CTkEntry(frame_inputs, height=35, width=170, corner_radius=10,placeholder_text="Número de clientes")
entry_num_clientes.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# # Campos de entrada para nome, horário de início e horário de término de cada cliente
entry_nomes = []
entry_horarios_inicio = []
entry_horarios_fim = []

def criar_campos_entrada():
    num_clientes = int(entry_num_clientes.get())
    btn_agendar.pack(pady=10)

    for i in range(num_clientes):
        label_nome = customtkinter.CTkLabel(frame_inputs, font=("Helvetica", 13), text=f"Nome do cliente {i+1}:")
        label_nome.grid(row=i+3, column=0, sticky="e")

        entry_nome = customtkinter.CTkEntry(frame_inputs, font=("Helvetica", 13))
        entry_nome.grid(row=i+3, column=1, padx=5, pady=5)
        entry_nomes.append(entry_nome)

        label_inicio = customtkinter.CTkLabel(frame_inputs, font=("Helvetica", 13), text=f"Início do serviço (cliente {i+1}):")
        label_inicio.grid(row=i+3, column=2, sticky="e")

        entry_inicio = customtkinter.CTkEntry(frame_inputs, font=("Helvetica", 13))
        entry_inicio.grid(row=i+3, column=3, padx=5, pady=5)
        entry_horarios_inicio.append(entry_inicio)

        label_fim = customtkinter.CTkLabel(frame_inputs,font=("Helvetica", 13), text=f"Término do serviço (cliente {i+1}):")
        label_fim.grid(row=i+3, column=4, sticky="e")

        entry_fim = customtkinter.CTkEntry(frame_inputs, font=("Helvetica", 13))
        entry_fim.grid(row=i+3, column=5, padx=5, pady=5)
        entry_horarios_fim.append(entry_fim)

# Botão para criar os campos de entrada
btn_criar_campos = customtkinter.CTkButton(frame_inputs, text="CRIAR CAMPOS", command=criar_campos_entrada, fg_color="#ffc1cc", hover_color="#fdf3ec", text_color="#494444", font=("Helvetica", 14, "bold"), height=35, width=170, corner_radius=10, border_width=2, border_color="#eba9b5")
btn_criar_campos.grid(row=1, column=2, padx=5, pady=10, sticky="w")

# Botão para agendar os serviços
btn_agendar = customtkinter.CTkButton(root, text="AGENDAR", command=agendar_servicos, fg_color="#ffc1cc", hover_color="#fdf3ec", text_color="#494444", font=("Helvetica", 14, "bold"), height=35, width=170, corner_radius=10, border_width=2, border_color="#eba9b5")

# Execução da janela principal
root.mainloop()