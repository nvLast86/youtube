from googleapiclient.discovery import build
import json


class Channel:
    """Класс Channel для работы с каналами Youtube"""
    api_key = 'AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI'

    def __init__(self, channel_id):
        self.__channel_id = channel_id
        self.channel_json_info = self.get_json_by_id()
        self.title = self.channel_json_info['items'][0]['snippet']['title']
        self.channel_description = self.channel_json_info['items'][0]['snippet']['description']
        self.url = r'https://www.youtube.com/channel/' + self.__channel_id
        self.video_count = self.channel_json_info['items'][0]['statistics']['videoCount']
        self.channel_view_count = self.channel_json_info['items'][0]['statistics']['viewCount']
        self.subscribers_count = int(self.channel_json_info['items'][0]['statistics']['subscriberCount'])

    def get_json_by_id(self):
        """
        Получение данных о канале по его id
        """
        youtube = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        return youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """метод ввыводит на печать содержимое json"""
        print(json.dumps(self.channel_json_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Получение объекта для работы с API вне класса
        """
        service = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        return service

    def to_json(self, filename):
        """
        Cоздание json файла с данными по каналу
        """
        data = {"title": self.channel_json_info}
        with open(f'{filename}', 'w', encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        """
        Вывод информации о канале
        """
        return f'Youtube-канал: {self.title} с {self.subscribers_count} подписчиков.'

    def __add__(self, other):
        """
        Сложение каналов по количеству подписчиков
        """
        return self.subscribers_count + other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count
