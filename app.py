from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    shape = None
    values = {}

    if request.method == 'POST':
        shape = request.form.get('shape')
        
        try:
            if shape == 'kubus':
                values['sisi'] = int(request.form.get('sisi', 0))
                result = values['sisi'] ** 3
            elif shape == 'balok':
                values['panjang'] = int(request.form.get('panjang', 0))
                values['lebar'] = int(request.form.get('lebar', 0))
                values['tinggi'] = int(request.form.get('tinggi', 0))
                result = values['panjang'] * values['lebar'] * values['tinggi']
            elif shape == 'tabung':
                values['radius'] = float(request.form.get('radius', 0))
                values['tinggitab'] = float(request.form.get('tinggitab', 0))
                result = 3.14159 * (values['radius'] ** 2) * values['tinggitab']
        except ValueError:
            result = "Error: Masukkan angka yang valid!"
    
    return render_template('index.html', result=result, shape=shape, values=values)

if __name__ == '__main__':
    app.run(debug=True)
