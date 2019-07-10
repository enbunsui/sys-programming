# -*- conding:utf-8 -*-

#文字列処理
s = "Hello"
s = 'Howdy'
print(s)

s = "Hello"
s = 'h' + s[1:]
print(s)

s = "Hello"
#s[0]='h' #文字列の場合、indexで変更できません!!!!
print(s[0])

s = "Hello"
s = s.lower()
print(s)

print('e' in s)
print('e' == s)
print(s.find("xy"))

#リスト処理
l = ['a','b','c']
print(l)

l = ['C','D','E']
print(l)

l = ['a','b','c']
l = ['GGG'] + l[1:]
print(l)

l = ['a','b','c']
l[0] = '0000'
print(l)

l = ['a','b','c']
l.append("yyyyy")
print(l)

l = ['a','b','c']
l.insert(0,"ssssss")
print(l)

#最後の項目
l = ['a','b','c']
l.pop()
print(l)


#何が違い？
del l[2]
l.pop(1)
print(c)

l = ['a','b','c']
if "a" in l:
    print("OK")



#FOR 0から右端含まない
for i in range(10):
    print(i)

for i in (0,7):
    tem = int(input())
    print(tem)

#リスト処理
l = [5,9,6,7,8]
l.append(["a","b"])
l.extend(["c","d"])
print(l)


#リスト処理 ソート
l = [5,9,6,7,8]
l.sort()
print(l)


l = [[5,9,6,7,8],[1,2,3],[121,12,13]]
def getSotKey(l):
    print(l[2])
    return  l[2]

l.sort(key=getSotKey)
print(l)





#fix_first
def fix_first(s):
    f = ""
    for i in range(len(s)):
        if i != 0 and s[0] == s[i] :
            f = f + "*"
        else:
            f = f + s[i]
    return f

print(fix_first("not aaa bnandn"))


#not_bad.py
def not_bad(s):
    str = ""
    i = 0
    notIndex = s.find("not")
    badIndex = s.find("bad")
    if notIndex < badIndex:
        str = s[notIndex + 3:].replace("bad","good")
        return  s[0 : notIndex + 3] + str
    else:
        return s

print(not_bad("bad not is "))
print(not_bad(" not is bad"))

#match_end.py
def match_end(s):
    strCount = 0
    for str in s:
        #2文字以上
        if len(str) >= 2:
            if str[0] == str[-1]:
                strCount += 1
    return strCount

print(match_end(["","aba","xx","bngghh","sdfds"]))

print(match_end(["","aba","","",""]))


#front_x.py
def front_x(x):	
    l = list(x)
    l.sort(key=lambda s:s.startswith("x"),reverse=True)
    return l

#front_x.py
def front_x(x):	
    l = list(x)
    return  sorted()

print(front_x(['bbb',	'ccc',	'axx',	'xzz',	'xaa']))	
print(front_x(['ccc',	'bbb',	'aaa',	'xcc',	'xaa']))	
print(front_x(['mix',	'xyz',	'apple',	'xanadu',	'aardvark']))

l = [1,2,2,2,2]
print(l)


#remove_adjacent.py
def remove_adjacent(li):	
    reList = []
    for str in list(li):
        if li.count(str) > 1:
            li.remove(str)
    return li

print(remove_adjacent([1,	2,	2,	3]))	
print(remove_adjacent([2,	2,	3,	3,	3]))	
print(remove_adjacent([]))	

#linear_merge.py
def linear_merge(li1,	li2):	
    l = li1 + li2
    l.sort()
    return l

print(linear_merge(['aa',	'xx',	'zz'],	['bb',	'cc']))	
print(linear_merge(['aa',	'xx'],	['bb',	'cc',	'zz']))	
print(linear_merge(['aa',	'aa'],	['aa',	'bb',	'bb']))

#辞書
ip_adrs = {'dis.ac.jp':	'175.184.120.230',	'g.dis.ac.jp':	'210.190.118.224'}
for i in ip_adrs.keys():
    print(i)

 #辞書
ip_adrs = {'dis.ac.jp':	'175.184.120.230',	'g.dis.ac.jp':	'210.190.118.224'}
for i in ip_adrs.values():
    print(i)

#辞書
ip_adrs = {'dis.ac.jp':	'175.184.120.230',	'g.dis.ac.jp':	'210.190.118.224'}
for i in ip_adrs.items():
    print(i)

 #ファイル処理
def file_open_read(fileName):
     f = open(fileName)
     str = f.read()
     print(str)
     f.close()


