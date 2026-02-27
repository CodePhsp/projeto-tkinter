from tkinter import filedialog as dlg
from pathlib import Path


class SearchFile():
    """
    Utiliza o askopenfilename para que o usuário busque o arquivo desejado.\n
    Retorna o nome base do arquivo. 
    """
    def ask_file(self) -> dict:
        ask_file_path = dlg.askopenfilename(filetypes = (("png","*.png"), ("jpg","*.jpg")))
        file = Path(ask_file_path) 

        data = {
            'name_base': file.name,
            'extension': file.suffix,
            'size': file.stat().st_size
        }
        
        return data