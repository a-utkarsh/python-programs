from kivy.app import App
from kivy.uix.label import Label
import nmap
import json
class SimpleKivy(App):

    def build(self):

        nm = nmap.PortScanner()
        a= nm.scan('google.com','80-81')
        print a

        return(Label(text =str(a)))


if __name__ == "__main__":
    SimpleKivy().run()
