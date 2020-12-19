import subprocess
import time
from subprocess import check_output
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def bme280_text():
    stdout = check_output(['./read_stats.sh']).decode('utf-8')
    return stdout

app = Flask(__name__)

db_name = 'environment_readings.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Reading(db.Model):
    __tablename__ = "sensor_readings"
    id = db.Column(db.Integer, primary_key=True)
    ctemp = db.Column(db.Float, unique=False, nullable=False)
    ftemp = db.Column(db.Float, unique=False, nullable=False)
    pressure = db.Column(db.Float, unique=False, nullable=False)
    humidity = db.Column(db.Float, unique=False, nullable=False)
    created_date = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html', bme280_text=bme280_text())

@app.route('/chart_test')
def chart_test():
    timestamp_labels = []
    tempf = []
    humidity = []
    pressure = []
    try:
        readings = db.session.query(Reading).limit(288).all()
        for reading in readings:
            unixtime = reading.created_date
            time_label = time.strftime('%H:%M:%S', time.localtime(float(unixtime)))
            timestamp_labels.append(time_label)
            tempf.append(round(float(reading.ftemp),1))
            humidity.append(round(float(reading.humidity),2))
            inpressure = round((float(reading.pressure) * 0.029529983071445),2) # mbar to inHg
            pressure.append(inpressure)

        return render_template('chart_test.html', timestamp_labels=timestamp_labels, temps=tempf, humids=humidity, press=pressure)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Error trying to retrieve data</h1>'
        return hed + error_text

@app.route('/test_db')
def testdb():
    try:
        readings = db.session.query(Reading).limit(288).all()
        return render_template('test_db.html', readings=readings)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something broke</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

