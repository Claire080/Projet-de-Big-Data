import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    data = pd.read_csv('out20.csv', usecols=['id', 'symbols', 'company_names', 'commentaires', 'impressions'])
except Exception as e:
    print(f"Erreur lors de la lecture du fichier CSV : {str(e)}")
    exit()
    
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Fonction pour nettoyer et analyser les sentiments
def analyze_sentiments(comment):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(comment)['compound']

    if sentiment_score >= 0.05:
        sentiment_category = "positif"
    elif sentiment_score <= -0.05:
        sentiment_category = "negatif"
    else:
        sentiment_category = "neutre"

    return sentiment_score, sentiment_category

data[['impressions', 'sentiment_category']] = data['commentaires'].apply(analyze_sentiments).apply(pd.Series)

try:
    data.to_csv('out20_with_sentiments.csv', index=False)
    print("Les scores de sentiment ont été ajoutés et le fichier a été enregistré avec succès.")
except Exception as e:
    print(f"Erreur lors de l'enregistrement du fichier CSV : {str(e)}")