from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

def preprocess_data(df):
    # Handle missing values if any
    df = df.dropna()

    # Encode categorical variables if necessary
    label_encoder = LabelEncoder()
    df['Species'] = label_encoder.fit_transform(df['Species'])

    # Separate features and target variable
    X = df.drop('Species', axis=1)
    y = df['Species']

    # Standardize the feature values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, label_encoder

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    return preprocess_data(df)