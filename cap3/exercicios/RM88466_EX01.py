#1 – O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados quando estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão, você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos. Como não estudamos listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.

#Inputs
#Informe nome 
#Informe qual alimento ingeriu
#Informe qual a caloria do alimento

nameUsuario = str(input("Informe o seu nome: "))
nameAlimento_0 = str(input("Informe o nome do 1° alimento: "))
caloriaAlimento_0 = float(input("Informe o número (cal) calorias do alimento: "))
nameAlimento_1 = str(input("Informe o nome do 2° alimento: "))
caloriaAlimento_1 = float(input("Informe o número (cal) calorias do alimento: "))

totalCalorias = caloriaAlimento_0 + caloriaAlimento_1
print("Olá,", nameUsuario, "\n Você consumiu total: ", totalCalorias, "cal")
print("alimentos consumidos: \n", nameAlimento_0, "\n", nameAlimento_1)