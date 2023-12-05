import requests
import sqlite3

def data():
    key = "3e0b83989687426c9d97d4331b39dd58"
    query = "tesla"
    from_date = "2023-11-4"

    #response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-11-04&sortBy=publishedAt&apiKey=API_KEY')
    response = requests.get(f'https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={key}')
    news_data = response.json()

    # connect to sqlite 3
    conn = sqlite3.connect('news_database.db')
    cursor = conn.cursor()

    #create table in db
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS news (
                   source_id TEXT,
                   source_name TEXT,
                   author TEXT,
                   title TEXT,
                   description TEXT,
                   url TEXT,
                   urltoimage TEXT,
                   publishedat TEXT,
                   content TEXT
)
''')


    # Insert dadta into table

    articles = news_data.get('articles',[])
    for article in articles:
        cursor.execute(''' 
INSERT INTO news (source_id, source_name, author,title, description, url, urltoimage, publishedat, content)
VALUES(?,?,?,?,?,?,?,?,?)
''',(article['source']['id'], article['source']['name'],article['author'], article['title'], article['description'], article['url'], article['urlToImage'],article['publishedAt'],article['content'] ))

    conn.commit()
    conn.close()

    print('data stored in sqlite')

data()
   