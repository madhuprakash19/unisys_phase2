from flask import Flask, jsonify, render_template, request,Response,send_file
import json as js
from client_library.xmlparser import parser
from client_library.xmlparser import parser
xp = parser()
from client_library.jsonparser import Parser
jp = Parser()
import json as js

from client_library.client import httpclient as hc
obj=hc()



xp = parser()
app = Flask(__name__)
course = [
    {"id": 1, "name": "Lakshana"},
    {"id": 2, "name": "Madhu"},
    {"id": 3, "name": "Nikitha"},
    {"id": 4, "name": "Laisha"},
]
@app.route("/app/api/course/all",methods=['GET'])
def show():
    return jsonify(course)


@app.route("/update/", methods=['PUT'])
def update():
    id = request.form.get("id")
    print(id)
    name = request.form.get("name")
    print(name)
    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course[i]["name"] = name
            return jsonify(course)


@app.route("/append/",methods=['POST'])
def append():
    print(request.content_length)
    id = request.form.get("id")
    name = request.form.get("name")
    print(id)
    print(name)
    d = {"id": int(id), "name": name}
    course.append(d)
    return jsonify(course)


@app.route("/remove/",methods=['DELETE'])
def remove():
    id = request.form.get("id")

    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course.remove(course[i])
            return jsonify(course)
    return "ID NOT FOUND TO DELETE"


@app.route("/showit/",methods=['GET'])
def showit():
    id = request.args.get("id")

    for i in range(0, len(course)):
        temp = course[i]["id"]
        print(temp)
        if int(temp) == int(id):
            print("sucess")
            return course[i]
    return "not found"

@app.route("/xmlresponse1/",methods=["GET"])
def xmlresponse1():
    return send_file('sample.xml', mimetype='xml')


@app.route("/duoresponse1/",methods=["GET"])
def duoresponse1():
    return send_file('duo_response1.json', mimetype='json')

@app.route("/duoauth1/",methods=["GET"])
def duo_auth1():
    return send_file('duo_auth1.json', mimetype='json')

@app.route("/duoauth2/",methods=["GET"])
def duo_auth2():
    return send_file('duo_auth2.json', mimetype='json')



@app.route("/xmlresponsemcp/",methods=["GET"])
def xmlresponsemcp():
    url = "http://"+address+":"+str(prt)+"/xmlresponse1/"
    print(url)
    r = obj.get(url)
    studentall = xp.iterateAll(r.content,'student')
    return jsonify(studentall)






@app.route("/jsonresponsemcp/",methods=["GET"])
def jsonresponsemcp():
    url =  "http://"+address+":"+str(prt)
    url_ = url +"/duoresponse1/"
    r = obj.get(url_)
    par = js.loads(r.content)
    result = {}
    if par["stat"] == 'OK':
        capablities = par["response"]["devices"][0]["capabilities"]
        result['capablities'] = capablities
        url1 = url+"/duoauth1/"
        url2 = url+"/duoauth2/"
        x = obj.get(url1)
        y = obj.get(url2)
        x_res = js.loads(x.content)
        if x_res["stat"] == "OK":
            res1 = x_res["response"]
            result['duo_auth1_response'] = res1

        y_res = js.loads(y.content)
        if y_res["stat"] == "OK":
            res2 = y_res["response"]
            result['duo_auth2_response'] = res2

    return result






if __name__ == "__main__":
    address = "172.16.11.206"
    prt = 8086
    app.run(host=address, port=prt ,debug=True)
