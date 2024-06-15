#conclusion version
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

#Use env function to secure my keys
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CX = os.getenv('GOOGLE_CX')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#https://docs.pytest.org/en/8.2.x/
client = OpenAI(api_key=OPENAI_API_KEY)

'''
Using ArrayStack implementation so that we can get query history later on
'''
class ArrayStack:
 
    def __init__(self):
        self._data = list()
    
    def push(self, e):
        self._data.append(e)

'''
log_query function will push query into stack
get_query_history displays the query history on web
'''
class BrowserHistory:
    def __init__(self):
        self.history = ArrayStack()  # Use an instance of ArrayStack to store the history

    def log_query(self, query):
        """ Log a new query to the history """
        self.history.push(query)

    def get_query_history(self):
        """ Return a list of all queries in the history """
        return list(reversed(self.history._data))
 
    
    
search_history = BrowserHistory()

'''
goolge search function performs a Google search using the Google Custom Search API.
param query: promt that users type
'''
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CX}&q={query}"
    response = requests.get(url)
    return response.json()

'''
search function is Flask route handler designed to respond to web-based search requests
'''
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    search_results = google_search(query)
    search_history.log_query(query)  
    return jsonify(search_results)

'''
Submit function is designed to respond to chatgpt interaction
'''
@app.route('/explain', methods=['POST'])
def submit():
        data = request.get_json() 
        prompt = data.get('prompt') #get promt
        response = client.chat.completions.create( #answer setup
            temperature=0,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "You are a helpful assistant and knows everything in the world"
            }, {
                "role": "user",
                "content": prompt
            }]
        )
        result = {'message': response.choices[0].message.content}
        print("Sending JSON:", result)  
        return jsonify(result)


'''
history function provide clients with a list of recently visited search queries
'''
@app.route('/history', methods=['GET'])
def history():
    return jsonify(search_history.get_query_history())



if __name__ == '__main__':
    app.run(port=5000)
