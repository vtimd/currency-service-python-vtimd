import requests
from xml.etree import ElementTree as ET
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/gbp/<float:usdvalue>")
def gbp(usdvalue):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    gbprate=subsubchild.attrib['rate']  

    usd = float(usdvalue) * float(gbprate)
    usdoutput = str(round(usd,2))        

#    print(usdoutput)
    return jsonify (usdoutput), 200

@app.route("/cad/<float:cadvalue>")
def cad(cadvalue):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'CAD':
                    cadrate=subsubchild.attrib['rate']

    cad = float(cadvalue) * float(cadrate)
    cadoutput = str(round(cad,2))        

#    print(cadoutput)
    return jsonify (cadoutput), 200 

@app.route("/jpy/<float:jpyvalue>")
def jpy(jpyvalue):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'JPY':
                    jpyrate=subsubchild.attrib['rate']  

    jpy = float(jpyvalue) * float(jpyrate)
    jpyoutput = str(round(jpy,2))        

#    print(jpyoutput)
    return jsonify (jpyoutput), 200 

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

