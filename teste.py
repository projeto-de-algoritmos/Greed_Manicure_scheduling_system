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
            clientes.append(( nome, inicio, fim))
        
        agenda = sorted(clientes, key=lambda x: x[1])
        
        messagebox.showinfo("Agendamento Final", str(agenda))
        
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para os horários.")



customtkinter.set_appearance_mode("Light")  # Modes: system (default), light, dark

root = customtkinter.CTk()
root.geometry("1000x700")
root.title("Sistema de Agendamento de Manicure")

# Frame para os campos de entrada
frame_inputs = customtkinter.CTkFrame(root)
frame_inputs.pack(padx=20, pady=20, expand=True, fill="both", anchor="center")


# # Campo de entrada para o número de clientes
label_num_clientes = customtkinter.CTkLabel(frame_inputs, text="Número de clientes:")
label_num_clientes.grid(row=0, column=0, sticky="e", padx=10, pady=10)

entry_num_clientes = customtkinter.CTkEntry(frame_inputs)
entry_num_clientes.grid(row=0, column=1, padx=10, pady=10)

# # Campos de entrada para nome, horário de início e horário de término de cada cliente
entry_nomes = []
entry_horarios_inicio = []
entry_horarios_fim = []

def criar_campos_entrada():
    num_clientes = int(entry_num_clientes.get())

    for i in range(num_clientes):
        label_nome = customtkinter.CTkLabel(frame_inputs, text=f"Nome do cliente {i+1}:")
        label_nome.grid(row=i+1, column=0, sticky="e")

        entry_nome = customtkinter.CTkEntry(frame_inputs)
        entry_nome.grid(row=i+1, column=1, padx=5, pady=5)
        entry_nomes.append(entry_nome)

        label_inicio = customtkinter.CTkLabel(frame_inputs, text=f"Início do serviço (cliente {i+1}):")
        label_inicio.grid(row=i+1, column=2, sticky="e")

        entry_inicio = customtkinter.CTkEntry(frame_inputs)
        entry_inicio.grid(row=i+1, column=3, padx=5, pady=5)
        entry_horarios_inicio.append(entry_inicio)

        label_fim = customtkinter.CTkLabel(frame_inputs, text=f"Término do serviço (cliente {i+1}):")
        label_fim.grid(row=i+1, column=4, sticky="e")

        entry_fim = customtkinter.CTkEntry(frame_inputs)
        entry_fim.grid(row=i+1, column=5, padx=5, pady=5)
        entry_horarios_fim.append(entry_fim)

# Botão para criar os campos de entrada
btn_criar_campos = customtkinter.CTkButton(frame_inputs, text="CRIAR CAMPOS", command=criar_campos_entrada, fg_color="#ffc1cc", hover_color="#fdf3ec", text_color="#494444", font=("Gilroy", 14))
btn_criar_campos.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

# Botão para agendar os serviços
btn_agendar = customtkinter.CTkButton(root, text="AGENDAR", command=agendar_servicos, fg_color="#ffc1cc", hover_color="#fdf3ec", text_color="#494444", font=("Gilroy", 14))
btn_agendar.pack(pady=10)

# Execução da janela principal
root.mainloop()