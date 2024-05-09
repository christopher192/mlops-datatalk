import pickle
from flask import Flask, request, jsonify

# function for usage
with open('lin_reg.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']

    return features

def predict(features):
    x = dv.transform(features)
    preds = model.predict(x)

    return float(preds[0])

# setup name of application
app = Flask('duration-prediction')

# setup route for prediction
@app.route('/predict', methods = ['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred
    }

    return jsonify(result)

if __name__ == "__main__":
    # set host = '0.0.0.0' to accept connections from outside
    app.run(debug = True, host = '0.0.0.0', port = 9696)