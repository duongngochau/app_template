import datetime
import json
import requests
from flask import render_template, redirect, request
from app import app

posts = []

@app.route('/')
def index():
    return render_template('index.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           readable_time=timestamp_to_string)

def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')