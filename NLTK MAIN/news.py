import copy
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold
from imblearn.over_sampling import SMOTE
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns

import json
import re

titles = []
categories = []

with open('News_Category_Dataset_v3.json', 'r', encoding='utf-8') as json_file:
    for line in json_file:
        try:
            entry = json.loads(line)
            if len(entry) >= 3 and entry['category'] in ['POLITICS', 'ENTERTAINMENT', 'SPORTS', 'BUSINESS', 'HEALTHY LIVING']:
                title = entry['headline'].lower()
                title = title.strip()
                title = re.sub(r'\W+', ' ', title)  # Remove non-word characters
                titles.append(title)
                categories.append(entry['category'])
        except json.JSONDecodeError:
            print(f"Error decoding JSON in line: {line}")

print("Titles:\n", "\n".join(titles))
print("\nCategories:\n", "\n".join(categories))

title_tr, title_te, category_tr, category_te = train_test_split(titles,categories)
title_tr, title_de, category_tr, category_de = train_test_split(title_tr,category_tr)
print("Training: ",len(title_tr))
print("Developement: ",len(title_de),)
print("Testing: ",len(title_te))

from wordcloud import WordCloud
text = " ".join(title_tr)
wordcloud = WordCloud().generate(text)
plt.figure()
plt.subplots(figsize=(20,12))
wordcloud = WordCloud(
    background_color="white",
    max_words=len(text),
    max_font_size=40,
    relative_scaling=.5).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

tokenizer = nltk.tokenize.RegexpTokenizer(r"\w+")
stop_words = nltk.corpus.stopwords.words("english")
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize, stop_words=stop_words)

vectorizer.fit(iter(title_tr))
Xtr = vectorizer.transform(iter(title_tr))
Xde = vectorizer.transform(iter(title_de))
Xte = vectorizer.transform(iter(title_te))

encoder = LabelEncoder()
encoder.fit(category_tr)
Ytr = encoder.transform(category_tr)
Yde = encoder.transform(category_de)
Yte = encoder.transform(category_te)

reverse_vocabulary = {}
vocabulary = vectorizer.vocabulary_
for word in vocabulary:
    index = vocabulary[word]
    reverse_vocabulary[index] = word

vector = vectorizer.transform(iter(['Nasa scientists are good']))
indexes = vector.indices
for i in indexes:
    print (reverse_vocabulary[i])

print("Number of features before reduction : ", Xtr.shape[1])
selection = VarianceThreshold(threshold=0.001)
Xtr_whole = copy.deepcopy(Xtr)
Ytr_whole = copy.deepcopy(Ytr)
selection.fit(Xtr)
Xtr = selection.transform(Xtr)
Xde = selection.transform(Xde)
Xte = selection.transform(Xte)
print("Number of features after reduction : ", Xtr.shape[1])

labels = list(set(Ytr))
counts = []
for label in labels:
    counts.append(np.count_nonzero(Ytr == label))
plt.pie(counts, labels=labels, autopct='%1.1f%%')
plt.show()

from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import numpy as np

# Assuming Xtr and Ytr are already defined and contain your data

sm = SMOTE(random_state=42)
Xtr_resampled, Ytr_resampled = sm.fit_resample(Xtr, Ytr)

labels = list(set(Ytr_resampled))
counts = [np.count_nonzero(Ytr_resampled == label) for label in labels]

plt.figure(figsize=(8, 8))  # Adjust the figure size as needed
plt.pie(counts, labels=labels, autopct='%1.1f%%')
plt.title('Class Distribution After SMOTE')
plt.show()

dc = DummyClassifier(strategy="stratified")
dc.fit(Xtr, Ytr)
pred = dc.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

dt = DecisionTreeClassifier()
dt.fit(Xtr, Ytr)
pred = dt.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

rf = RandomForestClassifier(n_estimators=40)
rf.fit(Xtr, Ytr)
pred = rf.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

nb = MultinomialNB()
nb.fit(Xtr, Ytr)
pred = nb.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

from sklearn.svm import SVC
svc = SVC()
svc.fit(Xtr, Ytr)
pred = svc.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

mlp = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100, 20), random_state=1, max_iter=400)
mlp.fit(Xtr, Ytr)
pred = mlp.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

pred = nb.predict(Xte)
print(classification_report(Yte, pred, target_names=encoder.classes_))
sns.heatmap(confusion_matrix(Yte, pred))

from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Assuming reverse_vocabulary is defined correctly

nb1 = MultinomialNB()
nb1.fit(Xtr_whole, Ytr_whole)

# Exponentiate the coefficients to interpret them as probabilities
coefs = np.exp(nb1.feature_log_prob_)

target_names = encoder.classes_

for i in range(len(target_names)):
    words = []
    for j in coefs[i].argsort():
        words.append(reverse_vocabulary[j])
    print(target_names[i], '-', words, "\n")

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Assuming reverse_vocabulary is defined correctly

# Initialize CountVectorizer
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize, stop_words=stop_words)

# Fit and transform training data
Xtr_transformed = vectorizer.fit_transform(title_tr)
Xte_transformed = vectorizer.transform(title_te)

# Train Multinomial Naive Bayes classifier
nb1 = MultinomialNB()
nb1.fit(Xtr_transformed, Ytr)

# Calculate accuracy on test data
pred = nb1.predict(Xte_transformed)
accuracy = np.mean(pred == Yte)
print('Accuracy:', accuracy)

# Assuming reverse_vocabulary, tokenizer, stop_words, vectorizer, and nb1 are defined as in your previous code

# Example input data (replace this with your actual input data)
new_titles = [
    "Bitcoin is going off",
    "Donald Trump is going to hell",
    "dj",
    "football",
    "businesses"
]

# Transform the new titles using the CountVectorizer
X_new_transformed = vectorizer.transform(new_titles)

# Make predictions using the trained Multinomial Naive Bayes classifier
predictions = nb1.predict(X_new_transformed)

# Print the predicted categories for each new title
for title, prediction in zip(new_titles, predictions):
    print(f'Title: {title} | Predicted Category: {encoder.classes_[prediction]}')


    
# Pickle
import os
import sys
import pickle

projectabspathname = os.path.abspath('news_pickle.pickle')
print(projectabspathname)
projectname = 'news.ipynb'
projectpickle = open(str(projectabspathname),'wb')
pickle.dump(projectname, projectpickle)
projectpickle.close()