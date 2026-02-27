from PIL import Image, ImageTk
import zlib
import io


# Refatorando...
class DecompressedFile():
    def decompress_file(self, id_file):
        try:
            image_bytes = zlib.decompress(id_file[0][1])
            image_stream = io.BytesIO(image_bytes)

            image = Image.open(image_stream)
            # image.thumbnail((100,100)) -> Ao utilizar o panedWindow a imagem poderá "renderizar" no tamanho original dela 

            self.decompress_image = ImageTk.PhotoImage(image) # Referência da imagem na memória
            self.lb_placholder.config(image=self.decompress_image)

        except Exception as ex:
            print("Error:", ex)