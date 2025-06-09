from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode="encrypt", emoji_mode=False):
    def shift_char(c, s):
        if c.isalpha():
            a = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - a + s) % 26 + a)
        return c

    result = ""
    if mode == "decrypt":
        shift = -shift

    for c in text:
        if emoji_mode and c.isalpha():
            emojis = ['😀','😁','😂','🤣','😃','😄','😅','😆','😉','😊','😋','😎','😍','😘','😗','😙','😚','🙂','🤗','🤩','🤔','🤨','😐','😑','😶','🙄']
            idx = (ord(c.lower()) - ord('a') + shift) % 26 if c.isalpha() else 0
            result += emojis[idx] if c.isalpha() else c
        else:
            result += shift_char(c, shift)
    return result

@app.route('/', methods=["GET", "POST"])
def index():
    result = ""
    input_text = ""
    shift = 3
    emoji_mode = False
    action = "encrypt"
    if request.method == "POST":
        input_text = request.form.get("inputText", "")
        shift = int(request.form.get("shift", 3))
        emoji_mode = bool(request.form.get("emojiMode"))
        action = request.form.get("action", "encrypt")
        result = caesar_cipher(input_text, shift, action, emoji_mode)
    return render_template("index.html", result=result, input_text=input_text, shift=shift, emoji_mode=emoji_mode, action=action)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)