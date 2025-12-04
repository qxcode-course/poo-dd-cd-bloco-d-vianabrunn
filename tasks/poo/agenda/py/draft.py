class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId (self):
        return self.__id
        
    def getNumber (self):
        return self.__number
        
    def __str__(self):
        return f'{self.__id}:{self.__number}'
    
    
            



class Contatos:
    def __init__(self, nome: str):
        self.__fones: list[Fone]=[]
        self.__nome = nome
        self.__favoritos = False

    def getNome (self):
        return self.__nome
    
    def getFones(self):
        return self.__fones
    
    def getFav(self):
        return self.__favoritos

    def __str__(self):
        fones_str = ', '.join(str(f) for f in self.__fones)
        return f'{self.__nome} [{fones_str}]'
    
    def tFav(self):
        self.__favoritos = True
        
    def addFone (self, fone: Fone):
        self.__fones.append(fone)

    




class Agenda:
    def __init__(self): 
        self.__contatos: list[Contatos]=[]

    def getContatos (self):
        return self.__contatos
    
    def addContato (self, nome: str, fone: Fone):
        for contato in self.__contatos:
            if contato.getNome() == nome:
                contato.addFone(fone)
                return
        novo_contato = Contatos(nome)
        novo_contato.addFone(fone)
        self.__contatos.append(novo_contato)
        self.__contatos.sort(key=lambda c: c.getNome().lower())




    def rmFone(self, num: int, nome: str):
        for contato in self.__contatos:
            if contato.getNome() == nome:
                if 0 <= num < len(contato.getFones()):
                    contato.getFones().pop(num)
                else:
                    print("Índice inválido")
                return
        print("Contato não encontrado")


    def rmName(self, nome: str):
        for contato in self.__contatos:
            if contato.getNome() == nome:
                self.__contatos.remove(contato)
                return
        print("Contato não encontrado")
        self.__contatos.sort(key=lambda c: c.getNome().lower())
        

    def search(self, texto: str):
        texto = texto.lower()
        selecionados = []

        for contato in self.__contatos:

            sinal = "@ " if contato.getFav() else "- "
            nome = contato.getNome().lower()

            fones_str = ", ".join(
                f"{fone.getId().lower()}:{fone.getNumber()}"
                for fone in contato.getFones()
            )

            linha = f"{sinal}{nome} [{fones_str}]"

            if texto in linha:
                selecionados.append((contato, linha))

        selecionados.sort(key=lambda c: c[0].getNome().lower())

        return selecionados    
    

    def showFav(self):
        favoritos = [c for c in self.__contatos if c.getFav()]
        favoritos.sort(key=lambda c: c.getNome().lower())
        return favoritos


    def __str__(self):
        contatos_ordenados = sorted(self.__contatos, key=lambda c: c.getNome())
        return '\n'.join(f'{"@" if contato.getFav() else "-"} {str(contato)}' for contato in contatos_ordenados)
        
def main():
    agenda = Agenda()

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break

        if args[0] == "show":
            print(agenda)

        if args[0] == "add":
            nome = args[1]
            for fone_str in args[2:]:
                if ":" not in fone_str:
                    print(f"Erro: Fone '{fone_str}' inválido. Use formato id:num.")
                    continue
                id_fone, num = fone_str.split(":", 1)
                fone = Fone(id_fone, num)
                agenda.addContato(nome, fone)

        if args[0] == "rmFone":
            nome = args[1]
            num = int(args[2])
            agenda.rmFone(num, nome)

        if args[0] == "rm":
            nome = args[1]
            agenda.rmName(nome)

        if args[0] == "tfav":
            nome = args[1]
            for contato in agenda.getContatos():
                if contato.getNome() == nome:
                    contato.tFav()
                    break
            else:
                print("Contato não encontrado")

        if args[0] == "search":
            texto = args[1]
            resultados = agenda.search(texto)
            for contato, linha in resultados:
                print(linha)
        if args[0] == "favs":
            favoritos = agenda.showFav()
            for contato in favoritos:
                simbolo = "@"
                print(f"{simbolo} {contato}")

main()