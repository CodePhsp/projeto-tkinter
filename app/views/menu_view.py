import customtkinter as ctk


class MenuGui:
    def menu(self, root) -> None:
        self.frame_menu = ctk.CTkFrame(root, width=160, height=200)
        self.frame_menu.pack(side='left', fill='both', padx= 10, pady= 10, ipadx=4)