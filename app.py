from flask import Flask, request, jsonify
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

@app.route('/tanglish', methods=['POST'])
def tanglish():
    data = request.get_json()
    tamil_text = data.get('text', '')
    tanglish_output = transliterate(tamil_text, sanscript.TAMIL, sanscript.ITRANS)
    return jsonify({'tanglish': tanglish_output})