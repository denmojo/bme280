import subprocess
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

@app.route('/')
def index():
    return render_template('index.html', bme280_text=bme280_text())

@app.route('/chart_test')
def chart_test():
    return render_template('chart_test.html')

@app.route('/test_db')
def testdb():
    try:
        db.session.query('id').from_statement(text('select * from sensor_readings')).all()
        return '<h1>It Works™</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something broke</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

