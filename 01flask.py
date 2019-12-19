from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='./', static_folder="", static_url_path="")


@app.route("/")
def main():
    return render_template("mainHtml.html")


if __name__ == "__main__":
    app.run(host='222.27.166.198', port=10001)