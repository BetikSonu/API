#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    # Kaynak : https://morioh.com/p/35f9f2f16908

#---------------------------------------------------#
from flask import Flask                             # ## pip install flask
from flask_restful import Resource, Api, reqparse   # ## pip install flask-restful
#---------------------------------------------------#

#-----------------------#
app = Flask(__name__)   #
api = Api(app)          #
#-----------------------#


# Çokomelli İşler


#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#