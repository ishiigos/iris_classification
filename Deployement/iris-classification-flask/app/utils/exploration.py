import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    """
    Function to explore the dataset and generate visualizations and summary statistics.
    
    Parameters:
    df (DataFrame): The input DataFrame containing the Iris dataset.
    
    Returns:
    None
    """
    # Display basic statistics
    print("Basic Statistics:")
    print(df.describe())
    
    # Display the distribution of species
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Species')
    plt.title('Distribution of Iris Species')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.show()
    
    # Pairplot for visualizing relationships
    sns.pairplot(df, hue='Species')
    plt.title('Pairplot of Iris Features')
    plt.show()
    
    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()