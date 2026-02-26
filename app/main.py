import customtkinter as ctk
from views.menu_view import MenuGui
from views.detail_view import DetailGui

class App(ctk.CTk, MenuGui):
    def __init__(self):
      self.app = ctk.CTk()
      self.menu(self.app)
      self.app.mainloop()



if __name__ == "__main__":
   app = App()