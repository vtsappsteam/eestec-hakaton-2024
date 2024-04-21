
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import pandas as pd


stop_words = set(stopwords.words('english'))

def cleanText(text):
    cleaned_text = re.sub(r'\([^)]*\)', '', text)
    words = cleaned_text.split()
    cleaned_text = [word for word in words if word.lower() not in stop_words]
    cleaned_text = ' '.join(cleaned_text)
    cleaned_text = cleaned_text.replace('[', '').replace(']', '').replace("'", "").replace(",", "").replace("Im", "")
    return cleaned_text

def wordCloudImage(text):
    text = cleanText(text)
    # Create and generate a word cloud image:
    wordcloud = WordCloud(background_color='white', collocations=True,width=750,height=750).generate(text)
    # Display the generated image:
    wordcloud_image = wordcloud.to_image()
    return wordcloud_image