from .spirit import Spirits

def game_loop (spirit: Spirits):
    print("Welcome to Spirit Game")
    
    while True:
        print(''''Что вы хотите сделать? 
              1 - покормить духа
              2 - уложить спать 
              3 - помедитировать 
              4 - поиграть 
              5 - посмотреть статусы
              0 - выйти из игры''')
        
        choice = int(input("Действие: "))
        
        if choice == 1:
            spirit.feed()
        elif choice == 2:
            spirit.sleep()
        elif choice == 3:
            spirit.meditate()
        elif choice == 4:
            spirit.play()
        elif choice == 5:
            print(spirit)
            print(spirit.stats)
        elif choice == 0:
            print("Ну ты и слабак что сдаешься. Щас твой питомец умрет")
            break 
        else:
            print("Неправльно, попробуй еще раз, вдруг получится правльно попасть в клавишу")