import subprocess
from subprocess import check_output
from flask import Flask, render_template

def bme280_text():
    stdout = check_output(['./read_stats.sh']).decode('utf-8')
    return stdout

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', bme280_text=bme280_text())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

