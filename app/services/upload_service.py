from services.compressed_service import CompressedFile
from repositories.repository import RepositoryFile


class UploadFile():
    def __init__(self) -> None:
        self.bd = RepositoryFile()
    
    
    def upload_file(self, path_file: str, name_file: str, description: str, extension: str):
        compress = CompressedFile()
        bynary_file = compress.compress_file(file=path_file)
        
        
        self.bd.insert(name_file, bynary_file, description, extension)
        
        