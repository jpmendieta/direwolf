# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:57:51 2015

@author: jp
"""

# Read yelp.csv into a DataFrame.
import pandas as pd
yelp = pd.read_csv('yelp.csv')
yelp.head(1)
# Create a new DataFrame that only contains the 5-star and 1-star reviews.
yelp_filtered = yelp[(yelp.stars == 1) | (yelp.stars == 5)]
yelp_filtered['stars'] = yelp_filtered.stars.map({1:0, 5:1})
# Split the new DataFrame into training and testing sets, using the review text as the only feature 
# and the star rating as the response.
from sklearn.cross_validation import train_test_split
 
X = yelp_filtered.text
y = yelp_filtered.stars
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Use CountVectorizer to create document-term matrices from X_train and X_test.
# Hint: If you run into a decoding error, instantiate the vectorizer with the argument decode_error='ignore'.
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect.fit(X_train)
vect.get_feature_names()
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)
X_train_tokens = vect.get_feature_names()

# Use Naive Bayes to predict the star rating for reviews in the testing set, and calculate the accuracy.
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)
y_pred_class = nb.predict(X_test_dtm)
nb_accuracy = metrics.accuracy_score(y_test, y_pred_class) #0.918

# Calculate the AUC.
# Hint 1: Make sure to pass the predicted probabilities to roc_auc_score, not the predicted classes.
# Hint 2: roc_auc_score will get confused if y_test contains fives and ones, so you will need to create a 
# new object that contains ones and zeros instead.
y_pred_prob = nb.predict_proba(X_test_dtm)[:, 1]
auc = metrics.roc_auc_score(y_test, y_pred_prob) #.940

# Plot the ROC curve.
import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

# Print the confusion matrix, and calculate the sensitivity and specificity. Comment on the results.
print metrics.confusion_matrix(y_test, y_pred_class)
# sensitivity: TP/Actual Yes
#specificity: TN/Actual No
sensitivity = 813/float(813+25) #0.97
specificity = 126/float(126+58) #0.68

#Sensitivity is higher than specificity

# Browse through the review text for some of the false positives and false negatives. 
# Based on your knowledge of how Naive Bayes works, do you have any theories about why 
# the model is incorrectly classifying these reviews?

#false positives
X_test[y_test < y_pred_class]
#false negatives
X_test[y_test > y_pred_class]
# These reviews are pretty long, which I think might be causing the model to incorrectly classifying them.  
# The longer a review, the more opportunity for ambiguity.

df = pd.DataFrame({'probability':y_pred_prob, 'actual':y_test})
df.hist(column='probability', by='actual', sharex=True, sharey=True)