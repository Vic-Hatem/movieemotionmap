import pandas as pd
from sklearn_som.som import SOM
from sklearn.manifold import TSNE


# Load the data.
def load_data(path):
    df=pd.read_csv(path,index_col=[0,1])
    return df

# Group by clusters
def group_by_culsters(data):
    # Variables
    cluster_0, cluster_1, cluster_2 = [], [], []
    cluster_3, cluster_4, cluster_5 = [], [], []
    cluster_6, cluster_7 = [], []
    print(len(data.columns))
    for i in data.values:
        if i[23] == 0: # Group by cluster 0
            cluster_0.append(i)
        if i[23] == 1: # Group by cluster 1
            cluster_1.append(i)
        if i[23] == 2: # Group by cluster 2
            cluster_2.append(i)
        if i[23] == 3: # Group by cluster 3
            cluster_3.append(i)
        if i[23] == 4: # Group by cluster 4
            cluster_4.append(i)
        if i[23] == 5: # Group by cluster 5
            cluster_5.append(i)
        if i[23] == 6: # Group by cluster 6
            cluster_6.append(i)
        if i[23] == 7: # Group by cluster 7
            cluster_7.append(i)

    # Drop the column cluster

    cluster_0 = pd.DataFrame(cluster_0,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_1 = pd.DataFrame(cluster_1,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_2 = pd.DataFrame(cluster_2,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_3 = pd.DataFrame(cluster_3,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_4 = pd.DataFrame(cluster_4,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_5 = pd.DataFrame(cluster_5,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_6 = pd.DataFrame(cluster_6,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])

    cluster_7 = pd.DataFrame(cluster_7,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])


    # combining all clusters in a single array
    clusters = []
    clusters.append(cluster_0)
    clusters.append(cluster_1)
    clusters.append(cluster_2)
    clusters.append(cluster_3)
    clusters.append(cluster_4)
    clusters.append(cluster_5)
    clusters.append(cluster_6)
    clusters.append(cluster_7)
    return clusters

# Get the values of the columns about the percent
def get_relevant_values(df_0,index):
    df_0=pd.DataFrame(df_0,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])
    if index == 0:
        relevant_data =df_0.loc[:,['signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index ==1:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index == 2:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index == 3:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index == 4:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_sadness','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index == 5:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_surprise','signature_zscore_percent_trust']]
    elif index == 6:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_trust']]
    elif index == 7:
        relevant_data = df_0.loc[:,['signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy','signature_zscore_percent_sadness','signature_zscore_percent_surprise']]

    return relevant_data

# Employing the SOM algorithm. Return the predictions.
def SOM_algorithm(clusters):
    index=0
    data=[]
    for cluster in clusters:
        relevantData=get_relevant_values(cluster,index)

        som = SOM(m=7, n=1, dim=7, random_state=1234)
        som.fit(relevantData.values)
        predictions = som.predict(relevantData.values)
        index += 1
        cluster=pd.DataFrame(cluster,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color'])
        cluster['cluster_level2']= predictions
        data.append(cluster)
    return data

# Employing the TSNE algorithm ON the new data we export.
def TSNE_algorithm(data):

    index=0
    for cluster in data:

        relevantData=get_relevant_values(cluster,index)

        tsne = TSNE(n_components=2, random_state=1234)
        X_2d = tsne.fit_transform(relevantData)

        cluster['tsne_glyph_x_level2']= X_2d[:, 0]
        cluster['tsne_glyph_y_level2']= X_2d[:, 1]
        index += 1

    return data

# Export the predictions appropriate data to CSV
def export_to_CSV(data):

    count = 0
    for cluster in data:
        cluster=pd.DataFrame(cluster)
        # cluster.drop([0], axis=1)
        # cluster.drop([0], axis=1)
        # if count==0:
        #     cluster.rename(columns = {'1': '_id', '2': 'movie_directors', '3': 'movie_genres', '4': 'movie_rating', '5': 'movie_stars',
        #                          '6': 'movie_writers', '7': 'name', '8': 'plot', '9': 'poster', '10': 'release_year',
        #                          '11': 'reviews_num',
        #                          '12': 'titleId', '13': 'tsne_glyph.x', '14': 'tsne_glyph.y',
        #                          '15': 'signature_zscore_percent_anticipation',
        #                          '16': 'signature_zscore_percent_disgust', '17': 'signature_zscore_percent_fear',
        #                          '18': 'signature_zscore_percent_joy', '19': 'signature_zscore_percent_sadness',
        #                          '20': 'signature_zscore_percent_surprise', '21': 'signature_zscore_percent_trust'}, inplace=True)
        # cluster = pd.DataFrame(cluster)
        print(cluster)

        if count == 0:
            cluster.to_csv("../Data/cluster_level2_anger.csv")
        elif count == 1:
            cluster.to_csv("../Data/cluster_level2_anticipation.csv")
        elif count == 2:
            cluster.to_csv("../Data/cluster_level2_disgust.csv")
        elif count == 3:
            cluster.to_csv("../Data/cluster_level2_fear.csv")
        elif count == 4:
            cluster.to_csv("../Data/cluster_level2_joy.csv")
        elif count == 5:
            cluster.to_csv("../Data/cluster_level2_sadness.csv")
        elif count == 6:
            cluster.to_csv("../Data/cluster_level2_surprise.csv")
        elif count == 7:
            cluster.to_csv("../Data/cluster_level2_trust.csv")
        count += 1


df_0=load_data("../Data/new_data_cluster_emotion.csv")
df_0= pd.DataFrame(df_0)
clusters=group_by_culsters(df_0)

clusterPredictions= SOM_algorithm(clusters)
d_tsne= TSNE_algorithm(clusterPredictions)
export_to_CSV(d_tsne)



