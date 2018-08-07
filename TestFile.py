from flask import Flask

APP = Flask(__name__)

@APP.route('/testfile', methods=['GET'])
def get_data():
    print('Dummy function..This is without updation')
    return "Hello..This is without updation"



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)
    APP.run()