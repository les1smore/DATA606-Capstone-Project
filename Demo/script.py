#pip install streamlit
#pip install pandas
#pip install sklearn


# IMPORT STATEMENTS
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
from xgboost import XGBClassifier 


df = pd.read_csv('/Users/leslie/Desktop/DATA606/data_nonull.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

# BACKGROUND
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/Users/leslie/Desktop/DATA606/app_background.jpg')   

# HEADINGS
st.title('Diabetes Checkup')
st.sidebar.header('User Data')
st.subheader('Training Data Stats')
st.write(df.describe())


# X AND Y DATA
x = df.drop(['Have_Diabetes'], axis = 1)
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x,y, stratify=y, test_size = 0.3, random_state = 142)


# FUNCTION
def user_report():
  pre_diabetic = st.sidebar.slider('Pre-diabetic', 0,9,2)
  take_insulin = st.sidebar.slider('Taking Insulin', 0,9,1)
  blood_pressure = st.sidebar.slider('High Blood Pressure', 0,1, 1)
  bmi = st.sidebar.slider('BMI Category', 1,4, 1) 
  age = st.sidebar.slider('Age', 1,13, 1)
  good_health = st.sidebar.slider('Good Health', 0,1,1)
  routine_checkup = st.sidebar.slider('Routine Check-up', 0,9,1)
  high_cholesterol = st.sidebar.slider('High Cholesterol', 0,1, 1)
  income = st.sidebar.slider('Income Category', 1,5,1)
  chd_mi = st.sidebar.slider('CHD-MI', 0,1, 1)
  kidney_disease = st.sidebar.slider('Kidney Disease', 0,1,1)
  race = st.sidebar.slider('Race/Ethnicity', 1,8,1)
  bp_meds = st.sidebar.slider('Taking BP Meds', 0,1,1)
  heavydrinker = st.sidebar.slider('Heavy Drinker', 0,1,1)
  


  user_report_data = {
      'Pre-diabetic':pre_diabetic,
      'Taking Insulin':take_insulin,
      'High Blood Pressure':blood_pressure,
      'BMI Category':bmi,
      'Age':age,
      'Good Health':good_health,
      'Routine Check-up':routine_checkup,
      'High Cholesterol':high_cholesterol,
      'Income Category':income,
      'CHD-MI':chd_mi,
      'Kidney Disease':kidney_disease,
      'Race/Ethnicity':race,
      'Taking BP Meds':bp_meds,
      'Heavy Drinker': heavydrinker
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data




# PATIENT DATA
user_data = user_report()
st.subheader('User Data')
st.write(user_data)




# MODEL
class_size = df['Have_Diabetes'].value_counts()
scale_pos_weight = class_size[0]/class_size[1] # total negative examples / total positive examples

xgb_tuned = XGBClassifier(min_child_weight = 1,
                             max_depth=1,
                             n_estimators=152, 
                             scale_pos_weight = scale_pos_weight)  # Handle the class imbalance

xgb_tuned.fit(x_train, y_train)
user_result = xgb_tuned.predict(x_test, ntree_limit=np.argmax(xgb_tuned.predict_proba(x_test)[:,1] >= 0.3661))


# VISUALISATIONS
st.title('Visualized User Report')



# COLOR FUNCTION
if user_result[0]==0:
  color = 'blue'
else:
  color = 'red'


# Age vs High Blood Pressure
st.header('High Blood Pressure (Others vs Yours)')
fig_bp = plt.figure()
ax1 = sns.scatterplot(x = 'Age', y = 'High Blood Pressure', data = df, hue = 'Have_Diabetes', palette = 'Greens')
ax2 = sns.scatterplot(x = user_data['Age'], y = user_data['High Blood Pressure'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,20,2))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_bp)



# Age vs BMI Category
st.header('BMI Category (Others vs Yours)')
fig_bmi = plt.figure()
ax3 = sns.scatterplot(x = 'Age', y = 'BMI Category', data = df, hue = 'Have_Diabetes' , palette='magma')
ax4 = sns.scatterplot(x = user_data['Age'], y = user_data['BMI Category'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,220,10))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_bmi)



# Age vs Taking Insulin
st.header('Taking Insulin (Others vs Yours)')
fig_insulin = plt.figure()
ax5 = sns.scatterplot(x = 'Age', y = 'Taking Insulin', data = df, hue = 'Have_Diabetes', palette='Reds')
ax6 = sns.scatterplot(x = user_data['Age'], y = user_data['Taking Insulin'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,130,10))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_insulin)


# Age vs Routine Check-up
st.header('Routine Check-up (Others vs Yours)')
fig_checkup = plt.figure()
ax7 = sns.scatterplot(x = 'Age', y = 'Routine Check-up', data = df, hue = 'Have_Diabetes', palette='Blues')
ax8 = sns.scatterplot(x = user_data['Age'], y = user_data['Routine Check-up'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,110,10))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_checkup)


# Age vs High Cholesterol
st.header('High Cholesterol (Others vs Yours)')
fig_chol = plt.figure()
ax9 = sns.scatterplot(x = 'Age', y = 'High Cholesterol', data = df, hue = 'Have_Diabetes', palette='rocket')
ax10 = sns.scatterplot(x = user_data['Age'], y = user_data['High Cholesterol'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,900,50))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_chol)


# Age vs CHD-MI
st.header('Coronary Heart Disease (Others vs Yours)')
fig_chd = plt.figure()
ax11 = sns.scatterplot(x = 'Age', y = 'CHD-MI', data = df, hue = 'Have_Diabetes', palette='rainbow')
ax12 = sns.scatterplot(x = user_data['Age'], y = user_data['CHD-MI'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,70,5))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_chd)


# Age vs Kidney Disease
st.header('Kidney Disease (Others vs Yours)')
fig_kid = plt.figure()
ax13 = sns.scatterplot(x = 'Age', y = 'Kidney Disease', data = df, hue = 'Have_Diabetes', palette='YlOrBr')
ax14 = sns.scatterplot(x = user_data['Age'], y = user_data['Kidney Disease'], s = 150, color = color)
#plt.xticks(np.arange(10,100,5))
#plt.yticks(np.arange(0,3,0.2))
plt.title('0 - No Diabetes & 1 - Have Diabetes')
st.pyplot(fig_kid)



# OUTPUT
st.subheader('Your Report: ')
output=''
if user_result[0]==1:
  output = 'You are at high risk for diabetes.'
else:
  output = 'You are at low risk for diabetes.'
st.title(output)
st.subheader('Accuracy: ')
st.write(str(round(accuracy_score(y_test, user_result),2)*100)+'%')
st.subheader('Recall: ')
st.write(str(round(recall_score(y_test, user_result),2)*100)+'%')
st.subheader('F1 Score: ')
st.write(str(round(f1_score(y_test, user_result),1)*100)+'%')
st.subheader('Precision: ')
st.write(str(round(precision_score(y_test, user_result),2)*100)+'%')



