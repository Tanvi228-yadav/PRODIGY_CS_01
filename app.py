from flask import Flask, render_template, request
from caesar_cipher import caesar_shift, emoji_to_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        mode = request.form.get("mode")
        theme = request.form.get("theme")
        shift = int(request.form.get("shift"))
        message = request.form.get("message")
        if mode == "e":
            if theme == "letters":
                result = caesar_shift(message, shift, theme='letters')
            elif theme == "emoji":
                result = caesar_shift(message, shift, theme='emoji')
        elif mode == "d":
            if theme == "letters":
                result = caesar_shift(message, shift, theme='letters', decrypt=True)
            elif theme == "emoji":
                result = emoji_to_text(message, shift)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)