from googleapiclient.discovery import build
import json

class Channel:
    """Класс Channel для работы с каналами Youtube"""
    api_key = 'AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI'

    def __init__(self, channel_id):
        youtube = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        self.__channel_id = channel_id
        self.channel_json_info = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        #self.get_channel_json_info()
        self.title = self.channel_json_info['items'][0]['snippet']['title']
        self.channel_description = self.channel_json_info['items'][0]['snippet']['description']
        self.url = r'https://www.youtube.com/channel/' + self.__channel_id
        self.video_count = self.channel_json_info['items'][0]['statistics']['videoCount']
        self.channel_view_count = self.channel_json_info['items'][0]['statistics']['viewCount']

    def get_channel_json_info(self):
        """Метод получения информации о канале в формате json"""
        with build('youtube', 'v3', developerKey=Channel.api_key) as channel_info:
            channel = channel_info.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
            print(channel)
         #   self.channel_json_info = json.dumps(channel, indent=2, ensure_ascii=False)
         #   print(self.channel_json_info)

    def get_json_by_id(self):
        """ метод создает специальный объект для работы с API youtube"""
        channel = self.channel_info.channels().list(id=self.__id, part='snippet,statistics').execute()
        self.channel_json_info = channel

    def get_channel_info_json(self):
        """метод сохраняет все атрибуты объекта channel, кроме json в файл по адресу path"""
        text = "["
        for dic in self.__dict__:
            if dic != 'json':
                text += "{'" + str(dic) + "':'" + str(self.__dict__[dic]) + "'}, \n"
        json_text = text[:-3] + "]"
        with open(path, "w", encoding="UTF-8") as file:
            file.write(str(json_text))

    def print_info(self):
        print(self.channel_json_info)

