import pickle
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class GetPrediction(Resource):
  def get(self):
    try:
      data = request.get_json()
      local_team = int(data.get('localTeam'))
      away_team = int(data.get('awayTeam'))

      predict_output = GetPrediction.predict(local_team, away_team)
      predict_output_str = str(predict_output)
      response_data = {'prediction': predict_output_str}
      return jsonify(response_data)

    except Exception as error:
      return {'error': str(error)}
    
  def predict(local_team, away_team):
    pkl_filename = "model_3.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)

    y_pred = model.predict([[local_team, away_team]])

    return y_pred[0]

api.add_resource(GetPrediction, '/getPrediction')

if __name__ == '__main__':
  app.run(port=5000)