import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df=pd.read_csv('./brain_stroke.csv')
 

st.sidebar.header("Specify Input Parameters")
age = st.sidebar.slider('Age', min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=(int(df['age'].min()),int(df['age'].max())))
gender = st.sidebar.selectbox('Gender', ['Both', 'Male', 'Female'])
smoking_status = st.sidebar.multiselect('Smoking Status', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
hypertension = st.sidebar.selectbox('Hypertension', ['Both', 0, 1])
ever_married = st.sidebar.selectbox('Marital Status', ['Both', 'Yes', 'No'])
work_type = st.sidebar.multiselect('Work Type', df['work_type'].unique().tolist())
residence_type = st.sidebar.selectbox('Residence Type', ['Both', 'Urban', 'Rural'])
stroke = st.sidebar.selectbox('Stroke Cases', ['All', 'Stroke', 'No Stroke'])

filtered_df = df[(df['age'] >= age[0]) & (df['age'] <= age[1])]
if gender != 'Both':
    filtered_df = filtered_df[filtered_df['gender'] == gender]
if smoking_status:
    filtered_df = filtered_df[filtered_df['smoking_status'].isin(smoking_status)]
if hypertension != 'Both':
    filtered_df = filtered_df[filtered_df['hypertension'] == hypertension]
if ever_married != 'Both':
    filtered_df = filtered_df[filtered_df['ever_married'] == ever_married]
if work_type:
    filtered_df = filtered_df[filtered_df['work_type'].isin(work_type)]
if residence_type != 'Both':
    filtered_df = filtered_df[filtered_df['Residence_type'] == residence_type]
if stroke != 'All':
    stroke_map = {'Stroke': 1, 'No Stroke': 0}
    filtered_df = filtered_df[filtered_df['stroke'] == stroke_map[stroke]]

st.title("Brain Strokes Data Analysis")

st.subheader("Gender and Stroke")
gender_stroke_counts = filtered_df.groupby('gender')['stroke'].value_counts().unstack().fillna(0)
gender_stroke_proportions = gender_stroke_counts.div(gender_stroke_counts.sum(axis=1), axis=0)
fig_gender_stroke, ax_gender_stroke = plt.subplots()
gender_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_gender_stroke)
ax_gender_stroke.set_xlabel('Gender')
ax_gender_stroke.set_ylabel('Count')
ax_gender_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_gender_stroke)
st.write("Count Chart: Gender and Stroke")
st.write("Count Values:")
st.write(gender_stroke_counts)

st.subheader("Proportional Chart: Gender and Stroke")
fig_gender_stroke_prop, ax_gender_stroke_prop = plt.subplots()
gender_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_gender_stroke_prop, legend=False)
ax_gender_stroke_prop.set_xlabel('Gender')
ax_gender_stroke_prop.set_ylabel('Proportion')
ax_gender_stroke_prop.set_ylim([0, 1])
ax_gender_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_gender_stroke_prop)
st.write("Proportional Values:")
st.write(gender_stroke_proportions)

st.subheader("Age and Stroke")
fig_age_stroke, ax_age_stroke = plt.subplots()
sns.boxplot(x='stroke', y='age', data=filtered_df, ax=ax_age_stroke)
ax_age_stroke.set_xlabel('Stroke')
ax_age_stroke.set_ylabel('Age')
st.pyplot(fig_age_stroke)

st.subheader("Hypertension and Stroke")
hypertension_stroke_counts = filtered_df.groupby('hypertension')['stroke'].value_counts().unstack().fillna(0)
hypertension_stroke_proportions = hypertension_stroke_counts.div(hypertension_stroke_counts.sum(axis=1), axis=0)
fig_hypertension_stroke, ax_hypertension_stroke = plt.subplots()
hypertension_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_hypertension_stroke)
ax_hypertension_stroke.set_xlabel('Hypertension')
ax_hypertension_stroke.set_ylabel('Count')
ax_hypertension_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_hypertension_stroke)
st.write("Count Chart: Hypertension and Stroke")
st.write("Count Values:")
st.write(hypertension_stroke_counts)

st.subheader("Proportional Chart: Hypertension and Stroke")
fig_hypertension_stroke_prop, ax_hypertension_stroke_prop = plt.subplots()
hypertension_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_hypertension_stroke_prop, legend=False)
ax_hypertension_stroke_prop.set_xlabel('Hypertension')
ax_hypertension_stroke_prop.set_ylabel('Proportion')
ax_hypertension_stroke_prop.set_ylim([0, 1])
ax_hypertension_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_hypertension_stroke_prop)
st.write("Proportional Values:")
st.write(hypertension_stroke_proportions)

# Repeat the same pattern for the remaining charts

st.subheader("Marital Status and Stroke")
marital_status_stroke_counts = filtered_df.groupby('ever_married')['stroke'].value_counts().unstack().fillna(0)
marital_status_stroke_proportions = marital_status_stroke_counts.div(marital_status_stroke_counts.sum(axis=1), axis=0)
fig_marital_status_stroke, ax_marital_status_stroke = plt.subplots()
marital_status_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_marital_status_stroke)
ax_marital_status_stroke.set_xlabel('Marital Status')
ax_marital_status_stroke.set_ylabel('Count')
ax_marital_status_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_marital_status_stroke)
st.write("Count Chart: Marital Status and Stroke")
st.write("Count Values:")
st.write(marital_status_stroke_counts)

st.subheader("Proportional Chart: Marital Status and Stroke")
fig_marital_status_stroke_prop, ax_marital_status_stroke_prop = plt.subplots()
marital_status_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_marital_status_stroke_prop, legend=False)
ax_marital_status_stroke_prop.set_xlabel('Marital Status')
ax_marital_status_stroke_prop.set_ylabel('Proportion')
ax_marital_status_stroke_prop.set_ylim([0, 1])
ax_marital_status_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_marital_status_stroke_prop)
st.write("Proportional Values:")
st.write(marital_status_stroke_proportions)

