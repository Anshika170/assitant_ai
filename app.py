from flask import Flask,request, jsonify
from assistant import legal_assistant

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def process_query():
    user_query = request.json.get('query')
    if user_query.lower() in ["exit", "bye"]:
        return jsonify({'response': "Goodbye! Have a great day!"})
    response = legal_assistant(user_query)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)


while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "bye","quit"]:
        print("Legal Assistant: Goodbye! Have a great day!")
        break
    response = legal_assistant(user_query)
    print("Legal Assistant:", response)


