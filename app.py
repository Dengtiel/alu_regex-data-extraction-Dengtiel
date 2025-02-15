from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Regular Expressions
regex_patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "url": r"https?://(?:www\.)?[a-zA-Z0-9./-]+",
    "phone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit_card": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "time": r"\b\d{1,2}:\d{2}(?::\d{2})?\s?(?:[APap][Mm])?\b",
    "date": r"\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b",
    "html_tag": r"<[^>]+>",
    "hashtag": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_data = {}
    if request.method == 'POST':
        text = request.form.get('text', '')
        for key, pattern in regex_patterns.items():
            extracted_data[key] = re.findall(pattern, text)
    
    return render_template('index.html', extracted_data=extracted_data)

if __name__ == '__main__':
    app.run(debug=True)
