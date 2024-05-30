import subprocess

resultado = subprocess.run(['python', '-c', codigo_python], capture_output=True, text=True)

# Verifica se a execução foi bem-sucedida
if resultado.returncode == 0:
    print("Código Python executado com sucesso:")
    print(resultado.stdout)
else:
    print("Erro ao executar o código Python:")
    print(resultado.stderr)
