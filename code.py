# --------------
# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report,confusion_matrix
import warnings
warnings.filterwarnings("ignore")

# Load the data
#Loading the Spam data from the path variable for the mini challenge
#Target variable is the 57 column i.e spam, non-spam classes 
df = pd.read_csv(path)

# Overview of the data



#Dividing the dataset set in train and test set and apply base logistic model


# Calculate accuracy , print out the Classification report and Confusion Matrix.


# Copy df in new variable df1


# Remove Correlated features above 0.75 and then apply logistic model


# Split the new subset of data and fit the logistic model on training data


# Calculate accuracy , print out the Classification report and Confusion Matrix for new data


# Apply Chi Square and fit the logistic model on train data use df dataset



# Calculate accuracy , print out the Confusion Matrix 


# Apply Anova and fit the logistic model on train data use df dataset



# Calculate accuracy , print out the Confusion Matrix 


# Apply PCA and fit the logistic model on train data use df dataset

   

# Calculate accuracy , print out the Confusion Matrix 


# Compare observed value and Predicted value




