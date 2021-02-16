from flask import Flask, request, jsonify
import util
import requests

app = Flask(__name__)

@app.route("/") 
def home_view():
    return "<h1>pickPicker Backend</h1>"
        

@app.route('/classify_image', methods= ['GET','POST'])
def classify_image():
    image_data = request.form['image_data']
    data=[]
    url = "https://api.unsplash.com/search/photos"
    query={"page":"1", "client_id":"vrB0FKvJ2uIq780UySc3VE8LI8uxKhja3MyxU1MN9MI"}

    q = util.classify_image(image_base64_data=image_data)
    query["query"]=q
    response = requests.get(url,params=query)
    for i in range(0,10):
        data.append(response.json()["results"][i]["urls"]["raw"])
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__=="__main__":
    print("Starting Python Flask Server")
    app.run(port=5000)