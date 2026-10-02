from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('rectangulo'))

@app.route('/rectangulo', methods=['GET', 'POST'])
def rectangulo():
    area = None
    perimetro = None

    if request.method == 'POST':
        base = float(request.form['base'])
        altura = float(request.form['altura'])

        area = base * altura
        perimetro = 2 * (base + altura)

    return render_template('rectangulo.html',
area=area,
perimetro=perimetro)
if __name__ == '__main__':
    app.run(debug=True)