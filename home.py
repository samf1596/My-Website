import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")