import time  # Importa a biblioteca time, que é usada para adicionar atrasos no programa, simulando o tempo de processamento e melhorando a experiência do usuário.

Produtos = {
    "arroz": 10.50,
    "feijão": 8.75,
    "macarrão": 5.25,
    "açúcar": 4.00,
    "sal": 2.50,
}  # Estrutura usada para simular um banco de dados de produtos, onde a chave é o nome do produto e o valor é o preço do produto.
Detalhe = (
    "=" * 80
)  # Detalhe usado para separar as seções do programa e deixar a interface mais organizada.
LimparConsole = (
    "\n" * 100
)  # Usado para deixar o console limpo e organizado, simulando o efeito de limpar a tela do console.


def Encerrar():  # Função usada para encerrar o programa de forma organizada, exibindo mensagens de despedida e agradecimento ao usuário.
    print(LimparConsole)
    print("Saindo do programa...")
    time.sleep(2)
    print(LimparConsole)
    print("Obrigado por utilizar o programa!")
    exit()


def FecharVenda(
    ProdutosVendidos,
):  # Função usada para fechar a venda, exibindo o valor total da venda e as opções de pagamento disponíveis.
    print(LimparConsole)
    print(Detalhe)
    ProdutoNaVenda(ProdutosVendidos)
    print("\n" + "-" * 80)
    print(
        f"Valor total da venda: R${sum(Produtos[p] * q for p, q in ProdutosVendidos.items()):.2f}"
    )
    print("\n" + "-" * 80)
    print("Formas de pagamento:")
    print("1 - Dinheiro")
    print("2 - Cartão de crédito")
    print("3 - Cartão de débito")
    print("4 - Pix")
    print("\n" + "-" * 80)
    print(
        "Digite 'pagar'para para pagar: (Digite 'voltar' para voltar ao menu principal ou 'sair' para sair do programa)"
    )

    Pagamento = input("> ").lower()

    if Pagamento == "pagar":
        print(LimparConsole)
        print("Pagamento realizado com sucesso!")
        time.sleep(2)
        print(LimparConsole)
        print("Voltando ao menu principal...")
        time.sleep(2)
        print(LimparConsole)
        return menu()
    elif Pagamento == "voltar":
        return menu()
    elif Pagamento == "sair":
        Encerrar()


def GerenciarProdutos():  # Função usada para gerenciar os produtos cadastrados no sistema, permitindo adicionar ou remover produtos.
    while True:
        print(LimparConsole)
        print(Detalhe)
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Voltar ao menu principal")
        print(Detalhe)

        PerguntaGerenciar = input("> ")

        if PerguntaGerenciar == "1":
            ProdutoInserir = ""  # Inicializa a variável ProdutoInserir como uma string vazia, que será usada para armazenar o nome do produto a ser adicionado ao sistema.
            while ProdutoInserir != "voltar":
                print(Detalhe)
                print("Produtos cadastrados: " + "\n")
                for p, v in Produtos.items():
                    print(
                        f"Produto: {p}, Valor: R${v:.2f}"
                    )  # Exibe a lista de produtos cadastrados no sistema, mostrando o nome do produto e o valor correspondente.
                print("Digite 'voltar' para voltar ao menu de gerenciar produtos.")
                print(Detalhe)

                ProdutoInserir = input(
                    "Digite o nome do produto: "
                ).lower()  # Solicita ao usuário que digite o nome do produto a ser adicionado ao sistema, convertendo o nome para letras minúsculas para padronização.

                if ProdutoInserir == "voltar":
                    continue
                else:
                    try:  # Solicita ao usuário que digite o valor do produto a ser adicionado ao sistema, convertendo o valor para float para permitir cálculos futuros.
                        ValorInserir = float(
                            input("Digite o valor do produto: ")
                        )  # Solicita ao usuário que digite o valor do produto a ser adicionado ao sistema, convertendo o valor para float para permitir cálculos futuros.
                    except (
                        ValueError
                    ):  # Trata a exceção caso o usuário digite um valor inválido, exibindo uma mensagem de erro e solicitando que o usuário digite o valor novamente.
                        print(
                            "Coloque o valor no formato correto (ex: 10.50)."
                        )  # Exibe uma mensagem de erro caso o usuário digite um valor inválido, solicitando que o usuário digite o valor novamente.
                        continue
                    Produtos[ProdutoInserir] = (
                        ValorInserir  # Adiciona o produto e o valor ao dicionário Produtos, permitindo que o produto seja vendido no sistema.
                    )
            else:
                print("Voltando ao menu de gerenciar produtos...")
                continue
        elif PerguntaGerenciar == "2":
            print(Detalhe)
            print("Produtos cadastrados: " + "\n")
            for p, v in Produtos.items():
                print(f"Produto: {p}, Valor: R${v:.2f}")
            print("Digite 'voltar' para voltar ao menu de gerenciar produtos.")
            print(Detalhe)

            ProdutoRemover = input("Digite o nome do produto a ser removido: ").lower()

            if ProdutoRemover == "voltar":
                continue
            else:
                if (
                    ProdutoRemover in Produtos
                ):  # Verifica se o produto digitado pelo usuário está cadastrado no sistema, permitindo que o produto seja removido caso esteja presente.
                    del Produtos[
                        ProdutoRemover
                    ]  # Remove o produto do dicionário Produtos, permitindo que o produto não seja mais vendido no sistema.
                    print(
                        f"Produto '{ProdutoRemover}' removido com sucesso."
                    )  # Exibe uma mensagem de sucesso caso o produto seja removido com sucesso, informando ao usuário que o produto foi removido do sistema.
                else:
                    print(
                        f"Produto '{ProdutoRemover}' não encontrado."
                    )  # Exibe uma mensagem de erro caso o produto digitado pelo usuário não esteja cadastrado no sistema, informando ao usuário que o produto não foi encontrado.
        elif PerguntaGerenciar == "3":
            return menu()


