import pickle
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

team_levels = {
  1: 'valor1', 
  2: 'valor2', 
  3: 'valor3',
  4: 'valor3',
  5: 'valor3',
  6: 'valor3',
  7: 'valor3',
  8: 'valor3',
  9: 'valor3', 
  10: 'valor3',
  11: 'valor3',
  12: 'valor3',
  13: 'valor3',
  14: 'valor3',
  15: 'valor3',
  16: 'valor3',
  17: 'valor3',
  18: 'valor3',
  19: 'valor3',
  20: 'valor3',
  21: 'valor3',
  22: 'valor3',
  23: 'valor3',
  23: 'valor3',
  25: 'valor25'
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