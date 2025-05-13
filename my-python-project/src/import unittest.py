import unittest
from my_python_project.src.app import gerar_estrofe, gerar_estrofe_modernizada, TEMAS_DETALHADOS # type: ignore

# filepath: my-python-project/src/test_app.py

class TestGerarEstrofe(unittest.TestCase):
    def test_gerar_estrofe_alternative_rock(self):
        subgenero = "Alternative Rock"
        tipo = "verso"
        linhas = 4
        estrofe, tipo_retorno = gerar_estrofe(subgenero, tipo, linhas)
        self.assertEqual(tipo_retorno, tipo)
        self.assertEqual(len(estrofe), linhas)
        for linha in estrofe:
            self.assertTrue(len(linha) > 0)

    def test_gerar_estrofe_indie_rock(self):
        subgenero = "Indie Rock"
        tipo = "verso"
        linhas = 4
        estrofe, tipo_retorno = gerar_estrofe(subgenero, tipo, linhas)
        self.assertEqual(tipo_retorno, tipo)
        self.assertEqual(len(estrofe), linhas)
        for linha in estrofe:
            self.assertTrue(len(linha) > 0)

    def test_gerar_estrofe_post_rock(self):
        subgenero = "Post-Rock"
        tipo = "verso"
        linhas = 4
        estrofe, tipo_retorno = gerar_estrofe(subgenero, tipo, linhas)
        self.assertEqual(tipo_retorno, tipo)
        self.assertEqual(len(estrofe), linhas)
        for linha in estrofe:
            self.assertTrue(len(linha) > 0)

class TestGerarEstrofeModernizada(unittest.TestCase):
    def test_gerar_estrofe_modernizada_alternative_rock(self):
        subgenero = "Alternative Rock"
        linhas = 4
        frases, esquema = gerar_estrofe_modernizada(subgenero, linhas)
        self.assertEqual(len(frases), linhas)
        self.assertIn(esquema, ["ABAB", "AABA", "ABCD"])
        for frase in frases:
            self.assertTrue(len(frase) > 0)

    def test_gerar_estrofe_modernizada_indie_rock(self):
        subgenero = "Indie Rock"
        linhas = 4
        frases, esquema = gerar_estrofe_modernizada(subgenero, linhas)
        self.assertEqual(len(frases), linhas)
        self.assertIn(esquema, ["ABAB", "AABA", "ABCD"])
        for frase in frases:
            self.assertTrue(len(frase) > 0)

    def test_gerar_estrofe_modernizada_post_rock(self):
        subgenero = "Post-Rock"
        linhas = 4
        frases, esquema = gerar_estrofe_modernizada(subgenero, linhas)
        self.assertEqual(len(frases), linhas)
        self.assertIn(esquema, ["ABAB", "AABA", "ABCD"])
        for frase in frases:
            self.assertTrue(len(frase) > 0)

if __name__ == "__main__":
    unittest.main()