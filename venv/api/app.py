from flask import Flask, request, jsonify, render_template
import re


app = Flask(__name__)
app.config["DEBUG"] = True


# Estrutura de saída JSON
resultado_verdadeiro = [{'output': 'True'},]
resultado_false = [{'output': 'False'},]


# Expressão regular que irá validar a string de entrada
expressao_regular = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()+-])[A-Za-z\d!@#$%^&*()+-]{9,}$"

@app.route('/', methods=['GET', 'POST'])
def api_all() -> Flask:

    # Validando condições
    if request.method == 'POST':

        # Input de senha no html
        campo_senha = request.form['senha']

        # Compilador do Regex
        compila_regex = re.compile(expressao_regular)

        # Variavel para validação da senha
        valida_senha = campo_senha

        # Lê o campo de senha e verifica se existe math com a expressão regular
        math = re.search(compila_regex, valida_senha)

        if len(valida_senha) == len(set(valida_senha)):                                         # verifica se  existe caracteres iguais, [a-z][A-Z][0-9][!@#$%^&*()+-]
            if math:                                                                            # Retorna True se os caracteres digitados batem com a expressão regular
                return render_template('index.html', output=resultado_verdadeiro), 200
            else:                                                                               # Retorna False se os caracteres não condizem com a expressão regular
                return render_template('index.html', output=resultado_false), 201
        else:                                                                                   # Return false se existir caracteres repetidos
            return render_template('index.html', output=resultado_false), 201
    return render_template('index.html'),201


if __name__ == '__main__':
    app.run()