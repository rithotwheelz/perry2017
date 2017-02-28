from flask import Flask
from flask import render_template
from flask import jsonify
import num

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("table.html")

@app.route('/_thing', methods= ['GET'])
def thing():
    capVolt = num.getit()
    RPM = num.getit()
    motorTemp = num.getit()
    contCurr = num.getit()
    cTemp = num.getit()
    speed = num.getit()
    accel = num.getit()
    ksi = num.getit()

    packVolt = num.getit()
    packCurr = num.getit()
    soc = num.getit()
    hTemp = num.getit()
    aTemp = num.getit()
    lTemp = num.getit()
    bLev = num.getit()

    return jsonify(capVolt=capVolt, RPM=RPM, motorTemp=motorTemp, contCurr=contCurr, cTemp=cTemp, speed=speed, accel=accel, ksi=ksi, packVolt=packVolt, packCurr=packCurr, soc=soc, hTemp=hTemp, aTemp=aTemp, lTemp=lTemp, bLev=bLev)


if __name__ == '__main__':
    app.run()
