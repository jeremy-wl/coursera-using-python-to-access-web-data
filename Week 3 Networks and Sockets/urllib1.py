import urllib.request as ur

f = ur.urlopen('http://www.baidu.com')

for line in f:
    print(line.strip())

# urllib only gets the content of the file; headers are omitted.
