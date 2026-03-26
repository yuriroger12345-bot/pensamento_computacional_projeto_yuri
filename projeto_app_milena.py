'''

CRUD
Barbearia

 Organizar e gerenciar clientes, agendamentos
 e serviços por meio das operações de cadastro,
 consulta, atualização e exclusão de dados.


 
'''


nome_cliente = input('inserir seu nome:')


print(f'Olá, {nome_cliente}! Seja bem-vindo(a) a nossa barbearia!')




nome_cliente = input ('Digite sua senha para ter acesso ao menu:')
print('Acesso permitido')
print ("escolha_menu")

print("\n=== BARBEARIA ===")
print("1. Cadastrar Cliente")
print("2. Agendar Serviço")
print("3. Meus Agendamentos")
print("4. Serviços e Preços")
print("5. Escolher Barbeiro")
print("6. Histórico e Pagamentos")
print("7. Avaliações")
print("8. Notificações")
print("0. Sair")

while True:

   escolha_menu = input("\nEscolha uma opção: ")

   if escolha_menu == '1':
   
      
    nome_cliente = input("Digite o nome do cliente: ")
    telefone_cliente = input("Digite o telefone do cliente: ")
    conta_cliente = input("Digite seu E-mail para concluir cadastro:")
    print("Cliente cadastrado com sucesso!")

   elif escolha_menu =='2':

        print("Agendar Serviço")  
        nome_cliente = input("Escolha o serviço que você deseja:")

        print("Corte")
        print("Barba")
        print("Luzes")
        print("Platinado")
        print("Alisamento")
        print("Corte infantil")
        print("Barboterapia")
        print("Limpeza de pele")
        print("Pezinho")
        print("Pigmentção")
        print("Hidratração Capilar")


        nome_cliente = input("produtos que o cliente prefere:")

   elif escolha_menu == '3':

        print("Meus Agendamentos")
        nome_cliente = input("digite o nome do cliente para exibir agenda:")
        
        print("08:00")
        print("09:00")
        print("10:00")
        print("11:00")
        print("12:00")
        print("13:00")
        print("14:00")
        print("15:00")
        print("16:00")
        print("17:00")
        print("18:00")
        print("19:00")
        print("20:00")

        nome_cliente = input("Selecione o horario que você deseja:")


        senha_cliente = input("digite a senha do cliente para confirmar o horário agendado:")
        print("Tudo certo! Seu horário está confirmado.")

   elif escolha_menu == '4':

        print("Serviços e Preços")
        print("1. Corte: 30.00")
        print("2. Barba: 20.00")
        print("3. Corte + Barba: 45.00")
        print("4. Luzes: 75.00")
        print("5. Platinado: 100.00")
        print("6. Alisamento: 70.00")
        print("7. Corte Infantil: 20.00")
        print("8. Barboaterapia: 120.00")
        print("9. Limpeza de pele: 65.00")
        print("10. Pezinho: 15.00")
        print("11. Pigmentação: 25.00")
        print("12. Hidratação Capilar: 40.00 ")

        nome_cliente = input("Digite a numeração que corresponde a sua escolha:")
        print("perfeito,seu agendamento foi marcado com sucesso")

   elif escolha_menu == '5':
        print("Escolher Barbeiro")
        print("1. Barbeiro Allan")
        print("2. Barbeiro Yuri")
        print("3. Barbeira Milena")
        nome_cliente = input("Digite o nome do barbeiro da sua preferência:")
        print("Barbeiro confirmado com sucesso.")

   elif escolha_menu == '6':

        print("Pagamentos")
        nome_client = input("escolha sua forma de pagamento")
        print("1. Debito 2. Crédito ou 3.pix")

        nome_cliente = input("Digite a numeração desejada: ")
        print("Forma de pagamento selecionada")
        print("Pagamento Confirmado")

        

   elif escolha_menu == '7':

        print("Avaliações")
        nome_cliente = input("digite o nome do barbeiro (ex: Barbeiro Allan) para avaliar o serviço:")
        avaliacao_cliente = input("digite sua avaliação (1 a 5 estrelas):")

   elif escolha_menu == '8':
        print("Notificações")
        nome_cliente = input("digite o nome do cliente para exibir notificações:")

   elif escolha_menu == '0':

        print("Saindo do sistema. Até logo!")
        

   else:
        print("Opção inválida. Por favor, tente novamente.")





