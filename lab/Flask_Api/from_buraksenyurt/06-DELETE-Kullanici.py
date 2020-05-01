@app.route('/kekik/api/kullanicilar/<int:kullanici_id>', methods=['DELETE'])
def delete_kullanici(kullanici_id):
    kullanici = [kullanici for kullanici in kullanicilar if kullanici['id'] == kullanici_id]
    if len(kullanici) == 0:
        return jsonify({'Kullanıcı': 'Bulunamadı'}), 404
    kullanicilar.remove(kullanici[0])
    return jsonify({'Kullanıcı Silindi': kullanici})