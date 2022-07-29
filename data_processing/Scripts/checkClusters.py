import numpy as np
import csv
import itertools
import copy
import pandas as pd



# Load the data.
def load_data(path):
    df=pd.read_csv(path)
    return df

# Get the values of the columns about the percent
def get_relevant_values(df_0):
    relevant_data = df_0.loc[:, ['signature_zscore_percent_anger', 'signature_zscore_percent_anticipation',
                                 'signature_zscore_percent_disgust', 'signature_zscore_percent_fear',
                                 'signature_zscore_percent_joy', 'signature_zscore_percent_sadness',
                                 'signature_zscore_percent_surprise', 'signature_zscore_percent_trust', 'cluster_1']]
    data = relevant_data.values
    return data

# Group by clusters
def group_by_clusters(data):
    # Variables
    cluster_0, cluster_1, cluster_2 = [], [], []
    cluster_3, cluster_4, cluster_5 = [], [], []
    cluster_6, cluster_7 = [],[]

    for i in data:
        if i[8] == 0: # Group by cluster 0
            cluster_0.append(i[:-1])
        if i[8] == 1: # Group by cluster 1
            cluster_1.append(i[:-1])
        if i[8] == 2: # Group by cluster 2
            cluster_2.append(i[:-1])
        if i[8] == 3: # Group by cluster 3
            cluster_3.append(i[:-1])
        if i[8] == 4: # Group by cluster 4
            cluster_4.append(i[:-1])
        if i[8] == 5: # Group by cluster 5
            cluster_5.append(i[:-1])
        if i[8] == 6: # Group by cluster 6
            cluster_6.append(i[:-1])
        if i[8] == 7: # Group by cluster 7
            cluster_7.append(i[:-1])

    cluster_0 = pd.DataFrame(cluster_0)
    cluster_1 = pd.DataFrame(cluster_1)
    cluster_2 = pd.DataFrame(cluster_2)
    cluster_3 = pd.DataFrame(cluster_3)
    cluster_4 = pd.DataFrame(cluster_4)
    cluster_5 = pd.DataFrame(cluster_5)
    cluster_6 = pd.DataFrame(cluster_6)
    cluster_7 = pd.DataFrame(cluster_7)

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


def specifyClusters(clusters):
    cluster_check = [-1]*8
    occupied = [0]*8
    i=0

    for cluster in clusters:
        mean_array = cluster.mean(axis=0)
        max_mean = mean_array.max()
        first_max = int(np.where(mean_array == max_mean)[0])
        cluster_check[i] = first_max
        i += 1
        occupied[first_max] += 1


    for i in range(8):
        emotion = occupied[i]

        if emotion > 1:
            min = 10000
            minimum_deviation_index = -1

            for j in range(8):
                if cluster_check[j] == i:
                    cluster_check[j]=-1
                    standard_deviation = clusters[j].std().mean()

                    if standard_deviation < min:
                        min=standard_deviation
                        minimum_deviation_index = j

            if minimum_deviation_index != -1:
                cluster_check[minimum_deviation_index] = i

    for i in range(8):
        if cluster_check[i] == -1:
            mean_duplicated = clusters[i].mean(axis=0)
            max_mean = mean_duplicated.max()
            first_max_duplicated = int(np.where(mean_duplicated == max_mean)[0])

            if cluster_check[i] == -1 and (first_max_duplicated not in cluster_check):
                cluster_check[i] = first_max_duplicated

            else:
                sorted_mean_array_duplicated = mean_duplicated.copy()
                sorted_mean_array_duplicated = np.sort(sorted_mean_array_duplicated)
                j = 6

                while j >= 0:
                    n_max = int(np.where(mean_duplicated == sorted_mean_array_duplicated[j])[0])
                    if cluster_check[i] == -1 and (n_max not in cluster_check):
                        cluster_check[i] = n_max
                        break

                    else:
                        j -= 1

    return cluster_check



def cluster_to_emotions(specifyClusters_emotions):
    emotion_color = []
    df = df_01.values
    for i in df:
        if i[23] == 0:
            emotion_color.append(specifyClusters_emotions[0])
        elif i[23] == 1:
            emotion_color.append(specifyClusters_emotions[1])
        elif i[23] == 2:
            emotion_color.append(specifyClusters_emotions[2])
        elif i[23] == 3:
            emotion_color.append(specifyClusters_emotions[3])
        elif i[23] == 4:
            emotion_color.append(specifyClusters_emotions[4])
        elif i[23] == 5:
            emotion_color.append(specifyClusters_emotions[5])
        elif i[23] == 6:
            emotion_color.append(specifyClusters_emotions[6])
        elif i[23] == 7:
            emotion_color.append(specifyClusters_emotions[7])
    return emotion_color


#----------------------------Main ----------------------------------------
df_01 = load_data("../Data/new_data_cluster.csv")
data1 = get_relevant_values(df_01)
clusters1 = group_by_clusters(data1)

specifyClusters_emotions1 = specifyClusters(clusters1)
emotion_color1 = cluster_to_emotions(specifyClusters_emotions1)
df_01['emotion_color'] = emotion_color1
df_01.to_csv("../Data/new_data_cluster_emotion.csv")
#----------------------------/Main ----------------------------------------
