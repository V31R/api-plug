# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
