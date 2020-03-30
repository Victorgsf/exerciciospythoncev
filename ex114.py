import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.google.com")
except:
    print("Não foi possível acessar o site.")
else:
    print("Foi possível acessar o site.")