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
            image.thumbnail((500,500))

            self.decompress_image = ImageTk.PhotoImage(image)
            
            return self.decompress_image

        except Exception as err:
            print("Error decompress file:", err)