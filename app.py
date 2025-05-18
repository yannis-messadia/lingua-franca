from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    detected_lang = ''
    if request.method == 'POST':
        original_text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        try:
            if source_lang == 'auto':
                result = translator.translate(original_text, dest=target_lang)
            else:
                result = translator.translate(original_text, src=source_lang, dest=target_lang)

            translation = result.text
            if source_lang == 'auto':
                detected_lang = f"(Detected language: {result.src})"
        except Exception as e:
            translation = f"Erreur lors de la traduction : {str(e)}"

    return render_template('index.html', translation=translation, detected_lang=detected_lang)


if __name__ == '__main__':
    app.run(debug=True)
