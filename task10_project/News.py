from datetime import datetime


class News:
    all=list()
    def __init__(self,url:str,type:str,topic:str,publish_date:datetime):
        assert type!=None,'type is required'
        assert topic != None, 'topic is required'
        assert publish_date != None, 'publish_date is required'
        assert url!=None,'url is required'


        News.all.append(self);


        self.__url = url
        self.__type = type
        self.__topic = topic
        self.__publish_date = publish_date


    # Getters - Read-Only

    @property
    def url(self):
        return self.__url
    @property
    def type(self):
        return self.__type
    @property
    def topic(self):
        return self.__topic
    @property
    def publish_date(self):
        return self.__publish_date


