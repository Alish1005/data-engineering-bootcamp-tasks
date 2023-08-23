from datetime import datetime


class News:

    def __init__(self,id:int,type:str,subtitle:str,publish_date:datetime):
        assert id>0