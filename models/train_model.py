from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved Successfully")