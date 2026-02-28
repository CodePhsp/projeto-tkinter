import tkinter as tk
from views.render_preview_view import RenderPreview
from views.form_view import Form
from services.search_file_service import SearchFile
from services.decompressed_service import DecompressedFile



class App:
    def __init__(self):
        self.app= tk.Tk()
        self.app.geometry('1000x550+280+100')
        self.app.title('Sistema de Upload de Arquivos - SisUpa')

        search_service= SearchFile()
        decompress_service= DecompressedFile()
        
        
        self.form= Form()
        self.preview= RenderPreview()
        
        self.form.form(self.app, search_service, self.preview.action_update_list)

        self.preview.frame_preview(self.app, decompress_service)

        self.app.mainloop()



if __name__ == '__main__':
  App()
