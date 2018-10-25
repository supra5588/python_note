from bs4 import BeautifulSoup

myHtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hahahahaha</title>
</head>
<body>
<h1>This is h1</h1>
<h1>This is another h1 tag</h1>
<h2>This is H2</h2>
<p>This is Lin</p>
</body>
</html>"""

myparser = BeautifulSoup(myHtml, 'html.parser')  # parser = 解析

myh1 = myparser.findAll('h1')
for i in myh1:
    # if "another" in i.string:
        print(i.string)
