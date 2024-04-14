# CDSA Semantic Annotation Analysis

In this project I have created a solution to the problem of semantic annotation of CDSA documents. The solution is based on the use of the Openai API by using of "GPT-3.5-Turbo" Model and a manually created model to detect semantic type it's own. We are focusing on get this type of information from the documents:

```bash
table_name,column_name,column_values,openAI_semantic_type,annotation,comments,model_x_semantic_type,annotation_x
Data/Datasets/Aam Aadmi Bima Yojana.csv,Country,['India'],Categorical,FALSE,,Location,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,State,"['Andaman And Nicobar Islands', 'Andhra Pradesh']",Categorical,FALSE,,Location,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,Year,"['Calendar Year (Jan - Dec), 2013', 'Calendar Year (Jan - Dec), 2014', 'Calendar Year (Jan - Dec), 2015']",Time,TRUE,,Time,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,New Lives Covered Under Aam Aadmi Bima Yojana (Aaby) (UOM:Number),"[0.0, 1675.0, 2.0, 1260399.2208146066, 5199301.969324921]",Numerical,TRUE,,Numerical,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,"Claims Setteled Under Aam Aadmi Bima Yojana (Aaby) Claims Settled Includes Death, Accident And Disability Claims (UOM:Number)","[0.0, 28796.42399340928, 21438.47108693504]",Numerical,TRUE,,Numerical,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,"Amount Of Claims Setteled Under Aam Aadmi Bima Yojana (Aaby) , Claims Settled Includes Death, Accident And Disability Claims (UOM:INR(IndianRupees))","[0.0, 941195.7727926464, 701542.094361908]",Numerical,TRUE,,Numerical,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,Scholarships Paid Under Aam Aadmi Bima Yojana (Aaby) (UOM:Number),"[0.0, 1150156.5358232283, 624686.2745482818]",Numerical,TRUE,,Numerical,TRUE
Data/Datasets/Aam Aadmi Bima Yojana.csv,Amount Of Scholarships Paid Under Aam Aadmi Bima Yojana (Aaby) (UOM:INR(IndianRupees)),"[0.0, 62131895.4556478, 222250786.31351]",Numerical,TRUE,,Numerical,TRUE
Data/Datasets/Details of Har Ghar Jal (100% Functional Household Tap Connections (FHTC) Coverage).csv,Country,['India'],Categorical,FALSE,,Location,TRUE
Data/Datasets/Details of Har Ghar Jal (100% Functional Household Tap Connections (FHTC) Coverage).csv,State,"['Andaman And Nicobar Islands', 'Andhra Pradesh']",Location,TRUE,,Location,TRUE
```

## Usage

```bash
git clone <repo-url> && cd <repo-name>
```

## Installation

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

```bash
./venv/Scripts/activate
```

### Install all Required Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

#### To Run only OpenAI Process

```bash
python updated_main.py
```
