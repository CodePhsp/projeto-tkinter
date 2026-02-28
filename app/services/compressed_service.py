
import zlib

   
class CompressedFile:
    def compress_file(self, file):
        try:
            file_compress = zlib.compress(open(file, 'rb').read(), 2)
            
            return file_compress
        
        except Exception as err:
            print(f"Erro compress file: ", err)