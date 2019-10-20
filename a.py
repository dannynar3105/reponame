import docker, requests
from flask import Flask,request,render_template,jsonify
import requests, json
import docker
from flask_cors import CORS

app = Flask(__name__,template_folder='.')
url = "http://0.0.0.0:5000"
CORS(app)
cors=CORS(app,resources={r"/api/*": {"origins": "*"}})


@app.route('/login')
def login():
  return render_template('a.html')

@app.route('/list/', methods=['GET','POST'])
def Images(vent=False):
    tag_list = []
    try:
      c = docker.from_env()
      imgs = c.images.list()
      for img in imgs:
        repo_tags = img.tags
        
        print (img)
        if not repo_tags:
           continue
        for repo_tag in repo_tags:
                s_list = repo_tag.split(":")
                print (s_list)
                tag = s_list[0]
                print (tag)
                tag1= s_list[1]
                repo = tag+":"+tag1
                print (repo)
                tag_list.append(repo)
      return json.dumps(tag_list)
    except Exception as e:  # pragma: no cover
              print ("Something with the Images went wrong " + str(e))
              return "no images" 


@app.route('/search/', methods=['GET','POST'])
def search():
  params2=request.get_data(as_text=True)
  print ("url is "+request.url)
  print ("image value =" + params2)
  try:
    c = docker.from_env()
    str1=params2.split(":")
    pimgval=str1[1].replace("\"","")
    dimgval=str1[2].replace("\"","")
    dimgval=dimgval[:-1]
    imgval=pimgval+":"+dimgval
    print ("searched image is "+imgval)
    vallist=c.images.list()
    for img in vallist:
        imgsval=img.tags
        print ("in the search for")
        for val in img.tags:
           imgname=val.split(":")
           print ("inside ..."+str(imgname))
           pname=imgname[0]
           tname=imgname[1]
           print (pname+"==="+tname)
           print (pimgval+"==="+dimgval)
           if (pname==pimgval and tname==dimgval):
              value=img
              print (value.history())
              return json.dumps(value.history())
  except Exception as e:
       print ("Error in reriveal " + str(e)) 
       return "no images"
  return "no images"





if __name__ == '__main__':
 app.run(host="0.0.0.0", port = 5000,debug=True)


