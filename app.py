from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

url_database = {}

def generate_short_url(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    if long_url:
        short_url = generate_short_url(long_url)
        url_database[short_url] = long_url
        return render_template('shortened.html', short_url=short_url)
    else:
        return redirect('/')

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('not_found.html')

if __name__ == '__main__':
    app.run(debug=True)
