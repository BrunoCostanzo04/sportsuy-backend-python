import pickle
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

team_levels = {
  1: 75, 
  2: 87, 
  3: 62,
  4: 89,
  5: 0,
  6: 0,
  7: 0,
  8: 67,
  9: 80, 
  10: 55,
  11: 70,
  12: 0,
  13: 0,
  14: 80,
  15: 91,
  16: 73,
  17: 52,
  18: 0,
  19: 0,
  20: 60,
  21: 82,
  22: 0,
  23: 0,
  23: 0,
  25: 44
}

class GetPrediction(Resource):
  def post(self):
    try:
      data = request.get_json()
      local_team = int(data.get('localTeam'))
      away_team = int(data.get('awayTeam'))

      home_team_level = team_levels.get(local_team, 20)
      away_team_level = team_levels.get(away_team, 20)

      predict_output = GetPrediction.predict(local_team, away_team, home_team_level, away_team_level)
      predict_output_str = str(predict_output)
      response_data = {'prediction': predict_output_str}

      return jsonify(response_data)
    
    except Exception as error:
      return {'error': str(error)}
    
  def predict(local_team, away_team, home_team_level, away_team_level):

    pkl_filename = "model_v2.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)
    y_pred = model.predict([[local_team, away_team, home_team_level, away_team_level]])
    print(y_pred)

    return y_pred[0]

api.add_resource(GetPrediction, '/getPrediction')

if __name__ == '__main__':
  app.run(port=5000)