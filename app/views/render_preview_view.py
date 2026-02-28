from tkinter import Scrollbar, ttk, messagebox
import tkinter as tk
from repositories.repository import RepositoryFile


class RenderPreview:
    """
    Define um espaço para renderizar a imagem em um painel redimensionável
    """
    def __init__(self) -> None:
        self.bd = RepositoryFile()
        self.lb_image = None
        self.preview_active = False
    
    
    def frame_preview(self, root, service) -> None:
        self.service_decompress = service
        
        self.fr_main = tk.Frame(root, width=100, height=100, background='black')
        self.fr_main.pack(side='left', fill='both', expand='yes')
    

        self.painel_redimensionavel = tk.PanedWindow(self.fr_main, width=100, height=100, orient='horizontal')
        self.painel_redimensionavel.pack(side='left', fill='both', expand='yes')


        self.fr_lista_arquivos = tk.Frame(self.painel_redimensionavel, width=100, height=100, background='gray25')
        self.fr_lista_arquivos.pack(side='left', fill='both', expand='yes')

        
        self.fr_action_visualizer = tk.Frame(self.fr_lista_arquivos, width= 100, height= 100, background='gray25')
        self.fr_action_visualizer.pack(side='top', fill='x')
        
        self.btn_visualizer = tk.Button(self.fr_action_visualizer, text='preview pane', font=('Courier', 10, 'bold'), command= self.action_visualizer)
        self.btn_visualizer.pack(side='right', fill='x', padx=10, pady=10)
        

        self.en_id = tk.Entry(self.fr_action_visualizer, bd=0, background='gray25', foreground='gray25')
        self.en_id.place(x=0, y=0)

        # Treeview - Titles
        self.see_list_of_files = ttk.Treeview(self.fr_lista_arquivos, height=15, column=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.see_list_of_files.heading("#0", text='')
        self.see_list_of_files.heading("#1", text='id')
        self.see_list_of_files.heading("#2", text='File')
        self.see_list_of_files.heading("#3", text='Description')
        self.see_list_of_files.heading("#4", text='Date modify')
        self.see_list_of_files.heading("#5", text='Extension')
        # Treeview - Columns
        self.see_list_of_files.column('#0', width=0, stretch=tk.NO)
        self.see_list_of_files.column('#1', width=5, anchor="center")
        self.see_list_of_files.column('#2', width=100, anchor="center")
        self.see_list_of_files.column('#3', width=150, anchor="center")
        self.see_list_of_files.column('#4', width=100, anchor="center")
        self.see_list_of_files.column('#5', width=30, anchor="center")
        self.see_list_of_files.pack(side='left', fill='both', expand='yes')

        scroll = Scrollbar(self.fr_lista_arquivos, orient="vertical")
        self.see_list_of_files.configure(yscrollcommand=scroll.set)
        scroll.config(command=self.see_list_of_files.yview)
        scroll.pack(side='left', fill='both')

        self.see_list_of_files.bind('<<TreeviewSelect>>', self.action_select_file)
        
        
        self.action_update_list()

        self.painel_redimensionavel.add(self.fr_lista_arquivos)


    def action_visualizer(self):
        if not self.preview_active:
            self.fr_image = tk.Frame(self.painel_redimensionavel, width=100, height=100, border=0)
            self.fr_image.pack(side='left', fill='both', expand='yes')

            self.fr_action_back = tk.Frame(self.fr_image, width= 100, height= 100, background='gray25')
            self.fr_action_back.pack(side='top', fill='x')
            
            self.btn_back = tk.Button(self.fr_action_back, text='close view', font=('Courier', 10, 'bold'), command= self.action_back)
            self.btn_back.pack(side='right', fill='x', padx=10, pady=10)


            self.lb_image = tk.Label(self.fr_image, text='Select a file to view.', background='gray30', foreground='white', font=('Courier', 12))
            self.lb_image.pack(fill='both', expand='yes')
            
            
            
            self.painel_redimensionavel.add(self.fr_image, minsize=220)

            self.btn_visualizer.configure(state='disabled')
            self.preview_active = True


    def action_back(self):
        if self.preview_active:
            self.painel_redimensionavel.remove(self.fr_image)
            self.btn_visualizer.configure(state='normal')
            self.preview_active = False
     
        
    def action_select_file(self, event):
        try:
            self.en_id.delete(0, tk.END)
            self.see_list_of_files.selection()

            for n in self.see_list_of_files.selection():
                columns= self.see_list_of_files.item(n, "values")
                self.en_id.insert(tk.END, columns[0])

            data= self.bd.read_unique(self.en_id.get())


            img= self.service_decompress.decompress_file(data)

            if self.lb_image is None:
                return
            else:
                self.lb_image.configure(text='', image=img)
            
            
            
        except Exception as err:
            print(f"Erro selecting file: ", err)

    def action_update_list(self):
        try:
            files = self.bd.read_all()
            self.see_list_of_files.delete(*self.see_list_of_files.get_children())
            
            for i in files:
                self.see_list_of_files.insert("", tk.END, values=i)
        
        except Exception as ex:
            print(f"Erro update list of file: ", ex)
