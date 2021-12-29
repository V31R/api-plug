# coding=<UTF-16>
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flask

from PIL import Image
from flask import send_file

from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/heroes/image/<cardID>', methods=['GET'])
def get_hero_image_data(cardID):
    filename="heroes_art/%s.png" % cardID.lower()
    try:
        pngfile = Image.open(filename)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)

    im_crop = pngfile.crop((42, 107, 488, 490))
    tempfilename='temp_heroes.png'
    im_crop.save(tempfilename, quality=95)
    return  send_file(tempfilename, mimetype='image/gif')

@app.route('/cards/image/<cardID>', methods=['GET'])
def get_cards_image_data(cardID):
    filename="cards_art/%s.png" % cardID.lower()
    try:
        pngfile = Image.open(filename)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)

    im_crop = pngfile.crop((28, 36, 470, 695))
    tempfilename='temp_card.png'
    im_crop.save(tempfilename, quality=95)
    return  send_file(tempfilename, mimetype='image/gif')

@app.route('/hero_power/image/<cardID>', methods=['GET'])
def get_hero_power_image_data(cardID):
    filename="heroes_art/%s.png" % cardID.lower()
    try:
        pngfile = Image.open(filename)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)

    im_crop = pngfile.crop((35, 47, 476, 704))
    tempfilename='temp_hp.png'
    im_crop.save(tempfilename, quality=95)
    pngfile = Image.open(tempfilename)
    print(pngfile.size, pngfile.format)
    return  send_file(tempfilename, mimetype='image/gif')


if __name__ == '__main__':
    app.run(host='192.168.192.133')
