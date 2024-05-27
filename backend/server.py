from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def generate_triangle(number):
    number_str = str(number)
    result = []
    for i in range (1, len(number_str) + 1):
        result.append(number_str[:i])
    return '\n'.join(result)


@app.route('/triangle', methods=['POST'])
def triangle_route():
    data = request.get_json()
    number = data['number']
    if number is None:
        return jsonify({'error': 'Missing required parameter: number'}), 400
    return jsonify(generate_triangle(number))


def odd_number(max_number):
    max_number = int(max_number)
    result = [str(i) for i in range(1, max_number + 1, 2)]
    return ', '.join(result)

@app.route('/generate_odd', methods=['POST'])
def odd_number_route():
    data = request.get_json()
    number = data['number']
    result = odd_number(number)
    return jsonify(result)


def prime_number(max_number):
    max_number = int(max_number)
    primes = []
    for num in range(2, max_number + 1):
        if all(num % i !=0 for i in range(2, int(num**0.5) + 1)):
            primes.append(str(num))
    return ', '.join(primes)

@app.route('/generate_prime', methods=['POST'])
def prime_number_route():
    data = request.get_json()
    number = data['number']
    result = prime_number(number)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)