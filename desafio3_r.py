class Jogo:
    def __init__(self, nome, idade, tipo):
        self.nome = nome 
        self.idade = idade
        self.tipo = tipo
       
 #sempre colocar o nome da função com o que ela faz
 #self é o objeto que está utilizando o método
 #Não preciso colocsr o tipo como parametro pois o objetivo é exatamente tornar isso mais flexivel, precisando apenas indicar o objeto 
 #Que criei com essa classe e que quero utilizar este metodo (função dentro da classe)
 #self.tipo acessa o aquela propriedade do objeto

    def tipo_ataque (self):

        match self.tipo:
            case "guerreiro":
             ataque = "espada"
            case "mago":
             ataque = "magia"
            case "monge":
             ataque = "artes marciais"
            case "arqueiro":
             ataque = "shuriken"
             #_ indica que qualquer outro valor que não esteja listado anteriormente     
            case _:
             ataque = "ataque misterioso "
   
        return ataque

        
    
 #Utilizo uma função detro classe para criar um método de apresentação universal. Criar ela dentro da classe torna 
 # o código mais legível e acessível, unindo todas as características do jogo


print("Bem vindo a batalha!")
print("Para melhor experiência digite as informações abaixo:")
name = input("Nome do jogador: ")
age = input("Idade do jogador: ")
#Não posso colocar "type" pois é um comando do python para identificar o tipo de dado
novo_ataque = "sim"
while True:
 # Converto para minusculo para padronizar a entrada
    hero = input("Tipo do jogador: ") .lower()
    jogador = Jogo(name, age, hero)

    forma_ataque = jogador.tipo_ataque() 

    print(f'O tipo {jogador.tipo} atacou usando {forma_ataque}')
    novo_ataque = input("Novo ataque?") 
    if novo_ataque.lower() == "não":
        break

    print("Digite as informações do novo ataque:")


print("Fim de jogo")