path = "C:/Users/user/Desktop/workspace/doc/sysp/test.txt"
file_open_read(path)



 #ファイル処理
def file_open_readline(fileName):
     f = open(fileName)
     while True:
         str = f.readline()
         if not str:
            f.close()
            break
         else:
            print(str.strip())


path = "C:/Users/user/Desktop/workspace/doc/sysp/test.txt"
file_open_readline(path)

 #ファイル処理
def file_open_readlines(fileName):
     f = open(fileName)
     str = f.readlines()
     for i in str:
         print(i.strip())

path = "C:/Users/user/Desktop/workspace/doc/sysp/test.txt"
file_open_readlines(path)



 #ファイル処理書込み
def file_open_write(fileName):
     f = open(fileName,mode="w")
     str = f.write("test")
     f.close()


path = "C:/Users/user/Desktop/workspace/doc/sysp/test.txt"
file_open_write(path)

#fizz_buzz 作成
def test(a):
    l = {"15":"aaa","5":"bbb","3":"ccc"}
    for i in l.keys():
        while (a % int(i) == 0):
             return l[i]
    return a


print(test(30))
print(test(1))
print(test(3))
print(test(5))
print(test(15))
print(test(16))

lst = [1,2,3,4]

def f(n):
    return n * 3

print([f(x) for x in lst  if f(x) % 2 == 0])

print([y for y in (f(x) for x in lst) if y % 2 == 0])

#事前定義済み
print(list(filter(lambda y: y % 2 == 0, map(f, lst))))




#fizz_buzz 作成
def test(a):
    l = {"15":"aaa","5":"bbb","3":"ccc"}
    for i in l.keys():
        while (a % int(i) == 0):
             return l[i]
    return a

def test(a):
    la = {3:"aaa",5:"bbb",15:"ccc"}
    fa = map(lambda x:x,la)
    fl = filter(lambda y :a % y == 0,la)
    try:
       ll = list(fl)
       print(ll[len(ll) - 1])
       print(la[ll[len(ll) - 1]])
    except :
       print("")
    

print(test(30))


print(test(1))
print(test(3))
print(test(5))
print(test(15))



def fb(n):
    dic = {15:"FizzBuzz",5:"Buzz",3:"Fizz"}
    try:
       ll = list(filter(lambda x : n % x == 0, map(lambda k:k,dic.keys())))
       return dic[ll[0]]
    except :
       return ""

i = 1
while i <= 200:
    print(i,fb(i))
    i = i + 1




ls = [1,2,3]
ls.insert(0,5)
print(ls)


a = "{:02d}{}".format(1000,"hello")
print(a)


a = "{:+012.3f}{}".format(5,"hello")
print(a)

for i in range(10):
    print(i)

def vlen(a, b):
    return len(a) - len(b)



ls = ["aaa","ddddddd","ccc","edssee","ffsdddddddddddf","dsdfsfdd","f333333ff"]
sorted(ls,cmp=lambda a,b : len(a) - len(b))

print(ls)


dic = {1:"a",2:"b"}

for i in dic.keys():
    print(i)


for i in dic.values():
    print(i)

for k,v in dic.items():
    print(k,'>',v)



import sys

if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1],"rU")
    except IOError:
        print("Sorry, the file " + sys.argv[1] + " does not exist.",    file=sys.stderr)
        sys.exit(1)
else:
    f = sys.stdin


#ファイルのテスト
def test(li):
    sum = 0
    index = 0
    for i in li:
        if i != 7:
            sum += i
            index += 1
        else:
            if index + 1 <= len(li) - 1:
                li[index + 1] = li[index + 1] * 2
                sum += i
    return sum

print(test([1,7,7,6,9]))
print(test([1,7,7,6,9]))
print(test([1,1,1,1,1]))


import re

str = "c,2,a,b,c,9"
pattern = re.compile("\d")
ret = pattern.match(str)
print(ret)
ret = re.search("\d",str)
print(ret.group())


import re

p = re.compile("[012345678]")
r = p.search("234")
print(r.group())
all = p.findall("234")
print(all)
tt = p.match("234")
print(tt)

p = re.compile("(aa|bb)test")
r = p.search("ffftest")
if not r == None :
    print(r.group())

r1 = p.search("bbtest.git")
if not r1 == None :
    print(r1.group())



f = re.sub(p,"cc","bbtestaatestPcccc")
print(f)


class A:
    def __init__(self):
        self.parm1 = "1"
        self.parm2 = "2"

    def  test(self):
        print("12345")

a = A()
a.test()

p = re.compile("aa*")
r = p.search("bbbaaaa")
print(r.group())
