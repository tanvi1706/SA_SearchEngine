from flask import Flask, render_template, request
from circularShift import circularShift 
from sorting import sortThem
app = Flask(__name__)
cs_lines = []
temp_list = []
objt = circularShift()

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/circular-shift', methods=['POST'])
def circular_shifting():
    global temp_list
    line = request.form['line'] # request.json['key']
    temp_list = objt.circular(line)
    return render_template('cs-template.html', currData=temp_list)

@app.route('/alphabetize', methods=['GET'])
def sortLines():
    # print(temp_list)
    cs_lines.extend(temp_list)
    # print(cs_lines)
    cs_line = sortThem.alphabetize(cs_lines)
    return render_template('sorted.html', data=cs_line)
