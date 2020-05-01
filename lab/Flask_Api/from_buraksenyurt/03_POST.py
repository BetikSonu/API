@app.route('/kekik/api/kullanicilar', methods=['POST'])
def post():
    yeniKullanici = {
        'id': kullanicilar[-1]['id'] + 1,
        'kullanici_adi': request.json['kullanici_adi'],
        'mahalle': request.json['mahalle'],
        'rutbe': request.json['rutbe'],
    }
    kullanicilar.append(yeniKullanici)
    return jsonify({'kullanici': yeniKullanici}), 201