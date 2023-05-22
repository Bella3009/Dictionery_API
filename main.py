from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1/<word>")
def dic_word(word):
    word = word.lower()
    resDict = data.loc[data["words"] == word]["definition"].squeeze()
    print(resDict)
    return {"Word": word,
            "Definition": resDict}

if __name__ == "__main__":
    app.run(debug=True)