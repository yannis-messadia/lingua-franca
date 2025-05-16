from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    if request.method == 'POST':
        original_text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        # La traduction sera ajoutée ici plus tard
        translation = f"(traduction simulée de: '{original_text}' vers {target_lang})"
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
