import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, mean_squared_error, mean_absolute_error

# Example ground truth and predicted labels
ground_truth = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]
predicted_labels = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]

# Calculate precision, recall, and F1-score
precision = precision_score(ground_truth, predicted_labels)
recall = recall_score(ground_truth, predicted_labels)
f1 = f1_score(ground_truth, predicted_labels)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Example actual and predicted ratings
actual_ratings = [3, 2, 4, 5, 1, 2, 3, 4, 5, 1]
predicted_ratings = [3.2, 2.5, 3.8, 4.9, 1.2, 1.8, 3.5, 4.2, 4.8, 1.5]

# Calculate RMSE and MAE
rmse = np.sqrt(mean_squared_error(actual_ratings, predicted_ratings))
mae = mean_absolute_error(actual_ratings, predicted_ratings)

print("RMSE:", rmse)
print("MAE:", mae)

