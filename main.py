import pandas as pd
from mannual_model import get_semantic_type
from openai_model import get_column_data_type
import os

if __name__ == '__main__':
    rows = []
    
    files = [f"Data/TestFiles/{files}" for files in os.listdir("Data/TestFiles") if files.endswith(".csv")]
    
    for file in files:
        print("Processing:", file)
        df = pd.read_csv(file)
        df = df.head()
        df_unique = df.apply(lambda x: x.str[:200].unique() if x.dtype == 'object' and x.str.len().max() > 200 else x.unique()[0:5] if len(x.unique()) > 5 else x.unique(), axis=0)
        for column in df.columns:  
            # Truncate column values to 200 characters if necessary
            if df[column].dtype == 'object' and df[column].str.len().max() > 200:
                df_unique[column] = pd.Series(df_unique[column]).str[:200]
            
            column_categories = get_semantic_type(df)
            semantic_type = get_column_data_type(column, df_unique[column].tolist())
            # print("OpenAI Result - ", semantic_type)
            # print("Mannual Result - ", column_categories.get(column, ""))
            
            
            # Create structure
            structure = {
                "table_name": file,
                "column_name": column,
                "column_values": df_unique[column].tolist(),
                "openAI_semantic_type": semantic_type,  # You may replace this with the function that calls OpenAI API for semantic type detection
                "annotation": "",
                "comments": "", 
                "model_x_semantic_type": column_categories.get(column, ""),  # Get semantic type from the dictionary
                "annotation_x": ""
            }
            
            rows.append(structure)
    output_df = pd.DataFrame(rows)
    output_df.to_csv("FinalOutput2.csv", index=False)
