from abc import ABC


class YouTube(ABC):
    """
    Абстрактный класс для будущего определения методов, которые будут переопределены
    в дочерних классах
    """

    @abstractmethod
    def get_youtube_api_key(self):
        """
        Метод получения API_KEY для работы с Youtube
        """
        pass

    @abstractmethod
    def get_youtube_object(self):
        """
        Метод получения объекта Youtube
        """
        pass



