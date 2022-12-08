def menuPrincipal():
    while True:
        escolha = input(
        """
        0- Finalizar o Programa
        1- Cadastrar Estados
        2- Cadastrar Cidades
        3- Relacionar Estado com Cidade
        4- Relatório de Estados
        5- Relatório de Cidades
        6- Atualizar números de casos
        Escolha:
        """
        )

        if escolha == '0': break
        elif escolha == '1': cadastrar_estado()
        elif escolha == '2': cadastrar_cidade()
        elif escolha == '3': relacionar_est_cid()
        elif escolha == '4': relatorio_estados()
        elif escolha == '5': relatorio_cidades()
        elif escolha == '6': atualizar_casos()
        else:
            input("\n> Escolha inválida. [Enter]")

lst_estados = []
lst_cidades = []


class Estado():
    def __init__(self, nome_estado, sigla_estado):
        self.nome_estado = nome_estado
        self.sigla_estado = sigla_estado
        self.cidades_estado = []

    def validar_tam_sigla(self):
        return not len(self.sigla_estado.strip()) > 3
        
    def tem_mesmo_nome(self,outro_estado):
        esse_nome = self.nome_estado.strip().lower()
        outro_nome = outro_estado.nome_estado.strip().lower()
        if esse_nome == outro_nome:
            return True
        return False
    
    def tem_mesma_sigla(self,outro_estado):
        return self.sigla_estado.strip().lower() == outro_estado.sigla_estado.strip().lower()

    def validar_estado(self,outro_estado):
        mesmo_nome = self.tem_mesmo_nome(outro_estado)
        mesma_sigla = self.tem_mesma_sigla(outro_estado)
        return not (mesmo_nome or mesma_sigla)

    def __eq__(self,outro_estado):
        return self.nome_estado == outro_estado.nome_estado

    def __repr__(self):
        return f'{self.nome_estado} - {self.sigla_estado}'

    def adicionar_cidade(self, cidade):
        self.cidades_estado.append(cidade)


class Cidade():
    
    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.qt_casos_cidade = 0

    def __eq__(self,outra_cidade):
        return self.nome_cidade.strip().lower() == outra_cidade.nome_cidade.strip().lower()

    def __repr__(self):
        return f'{self.nome_cidade}'

    def atualizar_casos(self,valor):
        if valor >= 0:
            self.qt_casos_cidade += valor;


def cadastrar_estado():
    mostrar_estados_cadastrados()
    while True: 
        nome = input("Informe o nome do Estado:")
        sigla = input("Informe a sigla do Estado:")
        estado = Estado(nome_estado=nome,sigla_estado=sigla)
        if not estado.validar_tam_sigla():
           print("Sigla inválida")
           continue
        else:
            if not lst_estados:
                lst_estados.append(estado)
                break
            else:    
                existe_estado = False
                for i in range(len(lst_estados)):
                    if not existe_estado:
                        if not estado.validar_estado(lst_estados[i]):
                            print("Nome ou/e sigla já existente")
                            existe_estado = True
                if existe_estado:
                    continue
                else:
                    lst_estados.append(estado)
                    return
                       

def cadastrar_cidade():
    mostrar_cidades_cadastradas()
    nome = input("Informe o nome da Cidade:")
    cidade = Cidade(nome_cidade=nome)
    lst_cidades.append(cidade)

def mostrar_cidades_cadastradas():
    print("\nCidades cadastradas")
    for cidade in lst_cidades:
        print(cidade)    

def mostrar_estados_cadastrados():
    print("\nEstados cadastrados")
    for estado in lst_estados:
        print(estado)

def escolher_cidade():
    nome = input("Digite o nome da cidade escolhida:")
    cidade = Cidade(nome)
    for i in range(len(lst_cidades)):
        if(cidade == lst_cidades[i]):
            return lst_cidades[i]
        else:
            continue
    return Cidade("")

def escolher_estado():
    nome = input("Digite o nome do estado escolhido:")
    estado = Estado(nome,"")
    for i in range(len(lst_estados)):
        if(estado == lst_estados[i]):
            return lst_estados[i]
        else:
            continue
    return Estado("","")
1

def relacionar_est_cid():
    mostrar_cidades_cadastradas()
    mostrar_estados_cadastrados()
    cidade = escolher_cidade()
    if(cidade.nome_cidade == ""):
        print("Cidade não cadastrada. Favor escolher uma cidade cadastrada")
        input("[Enter] Retorna ao menu.")
    else:
        estado = escolher_estado()
        if(estado.nome_estado == ""):
            print("Estado não cadastrado. Favor escolher um estado cadastrado")
            input("[Enter] Retorna ao menu.")
        else:
            estado.adicionar_cidade(cidade)
            print(f'Cidade {cidade.nome_cidade} vinculada ao Estado {estado.nome_estado}')

def relatorio_estados():
    print("\t=-=-=-=-=- Relatório do Estados:")
    for estado in lst_estados:
        total_de_casos = 0
        for cidade in estado.cidades_estado:
            total_de_casos += cidade.qt_casos_cidade
        print("\t--> {:<20} - total de Casos: {:<5}".format(estado.nome_estado, total_de_casos))
    input("[Enter] Retorna ao menu.")

def relatorio_cidades():
    print("\t=-=-=-=-=- Relatório do Cidades:")
    for cidade in lst_cidades:
        print("\t--> {:<20} - total de Casos: {:<5}".format(cidade.nome_cidade, cidade.qt_casos_cidade))
    input("[Enter] Retorna ao menu.")

def atualizar_casos():
    print("Escolha a cidade dentre as abaixo para atualizar a quantidade de casos.")
    mostrar_cidades_cadastradas()
    cidade = escolher_cidade()
    qtde = int(input("Informe a quantidade a ser atualizada:"))
    cidade.atualizar_casos(qtde)

if __name__ == "__main__":
    menuPrincipal()