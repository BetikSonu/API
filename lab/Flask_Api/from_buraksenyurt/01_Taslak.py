#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    # Kaynak : https://www.buraksenyurt.com/post/python-ile-rest-tabanli-servis-gelistirmek

#-----------------------------------#
from flask import Flask, jsonify    #
from flask import make_response     #
from flask import request           #
#-----------------------------------#

#-----------------------#
app = Flask(__name__)   #
#-----------------------#


# Çokomelli İşler


#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#