import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    # Load the dataset
    df = pd.read_csv('Iris.csv')
    
    # Preprocess the data
    X = df.drop(columns=['Species'])
    y = df['Species']
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Save the trained model
    with open('app/model/iris_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

if __name__ == "__main__":
    train_model()