@app.route('/kekik/api/kullanicilar/<int:kullanici_id>', methods=['GET'])
def get_kullanici(kullanici_id):
    kullanici = [kullanici for kullanici in kullanicilar if kullanici['id'] == kullanici_id]
    if len(kullanici) == 0:
        return jsonify({'Kullanıcı': 'Bulunamadı'}), 404
    return jsonify({'Kullanıcı': kullanici})