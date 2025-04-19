from src.details.app import app

HOST='0.0.0.0'
DEBUG=True
PORT=8000

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
