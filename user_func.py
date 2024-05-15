import ipykernel
from settings import *
import numpy as np
import pandas as pd
from IPython.display import display, HTML


# Пользовательские функции
def toratings(ds, dataset, showzero=False):
    """
    Преобразует таблицу к строкам: user_id, category_name, rating, timestamp
    """

    df2 = pd.DataFrame()
    cols = np.sort(dataset[SPLIT_CATEGORY].unique()).tolist() # Получаем значения всех категорий
    #ds = ds.loc[:, (ds != 0).any(axis=0)] # Удаляем столбцы с одними нулями
    ds.reset_index(inplace=True) # Преобразуем индекс в столбец

    ratings = pd.DataFrame()
    for col in cols:
        if col not in list(ds.columns):
            cols.remove(col)
    for col in cols:
        if showzero:
            dtmp = ds[ds[col]==0][['user_id', col, 'last_purchase']].rename(columns={col: 'rating'})
            dtmp.insert(0,'category',col)
            ratings=pd.concat([ratings,dtmp], ignore_index = True)
        dtmp = ds[ds[col]!=0][['user_id', col, 'last_purchase']].rename(columns={col: 'rating'})
        dtmp.insert(1,'category',col)
        ratings=pd.concat([ratings,dtmp], ignore_index = True)
    df2 = pd.to_datetime(ratings['last_purchase'])
    ratings['last_purchase'] = df2
    ratings['itemID'] = pd.factorize(ratings['category'])[0]+1
    return ratings.rename(columns={'last_purchase': 'timestamp', 'user_id': 'userID'})

def prdf(df):
    display(HTML(df.to_html()))
