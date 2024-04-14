import openai
import logging

# Set up logging
logging.basicConfig(filename='semantic_type_detector.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_column_data_type(column_name, sample_values):
    sample_values_text = ', '.join(map(str, sample_values))
    prompt = f"Given a dataset column with the header '{column_name}' and sample values [{sample_values_text}], what is the most likely semantic data type (e.g., Numerical, Location, Categorical, Time, URL, HTML)? Please consider the column header along with the values to identify the semantic type. We need these types for better visualisation of the data and a column that seems numerical might be a categorical type because the numbers represent categories not values. So if you believe a column header can be a categorical column with numbers as categories ( common cases will be column headers which identify a particular thing or place with a serial number, ID etc) please return Categorical as the answer. Please give your answer in a single word."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        data_type = response.choices[0].message.content.strip()
        return data_type
    except Exception as e:
        logging.error(f"Error in OpenAI completion: {e}")
        return ""