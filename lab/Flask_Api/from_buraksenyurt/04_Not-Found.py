@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'HTTP 404 Error': 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.'}), 404
    )