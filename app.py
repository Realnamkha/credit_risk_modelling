from flask import Flask, redirect, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.sav', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        v1 = request.form.get('ROCE (%)', type=float)
        v2 = request.form.get('CASA (%)', type=float)
        # Add more variables as needed
        
        # Make prediction
        result = model.predict([[v1, v2]])[0]  # Modify according to your model
        
        # Pass input values and result back to the template
        return render_template('index.html', result=result, v1=v1, v2=v2)  # Add more variables as needed
    else:
        # If GET request, redirect to home page
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)