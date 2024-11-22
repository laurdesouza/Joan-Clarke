def resumo():
    mensagem = "Joan Clark desempenhou um papel significativo na história da ciência da computação, especialmente no contexto da Segunda Guerra Mundial, como parte da equipe de decifradores de códigos em Bletchley Park, no Reino Unido. Ela trabalhou ao lado de figuras como Alan Turing no projeto de decodificação da máquina Enigma, usada pelos nazistas para criptografar suas comunicações. Clark, uma matemática brilhante, contribuiu com sua expertise para o desenvolvimento de métodos que ajudaram a automatizar a decifração de mensagens. Embora sua contribuição tenha sido ofuscada por preconceitos de gênero da época, ela foi peça-chave no processo de análise e organização dos dados gerados pelas máquinas de decifração, como a Bombe, inventada por Turing. Sua atuação em Bletchley Park ajudou a acelerar o fim da guerra, salvando milhões de vidas e estabelecendo fundamentos para o campo da criptografia e da computação moderna. Apesar de receber menos reconhecimento público do que alguns de seus colegas, seu trabalho exemplifica o papel vital das mulheres na ciência da computação desde suas origens."
    return mensagem


def doutorado():
    mensagem = "Joan Clarke (ou Joan Elisabeth Lowther Clarke) não tinha um doutorado. Ela se formou em matemática pela Universidade de Cambridge com destaque, obtendo um grau de primeira classe em 1939. No entanto, devido às políticas de gênero da época, Cambridge não conferia diplomas completos às mulheres, mesmo que elas tivessem alcançado resultados equivalentes aos de seus colegas homens. Apesar disso, Clarke demonstrou uma capacidade intelectual extraordinária e fez contribuições notáveis no campo da criptografia durante a Segunda Guerra Mundial. Seu trabalho em Bletchley Park, decifrando códigos da máquina Enigma, é amplamente reconhecido como uma contribuição crucial para os esforços de guerra dos Aliados."
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
