import requests
from xml.etree import ElementTree as ET
from flask import Flask
app = Flask(__name__)

@app.route("/gbp")
def gbp():

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    gbprate=subsubchild.attrib['rate']   

    print(gbprate)
    return gbprate  

@app.route("/cad")
def cad():

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'CAD':
                    cadrate=subsubchild.attrib['rate']
    print(cadrate)
    return cadrate

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

