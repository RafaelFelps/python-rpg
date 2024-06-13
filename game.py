import random

# Personagem: Classe mãe
# Herói: Controlado pelo usuario
# Inimigo: Adversário

class Personagem:
    def __init__(self, nome: str, vida: float, nivel: int):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano ):
        self.__vida -= int(dano)
        if self.__vida <= 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        return dano


class Heroi(Personagem):
    def __init__(self, nome: str, vida: float, nivel: int, habilidade: str):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
        return dano


class Inimigo(Personagem):
    def __init__(self, nome: str, vida: float, nivel: int, tipo: str):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"


class Jogo:
    """ Classe Orquestradora do Jogo """
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Maicao", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Escuridão")

        
    def iniciar_batalha(self):
        """" Fazer gestão da batalha em turnos """
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print("-----------------------------------")
            print(self.inimigo.exibir_detalhes())

            input("Pressione enter para atacar...\n")
            escolha = input("Escolha (1- Ataque normal, 2 - Ataque especial)\n")
            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Tente novamente!")

            if self.inimigo.get_vida() > 0:
                # Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("Parabéns, você venceu!")
        else:
            print("YOU DIED!")


# Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

