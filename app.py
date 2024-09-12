import streamlit as st
import pandas as pd
import plotly.express as px

vehicle_df = pd.read_csv('vehicles_us.csv')

# Add a header
st.header("Exploratory Data Analysis")

#Since I only want the make of a vehicle and not the model, I am going to filter out the model column that truly only contains the make--not including the model
make_vehicle = vehicle_df.copy()
make_vehicle['model'] = make_vehicle['model'].str.split().str[0]

#For this problem, we only care about the model and transmission columns so we should keep only these columns
make_vehicle = make_vehicle[['model', 'transmission']]

#In addition, we only care about manual transmissions so
make_vehicle = make_vehicle[make_vehicle['transmission'] == 'manual']

#Now we check to see which models offer the most amount of manual transmissions
grouped_make = make_vehicle.groupby('model').value_counts().sort_values(ascending=False)

#Create histogram
fig_histogram = px.histogram(make_vehicle, x='model', title='The Number of Manual Transmission Offered by Makers of Vehicles', labels={'model': 'Car Model', 'count': 'Number of Available Manual Transmissions'})

#Turning our grouped series into a dataframe so I can use the indexes as axes on the scatterplot
grouped_make_df = grouped_make.reset_index(name='manuals_offered')
fig_scatter = px.scatter(grouped_make_df, x='model', y='manuals_offered', labels={'model': 'Car Make', 'manuals_offered': 'Available Manual Transmissions'}, title="The Number of Available Transmissions that Car Makes Provide")


# Add a checkbox to show/hide the histogram
show_histogram = st.checkbox('Show Histogram')

# Show the histogram if the checkbox is selected
if show_histogram:
    st.plotly_chart(fig_histogram)

# Show the scatter plot by default
st.plotly_chart(fig_scatter)
