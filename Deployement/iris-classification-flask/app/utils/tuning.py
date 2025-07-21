from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def tune_hyperparameters(X_train, y_train):
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_features': ['auto', 'sqrt'],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, 
                               cv=3, n_jobs=-1, verbose=2, scoring='accuracy')
    
    grid_search.fit(X_train, y_train)
    
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    return best_params, best_score

def load_data(file_path):
    df = pd.read_csv(file_path)
    X = df.drop('species', axis=1)
    y = df['species']
    return X, y

def main():
    X, y = load_data('Iris.csv')
    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    best_params, best_score = tune_hyperparameters(X_train, y_train)
    print("Best Hyperparameters:", best_params)
    print("Best Score:", best_score)

if __name__ == "__main__":
    main()