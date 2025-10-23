from flask import Flask, request, jsonify
import calculadora

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a la API de la Calculadora!"

@app.route("/operar", methods=["POST"])
def operar():
    data = request.json
    op = data.get("operacion")
    a = data.get("a")
    b = data.get("b")

    try:
        if op == "sumar":
            resultado = calculadora.sumar(a, b)
        elif op == "restar":
            resultado = calculadora.restar(a, b)
        elif op == "multiplicar":
            resultado = calculadora.multiplicar(a, b)
        elif op == "dividir":
            resultado = calculadora.dividir(a, b)
        else:
            return jsonify({"error": "Operación no válida"}), 400

        return jsonify({"resultado": resultado})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
