from tkinter import END
import zlib


class CompressedFile():
    def compress_file(self):
        try:
            name_file = self.path_file.get()
            self.file_compress = zlib.compress(open(self.ask_path_file, 'rb').read(), 2)
            description = self.en_description.get('1.0', END)

            self.file_in_base(name_file=name_file, file=self.file_compress, description=description)
            self.path_file.delete(0, END)
            self.en_description.delete('1.0', END)

            self.update_list_of_file()

        except Exception as ex:
            print(f"Erro compress file: ", ex)