from Strategy.file_interface_strategy import FileStrategy
from PIL import Image, ImageTk
import io



class ImageStrategy(FileStrategy):
    def process_file(self, file):

        try:
            image_stream = io.BytesIO(file)

            image = Image.open(image_stream)
            image.thumbnail((500,500))

            if image is not None:
                self.decompress_image = ImageTk.PhotoImage(image)
                image_descompress = self.decompress_image
                return image_descompress
            else:
                return

        except Exception as err:
            print("Error decompress file:", err)

        return 