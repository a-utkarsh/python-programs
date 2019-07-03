
import urllib.request

import re

url = 'https://www.tutorialspoint.com/python3/python_networking.htm'

urllist = re.findall(r"""<\s*a\s*href=["']([^=]+)["']""",
           urllib.request.urlopen(url).read().decode("utf-8"))

print(urllist)
