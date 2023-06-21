print("=" * 10, " Игра Крестики-нолики для двух игроков ", "=" * 10)

board = list(range(1,10))

def draw_board(board): #функция отрисовывает игровое поле и нумерует клетки
   print("=" * 17)
   for i in range(3):
      print("||", board[0+i*3], "||", board[1+i*3], "||", board[2+i*3], "||")
      print("=" * 17)

def take_input(player_id): #функция отвечает за ввод данных и проверку, что введен порядковый номер клетки и клетка свободна
   valid = False
   while not valid:
      player_step = input("Введите номер клетки для хода " + player_id+"? ")
      player_step = int(player_step)
      if player_step >= 1 and player_step <= 9:#проверка, что номер клетки в нашем диапазоне 1-9
         if(str(board[player_step-1]) not in "XO"): #проверка, что клетка свободна
            board[player_step-1] = player_id
            valid = True
         else:
            print("Клетка занята, выберите другую клетку")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board): #функция определяет правила победы - перечисляет все варианты номеров клеток для победы - горизонталь или вертикаль или диагональ
   winner_cases = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for final in winner_cases:
       if board[final[0]] == board[final[1]] == board[final[2]]: #проверяем, если в каждой клетке из списка кейсов на победу значение одинаковое (или X или O), то значит победа у соотв игрока
          return board[final[0]] #функция возвращает код победителя (или X или O)
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)#вызываем функци отрисовки поля
        if counter % 2 == 0:#определяем чей ход. Первым всегда ходит X. Т.к. ходы должны чередоваться, то используем четность\нечетность
           take_input("X")#дописываем к приглашению код игрока (см в функции переменную player_id
        else:
           take_input("O")
        counter += 1
        if counter > 4:#проверяем, попал ли кто-то из игроков в список выигрышных кейсов. Минимальное количество ходов для победы =4
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

#input("Нажмите Enter для выхода!")