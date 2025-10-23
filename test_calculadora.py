import unittest
from calculadora import sumar, restar, multiplicar, dividir
from app import app

class TestCalculadora(unittest.TestCase):

    # === Pruebas unitarias ===
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 10)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    # === Pruebas de integración (API) ===
    def test_api_suma(self):
        tester = app.test_client(self)
        response = tester.post('/operar', json={"operacion": "sumar", "a": 4, "b": 6})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'10', response.data)

    def test_api_operacion_invalida(self):
        tester = app.test_client(self)
        response = tester.post('/operar', json={"operacion": "potencia", "a": 2, "b": 3})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
