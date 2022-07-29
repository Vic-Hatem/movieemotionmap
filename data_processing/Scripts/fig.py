import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Load the data.
def load_data(path):
    df=pd.read_csv(path)
    return df

# Get the values of the columns about the percent
def get_relevant_values(df_0):
    relevant_data = df_0.loc[:, ['tsne_glyph_x','tsne_glyph_y']]
    data = relevant_data.values
    relevant_data1 = df_0.loc[:, ['emotion_color']]
    data1 = relevant_data1.values
    return data, data1

# Function to map the colors as a list from the input list of x variables
def pltcolor(lst):
    cols=[]
    for l in lst:

        if l== 1:
            cols.append('#ff0000')
        elif l== 2:
            cols.append( "#ff6600")
        elif l== 3:
            cols.append("#ff6699")
        elif l== 4:
            cols.append( "#66cc66")
        elif l== 5:
            cols.append( "#ffff00")
        elif l== 6:
            cols.append( "#cc00ff")
        elif l== 7:
            cols.append( "#33adff")
        else:
            cols.append("#996633")
    return cols

def create_fig(d_tsne, predictions):
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(30, 40))
    x = d_tsne[:, 0]
    y = d_tsne[:, 1]
    # x2 = X_2d[:,0]
    # y2= X_2d[:,1]


    # Create the colors list using the function above
    colors = pltcolor(predictions)

    ax[0].scatter(x, y, c=colors)
    ax[0].title.set_text('SOM- OLD TSNE')
    plt.savefig('../Image/SOM_Map111.png')

df_0=load_data("../Data/new_data_cluster_emotion.csv")
d_tsne,emotion = get_relevant_values(df_0)
create_fig(d_tsne, emotion)