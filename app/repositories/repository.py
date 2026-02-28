
import sqlite3


class RepositoryFile:
    """
    Persiste dados no banco de dados sqlite.
    """
    def __init__(self) -> None:
        self._conection = sqlite3.connect("database.db")
        self._cursor = self._conection.cursor()
        self.create_table()
        
        


    def create_table(self) -> None:
        sql_query = ("""
                     CREATE TABLE IF NOT EXISTS tbl_files (
                         id INTEGER,
                         name_file TEXT,
                         file BLOB,
                         description TEXT,
                         date_modify DATE,
                         type_file TEXT,
                         PRIMARY KEY(id)
                     )
                     
                     """)
        
        self._cursor.execute(sql_query)
        self._conection.commit()


    def insert(self, name_file, file, description, extension):
        sql_query = ("""
                     INSERT INTO tbl_files (
                         name_file,
                         file,
                         description,
                         date_modify,
                         type_file
                         ) VALUES (?, ?, ?, date('now'), ?)
                     
                     """)
        sql_args = (name_file, sqlite3.Binary(file), description, extension)

        self._cursor.execute(sql_query, sql_args)
        self._conection.commit()


    def read_unique(self, id_file) -> list:
        sql_query =("SELECT name_file, file FROM tbl_files WHERE id = ? ")
        self._cursor.execute(sql_query, (id_file,))
        unique_file = self._cursor.fetchall()
        
        return unique_file


    def read_all(self) -> list:    
        sql_query = ("SELECT id, name_file, description, date_modify, type_file FROM tbl_files")
        self._cursor.execute(sql_query)
        all_files = self._cursor.fetchall()

        return all_files
    