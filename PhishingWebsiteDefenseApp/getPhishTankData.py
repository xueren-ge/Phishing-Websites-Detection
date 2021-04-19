import requests
import os
import pandas as pd
import sqlalchemy

store_path = './data/'
url = 'https://data.phishtank.com/data/7623396d52d879bf484826bc99a3b3a814c746ff4c4a88102ea6111338821247/online-valid.csv'

def import_data():
    filename = url.split("/")[-1]
    filepath = os.path.join(store_path, filename)

    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)

    engine = sqlalchemy.create_engine('mysql+pymysql://root:123456@localhost/pdms?charset=utf8')
    df = pd.read_csv(filepath)
    df.to_sql('t_phish_tank_website_info', engine, index=False, if_exists='replace')

if __name__ == '__main__':
    import_data()