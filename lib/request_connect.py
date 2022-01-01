from requests_html import HTMLSession as session

class Request:
    def __init__(self,url):
        self.url = url
        self.page_html = self._getInfo()

    def _getInfo(self):
        # делаем запрос к нужной странице
        responce = session().get(self.url)
        
        # выставляем кирилицу в качестве кодировки
        responce.encoding = 'utf-8'
        return responce.html



        
        