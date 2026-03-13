from services.decompressed_service import DecompressedFile
from Strategy.image_strategy import ImageStrategy
from Strategy.pdf_strategy import PdfStrategy


class FileProcessor:
    def __init__(self):
        self.decompress = DecompressedFile()
    
    def process_file(self, file):
        data = self.decompress.decompress_file(file)
            
        file_bytes= data['file_bytes']
        extension= data['extension']

        strategy = self.resolve_strategy(extension= extension)

        print(strategy.process_file(file_bytes))
        
        return strategy.process_file(file_bytes)
            
        
    
    def resolve_strategy(self, extension):
        if extension in ['.png', '.jpg']:
            return ImageStrategy()
        
        if extension in ['.pdf']:
            return PdfStrategy()