class   Calculadora :
    __area_paredes: float
    __area_teto: float

    def calcular_area_parede (self, Comodo ) :
        self.__area_paredes = 2 * (Comodo.largura + Comodo.profundidade) * Comodo.altura
        return self.__area_paredes


    def calcular_area_teto ( self, Comodo) :
        self.__area_teto = Comodo.largura * Comodo.profundidade
        return self.__area_teto

    def calcular_litragem_necessaria (self) :
        if self.__area_teto <= 0 or self.__area_paredes <=0 :
            print("Não foi possivel calcular a quantidade de tinta cheque os valores passado e tente novamente!")
            exit()
        return (self.__area_teto + self.__area_paredes) / 10