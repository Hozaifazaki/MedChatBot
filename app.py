## Version 1 - before connexion
# from flask import Flask, render_template


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

### Version 2 - after adding connexion to connect the API
from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")  ## Create connexion app, specificatio_dir the path to swagger.yaml
app.add_api("swagger.yml")  ## Add the API file to the app


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)