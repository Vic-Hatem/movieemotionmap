import pandas as pd
import numpy as np
import csv
import itertools
import copy
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

# load the data
def load_data(path):
    df=pd.read_csv(path)
    return df

def convert_ratings(data):
    ratings=[]
    for i in data:
        if i >= 8:
            ratings.append(5)
        elif i >= 6:
            ratings.append(4)
        elif i >= 4:
            ratings.append(3)
        elif i >= 2:
            ratings.append(2)
        elif i > 0:
            ratings.append(1)
        elif i==0:
            ratings.append(0)

    return ratings

# zscore to percent for anger
def zscore_percent_anger(df):
    signature_zscore_percent_anger=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_anger.append(zscore_percent)
    return signature_zscore_percent_anger

# zscore to percent for anticipation
def zscore_percent_anticipation(df):
    signature_zscore_percent_anticipation=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_anticipation.append(zscore_percent)
    return signature_zscore_percent_anticipation

# zscore to percent for disgust
def zscore_percent_disgust(df):
    signature_zscore_percent_disgust=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_disgust.append(zscore_percent)
    return signature_zscore_percent_disgust

# zscore to percent for fear
def zscore_percent_fear(df):
    signature_zscore_percent_fear=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_fear.append(zscore_percent)
    return signature_zscore_percent_fear

# zscore to percent for joy
def zscore_percent_joy(df):
    signature_zscore_percent_joy=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_joy.append(zscore_percent)
    return signature_zscore_percent_joy

# zscore to percent for sadness
def zscore_percent_sadness(df):
    signature_zscore_percent_sadness=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_sadness.append(zscore_percent)
    return signature_zscore_percent_sadness

# zscore to percent for surprise
def zscore_percent_surprise(df):
    signature_zscore_percent_surprise=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_surprise.append(zscore_percent)
    return signature_zscore_percent_surprise

# zscore to percent for trust
def zscore_percent_trust(df):
    signature_zscore_percent_trust=[]
    for zscore in df:
        zscore_percent=scipy.stats.norm.sf(zscore * (-1))
        signature_zscore_percent_trust.append(zscore_percent)
    return signature_zscore_percent_trust

# extracting the relevant columns
def relevent_data(df):
    relevant_data= df.loc[:,['_id','movie_directors','movie_genres','movie_rating','movie_stars','movie_writers','name','plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y']]
    return relevant_data


df_0=load_data("../Data/finalCollection.csv")

# getting all new percentages for each  of the 8 emotion
percent_anger=zscore_percent_anger(df_0["signature_zscore.anger"]).copy()
percent_anticipation=zscore_percent_anticipation(df_0["signature_zscore.anticipation"]).copy()
percent_disgust=zscore_percent_disgust(df_0["signature_zscore.disgust"]).copy()
percent_fear=zscore_percent_fear(df_0["signature_zscore.fear"]).copy()
percent_joy=zscore_percent_joy(df_0["signature_zscore.joy"]).copy()
percent_sadness=zscore_percent_sadness(df_0["signature_zscore.sadness"]).copy()
percent_surprise=zscore_percent_surprise(df_0["signature_zscore.surprise"]).copy()
percent_trust=zscore_percent_trust(df_0["signature_zscore.trust"]).copy()
ratings=convert_ratings(df_0["movie_rating"]).copy()

df_0=relevent_data(df_0)

# adding all the new columns to the original dataframe
df_0['signature_zscore_percent_anger']=percent_anger
df_0['signature_zscore_percent_anticipation']=percent_anticipation
df_0['signature_zscore_percent_disgust']=percent_disgust
df_0['signature_zscore_percent_fear']=percent_fear
df_0['signature_zscore_percent_joy']=percent_joy
df_0['signature_zscore_percent_sadness']=percent_sadness
df_0['signature_zscore_percent_surprise']=percent_surprise
df_0['signature_zscore_percent_trust']=percent_trust
df_0['movie_rating']=ratings

# writing the data a new csv file
df_0.to_csv('../Data/new_data_percent.csv')