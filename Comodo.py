class Comodo :
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.__altura = 2.9
        self.largura = largura
        self.profundidade = profundidade

    @property
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print("valor informado para largura é inválido!")
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print("Valor informado para a profundidade é inválido")
            exit()