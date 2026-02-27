from tkinter import Scrollbar, ttk, NO
import tkinter as tk


class RenderPreview():
    """
    Define um espaço para renderizar a imagem em um painel redimensionável
    """
    def frame_preview(self, root) -> None:
        # CONFIGURAÇÃO DO PAINEL REDIMENSIONAVEL
        self.fr_main = tk.Frame(root, width=100, height=100, background='black')
        self.fr_main.pack(side='left', fill='both', expand='yes')
    

        self.painel_redimensionavel = tk.PanedWindow(self.fr_main, width=100, height=100, orient='horizontal')
        self.painel_redimensionavel.pack(side='left', fill='both', expand='yes')

        # AQUI VAI LISTAR OS ARQUIVOS CARREGADOS NA BASE DE DADOS
        self.fr_lista_arquivos = tk.Frame(self.painel_redimensionavel, width=100, height=100, background='gray25')
        self.fr_lista_arquivos.pack(side='left', fill='both', expand='yes')

        # ACTION VISUALIZER
        self.fr_action_visualizer = tk.Frame(self.fr_lista_arquivos, width= 100, height= 100, background='gray25')
        self.fr_action_visualizer.pack(side='top', fill='x')
        
        self.btn_visualizer = tk.Button(self.fr_action_visualizer, text='visualizer', font=('Courier', 10, 'bold'), command= self.action_visualizer)
        self.btn_visualizer.pack(side='right', fill='x', padx=10, pady=10)
        
        # self.ID_en = Entry(self.fr_container_views, bd=0)
        # self.ID_en.place(relx=0.12, rely=0.45)

        # Titles
        self.see_list_of_files = ttk.Treeview(self.fr_lista_arquivos, height=15, column=('col1', 'col2', 'col3', 'col4'))
        self.see_list_of_files.heading("#0", text='')
        self.see_list_of_files.heading("#1", text='id')
        self.see_list_of_files.heading("#2", text='Name file')
        self.see_list_of_files.heading("#3", text='Description')
        self.see_list_of_files.heading("#4", text='Modified by')
        # Columns
        self.see_list_of_files.column('#0', width=0, stretch=NO)
        self.see_list_of_files.column('#1', width=10, anchor="center")
        self.see_list_of_files.column('#2', width=70, anchor="center")
        self.see_list_of_files.column('#3', width=100, anchor="center")
        self.see_list_of_files.column('#4', width=100, anchor="center")
        self.see_list_of_files.pack(side='left', fill='both', expand='yes')

        scroll = Scrollbar(self.fr_lista_arquivos, orient="vertical")
        self.see_list_of_files.configure(yscrollcommand=scroll.set)
        scroll.config(command=self.see_list_of_files.yview)
        scroll.pack(side='left', fill='both')

        self.see_list_of_files.bind('<<TreeviewSelect>>', lambda a: print('nada'))
        
        #self.update_list_of_file()

        self.painel_redimensionavel.add(self.fr_lista_arquivos)

    def action_visualizer(self):
        # AQUI VAI MOSTAR A IMAGEM
        self.fr_image = tk.Frame(self.painel_redimensionavel, width=20, height=100, border=0)
        self.fr_image.pack(side='left', fill='both', expand='yes')

        # ACTION RETRY
        self.fr_action_back = tk.Frame(self.fr_image, width= 100, height= 100, background='gray25')
        self.fr_action_back.pack(side='top', fill='x')
        
        self.btn_back = tk.Button(self.fr_action_back, text='X', font=('Courier', 10, 'bold'), command= self.action_back)
        self.btn_back.pack(side='right', fill='x', padx=10, pady=10)


        self.lb_image = tk.Label(self.fr_image, text='Selecione um arquivo para visualizar.', background='gray30', foreground='white', font=('Courier', 8))
        self.lb_image.pack(fill='both', expand='yes')
        
        self.painel_redimensionavel.add(self.fr_image, minsize=220)

        self.btn_visualizer.configure(state='disabled')

    def action_back(self):
        self.fr_image.destroy()
        self.btn_visualizer.configure(state='normal')
