import docker
from flask import Flask,request, jsonify
import requests, json
import docker
from flask_cors import CORS

app = Flask(__name__)
url = "http://0.0.0.0:5000"
CORS(app)
cors=CORS(app,resources={r"/api/*": {"origins": "*"}})

@app.route('/list/', methods=['GET','POST'])
def Images(vent=False):
    tag_list = []
    try:
      c = docker.from_env()
      imgs = c.images.list()
      for img in imgs:
        repo_tags = img.tags
        if not repo_tags:
            continue
        for repo_tag in repo_tags:
                s_list = repo_tag.split(":")
                tag = s_list[0]
                repo = ":".join(s_list[:-1])
                tag_list.append(tag)
      return json.dumps(tag_list)
    except Exception as e:  # pragma: no cover
              print ("Something with the Images went wrong " + str(e))
              return "no images" 

    

if __name__ == '__main__':
 app.run(host="0.0.0.0", port = 5000,debug=True)