def ListarProdutos():  # Função usada para listar os produtos cadastrados no sistema, exibindo o nome do produto e o valor correspondente.
    print(Detalhe)
    print("Produtos cadastrados: " + "\n")
    for p, v in Produtos.items():
        print(
            f"{p}      R${v:.2f}"
        )  # Exibe a lista de produtos cadastrados no sistema, mostrando o nome do produto e o valor correspondente.
    print(Detalhe)


def ProdutoNaVenda(
    ProdutosVendidos,
):  # Função usada para listar os produtos que estão sendo vendidos no momento, exibindo o nome do produto, a quantidade vendida e o valor total da venda.
    for p, q in ProdutosVendidos.items():
        print(
            f"{q}*   {p}    R${Produtos[p] * q:.2f}   Unitário: R${Produtos[p]:.2f}"
        )  # Exibe a lista de produtos que estão sendo vendidos no momento, mostrando a quantidade vendida, o nome do produto, o valor total da venda e o valor unitário do produto.


def pdv():  # Função usada para simular o ponto de venda (PDV) do sistema, permitindo que o usuário selecione os produtos a serem vendidos, informe a quantidade e finalize a venda.
    ProdutosVendidos = {}
    while True:
        print(LimparConsole)
        print("Produtos do sistema:")
        ListarProdutos()  # Exibe a lista de produtos cadastrados no sistema, mostrando o nome do produto e o valor correspondente.
        print(Detalhe)
        print("Produtos na venda:")
        ProdutoNaVenda(
            ProdutosVendidos
        )  # Exibe a lista de produtos que estão sendo vendidos no momento, mostrando a quantidade vendida, o nome do produto, o valor total da venda e o valor unitário do produto.
        print(Detalhe)
        print(
            "\nDigite o nome do produto a ser vendido ('fechar venda' para encerrar a venda ou 'voltar' para retornar ao menu): "
        )

        ProdutoVenda = input("> ").lower()

        if ProdutoVenda == "fechar venda":
            FecharVenda(ProdutosVendidos)
        if ProdutoVenda not in Produtos:
            while (
                ProdutoVenda not in Produtos
            ):  # Verifica se o produto digitado pelo usuário está cadastrado no sistema, caso não esteja, solicita que o usuário digite novamente o nome do produto a ser vendido.
                time.sleep(1.3)
                print("Produto não encontrado. Tente novamente.")
                print(LimparConsole)
                print(
                    "Digite o nome do produto a ser vendido ('sair' para encerrar a venda ou 'fechar venda' para fechar a venda):"
                )

                ProdutoVenda = input("> ").lower()
                if ProdutoVenda == "sair":
                    Encerrar()
                elif ProdutoVenda == "fechar venda":
                    FecharVenda(ProdutosVendidos)
        elif ProdutoVenda == "voltar":
            return menu()
        else:
            try:
                ProdutoQuatidade = float(input("Digite a quantidade do produto: "))
            except ValueError:
                print("Coloque a quantidade no formato correto (ex: 2.5).")
                continue
            ProdutosVendidos[ProdutoVenda] = ProdutoQuatidade


def menu():  # Função usada para exibir o menu principal do sistema, permitindo que o usuário escolha entre gerenciar produtos, listar produtos, acessar o PDV ou encerrar o programa.
    while True:
        print(Detalhe)
        print("1 - Gerenciar Produto")
        print("2 - Listar Produtos")
        print("3 - PDV")
        print("4 - Sair")
        print(Detalhe)

        MenuSelecao = input("Escolha uma opção: ")

        if (
            MenuSelecao != "1"
            and MenuSelecao != "2"
            and MenuSelecao != "3"
            and MenuSelecao != "4"
        ):  # Verifica se a opção escolhida pelo usuário é válida, caso não seja, exibe uma mensagem de erro e solicita que o usuário escolha novamente.
            print("Opção inválida. Tente novamente.")
            return menu()
        elif MenuSelecao == "1":
            print(LimparConsole)
            GerenciarProdutos()
        elif MenuSelecao == "2":
            print(LimparConsole)
            ListarProdutos()
            return menu()
        elif MenuSelecao == "3":
            print(LimparConsole)
            pdv()
        elif MenuSelecao == "4":
            Encerrar()
        return MenuSelecao


menu()
