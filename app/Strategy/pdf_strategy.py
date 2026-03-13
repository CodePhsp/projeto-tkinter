from Strategy.file_interface_strategy import FileStrategy
from PIL import Image, ImageTk
import fitz



class PdfStrategy(FileStrategy):
    def process_file(self, file):
        try:

            document_pdf = fitz.open(stream=file, filetype='pdf')
            page_document = document_pdf.load_page(0)

            pix = page_document.get_pixmap()

            pdf_stream = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)

            if document_pdf is not None:
                self.decompress_image = ImageTk.PhotoImage(pdf_stream)
                pdf_descompress = self.decompress_image
                return pdf_descompress
            else:
                return
        
        except Exception as erro:
            print(f'Erro in process pdf: {erro}')
            