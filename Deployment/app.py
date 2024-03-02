import numpy as np
from flask import Flask, request, render_template
import pickle

# flask app
app = Flask(__name__)
# loading model
emotional_model = pickle.load(open('emotional_wellbeing_model.pkl', 'rb'))
behavioral_model = pickle.load(open('behavioral_wellbeing_model.pkl', 'rb'))

@app.route('/')
def homepage():
    return render_template('Home.html')

@app.route('/Output', methods = ['POST'])
def home():
    x = str(request.form['Time_Period'])
    if x == 'Behavior':
        return render_template('Behavioral.html')
    elif x == "Emotion":
        return render_template('Emotional.html')
    else:
        return render_template('Home.html')

@app.route('/emotion_prediction' ,methods = ['POST'])
def emotion_prediction():
    final_features = [int(x) for x in request.form.values()]
    final_features = [np.array(final_features)]
    prediction = emotional_model.predict(final_features)

    return render_template('Emotional.html', output='Child Emotional Wellbeing Status is :  {}'.format(prediction[0]))

@app.route('/behavior_prediction' ,methods = ['POST'])
def behavior_prediction():
    final_features = [int(x) for x in request.form.values()]
    final_features = [np.array(final_features)]
    prediction = behavioral_model.predict(final_features)

    return render_template('Behavioral.html', output='Child Behavioral Wellbeing Status is :  {}'.format(prediction[0]))



if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)