import pandas as pd

def feature_engineering(data):
    # Example feature engineering
    data['total_charges'] = data['tenure'] * data['monthly_charges']
    data = pd.get_dummies(data, columns=['gender', 'contract'], drop_first=True)
    return data

if __name__ == "__main__":
    sample_data = pd.read_csv('sample_data.csv')
    processed_data = feature_engineering(sample_data)
    print("Processed Data:", processed_data.head())
