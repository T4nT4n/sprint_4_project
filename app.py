import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

#Reading the CSV file
vehicle_df = pd.read_csv('vehicles_us.csv')

# Adding a header
st.header("Exploratory Data Analysis")

#Formatting the CSV File

#Let's fill the null values of the model year column with zero and convert to integer type
vehicle_df['model_year'] = vehicle_df['model_year'].fillna(0).astype(int)

#Let's fill the null values of the cylinders column with zero
vehicle_df['cylinders'] = vehicle_df['cylinders'].fillna(0).astype(int)

#Let's fill the null values of the odometer column with -1
vehicle_df['odometer'] = vehicle_df['odometer'].fillna(-1)

#Let's fill in the null values within the paint color column to be filled in with "unknown"
vehicle_df['paint_color'] = vehicle_df['paint_color'].fillna('unknown')

#Let's fill in the null values in the 4wd column with 0. 1 represents True and 0 respresents False
vehicle_df['is_4wd'] = vehicle_df['is_4wd'].fillna(0).astype(int)

#Let's convert the date_posted column into datetime type
vehicle_df['date_posted'] = pd.to_datetime(vehicle_df['date_posted'])

#Dataframe for the Historgram

#We filter out the models of the cars, and keeping solely the make of the car
make_vehicle = vehicle_df[['model', 'transmission']].copy()
make_vehicle['model'] = make_vehicle['model'].str.split().str[0]

#Create histogram
fig_histogram = px.histogram(make_vehicle, x='model', title='The Number of Manual Transmission Offered by Makers of Vehicles', labels={'model': 'Car Model', 'count': 'Number of Available Manual Transmissions'})

#Dataframe for the Scatter plot

#Now we are going to group by the model of the vehicle and count the number of occurence that appear in the model index
grouped_make = make_vehicle[make_vehicle['transmission'] == 'manual'].groupby('model').size().sort_values(ascending=False)

#Turning our grouped series into a dataframe so I can use the indexes as axes on the scatterplot
grouped_make_df = grouped_make.reset_index(name='manuals_offered')
fig_scatter = px.scatter(grouped_make_df, x='model', y='manuals_offered', labels={'model': 'Car Make', 'manuals_offered': 'Available Manual Transmissions'})

# Add a checkbox to show/hide the histogram
show_histogram = st.checkbox('Show Histogram')

# Show the histogram if the checkbox is selected
if show_histogram:
    st.plotly_chart(fig_histogram)

# Show the scatter plot by default
st.plotly_chart(fig_scatter)
