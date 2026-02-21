from flask import Flask, render_template, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    content = request.form['content']

    tex = r"""
\documentclass{article}
\usepackage{amsmath}
\begin{document}
""" + content + r"""
\end{document}
"""

    with open("output.tex","w",encoding="utf-8") as f:
        f.write(tex)

    subprocess.run(["pdflatex","output.tex"])

    return send_file("output.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run()