from flask import Flask
import json

from caption.Caption import CaptionAPIs
from embed.Embed import EmbedAPIs
from llm.LLM import ChatAPIs
from paint.Paint import PaintAPIs
from search.Search import SearchAPIs

with open("config.json", "r", encoding="utf-8") as c:
    config = json.loads(c.read())

chatApi    = ChatAPIs   [config["chat"   ]]()
embedApi   = EmbedAPIs  [config["embed"  ]]()
captionApi = CaptionAPIs[config["caption"]]()
paintApi   = PaintAPIs  [config["paint"  ]]()
searchApi  = SearchAPIs [config["search" ]]()

app = Flask(__name__)

@app.route('/ciallo')
def ciallo():
    return 'Ciallo～(∠・ω< )⌒★'

@app.route('/chat')
def chat():
    ...

@app.route('/embed')
def embed():
    ...

@app.route('/caption')
def caption():
    ...

@app.route('/paint')
def paint():
    ...

@app.route('/search')
def search():
    ...


if __name__ == '__main__':
    app.run(debug=True)
