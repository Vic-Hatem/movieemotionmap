import numpy as np

import pandas as pd



# Load the data.
def load_data(path):
    df=pd.read_csv(path,index_col=0)
    return df

# Get the values of the columns about the percent
def get_relevant_values(clusters):

    data=[]
    for cluster in clusters:
        cluster = pd.DataFrame(cluster,columns=['_id', 'movie_directors', 'movie_genres', 'movie_rating', 'movie_stars', 'movie_writers', 'name',
                     'plot', 'poster', 'release_year', 'reviews_num', 'titleId', 'tsne_glyph.x', 'tsne_glyph.y',
                     'signature_zscore_percent_anger', 'signature_zscore_percent_anticipation',
                     'signature_zscore_percent_disgust', 'signature_zscore_percent_fear',
                     'signature_zscore_percent_joy', 'signature_zscore_percent_sadness',
                     'signature_zscore_percent_surprise', 'signature_zscore_percent_trust', 'cluster_1',
                     'emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

        relevant_data = cluster.loc[:, ['signature_zscore_percent_anger', 'signature_zscore_percent_anticipation',
                                     'signature_zscore_percent_disgust', 'signature_zscore_percent_fear',
                                     'signature_zscore_percent_joy', 'signature_zscore_percent_sadness',
                                     'signature_zscore_percent_surprise', 'signature_zscore_percent_trust']]
        data.append(relevant_data)

    return data

def group_by_culsters(data):

    # Variables
    cluster_0, cluster_1, cluster_2 = [], [], []
    cluster_3, cluster_4, cluster_5 = [], [], []
    cluster_6 = []
    for i in data.values:
        if i[24] == 0: # Group by cluster 0
            cluster_0.append(i)
        if i[24] == 1: # Group by cluster 1
            cluster_1.append(i)
        if i[24] == 2: # Group by cluster 2
            cluster_2.append(i)
        if i[24] == 3: # Group by cluster 3
            cluster_3.append(i)
        if i[24] == 4: # Group by cluster 4
            cluster_4.append(i)
        if i[24] == 5: # Group by cluster 5
            cluster_5.append(i)
        if i[24] == 6: # Group by cluster 6
            cluster_6.append(i)


    # Drop the column cluster
    cluster_0 = pd.DataFrame(cluster_0,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

    cluster_1 = pd.DataFrame(cluster_1,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])


    cluster_2 = pd.DataFrame(cluster_2,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

    cluster_3 = pd.DataFrame(cluster_3,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

    cluster_4 = pd.DataFrame(cluster_4,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

    cluster_5 = pd.DataFrame(cluster_5,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])

    cluster_6 = pd.DataFrame(cluster_6,columns=['_id', 'movie_directors','movie_genres', 'movie_rating', 'movie_stars','movie_writers','name', 'plot','poster','release_year','reviews_num','titleId','tsne_glyph.x','tsne_glyph.y','signature_zscore_percent_anger','signature_zscore_percent_anticipation','signature_zscore_percent_disgust','signature_zscore_percent_fear','signature_zscore_percent_joy', 'signature_zscore_percent_sadness','signature_zscore_percent_surprise', 'signature_zscore_percent_trust','cluster_1','emotion_color','cluster_level2','tsne_glyph_x_level2','tsne_glyph_y_level2'])



    # combining all clusters in a single array
    clusters = []
    clusters.append(cluster_0)
    clusters.append(cluster_1)
    clusters.append(cluster_2)
    clusters.append(cluster_3)
    clusters.append(cluster_4)
    clusters.append(cluster_5)
    clusters.append(cluster_6)

    return clusters

def specifyClusters(clusters,index):
    cluster_check=[-1]*7
    occupied=[0]*8

    occupied[index]=1

    i = 0
    for cluster in clusters:

        mean_array = cluster.mean(axis=0)
        max_mean = mean_array.max()
        first_max = int(np.where(mean_array == max_mean)[0])
        if first_max != index:
            cluster_check[i] = first_max
            occupied[first_max] += 1
        else:
            sorted_mean_array_duplicated = mean_array.copy()
            sorted_mean_array_duplicated = np.sort(sorted_mean_array_duplicated)
            j = 6

            while j >= 0:
                n_max = int(np.where(mean_array == sorted_mean_array_duplicated[j])[0])
                if cluster_check[i] == -1 and (n_max not in cluster_check) and (n_max != index):
                    cluster_check[i] = n_max
                    occupied[n_max]+=1
                    break
                else:
                    j -= 1
        i += 1

    for i in range(8):
        if i != index:
            emotion = occupied[i]
            if emotion > 1:
                min = 10000
                minimum_deviation_index = -1
                for j in range(7):
                    if cluster_check[j] == i:
                        cluster_check[j]=-1
                        standard_deviation = clusters[j].std().mean()
                        if standard_deviation < min:
                            min=standard_deviation
                            minimum_deviation_index = j
                if minimum_deviation_index != -1:
                    cluster_check[minimum_deviation_index] = i

    for i in range(7):

        if cluster_check[i] == -1:
            mean_duplicated = clusters[i].mean(axis=0)
            max_mean = mean_duplicated.max()
            first_max_duplicated = int(np.where(mean_duplicated == max_mean)[0])
            if first_max_duplicated != index:
                if first_max_duplicated not in cluster_check:
                    cluster_check[i] = first_max_duplicated

                else:
                    sorted_mean_array_duplicated = mean_duplicated.copy()
                    sorted_mean_array_duplicated = np.sort(sorted_mean_array_duplicated)
                    j = 6

                    while j >= 0:
                        n_max = int(np.where(mean_duplicated == sorted_mean_array_duplicated[j])[0])
                        if n_max not in cluster_check and (n_max != index):
                            cluster_check[i] = n_max
                            break

                        else:
                            j -= 1
            else:
                sorted_mean_array_duplicated = mean_duplicated.copy()
                sorted_mean_array_duplicated = np.sort(sorted_mean_array_duplicated)
                j = 6

                while j >= 0:
                    n_max = int(np.where(mean_duplicated == sorted_mean_array_duplicated[j])[0])
                    if n_max not in cluster_check and (n_max != index):
                        cluster_check[i] = n_max
                        break
                    else:
                        j -= 1

    return cluster_check



def cluster_to_emotions(specifyClusters_emotions,df_01):
    emotion_color = []
    df = df_01.values
    for i in df:
        if i[24] == 0:
            emotion_color.append(specifyClusters_emotions[0])
        elif i[24] == 1:
            emotion_color.append(specifyClusters_emotions[1])
        elif i[24] == 2:
            emotion_color.append(specifyClusters_emotions[2])
        elif i[24] == 3:
            emotion_color.append(specifyClusters_emotions[3])
        elif i[24] == 4:
            emotion_color.append(specifyClusters_emotions[4])
        elif i[24] == 5:
            emotion_color.append(specifyClusters_emotions[5])
        elif i[24] == 6:
            emotion_color.append(specifyClusters_emotions[6])

    return emotion_color


#----------------------------Main ----------------------------------------

lvl2_file_paths=['anger','anticipation','disgust','fear','joy','sadness','surprise','trust']
index = 0

for name in lvl2_file_paths:
    df_01 = load_data("../Data/cluster_level2_"+name+".csv")
    clusters1 = group_by_culsters(df_01)

    data1 = get_relevant_values(clusters1)

    specifyClusters_emotions1 = specifyClusters(data1,index)
    emotion_color1 = cluster_to_emotions(specifyClusters_emotions1,df_01)
    df_01['emotion_color_lvl2'] = emotion_color1
    df_01.to_csv("../Data/lvl2_"+name+".csv")
    index += 1


#----------------------------/Main ----------------------------------------
