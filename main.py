from flask import *

from researchSupprortApp.api import api

# Flaskインスタンスの作成
app = Flask(__name__)

#apiサーバーの作成
app.register_blueprint(api)

# ルートページのルーティング
@app.route('/',endpoint="home")
def home():
    message = 'Top page'
    return render_template('index.html', message=message)

@app.route('/controll_stage/<path:contoroll_stage_option>',endpoint="controll_stage", methods=["GET","POST"])
def controll_stage(contoroll_stage_option):
    if request.method == "POST":
        do_val=request.form["action"]
        app.logger.debug(do_val)
        return redirect(url_for("controll_stage",contoroll_stage_option="home"))
    else:
        return render_template("controll_stage.html")
@app.route('/messure_osiro/<path:mes_osiro_option>',endpoint="messure_osiro")
def messure_osiro(mes_osiro_option):
    return render_template("mes_osiro.html")

@app.errorhandler(404)
def take_care_404(error):
    return render_template("404.html",error=error)

@app.route("/dev/<path:dev_path>")
def dev(dev_path):
    return render_template("dev.html")

# アプリの実行
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')