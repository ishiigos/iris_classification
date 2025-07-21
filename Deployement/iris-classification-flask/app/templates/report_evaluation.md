# Model Evaluation Report

## Overview
This document summarizes the evaluation of the Iris classification model. The evaluation process includes the assessment of various performance metrics to determine the model's effectiveness in classifying the Iris species.

## Evaluation Metrics
The following metrics were calculated to evaluate the model's performance:

- **Accuracy**: The proportion of true results among the total number of cases examined.
- **Precision**: The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall (Sensitivity)**: The ratio of correctly predicted positive observations to all actual positives.
- **F1 Score**: The weighted average of Precision and Recall, providing a balance between the two.

## Confusion Matrix
A confusion matrix was generated to visualize the performance of the classification model. It shows the true positive, true negative, false positive, and false negative predictions.

| Actual \ Predicted | Setosa | Versicolor | Virginica |
|---------------------|--------|------------|-----------|
| Setosa              | TP     | FP         | FN        |
| Versicolor          | FN     | TP         | FP        |
| Virginica           | FN     | FP         | TP        |

## Classification Report
The classification report provides a detailed breakdown of the precision, recall, and F1 score for each class.

### Class-wise Performance
- **Setosa**: 
  - Precision: 
  - Recall: 
  - F1 Score: 

- **Versicolor**: 
  - Precision: 
  - Recall: 
  - F1 Score: 

- **Virginica**: 
  - Precision: 
  - Recall: 
  - F1 Score: 

## Conclusion
The evaluation results indicate that the model performs well in classifying the Iris species. Further analysis and potential improvements can be explored in the hyperparameter tuning phase.