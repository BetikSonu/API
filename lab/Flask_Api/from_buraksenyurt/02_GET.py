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

kullanicilar = [
    {'id': 1000,'kullanici_adi': 'keyiflerolsun','mahalle': 'KekikAkademi','rutbe': 'root'},
    {'id': 1001,'kullanici_adi': 'raifpy','mahalle': 'KekikSiber','rutbe': 'python'},
    {'id': 1002,'kullanici_adi': 'ykslkrkci','mahalle': 'KekikSiber','rutbe': 'hain'},
    {'id': 1003,'kullanici_adi': 'Kullanici_bot','mahalle': 'KekikSiber','rutbe': 'BOT'},
]

@app.route('/kekik/api/kullanicilar', methods=['GET'])
def get():
    return jsonify({'kullanicilar': kullanicilar})

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#