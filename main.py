from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Dictionery_index.html")

@app.route("/api/v1/<word>")
def dic_word(word):
    
    return {"Word": word,
                 "Definition": word.upper()}
if __name__ == "__main__":
    app.run(debug=True)
