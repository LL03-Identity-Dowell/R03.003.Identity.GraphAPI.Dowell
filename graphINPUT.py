from flask import Flask , jsonify
#from flask import render_template
import matplotlib.pyplot as plt
import io
import base64
from random import sample
import pandas as pd

app = Flask(__name__)

@app.route('/plot/<col>/<row>')
def build_plot(col,row):
    img = io.BytesIO()
    df = pd.read_csv('data.csv')
    df.plot.bar(x = col, y = row)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url)

app.run()