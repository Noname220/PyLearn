import random

from time import sleep

print ("Виберіть будь ласка: ")
print ("1  камінь")
print ("2  Папір")
print ("3  Ножиці")

player = int(input("Виберіть з 1-3: "))
pc = random.choice([1,2,3])
print ("PC choose: "+ str(pc))
if player == pc :
    print('DRAW!!!')
elif (player == 1 and pc ==3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
    print ("You WIN!!!")
elif (pc == 1 and player ==3) or (pc == 2 and player == 1) or (pc == 3 and player == 2):
    print('PC Win')













'''if player == 1:
    print ("Ви вибрали Камінь");
    sleep (2)
    print ("CPU вибирає Paper");
    sleep (.5)
    print ("Ви програли, і ви ніколи більше не виграєте!");

elif player == 2:
    print ("Ви вибрали Папір");
    sleep (2)
    print ("CPU вибирає Ножениці");
    sleep (.5)
    print ("Ви програли, і ви ніколи більше не виграєте!")

else:
    print ("Ви вибрали Ножниці");
    sleep (2)
    print ("CPU вибирає Камінь");
    sleep (.5)
    print ("Ви програли, і ви ніколи більше не виграєте!")'''