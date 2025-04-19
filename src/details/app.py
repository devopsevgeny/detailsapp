from flask import Flask, request, render_template
from src.details.libs import libs

app = Flask(__name__)


@app.route('/')
def detect_os():
    user_agent=request.headers.get('User-Agent')
    os_name = libs.parse_os(user_agent)
    return render_template('index.html', os=os_name)

