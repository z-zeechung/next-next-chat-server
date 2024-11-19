# _N_<sup>2</sup>CHAT Backend Server

This is the dev server for [_N_<sup>2</sup>CHAT](https://github.com/z-zeechung/next-next-chat).

## TODO
- [ ] Implement LLM tool call
- [ ] Implement `stt` (speech to text) API

### _Please help us implement interfaces for more platforms!_

## Running the Backend Server
1. Clone this repository
2. `pip install -r requirements.txt`
3. Copy `config.json.template` to `config.json`
4. Configure `config.json`
   + `mirror`: Generally you don't have to change this value. If your region isn't accessible to Huggingface, you can configure mirror site here.
   + `chat`: The chat model. Currently support:
     + `qwen-1.5b`: A 1.5B chat model running locally
   + `embed`: The embedding model that converts text into vector. Currently support:
     + `bge-small-en`: BGE embedding model for English
     + `bge-small-zh`: BGE embedding model for Chinese
   + `caption`: The model that describes image content. Currently support:
     + `dummy`: A dummy model that simply returns user's input
   + `paint`: The model that generates image based on user's input and reference image. Currently support:
     + `dummy`: A dummy model that returns an image with user's input writing on it
   + `search`: Query from search engine. Currently support:
     + `baidu`: Baidu search
5. run `app.py`
