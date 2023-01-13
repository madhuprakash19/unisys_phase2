import json







# displayRoot
# displayAllTag
# findContent
# iterateOne
# iterateAll

class Parser:

    def load(self,temp):
        try:
            return json.loads(temp)
        except:
            return None


    def normal(self,a):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"
        

    def displayRoot(self,a):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"
        print(y)
        return list(y.keys())


    def displayAllKey(self,a):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"
        ls = []
        def recursive_items(dictionary):
            for key, value in dictionary.items():
                if type(value) is dict:
                    yield (key, value)
                    yield from recursive_items(value)
                else:
                    yield (key, value)


        for key, value in recursive_items(y):
            ls.append(key)
        return list(set(ls))

    def findContent(self,a,tag):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"
        def myprint(y,tag,arr):
            for k, v in y.items():
                if isinstance(v, dict):
                    #if list of dict...then check like above loop...nd pass
                    #each nested dict to find the content
                    #json_response2
                    myprint(v,tag,arr)
                else:
                    if k == tag:
                        arr.append(v)
        arr = []
        myprint(y,tag,arr)
        return arr

    def iterateAll(self,a,tag):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"

        def myprint(y,tag,arr):
            for k, v in y.items():
                if isinstance(v, dict):
                    print(v)
                    if k == tag:
                        arr.append(y)
                    myprint(v,tag,arr)

        arr = []
        myprint(y,tag,arr)
        return arr


    def iterateOne(self,a,tag):
        y = self.load(a)
        if y==None:
            return "There was error in parsing"
        def myprint(y,tag,k):
            if k == tag:
                return y
            for k, v in y.items():
                if k==tag:
                    return v
                if isinstance(v, dict):
                    res = myprint(v,tag,k)
                    if res!=None:
                        return res
            return None

        return myprint(y,tag,'')
