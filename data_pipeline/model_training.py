from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data):
    X = data.drop('churn', axis=1)
    y = data['churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, 'churn_model.pkl')
    print("Model Trained and Saved")

if __name__ == "__main__":
    processed_data = pd.read_csv('processed_data.csv')
    train_model(processed_data)
