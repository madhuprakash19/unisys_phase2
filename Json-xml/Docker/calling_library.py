from client_library.client import httpclient as hc
from client_library.xmlparser import parser
xp = parser()
from client_library.jsonparser import Parser
jp = Parser()
import json as js
def main():
    def responseCheck(res):
        flag = -1
        if res >= 200 and res <= 299:
            print("Request Success")
            flag = 1
        elif res >= 300 and res <= 399:
            print("Redirection Message")
            flag = -1
        elif res >= 400 and res <= 499:
            print("Client error")
            flag = -1
        elif res >= 500 and res <= 599:
            print("Server error")
            flag = -1
        return flag
    obj=hc()

    #Get Request
    def getRequest(url):
        auth=()
        allow_redirects=True
        cert=''
        cookies={}
        header={}
        proxies={}
        stream=True
        timeout=3
        verify=True
        r = obj.get(url,auth,allow_redirects,cert,cookies,header,proxies,stream,timeout,verify)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r.content)

    # Post Request
    def postRequest(url):
        data={"id":5,"name":"test"}
        json={}
        allow_redirects=True
        cert=''
        cookies={}
        header={}
        proxies={}
        stream=True
        timeout=3
        verify=True
        r = obj.post(url,data,json,allow_redirects,cert,cookies,header,proxies,stream,timeout,verify)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r.content)

    # Delete Request
    def deleteRequest(url):
        data={"id":1}
        allow_redirects=True
        auth=()
        cert=''
        cookies={}
        header={}
        proxies={}
        stream=True
        timeout=3
        verify=True
        r = obj.delete(url,data,allow_redirects,auth,cert,cookies,header,proxies,stream,timeout,verify)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r.content)

    #Put Request
    def putRequest(url):
        data={"id":1,"name":"unisys"}
        allow_redirects=True
        cert=''
        cookies={}
        header={}
        proxies={}
        stream=True
        timeout=3
        verify=True
        r = obj.put(url,data,allow_redirects,cert,cookies,header,proxies,stream,timeout,verify)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r.content)



    def xml(url):
        r = obj.get(url)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r)
            print(r.content)
            print(xp.displayRoot(r.content))
            print(xp.displayAllTag(r.content))
            print(xp.findContent(r.content,'name'))
            print(xp.iterateOne(r.content,'student'))
            print(xp.iterateAll(r.content,'student'))

    def json(url):
        url_ = url+"duoresponse1/"
        r = obj.get(url_)
        if r==999:
            print("Request timed out")
        elif responseCheck(r.status_code) == 1:
            print(r)
            par = js.loads(r.content)
            if par["stat"] == 'OK':
                print(par["response"]["devices"][0]["capabilities"])
                url1 = url+"duoauth1/"
                url2 = url+"/duoauth2"
                x = obj.get(url1)
                y = obj.get(url2)
                x_res = js.loads(x.content)
                if x_res["stat"] == "OK":
                    print(x_res["response"])

                y_res = js.loads(y.content)
                if y_res["stat"] == "OK":
                    print(y_res["response"])




    print("1.Get Request\n2.Post Request\n3.Put Request\n4.Delete Request\n5.XML\n6.JSON\n7.Exit\n")
    while(True):
        ch=int(input("Enter your choice: "))
        if(ch==1):
            url=input("Enter the url:")
            getRequest(url)
        elif(ch==2):
            url=input("Enter the url:")
            postRequest(url)
        elif(ch==3):
            url=input("Enter the url:")
            putRequest(url)
        elif(ch==4):
            url=input("Enter the url:")
            deleteRequest(url)
        elif(ch==5):
            url=input("Enter the url:")
            xml(url)
        elif(ch==6):
            url=input("Enter the url:")
            json(url)
        elif(ch==7):
            break
        else:
            print("Invalid Input")
            break


if __name__== '__main__':
    main()
