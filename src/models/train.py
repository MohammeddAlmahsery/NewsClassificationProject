import pickle
from sklearn.svm import SVC
import os
import sys 

if os.path.exists("src/models/svm_model.pkl"):
    sys.exit()

# Load data
with open("src/preprocessing/train_test_data.pkl", "rb") as file:
    X_train, _, y_train, _ = pickle.load(file)

# Train an SVM model
svm_model = SVC(kernel='rbf')
svm_model.fit(X_train, y_train)

# Save the trained model
with open(r"src/models/svm_model.pkl", "wb") as file:
    pickle.dump(svm_model, file)

print("Training complete. Model saved as 'svm_model.pkl'.")
