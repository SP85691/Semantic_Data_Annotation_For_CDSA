import os
import pandas as pd
import openai

# Function to get semantic data type
def get_column_data_type(column_name, sample_values):
    sample_values_text = ', '.join(map(str, sample_values))
    prompt = f"Given a dataset column with the header '{column_name}' and sample values [{sample_values_text}], what is the most likely semantic data type (e.g., Numerical, Location, Categorical, Time, URL, HTML)? Please consider the column header along with the values to identify the semantic type. We need these types for better visualisation of the data and a column that seems numerical might be a categorical type because the numbers represent categories not values. So if you believe a column header can be a categorical column with numbers as categories ( common cases will be column headers which identify a particular thing or place with a serial number, ID etc) please return Categorical as the answer. Please give your answer in a single word."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    data_type = response.choices[0].message.content.strip()
    return data_type


if __name__ == '__main__':
    # Base directory for datasets
    BASE_DIR = "Data/Datasets"
    
    # Create a list to store row dictionaries
    rows = []

    # Loop through files in the base directory
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".csv"):
                csv_path = os.path.join(root, file)
                print("Processing:", csv_path)
                df = pd.read_csv(csv_path)

                # Get unique data
                df_unique = df.apply(lambda x: x.unique()[0:5] if len(x.unique()) > 5 else x.unique())

                # Iterate over columns
                for column_name in df.columns:
                    # Get semantic data type
                    semantic_type = get_column_data_type(column_name, df_unique[column_name].tolist())

                    # Create structure
                    structure = {
                        "table_name": csv_path,
                        "column_name": column_name,
                        "column_values": df_unique[column_name].tolist(),
                        "openAI_semantic_type": semantic_type,
                        "annotation": "",
                        "comments": "",
                    }

                    # Append structure to list
                    rows.append(structure)

    # Create DataFrame from the list of dictionaries
    output_df = pd.DataFrame(rows)

    # Save output dataframe to CSV file
    output_df.to_csv("Data/FinalOutput2.csv", index=False)
