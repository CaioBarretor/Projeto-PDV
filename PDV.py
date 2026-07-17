Produtos = {}
Detalhe = "=" * 30

def gerenciar_produto():
    while True:
        print(Detalhe)
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Voltar ao menu principal")
        print(Detalhe)
        
        PerguntaGerenciar = input('> ')
        
        if PerguntaGerenciar == "1":
            ProdutoInserir = ""
            while ProdutoInserir != "voltar":
                print(Detalhe)
                print("Produtos cadastrados: " + "\n")
                for p, v in Produtos.items():
                    print(f"Produto: {p}, Valor: R${v:.2f}")
                print("Digite 'voltar' para voltar ao menu de gerenciar produtos.")
                print(Detalhe)
                
                ProdutoInserir = input("Digite o nome do produto: ").lower()
                if ProdutoInserir == "voltar":
                    continue
                else:
                    try:
                        ValorInserir = float(input("Digite o valor do produto: "))
                    except ValueError:
                        print("Coloque o valor no formato correto (ex: 10.50).")
                        continue
                    Produtos[ProdutoInserir] = ValorInserir
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
                if ProdutoRemover in Produtos:
                    del Produtos[ProdutoRemover]
                    print(f"Produto '{ProdutoRemover}' removido com sucesso.")
                else:
                    print(f"Produto '{ProdutoRemover}' não encontrado.")
        elif PerguntaGerenciar == "3":
            return menu()
        

def listar_produtos():
    print(Detalhe)
    print("Produtos cadastrados: " + "\n")
    for p, v in Produtos.items():
        print(f"Produto: {p}, Valor: R${v:.2f}")
    print(Detalhe)
    

def menu():
    while True:
        print(Detalhe)
        print("1 - Gerenciar Produto")
        print("2 - Listar Produtos")
        print("3 - Sair")
        print(Detalhe)
        
        MenuSelecao = input("Escolha uma opção: ")
        
        if MenuSelecao != "1" and MenuSelecao != "2" and MenuSelecao != "3":
            print("Opção inválida. Tente novamente.")
            return menu()
        elif MenuSelecao == "1":
            gerenciar_produto()
        elif MenuSelecao == "2":
            listar_produtos()
            return menu()
        elif MenuSelecao == "3":
            print("Saindo do programa...")
            exit()
        return MenuSelecao


menu()
