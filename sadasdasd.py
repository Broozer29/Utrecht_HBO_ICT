

from urllib.request import urlopen

hostname='0.0.0.0'
def httpconnect(action):
    url='http://{}/{}'.format(hostname,action)
    try:
        print(urlopen(url).read().decode())
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))
        exit()

def knopin():
    httpconnect('knopin')
def knopuit():
    httpconnect('knopuit')

httpconnect('')
while True:
    invoer=input()
    if invoer=='+':
        knopin()
    elif invoer=='-':
        knopuit()