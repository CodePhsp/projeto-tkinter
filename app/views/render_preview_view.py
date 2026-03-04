from tkinter import Scrollbar, ttk, messagebox
import tkinter as tk
from repositories.repository import RepositoryFile





class RenderPreview:
    """
    View: Renderiza imagens em um painel redimensionável
    """
    def __init__(self) -> None:
        self.bd = RepositoryFile()
        self.lb_image = None
        self.preview_active = False
    
    
    def frame_preview(self, root, service_decompress) -> None:
        self.service_decompress = service_decompress
        
        self.fr_main = tk.Frame(root, width=100, height=100, background='black')
        self.fr_main.pack(side='left', fill='both', expand='yes')
    

        self.painel_redimensionavel = tk.PanedWindow(self.fr_main, width=100, height=100, orient='horizontal')
        self.painel_redimensionavel.pack(side='left', fill='both', expand='yes')


        self.fr_lista_arquivos = tk.Frame(self.painel_redimensionavel, width=100, height=100, background='gray25')
        self.fr_lista_arquivos.pack(side='left', fill='both', expand='yes')

        
        self.fr_action_visualizer = tk.Frame(self.fr_lista_arquivos, width= 100, height= 100, background='gray25')
        self.fr_action_visualizer.pack(side='top', fill='x')
        
        self.btn_visualizer = tk.Button(self.fr_action_visualizer, text='Preview pane', font=('Courier', 10, 'bold'), command= self.action_visualizer)
        self.btn_visualizer.pack(side='right', fill='x', padx=10, pady=10)

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
        self.see_list_of_files.column('#1', width=5, stretch=tk.NO)
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

    def action_visualizer(self) -> None:
        if not self.preview_active: # (true)
            self.fr_image = tk.Frame(self.painel_redimensionavel, width=100, height=100, border=0)
            self.fr_image.pack(side='left', fill='both', expand='yes')

            self.fr_action_back_list_file = tk.Frame(self.fr_image, width= 100, height= 100, background='gray25')
            self.fr_action_back_list_file.pack(side='top', fill='x')
            
            # CLOSE PANED OF PREVIEW
            self.btn_back_list_file = tk.Button(self.fr_action_back_list_file, text='Close view', font=('Courier', 10, 'bold'), command= self.action_back_list_file)
            self.btn_back_list_file.pack(side='left', fill='x', padx=10, pady=10)

            self.btn_next_file = tk.Button(self.fr_action_back_list_file, text='Next', font=('Courier', 10, 'bold'), command= self.action_next_file)
            self.btn_next_file.pack(side='right', fill='x', padx=10, pady=10)
        
            self.btn_back_file = tk.Button(self.fr_action_back_list_file, text='Back', font=('Courier', 10, 'bold'), command= self.action_back_file)
            self.btn_back_file.pack(side='right', fill='x', padx=10, pady=10)

            # RENDER IMAGE
            self.lb_image = tk.Label(self.fr_image, text='Select a file to view.', background='gray30', foreground='white', font=('Courier', 12))
            self.lb_image.pack(side='top', fill='both', expand='yes')

            self.painel_redimensionavel.add(self.fr_image, minsize=220)

            self.btn_visualizer.configure(state='disabled')
            self.preview_active = True


    def action_back_list_file(self) -> None:
        if self.preview_active:
            self.painel_redimensionavel.remove(self.fr_image)
            self.btn_visualizer.configure(state='normal')
            self.preview_active = False
     

    def action_next_file(self) -> None:
        selected = self.see_list_of_files.selection() # Coleta o item selecionado
        all_records = self.see_list_of_files.get_children() # Coleta toda a cadeia de itens da treeview

        # Evita IndexError
        if not selected:
            return

        index_selected = all_records.index(selected[0]) # Coleta o index do item selecionado
        
        next_record = index_selected + 1 # Incrementa 1 ao index selecionado
        
        if next_record < len(all_records):
            new_index = all_records[next_record] # Após o incremento, coleta o item do no index

            self.see_list_of_files.selection_remove(selected)
            self.see_list_of_files.selection_set(new_index) # Move o item selecionado (campo visual da treeview) com base no novo item
            self.see_list_of_files.focus(new_index) # Foca no novo item (campo visaul da treeview)
        
            # Seleciona o itens de cada coluna, mas neste caso é selecionado apenas o campo id da treeview
            columns= self.see_list_of_files.item(new_index, "values")
            
            
            # Verifica se o widget foi gerado, se não for nulo é realizada a consulta na base de dados
            # columns[0] é o parâmetro do id na base de dados
            # Realiza a descrompressão do arquivo e gera o widget para renderizar a imagem selecionada
            # Se o valor for nulo nenhum passo anterior é realizado
            if self.lb_image is not None:
                data= self.bd.read_unique(columns[0])
                img= self.service_decompress.decompress_file(data)
                self.lb_image.configure(text='', image=img)
            else:
                return
            
        # Trava de limite range
        if next_record >= len(all_records):
            self.btn_next_file.configure(state='disabled')

        self.btn_back_file.configure(state='normal')
            
            
    def action_back_file(self) -> None:
        selected = self.see_list_of_files.selection()
        all_records = self.see_list_of_files.get_children()

        # Evita IndexError
        if not selected:
            return

        index_selected = all_records.index(selected[0])
        
        back_record = index_selected - 1
        
        if  back_record >= 0:
            new_index = all_records[back_record]


            self.see_list_of_files.selection_set(new_index)
            self.see_list_of_files.focus(new_index)
            self.see_list_of_files.see(new_index)
            
        
            columns= self.see_list_of_files.item(new_index, 'values')
            
            
            if self.lb_image is not None:
                data= self.bd.read_unique(columns[0])
                img= self.service_decompress.decompress_file(data)
                self.lb_image.configure(text='', image=img)
            else:
                return
            
        # Trava de limite range
        if back_record <= 0:
            self.btn_back_file.configure(state='disabled')

        self.btn_next_file.configure(state='normal')
            

    def action_select_file(self, event):
        selected = self.see_list_of_files.selection()
        if not selected:
            return
            
        id_item = selected[0]
            
        column = self.see_list_of_files.item(id_item, "values")
        if not column:
            return
                
        data= self.bd.read_unique(column[0])
        if not data:
            return
            
        if not self._widget_is_alive():
            return
            
        img= self.service_decompress.decompress_file(data)
            
        self.lb_image.configure(text='', image=img)

            
            
        self.btn_back_file.configure(state='normal')
        self.btn_next_file.configure(state='normal')
        
    def _widget_is_alive(self):
        try:
            return self.lb_image.winfo_exists()
        except Exception:
            return False


    def action_update_list(self) -> None:
        try:
            files = self.bd.read_all()
            self.see_list_of_files.delete(*self.see_list_of_files.get_children())
            
            for i in files:
                self.see_list_of_files.insert("", tk.END, values=i)
        
        except Exception as ex:
            print(f"Erro update list of file: ", ex)

