from flask import Flask, render_template, request
import random
from collections import Counter

app = Flask(__name__)

# Fungsi bantu hitung statistik
def hitung_mean(data):
    return round(sum(data) / len(data), 2)

def hitung_median(data):
    data = sorted(data)
    n = len(data)
    tengah = n // 2
    if n % 2 == 0:
        return round((data[tengah - 1] + data[tengah]) / 2, 2)
    else:
        return data[tengah]

def hitung_modus(data):
    freq = Counter(data)
    max_freq = max(freq.values())
    modus = [k for k, v in freq.items() if v == max_freq]
    return modus[0] if len(modus) == 1 else modus

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    try:
        jumlah_data = int(request.form['jumlah'])
    except:
        jumlah_data = 10  # default jika tidak valid

    data = [random.randint(0, 100) for _ in range(jumlah_data)]
    mean = hitung_mean(data)
    median = hitung_median(data)
    modus = hitung_modus(data)
    minimum = min(data)
    maksimum = max(data)

    return render_template(
        'results.html',
        data=data,
        mean=mean,
        median=median,
        modus=modus,
        minimum=minimum,
        maksimum=maksimum
    )

if __name__ == '__main__':
    app.run(debug=True)
