# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------#
from flask import Flask                 #
from flask import jsonify,make_response #
from flask import request               #
from flask import send_from_directory   #
from time import strftime               #
#---------------------------------------#
from crawl.nobetciEczane import ECZANE  #
from crawl.udemyKupon import TR, EN     #
from crawl.mikropAdam import mikropAdam #
#---------------------------------------#

#-----------------------#
app = Flask(__name__)   #
#-----------------------#

hata = {
    'HATALI İSTEK!' : 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.',
    'nobetciEczane' : [{
        'istek > /dizin' : '/nobetciEczane/Canakkale/Merkez',
        'istek > ?argüman' : '/nobetciEczane?il=Canakkale&ilce=Merkez'
    }],
    'udemyKupon' : [{
        'istek > TR' : '/udemyKupon/TR?Sayfa=1',
        'istek > EN' : '/udemyKupon/EN?Sayfa=1'
    }],
    'mikropAdam' : [{
        'istek' : '/mikropAdam'
    }]
}

@app.route('/nobetciEczane/<il>/<ilce>', methods=['GET'])
def NobetciDizin(il,ilce):
    if not il or not ilce: return jsonify(hata)

    if ECZANE(il, ilce):
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), nobetciEczaneler=ECZANE(il, ilce))
    else: return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), nobetciEczaneler=[{"jajaja":"GÜLDÜK !"}])

@app.route('/nobetciEczane', methods=['GET'])
def NobetciArg():
    il = request.args.get('il')
    ilce = request.args.get('ilce')

    if not il or not ilce: return jsonify(hata)

    if ECZANE(il, ilce):
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), nobetciEczaneler=ECZANE(il, ilce))
    else: return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), nobetciEczaneler=[{"jajaja":"GÜLDÜK !"}])

@app.route('/udemyKupon/TR', methods=['GET'])
def UdemyTR():
    hangi_sayfa = request.args.get('Sayfa')

    try:
        hangi_sayfa = int(hangi_sayfa)
    except ValueError:
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=[{"jajaja":"GÜLDÜK !"}])
    except TypeError:
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=TR(1))

    return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=TR(hangi_sayfa))

@app.route('/udemyKupon/EN', methods=['GET'])
def UdemyEN():
    hangi_sayfa = request.args.get('Sayfa')

    try:
        hangi_sayfa = int(hangi_sayfa)
    except ValueError:
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=[{"jajaja":"GÜLDÜK !"}])
    except TypeError:
        return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=EN(1))

    return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), udemyKupon=EN(hangi_sayfa))

@app.route('/mikropAdam', methods=['GET'])
def MikropAdam():
    return jsonify(sunucu_saat=strftime('%d/%m %H:%M:%S'), mikropAdam=mikropAdam())

@app.route('/favicon.ico', methods=['GET'])
def Favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def Not_Found(error):
    return make_response(jsonify(hata), 404)

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#