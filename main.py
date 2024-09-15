from flask import *

# Flaskインスタンスの作成
app = Flask(__name__)

# ルートページのルーティング
@app.route('/')
def home():
    message = 'Top page'
    return render_template('index.html', message=message)

@app.route('/controll_stage/<path:contoroll_option>')
def controll(contoroll_option):
    return render_template("controll_stage.html")
@app.route('/messure_osiro/<path:mes_osiro_option>')
def messure_osiro(mes_osiro_option):
    return render_template("mes_osiro.html")

@app.errorhandler(404)
def take_care_404(error):
    return render_template("404.html",error=error)

# アプリの実行
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')