import pandas as pd
import matplotlib.pyplot as plt


try:
    data = pd.read_csv('out20_with_sentiments.csv', usecols=['id', 'symbols', 'company_names', 'commentaires', 'impressions', 'sentiment_category'])
except Exception as e:
    print(f"Erreur lors de la lecture du fichier CSV : {str(e)}")
    exit()

# Vérifier les catégories disponibles
sentiment_categories = data['sentiment_category'].unique()

# Définir les couleurs pour chaque catégorie
colors = {'positif': 'green', 'negatif': 'red', 'neutre': 'gray'}

plt.bar(sentiment_categories, data['sentiment_category'].value_counts(), color=[colors[cat] for cat in sentiment_categories])
plt.title('Distribution of Sentiment Categories')
plt.xlabel('Sentiment Category')
plt.ylabel('Number of Comments')
plt.show()
plt.savefig('/app/graph.png')