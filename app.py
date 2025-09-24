# app.py
from flask import Flask, request, render_template
import pickle
import numpy as np
from weather import weather_bp  # 🔹 import the weather blueprint

app = Flask(__name__)

# ----------------- LOAD CROP MODEL ----------------- #
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ----------------- REGISTER BLUEPRINT ----------------- #
app.register_blueprint(weather_bp)  # 🔹 register the weather blueprint

# ----------------- ROUTES ----------------- #

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# ----------------- CROP PREDICTION ----------------- #

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        N = float(request.form['nitrogen'])
        P = float(request.form['phosphorus'])
        K = float(request.form['potassium'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form.get('ph', 7))
        rainfall = float(request.form.get('rainfall', 100))

        # Prepare features and predict
        input_features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        prediction = model.predict(input_features)[0]

        # Return crop.html with prediction
        return render_template('crop.html', prediction=f"✅ Recommended Crop: {prediction}")

    except Exception as e:
        return render_template('crop.html', prediction=f"⚠️ Error: {e}")

# ----------------- YIELD ESTIMATOR ----------------- #

@app.route('/yield', methods=['GET'])
def yield_estimator():
    return render_template('yield.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    try:
        crop = request.form['crop']
        area = float(request.form['area'])
        soil_quality = float(request.form['soil_quality'])
        rainfall = float(request.form['rainfall'])

        # Simple estimation formula (replace with ML model later)
        estimated_yield = area * soil_quality * (rainfall / 100)  # quintals approx
        estimated_yield = round(estimated_yield, 2)

        return render_template('yield.html', estimated_yield=estimated_yield)
    except Exception as e:
        return render_template('yield.html', estimated_yield=f"⚠️ Error: {e}")

# ----------------- RUN APP ----------------- #

if __name__ == '__main__':
    app.run(debug=True)











