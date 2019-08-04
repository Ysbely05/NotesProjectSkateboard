from flask import Flask
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.secret_key = "secret key"
# add the files to the "upload" folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Gives a max size od 16 MB per images/file
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

from app import routes