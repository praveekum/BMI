# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:44:19 2021

@author: prave
"""

from flask import Flask
app = Flask (__name__)
@app.route("/")
def hello():
    return "Hello World"
if __name__ == '__main__':
    app.run()    