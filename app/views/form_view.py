import tkinter as tk


class Form:
    def form(self, root, service) -> None:
        self.service = service

        self.fr_main = tk.Frame(root, width= 100, height= 100, background='gray25')
        self.fr_main.pack(side='left', fill='both', ipadx= 40)

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
        self.fr_action_search.pack(side='top', fill='x', expand='yes')
        
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
        self.en_description_file.insert(tk.END, "Insira uma descrição...\n")

        # BUTTON UPLOAD---
        self.fr_action_description_file = tk.Frame(self.fr_form, width= 100, height= 100, background='gray25')
        self.fr_action_description_file.pack(side='top', fill='x', padx= 10)

        self.btn_upload = tk.Button(self.fr_action_description_file, text='upload file', state='disabled', font=('Courier', 10, 'bold'), command= ...)
        self.btn_upload.pack(side='right', fill='x', pady=5)

        # INFORMATIONS ADDITIONNELLES
        self.lf_adtionais_info = tk.LabelFrame(self.fr_main, text='Informations additionalles', padx= 10, pady= 10, background='gray25', foreground='white', font=('Courier', 14, 'bold'))
        self.lf_adtionais_info.pack(side='top', fill='both', expand='yes', padx= 10, pady= 10)

        self.lb_extension_file = tk.Label(self.lf_adtionais_info, text='Extensão: ', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_extension_file.pack(side='top', fill='x', padx= 10)

        self.lb_size_file = tk.Label(self.lf_adtionais_info, text='Size: ', background='gray25', foreground='white', font=('Courier', 12, 'bold'))
        self.lb_size_file.pack(side='top', fill='x', padx= 10)

    
    def action_search(self):
        file = self.service.ask_file()
        self.origem_path_file.set(file.get('name_base'))

        self.btn_upload.configure(state='normal')

        self.lb_extension_file.configure(text=f'Extensão: {file.get('extension')}')
        self.lb_size_file.configure(text=f'Size: {file.get('size')/1024} bytes')