# Repeat the same pattern for the remaining charts

st.subheader("Work Type and Stroke")
work_type_stroke_counts = filtered_df.groupby('work_type')['stroke'].value_counts().unstack().fillna(0)
work_type_stroke_proportions = work_type_stroke_counts.div(work_type_stroke_counts.sum(axis=1), axis=0)
fig_work_type_stroke, ax_work_type_stroke = plt.subplots()
work_type_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_work_type_stroke)
ax_work_type_stroke.set_xlabel('Work Type')
ax_work_type_stroke.set_ylabel('Count')
ax_work_type_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_work_type_stroke)
st.write("Count Chart: Work Type and Stroke")
st.write("Count Values:")
st.write(work_type_stroke_counts)

st.subheader("Proportional Chart: Work Type and Stroke")
fig_work_type_stroke_prop, ax_work_type_stroke_prop = plt.subplots()
work_type_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_work_type_stroke_prop, legend=False)
ax_work_type_stroke_prop.set_xlabel('Work Type')
ax_work_type_stroke_prop.set_ylabel('Proportion')
ax_work_type_stroke_prop.set_ylim([0, 1])
ax_work_type_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_work_type_stroke_prop)
st.write("Proportional Values:")
st.write(work_type_stroke_proportions)

# Repeat the same pattern for the remaining charts

st.subheader("Residence Type and Stroke")
residence_type_stroke_counts = filtered_df.groupby('Residence_type')['stroke'].value_counts().unstack().fillna(0)
residence_type_stroke_proportions = residence_type_stroke_counts.div(residence_type_stroke_counts.sum(axis=1), axis=0)
fig_residence_type_stroke, ax_residence_type_stroke = plt.subplots()
residence_type_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_residence_type_stroke)
ax_residence_type_stroke.set_xlabel('Residence Type')
ax_residence_type_stroke.set_ylabel('Count')
ax_residence_type_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_residence_type_stroke)
st.write("Count Chart: Residence Type and Stroke")
st.write("Count Values:")
st.write(residence_type_stroke_counts)

st.subheader("Proportional Chart: Residence Type and Stroke")
fig_residence_type_stroke_prop, ax_residence_type_stroke_prop = plt.subplots()
residence_type_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_residence_type_stroke_prop, legend=False)
ax_residence_type_stroke_prop.set_xlabel('Residence Type')
ax_residence_type_stroke_prop.set_ylabel('Proportion')
ax_residence_type_stroke_prop.set_ylim([0, 1])
ax_residence_type_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_residence_type_stroke_prop)
st.write("Proportional Values:")
st.write(residence_type_stroke_proportions)

# Repeat the same pattern for the remaining charts

st.subheader("Smoking Status and Stroke")
smoking_status_stroke_counts = filtered_df.groupby('smoking_status')['stroke'].value_counts().unstack().fillna(0)
smoking_status_stroke_proportions = smoking_status_stroke_counts.div(smoking_status_stroke_counts.sum(axis=1), axis=0)
fig_smoking_status_stroke, ax_smoking_status_stroke = plt.subplots()
smoking_status_stroke_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_smoking_status_stroke)
ax_smoking_status_stroke.set_xlabel('Smoking Status')
ax_smoking_status_stroke.set_ylabel('Count')
ax_smoking_status_stroke.legend(['No Stroke', 'Stroke'], loc='upper right')
st.pyplot(fig_smoking_status_stroke)
st.write("Count Chart: Smoking Status and Stroke")
st.write("Count Values:")
st.write(smoking_status_stroke_counts)

st.subheader("Proportional Chart: Smoking Status and Stroke")
fig_smoking_status_stroke_prop, ax_smoking_status_stroke_prop = plt.subplots()
smoking_status_stroke_proportions.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax_smoking_status_stroke_prop, legend=False)
ax_smoking_status_stroke_prop.set_xlabel('Smoking Status')
ax_smoking_status_stroke_prop.set_ylabel('Proportion')
ax_smoking_status_stroke_prop.set_ylim([0, 1])
ax_smoking_status_stroke_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_smoking_status_stroke_prop)
st.write("Proportional Values:")
st.write(smoking_status_stroke_proportions)

st.subheader("Stroke Cases")
stroke_counts = filtered_df['stroke'].value_counts()
fig_stroke_cases, ax_stroke_cases = plt.subplots()
stroke_counts.plot(kind='bar', color=['skyblue', 'salmon'], ax=ax_stroke_cases)
ax_stroke_cases.set_xlabel('Stroke')
ax_stroke_cases.set_ylabel('Count')
ax_stroke_cases.set_xticklabels(['No Stroke', 'Stroke'])
st.pyplot(fig_stroke_cases)
st.write("Count Values:")
st.write(stroke_counts)

st.subheader("Proportional Chart: Stroke Cases")
stroke_proportions = stroke_counts / stroke_counts.sum()
fig_stroke_cases_prop, ax_stroke_cases_prop = plt.subplots()
stroke_proportions.plot(kind='bar', color=['skyblue', 'salmon'], ax=ax_stroke_cases_prop, legend=False)
ax_stroke_cases_prop.set_xlabel('Stroke')
ax_stroke_cases_prop.set_ylabel('Proportion')
ax_stroke_cases_prop.set_ylim([0, 1])
ax_stroke_cases_prop.set_xticklabels(['No Stroke', 'Stroke'])
ax_stroke_cases_prop.legend(['No Stroke', 'Stroke'], bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig_stroke_cases_prop)
st.write("Proportional Values:")
st.write(stroke_proportions)
