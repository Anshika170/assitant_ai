from flask import Flask,request,jsonify
from assistant import legal_assistant
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/query', methods=['GET','POST'])
def process_query():
    if request.method == 'POST':
        user_query = request.json.get('query')
        if user_query.lower() in ["exit", "bye"]:
            return jsonify({'response': "Goodbye! Have a great day!"})
        response = legal_assistant(user_query)
        return jsonify({'response': response})
   
    elif request.method == 'GET':
        return jsonify({'message': 'This is a GET request'})


if __name__ == "__main__":
    app.run(debug=True)





