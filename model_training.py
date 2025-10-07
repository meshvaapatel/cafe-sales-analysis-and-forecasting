import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import pickle  

# 1. Load Data
df = pd.read_csv(r'D:\UPCOMMING PROJECTS\PROJECT - 2\Cafe Sales Analysis & Forecasting\cafe_sales_cleaned.csv')

# Drop unnecessary columns for this model
df = df.drop(['transaction_id', 'transaction_date', 'price_per_unit', 'total_price_check'], axis=1)

# Define features (X) and target (y)
X = df.drop('total_spent', axis=1)
y = df['total_spent']

# 2. Preprocessing
# Identify categorical and numerical features
categorical_features = ['item', 'payment_method', 'location', 'weekday']
numerical_features = ['quantity', 'day', 'month', 'is_weekend']

# Create a preprocessor using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# 3. Choose and Define the Model
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

# 4. Create the ML Pipeline
ml_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('regressor', model)])

# 5. Split Data and Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the model...")
ml_pipeline.fit(X_train, y_train)
print("Model training complete.")

# 6. Evaluate the Model
y_pred = ml_pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model evaluation on test data:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {mse**0.5:.2f}")

# 7. Save the Model
# Use pickle to save the pipeline with the .pkl extension
with open('cafe_sales_model.pkl', 'wb') as file:
    pickle.dump(ml_pipeline, file)

print("\nModel pipeline saved as 'cafe_sales_model.pkl'")
