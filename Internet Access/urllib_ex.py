import urllib.request
import  webbrowser

x = urllib.request.urlopen('https://www.google.com/')
print("result code: " +str(x.getcode()))
print(x.read())
webbrowser.open('https://www.google.com/')