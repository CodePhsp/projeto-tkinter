import tkinter as tk
from views.render_preview_view import RenderPreview
from views.form_view import Form
from services.search_file_service import SearchFile



class App(Form, RenderPreview):
    def __init__(self):
      self.app = tk.Tk()
      self.app.geometry('930x550+560+100')
      self.app.title('Sistema de Upload de Arquivos - SisUpa')
      service = SearchFile()
      self.form(self.app, service)
      self.frame_preview(self.app)
      self.app.mainloop()



if __name__ == '__main__':
  App()
