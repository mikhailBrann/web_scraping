from lib.request_connect import Request

#список ключевых слов для поиска статей
KEYWORDS = ['дизайн', 'фото', 'web', 'Python']

SITE_URL = 'https://habr.com/ru/all/' 
page = Request(SITE_URL).page_html
articles_list = page.find('.tm-articles-list__item')

for article in articles_list:
    hubs_wrapp = article.find('.tm-article-snippet__hubs-item-link')
    #обрабатываем теги и приводим к нижнему регистру
    hub_tags = set(hub.find('span', first=True).text.lower() for hub in hubs_wrapp)
    
    #преобразуем список введенных тегов в множество и приводим к нижнему регистру
    if set(key.lower() for key in KEYWORDS) & hub_tags:
        date = article.find('.tm-article-snippet__datetime-published > time', first=True).attrs['title']
        link = article.find('.tm-article-snippet__title-link', first=True)
        title = link.find('span', first=True).text 
        
        # для корректного отображения ссылки затер окончание
        print(f"<{date}> - <{title}> - <{SITE_URL.replace('/ru/all/', link.attrs['href'])}>")

    










