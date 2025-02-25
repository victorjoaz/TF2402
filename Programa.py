def adicionar_produto(inventario, nome, preco, quantidade):
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}

def remover_produto(inventario, nome):
    if nome in inventario:
        del inventario[nome]
    else:
        print(f"Produto '{nome}' não encontrado no inventário.")

def listar_produtos(inventario):
    for nome, info in inventario.items():
        print(f"Nome: {nome}, Preço: R${info['preco']}, Quantidade: {info['quantidade']}")

def main():
    inventario = {}

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(inventario, nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto a remover: ")
            remover_produto(inventario, nome)
        elif opcao == '3':
            listar_produtos(inventario)
        elif opcao == '4':
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
