from flask import Flask, request, Response
import json
from flask_cors import cross_origin  

from apis import CAPTION_APIS, CHAT_APIS, EMBED_APIS, PAINT_APIS, SEARCH_APIS
from data_types import Message, Tool

with open("config.json", "r", encoding="utf-8") as c:
    config = json.loads(c.read())

# 国内的话可以改config.json里的mirror字段，来挂国内huggingface镜像
import os
os.environ['HF_ENDPOINT'] = config['mirror']

# Load APIs
ChatAPI = CHAT_APIS[config['chat']]()
EmbedAPI = EMBED_APIS[config['embed']]()
CaptionAPI = CAPTION_APIS[config['caption']]()
PaintAPI = PAINT_APIS[config['paint']]()
SearchAPI = SEARCH_APIS[config['search']]()

app = Flask(__name__)

@app.route('/ciallo')
def ciallo():
    return 'Ciallo～(∠・ω< )⌒★'

@app.route('/chat', methods=['POST'])
@cross_origin(origin='*')
def chat():
    data = json.loads(request.stream.read().decode())
    messages = []
    model = "regular"
    tools = []
    if 'messages' in data:
        messages = data['messages']
        messages = [Message(msg['role'], msg['content']) for msg in messages]
    if 'model' in data:
        model = data['model']
    if 'tools' in data:
        tools = data['tools']
        tools = [Tool(t['name'], t['type'], t['description'], [Tool.ToolParam(p['name'], p['type'], p['description']) for p in t["params"]]) for t in tools]
    def generate():
        for t in ChatAPI.chat(messages, model, tools):
            yield json.dumps({"result": t})+"\n"
    return Response(generate())

@app.route('/embed', methods=['POST'])
@cross_origin(origin='*')
def embed():
    data = json.loads(request.stream.read().decode())
    return json.dumps(EmbedAPI.embed(data))

@app.route('/caption', methods=['POST'])
@cross_origin(origin='*')
def caption():
    data = json.loads(request.stream.read().decode())
    prompt, image = "", ""
    if 'prompt' in data:
        prompt = data['prompt']
    if 'image' in data:
        image = data['image']
    def generate():
        for t in CaptionAPI.caption(image, prompt):
            yield json.dumps({"result": t})+"\n"
    return Response(generate())

@app.route('/paint', methods=['POST'])
@cross_origin(origin='*')
def paint():
    data = json.loads(request.stream.read().decode())
    prompt, image = "best quality, 8k wallpaper, high res", None
    if 'prompt' in data:
        prompt = data['prompt']
    if 'image' in data:
        image = data['image']
    data = PaintAPI.paint(prompt, image)
    return Response(data)

@app.route('/search', methods=['POST'])
@cross_origin(origin='*')
def search():
    data = json.loads(request.stream.read().decode())
    query = ""
    count = 1
    index = 0
    if 'query' in data:
        query = data['query']
    if 'count' in data:
        count = data['count']
    if 'index' in data:
        index = data['index']
    return json.dumps({
        'result': [{
            'url': r.url,
            'digest': r.digest
        } for r in SearchAPI.search(query, count, index)]
    })


if __name__ == '__main__':
    app.run(host='127.114.51.4', port=19198, debug=True)
