from flask import Flask, render_template, request, send_file
import subprocess

app = Flask(__name__)
import tempfile
import os

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

    with tempfile.TemporaryDirectory() as tempdir:
        tex_path = os.path.join(tempdir, "output.tex")

        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex)

        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "output.tex"],
            cwd=tempdir
        )

        pdf_path = os.path.join(tempdir, "output.pdf")
        return send_file(pdf_path, as_attachment=True)
if __name__ == "__main__":
    app.run()