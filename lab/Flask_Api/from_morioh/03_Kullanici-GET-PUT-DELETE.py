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