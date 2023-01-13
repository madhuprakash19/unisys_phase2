import xml.etree.ElementTree as ET
from copy import deepcopy

class parser:

    def parse(self,temp):
        try:
            return ET.fromstring(temp)
        except:
            return None

    def displayRoot(self,a):
        mytree = self.parse(a)
        if mytree==None:
            return a
        list=[]
        list.append(mytree.tag)
        return list

    def displayAllTag(self,a):
        myroot = self.parse(a)
        if myroot==None:
            return "There was error in parsing"
        elemList = []
        for elem in myroot.iter():
            elemList.append(elem.tag)

        temp = list(set(elemList))

        return temp

    def getDetails(self,a,tagName):
        mytree = self.parse(a)
        if mytree==None:
            return "There was error in parsing"
        x = mytree.findall('.//name')
        # for x in myroot.findall(tagName):
           # name =x.find('name').text
           # usn = x.find('usn').text
           # print(name, usn)
        elem = ET.parse('sample.xml')
        root = elem.getroot()
        ab = root.iterfind('name')
        print(ab)
        for i in ab(0):
            print(i)
        # def perf_func(elem, func, level=0):
        #     func(elem,level)
        #     for child in elem[0].getchildren():
        #         perf_func(child, func, level+1)
        #
        # def print_level(elem,level):
        #     print('-'*level+elem.tag)
        # root = ET.parse('sample.xml')
        # perf_func(root.getroot(), print_level)

    def findContent(self,a,tagname):
        root = self.parse(a)
        if root==None:
            return "There was error in parsing"
        def find(r1,tagname,content):
            if r1.tag == tagname:
                if len(r1.text):
                    content.append(deepcopy(r1.text))

            for i in r1:
                find(i,tagname,content)

        content = []
        find(root,tagname,content)
        return content


    def iterateOne(self,a,tagname):
        root = self.parse(a)
        if root==None:
            return "There was error in parsing"
        ans = {}
        def find(r1,tagname):
            print(r1.tag)
            if r1.tag == tagname:
                return r1

            for i in r1:
                res = find(i,tagname)
                if res!=None:
                    return res
            return None

        tag = find(root,tagname)
        print(tag)
        if tag == None:
            return None
        else:
            for i in tag:
                ans[i.tag] = i.text
        return ans


    def iterateAll(self,a,tagname):
        root = self.parse(a)
        if root==None:
            return "There was error in parsing"
        ans = []
        arrayoftags = []
        def find(r1,tagname,arrayoftags):
            if r1.tag == tagname:
                arrayoftags.append(deepcopy(r1))

            for i in r1:
                res = find(i,tagname,arrayoftags)
            return arrayoftags

        find(root,tagname,arrayoftags)
        if len(arrayoftags)>0:
            for i in arrayoftags:
                temp = {}
                for j in i:
                    temp[j.tag] = j.text
                ans.append(temp)

        return ans
