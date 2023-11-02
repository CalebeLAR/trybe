import subprocess


class ParaFixar:
    def Exercício01():
        """Escreva uma nova função de teste no arquivo test_analyzer.py que
        passe pela linha 11 do arquivo analyzer.py do exemplo, garantindo 100%
        de cobertura de testes."""
        comando = "python3 -m pytest --cov analyzer --cov-report=term-missing"
        try:
            resultado = subprocess.check_output(
                comando, shell=True, stderr=subprocess.STDOUT, text=True
            )
            print(resultado)
        except subprocess.CalledProcessError as e:
            return f"Erro ao executar o comando: {e}"
