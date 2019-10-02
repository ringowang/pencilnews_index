import requests
import csv
from datetime import datetime

base_url = 'https://www.pencilnews.cn/p/'

for page in range(0,20):
    print(page)
    main_list = []

    url = 'https://api.pencilnews.cn/articles?page={}&page_size=400&cate_id=2'.format(str(19-int(page)))
    r = requests.get(url)
    data = r.json()['data']['articles']
    for article in data:
        info = article['article_info']
        article_url = base_url + str(info.get('article_id'))
        raw_date = info.get('create_at')
        try:
            complete_date = datetime.strptime(raw_date,'%Y-%m-%d %H:%M:%S')
        except:
            complete_date = datetime.strptime(raw_date,'%Y-%m-%d')
        date_str = datetime.strftime(complete_date, '%Y-%m-%d')
        raw_title = info.get('title')
        title_str = '[{}]({})'.format(raw_title, article_url)
        data_rubbing = [date_str, 'aaaa', title_str]
        main_list.append(data_rubbing)

    with open('articles.csv', 'a+', newline='',encoding='utf-8-sig') as f:
        w = csv.writer(f)
        main_list.reverse()
        w.writerows(main_list)