import tkinter as tk




class Form:
    """
    View: Formulário
    """
    def form(self, root, service_search, service_upload, on_update_sucess) -> None:
        self.service_search = service_search
        self.service_upload = service_upload
        self.on_update_sucess = on_update_sucess


        self.fr_main = tk.Frame(root, width= 100, height= 100, background='gray25')
        self.fr_main.pack(side='left', fill='both', ipadx= 20)

        self.lb_title = tk.Label(self.fr_main, text='Upload file', background='gray25', foreground='white', font=('Courier', 20, 'bold'))
        self.lb_title.pack(side='top', fill='x')

        self.fr_form = tk.Frame(self.fr_main, width= 100, height= 100, background='gray25')
        self.fr_form.pack(side='top', fill='both', ipady=15)


        # ORIGEM---
        self.fr_origem = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_origem.pack(side='top', fill='x', expand='yes', padx= 10)

        self.lb_origem = tk.Label(self.fr_origem, text='File', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_origem.pack(side='left', fill='x')

        self.origem_path_file = tk.StringVar()
        self.en_origem = tk.Entry(self.fr_origem, textvariable=self.origem_path_file, font=('Courier', 12, 'bold'), state='disabled')
        self.en_origem.pack(side='top', fill='x')

        # BUTTON SEARCH---
        self.fr_action_search = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_action_search.pack(side='top', fill='x')
        
        self.btn_search = tk.Button(self.fr_action_search, text='search', font=('Courier', 10, 'bold'), command= self.action_search) 
        self.btn_search.pack(side='right', fill='x', padx=10)

        # DESCRIPTION FILE---
        self.fr_description_file = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_description_file.pack(side='top', fill='x', expand='yes')

        self.lb_description_file = tk.Label(self.fr_description_file, text='Descrition file', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_description_file.pack(side='left', fill='x', padx= 10)

        self.fr_children_description_file = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_children_description_file.pack(side='top', fill='x', expand='yes')
        
        self.en_description_file = tk.Text(self.fr_children_description_file, width=10, height=10, font=('Courier', 12, 'bold'))
        self.en_description_file.pack(side='top', fill='x', padx= 10)
        self.en_description_file.insert(tk.END, "Enter a description...")

        # BUTTON UPLOAD---
        self.fr_action_description_file = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_action_description_file.pack(side='top', fill='x', padx= 10)

        self.btn_upload = tk.Button(self.fr_action_description_file, text='upload file', state='disabled', font=('Courier', 10, 'bold'), command= self.action_upload) 
        self.btn_upload.pack(side='right', fill='x', pady=5)

        # INFORMATIONS ADDITIONNELLES
        self.lf_adtionais_info = tk.LabelFrame(self.fr_main, text='Informations additionalles', padx= 10, pady= 10, background='gray25', foreground='white', font=('Courier', 14, 'bold'))
        self.lf_adtionais_info.pack(side='top', fill='x', padx= 10, pady= 10)
        
        self.fr_extension_file = tk.Frame(self.lf_adtionais_info, background='gray25')
        self.fr_extension_file.pack(side='top', fill='both', padx= 10)

        self.lb_extension_file = tk.Label(self.fr_extension_file, text='Extension:', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_extension_file.pack(side='left', fill='x')
        
        self.extension_file = tk.StringVar()
        self.en_extension_file = tk.Entry(self.fr_extension_file, textvariable=self.extension_file, font=('Courier', 12, 'bold'), state='disabled')
        self.en_extension_file.pack(side='left', fill='x', expand='yes')
        
        
        self.fr_size_file = tk.Frame(self.lf_adtionais_info, background='gray25')
        self.fr_size_file.pack(side='top', fill='both', padx= 10)

        self.lb_size_file = tk.Label(self.fr_size_file, text='Size:', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_size_file.pack(side='left', fill='x', ipadx= 25)
        
        self.size_file = tk.StringVar()
        self.en_size_file = tk.Entry(self.fr_size_file, textvariable=self.size_file, font=('Courier', 12, 'bold'), state='disabled')
        self.en_size_file.pack(side='left', fill='x', expand='yes')

    def action_search(self):
        self.file = self.service_search.ask_file()
        self.origem_path_file.set(self.file.get('name_base'))
        self.extension_file.set(self.file.get('extension'))
        self.size_file.set(self.file.get('size'))

        self.btn_upload.configure(state='normal')


    def action_upload(self):
        # GET VALUES
        file_name = self.en_origem.get()
        description = self.en_description_file.get('1.0', 'end-1c')
        extension = self.en_extension_file.get()
        
        # EXCLUDE VELUES OF ENTRYS
        self.en_origem.configure(state='normal')
        self.en_origem.delete(0, tk.END)
        self.en_origem.configure(state='disabled')
        
        self.en_description_file.delete('1.0', tk.END)
        
        self.en_extension_file.configure(state='normal')
        self.en_extension_file.delete(0, tk.END)
        self.en_extension_file.configure(state='disabled')
        
        self.en_size_file.configure(state='normal')
        self.en_size_file.delete(0, tk.END)
        self.en_size_file.configure(state='disabled')
        
        # SET VALUE STANDARD
        self.en_description_file.insert(tk.END, "Enter a description...")

        
        self.service_upload.upload_file(self.file.get('path'), file_name, description, extension)
        self.btn_upload.configure(state='disabled')
        
        if self.service_upload:
            self.on_update_sucess()
