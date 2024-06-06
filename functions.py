#Importing relevant libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
%matplotlib inline

import warnings
warnings.filterwarnings("ignore")

import xgboost as xgb
import joblib
import pickle

#sklearn preprocessing
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler, LabelEncoder ,OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline

from sklearn.feature_selection import RFECV

# sklearn classification models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier

from imblearn.over_sampling import SMOTE

#sklearn evaluation metrics and validation
from sklearn.model_selection import train_test_split, KFold,StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score,roc_curve, auc
from sklearn.metrics import roc_auc_score,confusion_matrix, classification_report

from sklearn.compose import ColumnTransformer

import functions as f


# Function to print the shape of the DataFrame
def data_shape(churn_data):
    print("Data Shape:")
    print(f"Number of Rows: {churn_data.shape[0]}")
    print(f"Number of Columns: {churn_data.shape[1]}\n")

# Function to display information about the data
def data_info(churn_data):
    print("Data Information:")
    print(churn_data.info())

# Function to check for missing values
def missing_data(churn_data):
    print("\nMissing Values:")
    print(churn_data.isnull().sum())
# Function to identify and display duplicate rows
def duplicates(churn_data):
    duplicates = churn_data[churn_data.duplicated()]
    print("\nDuplicate Rows:")
    print(duplicates)
# Function to display descriptive statistics of numerical columns
def data_description(churn_data):
    print("\nDescriptive Statistics:")
    print(churn_data.describe())
# Function to explore the dataset
def explore_dataset(churn_data):
    data_shape(churn_data)
    data_info(churn_data)
    missing_data(churn_data)
    duplicates(churn_data)
    data_description(churn_data)
