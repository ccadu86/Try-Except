
while True:  # Inicia um loop infinito, para continuar pedindo entrada até que uma divisão válida seja realizada.
    try:  # Inicia o bloco onde exceções serão monitoradas.
        a = int(input('Numerador: '))  # Solicita ao usuário o numerador da divisão.
        b = int(input('Denominador: '))  # Solicita ao usuário o denominador da divisão.
        r = a / b  # Realiza a divisão entre a e b e armazena o resultado em r.
        print(f'O resultado é {r:.2f}')  # Imprime o resultado da divisão formatado com duas casas decimais.
        break  # Interrompe o loop, caso a divisão tenha sido realizada com sucesso.
    except Exception as erro:  # Captura qualquer exceção que ocorra no bloco try e a associa a uma variável erro.
        print(f'Problema encontrado foi {erro.__class__}')  # Imprime a classe da exceção que ocorreu.

        
    
