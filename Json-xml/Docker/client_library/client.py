import requests
class httpclient:
    # #While calling the get function,
    # just pass the url if any other attributes need to be passed,then pass them along with the url
    # for example,
    # request.get(url,(),(params))
    # Here we have passed params but did not pass auth, auth has to be explicitly mentioned as empty
    # By default allow_redirects,stream,verify is set as true and timeout is set to 3 seconds
    # If there is request read timeout,it returns 999.
    # 999 is taken as a custom exception because it is out of bound value in the response check function.
    def get(self, url, auth=(), allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.get(url,auth=auth,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    # #While calling the post function,
    # just pass the url if any other attributes need to be passed,then pass them along with the url
    # for example,
    # request.post(url,{},{json_file})
    # Here we have passed json file but did not pass data, data has to be explicitly mentioned as empty.
    # By default allow_redirects,stream,verify is set as true and timeout is set to 3 seconds.
    # If there is request read timeout,it returns 999.
    # 999 is taken as a custom exception because it is out of bound value in the response check function.
    def post(self, url,data={},json={}, allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.post(url,data=data,json=json,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    # #While calling the delete function,
    # just pass the url if any other attributes need to be passed,then pass them along with the url
    # for example,
    # request.delete(url,allow_redirects=True, auth=(),cert='',cookies={},{headers})
    # Here we have passed headers but did not pass auth,allow_redirects,certificate,cookies, so these has to be explicitly mentioned as empty.
    # By default allow_redirects,stream,verify is set as true and timeout is set to 3 seconds.
    # If there is request read timeout,it returns 999.
    # 999 is taken as a custom exception because it is out of bound value in the response check function.
    def delete(self,url,data={},allow_redirects=True,auth=(),cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.delete(url,data=data,allow_redirects=allow_redirects,auth=auth,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    # #While calling the put function,
    # just pass the url if any other attributes need to be passed,then pass them along with the url
    # for example,
    # request.put(url,allow_redirects=True, auth=(),cert='',cookies={},{headers})
    # Here we have passed headers but did not pass auth,allow_redirects,certificate,cookies, so these has to be explicitly mentioned as empty.
    # Here we have passed params but did not pass auth, auth has to be explicitly mentioned as empty
    # By default allow_redirects,stream,verify is set as true and timeout is set to 3 seconds.
    # If there is request read timeout,it returns 999.
    # 999 is taken as a custom exception because it is out of bound value in the response check function.
    def put(self, url,data={},allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.put(url,data=data,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
