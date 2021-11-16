import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Import the streamlit Python module.
import streamlit as st
# Configure your home page.

# Set the title to the home page contents.
st.set_page_config(page_title='Census Visualisation Web App',page_icon=':random:',layout='centered',initial_sidebar_state='auto')
# Provide a brief description for the web app.
st.subheader('''This web app allows a user to predict the prices of a car 
based on their engine size, horse power, dimensions and the drive wheel type parameters''')

st.header('View Data')
# Add an expander and display the dataset as a static table within the expander.
with st.beta_expander('View DataSet'):
   st.table(census_df)

# Create three beta_columns.
beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
# Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
with beta_col1:
      if st.checkbox('Show all column names'):
        st.table(list(census_df.columns))

# Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
with beta_col2:
  if st.checkbox("View column data type"):
    st.table(census_df.dtypes)

# Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
with beta_col2:
      if st.checkbox('View column data'):
        column_data = st.selectbox('Select Column',('native-country','workclass','occupation'))
        if column_data == 'native-country':
          st.write(census_df['native-country'])
        elif column_data == 'workclass':
          st.write(census_df['workclass'])
        elif column_data =='occupation':
          st.write(census_df['occupation'])

# Display summary of the dataset on the click of checkbox.
if st.checkbox('Show summary'):
  st.table(census_df.describe())