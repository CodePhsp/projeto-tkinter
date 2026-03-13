from abc import ABC, abstractmethod


class FileStrategy(ABC):

    @abstractmethod
    def process_file(self, file):
        pass