from collections import OrderedDict


class Auxiliar:
    def __init__(self, verbo):
        self.sufixo = verbo[-2:]
        self.verbo = verbo
        self.pessoas = ["eu", "tu", "ela/ele", "nós", "vós", "elas/eles"]

        if self.sufixo not in ['ar', 'er', 'ir']:
            print("Sua palavra não é um verbo")

    def resposta(self, irregulares, sufixos):
        conjugado = OrderedDict()
        if self.verbo not in irregulares:

            radical = self.verbo[:-2]

            for pessoa, sufixo in zip(self.pessoas, sufixos):
                conjugado[pessoa] = f"{radical}{sufixo}"

        else:
            for pessoa, verbo in zip(self.pessoas, irregulares[self.verbo]):
                conjugado[pessoa] = verbo

        return conjugado

    
class Indicativo(Auxiliar):
    def presente(self):
        irregulares = {}

        if self.sufixo == 'ar':
            irregulares["dar"] = ["dou", "dás", "dá", "damos", "dais", " 	dão"]
            irregulares["estar"] = [
                "estou",
                "estás",
                "está",
                "estamos",
                "estais",
                "estão",
            ]
            irregulares["passear"] = [
                "passeio",
                "passeias",
                "passeia",
                "passeamos",
                "passeais",
                "passeiam",
            ]
            irregulares["averiguar"] = [
                "averíguo",
                "averíguas",
                "averígua",
                "averiguamos",
                "averiguais",
                "averíguam",
            ]

            sufixos = ["o", "as", "a", "amos", "ais", "am"]

        elif self.sufixo == 'er':
            sufixos = ["o", "es", "e", "emos", "eis", "em"]
        elif self.sufixo == 'ir':
            sufixos = ["o", "es", "e", "mos", "is", "em"]

        return self.resposta(irregulares, sufixos)

    def pret_per(self):
        irregulares = {}
        radical = self.verbo[:-2]

        if self.sufixo == 'ar':
            irregulares["dar"] = [
                "dei",
                "deste",
                "deu",
                "demos",
                "destes",
                "deram",
            ]
            irregulares["estar"] = [
                "estive",
                "estiveste",
                "esteve",
                "estivemos",
                "estivestes",
                "estiveram",
            ]
            irregulares["passear"] = [
                "passeei",
                "passeaste",
                "passeou",
                "passeamos",
                "passeastes",
                "passearam",
            ]

        elif self.sufixo == 'er':
            sufixos = ["i", "este", "eu", "emos", "estes", "eram"]
        elif self.sufixo == 'ir':
            sufixos = ["i", "iste", "iu", "imos", "istes", "iram"]

        return self.resposta(irregulares, sufixos)

    def pret_imper(self):
        irregulares = {}

        if self.sufixo == 'ar':
            sufixos = ["ava", "avas", "ava", "ávamos", "áveis", "avam"]
        elif self.sufixo == 'er':
            sufixos = ["ia", "ias", "ia", "íamos", "íeis", "iam"]
        elif self.sufixo == 'ir':
            sufixos = ["ia", "ias", "ia", "íamos", "íeis", "iam"]

        return self.resposta(irregulares, sufixos)

    def pret_maisque(self):
        irregulares = {}

        if self.sufixo == 'ar':
            sufixos = ["ara", "aras", "ara", "áramos", "áreis", "aram"]
        elif self.sufixo == 'er':
            sufixos = ["era", "eras", "era", "êramos", "êreis", "eram"]
        elif self.sufixo == 'ir':
            sufixos = ["ira", "iras", "ira", "íramos", "íreis", "iram"]

        return self.resposta(irregulares, sufixos)

    def futuro_pres(self):
        irregulares = {}

        if self.sufixo == 'ar':
            sufixos = ["arei", "arás", "ará", "aremos", "areis", "arão"]
        elif self.sufixo == 'er':
            sufixos = ["erei", "erás", "erá", "eremos", "ereis", "erão"]
        elif self.sufixo == 'ir':
            sufixos = ["irei", "irás", "irá", "iremos", "ireis", "irão"]

        return self.resposta(irregulares, sufixos)

    def futuro_pret(self):
        irregulares = {}

        if self.sufixo == 'ar':
            sufixos = ["aria", "arias", "aria", "aríamos", "aríeis", "ariam"]
        elif self.sufixo == 'er':
            sufixos = ["eria", "erias", "eria", "eríamos", "eríeis", "eriam"]
        elif self.sufixo == 'ir':
            sufixos = ["iria", "irias", "iria", "iríamos", "iríeis", "iriam"]

        return self.resposta(irregulares, sufixos)


class Subjuntivo(Auxiliar):
    def __init__(self, verbo):
        super().__init__(verbo)
        
        self.sufixo = verbo[-2:]
        self.pessoas = ["que eu", "que tu", "que ela/ele", "que nós", "que vós", "que elas/eles"]

    def presente(self):  # que eu xurugue
        self.radical = self.verbo[:-2]
        irregulares = {}

        if self.sufixo == 'ar':
            if self.radical[-1] == "g" or self.radical[-1] == "q":
                sufixos = ["ue", "ues", "ue", "uemos", "ueis", "uem"]
            else:
                sufixos = ["e", "es", "e", "emos", "eis", "em"]

        elif self.sufixo == 'er':
            sufixos = ["a", "as", "a", "amos", "ais", "am"]
        
        elif self.sufixo == 'ir':
            sufixos = ["a", "as", "a", "amos", "ais", "am"]

        return self.resposta(irregulares, sufixos)

    def preterito_imperfeito(self):  # se eu xurugasse
        irregulares = {}

        if self.sufixo == 'ar':
            sufixos = ["asse", "asses", "asse", "ássemos", "ásseis", "assem"]

        elif self.sufixo == 'er':
            sufixos = ["esse", "esses", "esse", "êssemos", "êsseis", "essem"]

        elif self.sufixo == 'ir':
            sufixos = ["isse", "isses", "isse", "íssemos", "ísseis", "issem"]

        return self.resposta(irregulares, sufixos)

    def futuro(self):  # quando eu xurugar
        irregulares = {}

        if self.sufixo == "ar":
            sufixos = ["ar", "ares", "ar", "armos", "ardes", "arem"]

        elif self.sufixo == "er":
            sufixos = ["er", "eres", "er", "ermos", "erdes", "erem"]

        elif self.sufixo == "ir":
            sufixos = ["ir", "ires", "ir", "irmos", "irdes", "irem"]
        return self.resposta(irregulares, sufixos)

# class Imperativo(Auxiliar):
#     def afirmativo():
#         pass
#     def negativo():
#         pass
#     def infinitivo():
#         pass
