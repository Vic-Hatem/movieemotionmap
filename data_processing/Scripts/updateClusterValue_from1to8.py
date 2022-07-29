# importing the pandas library
import pandas as pd

import os


def change_pics_prefix():
    for file_name in os.listdir("pics"):
        new_file = str("tt" + file_name)
        os.rename("pics/" + file_name, new_file)
        
# Load the data.
def load_data(path):
    df=pd.read_csv(path,index_col=0)
    return df

def update_values_clusters_lvl2(df,name):

    index_row=0
    length= len(df)
    for row in df.values:
        if index_row<length:
            # updating the column 'emotion_color_lvl2' value/data
            value_emotion = df.loc[index_row, 'emotion_color_lvl2']
            value_emotion = value_emotion + 1
            df.loc[index_row, 'emotion_color_lvl2'] = value_emotion

            # updating the column 'cluster_level2' value/data
            value_cluster = df.loc[index_row, 'cluster_level2']
            value_cluster = value_cluster + 1
            df.loc[index_row, 'cluster_level2'] = value_cluster

            # updating the column ''emotion_color'' value/data
            value_emotion_lvl1 = df.loc[index_row, 'emotion_color']
            value_emotion_lvl1 = value_emotion_lvl1 + 1
            df.loc[index_row, 'emotion_color'] = value_emotion_lvl1

            # updating the column 'cluster_1' value/data
            value_cluster_lvl1 = df.loc[index_row, 'cluster_1']
            value_cluster_lvl1 = value_cluster_lvl1 + 1
            df.loc[index_row, 'cluster_1'] = value_cluster_lvl1

            index_row += 1

    # df = titleid_cut(df)
    df = rename_dots(df)
    # writing into the file
    df.to_csv(name, index=False)

def update_values_clusters(df,name):

    index_row=0
    length=len(df)
    for row in df.values:
        if index_row<length:
            # updating the column ''emotion_color'' value/data
            value_emotion = df.loc[index_row, 'emotion_color']
            value_emotion = value_emotion + 1
            df.loc[index_row, 'emotion_color'] = value_emotion

            # updating the column 'cluster_1' value/data
            value_cluster = df.loc[index_row, 'cluster_1']
            value_cluster = value_cluster + 1
            df.loc[index_row, 'cluster_1'] = value_cluster
            index_row += 1


    # df=titleid_cut(df)
    df=rename_dots(df)
    # df.loc[5, 'cluster_level2'] = 'SHIV CHANDRA'
    #
    # writing into the file
    df.to_csv(name, index=False)

# def titleid_cut(data):
#     titleids=[]
#     for i in data['titleId']:
#         titleids.append(i[2:])
#
#     data['titleId']=titleids
#     return data

def rename_dots(data):
	data.rename(columns = {'tsne_glyph.x':'tsne_glyph_x','tsne_glyph.y':'tsne_glyph_y'},inplace=True)
	return data


#----------------------------Main ----------------------------------------
lvl2_file_paths=['anger','anticipation','disgust','fear','joy','sadness','surprise','trust']
index = 0

for name in lvl2_file_paths:
    help_name="../Data/lvl2_"+name+".csv"
    df_01 = load_data(help_name)
    # titleid_cut(df_01)
    update_values_clusters_lvl2(df_01,help_name)
    print("Done with: ",help_name)



df_01= load_data("../Data/new_data_cluster_emotion.csv")
update_values_clusters(df_01,"../Data/new_data_cluster_emotion.csv")
print("Done with: ../Data/new_data_cluster_emotion.csv")