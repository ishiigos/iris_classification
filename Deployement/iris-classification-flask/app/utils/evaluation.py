def calculate_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def calculate_precision(y_true, y_pred):
    return precision_score(y_true, y_pred, average='weighted')

def calculate_recall(y_true, y_pred):
    return recall_score(y_true, y_pred, average='weighted')

def calculate_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='weighted')

def generate_classification_report(y_true, y_pred):
    return classification_report(y_true, y_pred)

def plot_confusion_matrix(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.title('Confusion Matrix')
    plt.show()