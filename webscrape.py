# import requests
# req = requests.request('GET', 'https://itsmycode.com/importerror-no-module-named-requests/')
# print(req)


#imports library which contains a open url method
from urllib.request import urlopen
#sets the url equal to something
url = "https://itsmycode.com/importerror-no-module-named-requests/"
#opens the page
page = urlopen(url)

# prints the html of the page so a person knows what to look for i
#could also inspect
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

# string method
#finds the html index of the title of the url
title_index=html.find("<title>")
end_index = html.find("</title>")
title=title = html[title_index:end_index]
print(title)

