import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import time
import sys

# ==========================================
# 1. PROFESSIONAL LOGGING SETUP
# ==========================================
def print_log(message):
    """Prints a timestamped system log."""
    print(f"[SYSTEM] {time.strftime('%H:%M:%S')} - {message}")

def main():
    print("\n" + "="*55)
    print("  STUDENT PERFORMANCE AI - MODEL COMPILER v5.1  ")
    print("="*55)

    try:
        # ==========================================
        # 2. DATA INGESTION
        # ==========================================
        print_log("Initializing Data Ingestion Module...")
        df = pd.read_csv('student_data.csv')

        print_log("Validating features and target variables...")
        features = ['studytime', 'absences', 'G1', 'G2']
        target = 'G3'

        X = df[features]
        y = df[target]

        # ==========================================
        # 3. DATA SPLITTING
        # ==========================================
        print_log("Splitting dataset (80% Training / 20% Validation)...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # ==========================================
        # 4. ADVANCED MODEL TRAINING
        # ==========================================
        print_log("Compiling Random Forest Regressor Engine...")
        
        # Upgraded model with professional tuning parameters
        model = RandomForestRegressor(
            n_estimators=200,      # More trees for better accuracy
            max_depth=15,          # Prevents over-complicating the logic
            min_samples_split=4,   # Requires reliable data patterns
            random_state=42
        )

        time.sleep(0.5) # Simulating build processing
        model.fit(X_train, y_train)

        # ==========================================
        # 5. EVALUATION PROTOCOLS
        # ==========================================
        print_log("Executing Model Evaluation Protocols...")
        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        # Calculate a rough percentage-based accuracy score based on R2
        accuracy_grade = max(0, min(100, (r2 * 100)))

        print("\n" + "-"*55)
        print(" 📊 EVALUATION METRICS REPORT")
        print("-"*55)
        print(f" -> Mean Absolute Error (MAE): {mae:.2f} points off")
        print(f" -> R-Squared Score (R2):      {r2:.2f}")
        print(f" -> Model Accuracy Grade:      {accuracy_grade:.1f}%")
        print("-"*55 + "\n")

        # ==========================================
        # 6. MODEL SERIALIZATION
        # ==========================================
        print_log("Serializing and securing model core...")
        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)

        print_log("SUCCESS: 'model.pkl' generated and ready for deployment.")
        print("="*55 + "\n")

    except FileNotFoundError:
        print("\n[ERROR] CRITICAL FAILURE: 'student_data.csv' not found.")
        print("[ERROR] Please ensure the data file is placed in the root directory.\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] UNEXPECTED EXCEPTION: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()