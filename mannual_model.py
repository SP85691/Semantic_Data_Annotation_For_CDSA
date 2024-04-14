import os
import pandas as pd
from geopy.geocoders import Nominatim
import logging

# Set up logging
logging.basicConfig(filename='semantic_type_detector.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_semantic_type(df):
    column_categories = {}
    location_keywords = ['location', 'place', 'address', 'city', 'state', 'country', 'region', 'postal', 'zipcode', 'district']
    calendar_keywords = ['calendar', 'time', 'date', 'week', 'month', 'year', 'hour', 'minute', 'second', 'day', 'datetime', 'timestamp']

    geolocator = Nominatim(user_agent="semantic_type_detector")  # Initialize geocoder

    for col in df.columns:
        # Check if any of the location keywords are in the column header
        if any(keyword in col.lower() for keyword in location_keywords):
            column_categories[col] = 'Location'
        
        # Check if any of the calendar keywords are in the column header
        elif any(keyword in col.lower() for keyword in calendar_keywords):
            column_categories[col] = 'Time'
        
        # Check if the column contains URL data
        elif df[col].apply(lambda x: isinstance(x, str) and x.startswith('http')).any():
            column_categories[col] = 'URL'
        
        # Check if the column contains HTML data
        elif df[col].apply(lambda x: isinstance(x, str) and '<html>' in x.lower()).any():
            column_categories[col] = 'HTML'
        
        # Check if the column contains string data
        elif pd.api.types.is_string_dtype(df[col]):
            # Check if the column has less than a certain threshold of unique values
            if df[col].nunique() <= 100:  # Adjust the threshold as needed
                column_categories[col] = 'Categorical'
            else:
                # Check if any value contains location information
                try:
                    if df[col].apply(lambda x: geolocator.geocode(x) is not None).any():
                        column_categories[col] = 'Location'
                    else:
                        column_categories[col] = 'Categorical'
                except Exception as e:
                    logging.error(f"Error in geocoding: {e}")
                    column_categories[col] = 'Categorical'
        
        elif pd.api.types.is_numeric_dtype(df[col]):
            if df[col].dtype == 'int64' or df[col].dtype == 'float64':
                column_categories[col] = 'Numerical'
            else:
                column_categories[col] = 'Numerical'
    
    return column_categories