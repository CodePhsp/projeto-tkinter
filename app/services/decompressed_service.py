
import zlib



# Refatorando...
class DecompressedFile:
    def decompress_file(self, id_file) -> dict:
        try:
            file_bytes = zlib.decompress(id_file[0][1])

            data= {
                'file_bytes': file_bytes,
                'extension': id_file[0][2]
            }

            return data

        except Exception as err:
            print("Error decompress file:", err)