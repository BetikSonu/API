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
api = Api(app)          #-----------#
parser = reqparse.RequestParser()   #
#-----------------------------------#

kullanicilar = {
    '1': {'kullanici_adi': 'keyiflerolsun', 'mahalle': 'KekikAkademi', 'rutbe': 'root'},
    '2': {'kullanici_adi': 'raifpy', 'mahalle': 'KekikSiber', 'rutbe': 'python'},
    '3': {'kullanici_adi': 'ykslkrkci', 'mahalle': 'KekikSiber', 'rutbe': 'hain'},
    '4': {'kullanici_adi': 'Kullanici_bot', 'mahalle': 'KekikSiber', 'rutbe': 'BOT'}
}

class KullaniciListesi(Resource):
    def get(self):
        return kullanicilar

    def post(self):
        parser.add_argument('kullanici_adi')
        parser.add_argument('mahalle')
        parser.add_argument('rutbe')
        args = parser.parse_args()

        kullanici_id = int(max(kullanicilar.keys())) + 1
        kullanici_id = '%i' % kullanici_id

        kullanicilar[kullanici_id] = {
            'kullanici_adi': args['kullanici_adi'],
            'mahalle': args['mahalle'],
            'rutbe': args['rutbe']
        }

        return kullanicilar[kullanici_id], 201

api.add_resource(KullaniciListesi, '/kullanicilar/')

class Kullanici(Resource):
    def get(self, kullanici_id):
        if kullanici_id not in kullanicilar:
            return 'Kullanıcı Bulunamadı', 404
        else:
            return kullanicilar[kullanici_id]

    def put(self, kullanici_id):
        parser.add_argument('kullanici_adi')
        parser.add_argument('mahalle')
        parser.add_argument('rutbe')
        args = parser.parse_args()

        if kullanici_id not in kullanicilar:
            return 'Kayıt Bulunamadı', 404
        else:
            kullanici = kullanicilar[kullanici_id]
            kullanici['kullanici_adi'] = args['kullanici_adi'] if args['kullanici_adi'] is not None else kullanici['kullanici_adi']
            kullanici['mahalle'] = args['mahalle'] if args['mahalle'] is not None else kullanici['mahalle']
            kullanici['rutbe'] = args['rutbe'] if args['rutbe'] is not None else kullanici['rutbe']
            return kullanici, 200

    def delete(self, kullanici_id):
        if kullanici_id not in kullanicilar:
            return 'Bulunamadı', 404
        else:
            del kullanicilar[kullanici_id]
            return 'Kullanıcı Kaydı Silindi', 204

api.add_resource(Kullanici, '/kullanicilar/<kullanici_id>')

# https://addons.opera.com/tr/extensions/details/rested/

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#