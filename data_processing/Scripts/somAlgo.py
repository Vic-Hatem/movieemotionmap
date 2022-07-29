import pandas as pd
import matplotlib.pyplot as plt
from sklearn_som.som import SOM
from matplotlib.colors import ListedColormap
from sklearn.manifold import TSNE


# Load the data.
def load_data(path):
    df=pd.read_csv(path)
    return df

# Get the values of the columns about the percent
def get_relevant_values(df_0):
    relevant_data = df_0.loc[:, ['signature_zscore_percent_anger', 'signature_zscore_percent_anticipation',
                                 'signature_zscore_percent_disgust', 'signature_zscore_percent_fear',
                                 'signature_zscore_percent_joy', 'signature_zscore_percent_sadness',
                                 'signature_zscore_percent_surprise', 'signature_zscore_percent_trust']]
    data = relevant_data.values
    return data

# Get TSNE values that we got it.
def TSNE_values(df_0):
    # TSNE dimensions from the data "final_Collection.csv" we got.
    d_tsne1 = df_0.loc[:, ['tsne_glyph.x', 'tsne_glyph.y']]
    d_tsne = d_tsne1.values
    return d_tsne

# Employing the SOM algorithm. Return the predictions.
def SOM_algorithm(data):
    som = SOM(m=8, n=1, dim=8, random_state=1234)
    som.fit(data)
    predictions = som.predict(data)
    print(predictions)
    return predictions

# Employing the TSNE algorithm ON the new data we export.
def TSNE_algorithm(data):
    tsne = TSNE(n_components=2, init='random')
    X_2d = tsne.fit_transform(data)
    return X_2d

# Export the predictions appropriate data to CSV
def export_to_CSV(df_0,predictions):
    # Export the data to new CSV.
    df_1 = df_0.loc[:, ['_id','movie_directors','movie_genres','movie_rating','movie_stars',
                        'movie_writers','name','plot','poster','release_year','reviews_num',
                        'titleId','tsne_glyph.x','tsne_glyph.y',
                        'signature_zscore_percent_anger', 'signature_zscore_percent_anticipation',
                        'signature_zscore_percent_disgust', 'signature_zscore_percent_fear',
                        'signature_zscore_percent_joy', 'signature_zscore_percent_sadness',
                        'signature_zscore_percent_surprise', 'signature_zscore_percent_trust'
                        ]]
    df_1['cluster_1'] = predictions
    df_1.to_csv("../Data/new_data_cluster.csv")

def create_fig(d_tsne, predictions):
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(30, 40))
    x = d_tsne[:, 0]
    y = d_tsne[:, 1]
    # x2 = X_2d[:,0]
    # y2= X_2d[:,1]
    colors = ['red', 'green', 'blue', 'brown', 'pink', 'orange', 'purple', 'yellow']

    ax[0].scatter(x, y, c=predictions, cmap=ListedColormap(colors))
    ax[0].title.set_text('SOM- OLD TSNE')
    ax[1].scatter(x, y, c=predictions, cmap=ListedColormap(colors))
    ax[1].title.set_text('SOM- OUR TESNE')
    plt.savefig('cluster.png')

df_0=load_data("../Data/new_data_percent.csv")
data = get_relevant_values(df_0)
d_tsne= TSNE_values(df_0)
predictions= SOM_algorithm(data)
export_to_CSV(df_0, predictions)


