import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os
import sys 

if os.path.exists("src/models/evaluation_results.txt"):
    sys.exit()

# Load the trained model
with open("src/models/svm_model.pkl", "rb") as file:
    svm_model = pickle.load(file)

# Load the test data
with open("src/preprocessing/train_test_data.pkl", "rb") as file:
    _, X_test, _, y_test = pickle.load(file)  # Only extract test data

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Display results
print(f"Model Accuracy: {accuracy:.4f}\n")
print("Confusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)

# Save evaluation results to a file
with open("src/models/evaluation_results.txt", "w") as file:

    file.write(f"Model Accuracy: {accuracy:.4f}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(conf_matrix) + "\n\n")
    file.write("Classification Report:\n")
    file.write(class_report)

print("Evaluation complete. Results saved to 'evaluation_results.txt'.")
