import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import mplleaflet as leaf

df = pd.read_csv('copacabana_lat_lng.csv')

plt.scatter(df['lng'], df['lat'], marker='.')

leaf.show()


