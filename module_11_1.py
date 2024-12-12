import requests
from PIL import Image
'''from flask import Flask

app = Flask('example_site')
@app.route('/')
def open_web():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)       Это я пытался разобраться ещё и с Flask

r = requests.get('http://127.0.0.1:5000')
print(r.text)'''
information = {"name": "Nikita", "lesson": "one"}
headers = {'accept': '"!/!"', 'host': 'httnikita', 'user-agent': 'i sent request'}
r = requests.get('https://httpbin.org/get', params=information, headers=headers)
r.encoding = 'utf-8'
print(r.text)
# У этой библиотеки большой функционал, но для её полноценного использования, по крайней мере, нужно изучить информацию про сайты и URL
print(r.status_code)
print(r.url)



size = (3840, 2160)

image = Image.open('waterfall_precipice_sunlight_122934_3840x2400.jpg')
image.resize(size)
image.rotate(45, expand=True)
color = image.convert("L")
image.save('waterfall_precipice_sunlight_122934_3840x2400.png')
image.show()
color.show()

