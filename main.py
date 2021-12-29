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
    tempfilename = 'temp_heroes.png'
    try:
        pngfile = Image.open(filename)
        im_crop = pngfile.crop((42, 107, 488, 490))
        im_crop.save(tempfilename, quality=95)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)
    return send_file(tempfilename, mimetype='image/gif')

@app.route('/cards/image/<cardID>', methods=['GET'])
def get_cards_image_data(cardID):
    filename="cards_art/%s.png" % cardID.lower()
    tempfilename = 'temp_card.png'
    try:
        pngfile = Image.open(filename)
        im_crop = pngfile.crop((28, 36, 470, 695))
        im_crop.save(tempfilename, quality=95)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)
    return send_file(tempfilename, mimetype='image/gif')

@app.route('/hero_power/image/<cardID>', methods=['GET'])
def get_hero_power_image_data(cardID):
    filename="heroes_art/%s.png" % cardID.lower()
    tempfilename = 'temp_hp.png'
    try:
        pngfile = Image.open(filename)
        im_crop = pngfile.crop((35, 47, 476, 704))
        im_crop.save(tempfilename, quality=95)
    except Exception as e:
        return flask.make_response('Dude, why you asked me about <b>%s</b>? Idk this buddy..' % str(cardID), 404)

    return  send_file(tempfilename, mimetype='image/gif')


if __name__ == '__main__':
    app.run(host='192.168.192.133')
