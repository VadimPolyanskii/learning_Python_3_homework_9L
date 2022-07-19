import random
import numpy as np
import pandas as pd
# import self as self


class MakePlayers:
    def __init__(self,
                 cards4plaer,
                 humans,
                 robots,
                 mincars4plaer,
                 maxcars4plaer,
                 minplaers,
                 sizecoloda,
                 startpole
                 ):
        """
        Вспомогательный класс к классу class Durack
        для создания игроков через метод maker_players()
        """
        self.MAX_PLAYERS = None
        self.CARDS_4PLAYER = cards4plaer
        self.humans = humans
        self.robots = robots
        self.MINCARDS_4PLAER = mincars4plaer
        self.MAXCARDS_4PLAER = maxcars4plaer
        self.MIN_PLAYERS = minplaers
        self.QQUANTY_COLODA = sizecoloda
        self.START_pole = startpole

    def __call__(self):
        players, cards4plaer = self.maker_players()
        return players, cards4plaer

    @property
    def opros(self):
        """
        Функция опросом устанавливает
        CARDS_4PLAYER - количество карт у игроков по игре
        hum - количество человек в игре
        rob - количество роботов в игре
        """
        err_h = True
        err_r = True
        err_cards = True

        # определение CARDS_4PLAYER
        while err_cards:
            if not self.CARDS_4PLAYER:  # and self.CARDS_4PLAYER is not None:
                try:
                    self.CARDS_4PLAYER = int(input(
                        f"Укажите количество карт выдаваемых на руки от {self.MINCARDS_4PLAER} до {self.MAXCARDS_4PLAER} включительно: "))
                    # проверка на вхождение в диапазон
                    if self.CARDS_4PLAYER is not None \
                            and self.MINCARDS_4PLAER <= self.CARDS_4PLAYER <= self.MAXCARDS_4PLAER:
                        err_cards = False
                    # else:
                    # pass
                except:
                    print("Ошибка, укажите число карт")
                    pass
            else:
                if self.CARDS_4PLAYER is None:
                    pass
                elif not type(self.CARDS_4PLAYER) == int:
                    print("Ошибка, укажите число карт")
                    self.CARDS_4PLAYER = None
                    pass
                else:
                    err_cards = False

        # определение MAX_PLAYERS
        self.MAX_PLAYERS = self.QQUANTY_COLODA // self.CARDS_4PLAYER
        # если что-то из self.humans or и self.robots не задано

        if (not self.humans and self.humans != 0) or not (self.robots and self.robots != 0):
            # определение self.humans
            while err_h and err_r:
                print(
                    f"Количество участников (роботы и люди) должно быть в сумме не менее {self.MIN_PLAYERS} и не более {self.MAX_PLAYERS}")
                while err_h:
                    if not self.humans and self.humans != 0:  # если self.humans не зздан ранее
                        try:
                            self.humans = int(input('Введите количество игроков людей: '))
                            err_h = False  # выход
                        except:
                            print("Ошибка, укажите число человек")
                            pass
                    else:  # если self.humans зздан то проверка
                        if type(self.humans) == int:  # если self.humans число
                            print(f'Количество людей уже задано - {self.humans}')
                            err_h = False  # выход

                        else:  # если self.humans не число
                            print("Ошибка, укажите число человек")
                            self.humans = None  # сброс self.humans

                # определение self.robots
                if not self.robots and self.robots != 0:  # если self.robots не зздан ранее
                    while err_r:
                        try:
                            self.robots = int(input('Введите количество игроков роботов: '))
                            err_r = False  # выход
                        except:
                            print("Ошибка, укажите число роботов")
                            pass
                else:  # если self.robots задан то проверка
                    if type(self.robots) == int:
                        print(f'Количество роботов уже задано - {self.robots}')
                        err_r = False  # выход

                    else:  # если self.robots не число
                        print("Ошибка, укажите число роботов")
                        self.robots = None  # сброс self.robots

                # проверка на вхождение в диапазон суммарного кол-ва игроков
                if self.humans + self.robots > self.MAX_PLAYERS \
                        or self.humans + self.robots < self.MIN_PLAYERS:  # если не в диапозоне
                    print(
                        f'Ошибка, указано суммарное количество игроков не в диапазоне {self.MIN_PLAYERS} - {self.MAX_PLAYERS}')
                    print()
                    err_h = True  # сброс
                    err_r = True  # сброс
                    if self.humans == 0 and self.robots == 0:
                        self.humans = None  # сброс
                        self.robots = None  # сброс
                else:
                    pass  # выход

        return self.humans, self.robots, self.CARDS_4PLAYER

    def make_player(self, robot=True, number=0):
        """
        Функция создает игрока
        роботу -  имя с переданным порядковым номером
        человеку - с введенным именем
        """
        player = self.START_pole.copy().astype(int)
        if robot:
            # определяем случайно стиль игры робота
            style = random.choice(('min', 'rand'))
            player.name = f'Robot_{number}({style})'
        else:
            player.name = input('Введите имя человека: ').title()
        return player

    def maker_players(self):
        """
        Функция создает список игроков players
        """
        hum, rob, cards4plaer = self.opros
        players = []
        if rob:
            for i in range(rob):
                players.append(self.make_player(number=i + 1))
        if hum:
            for _ in range(hum):
                print(f'Игрок {_ + 1}:')
                players.append(self.make_player(robot=False))
        return players, cards4plaer


class Razdaza:

    def __init__(self,
                 playcoloda,
                 cards4plaer,
                 poleigry,
                 bitta,
                 startcoloda
                 ):
        """
        Вспомогательный класс к классу class Durack
        раздает карты игрокам методом razdacha_card()
        """

        self.PLAY_coloda = playcoloda
        self.CARDS_4PLAYER = cards4plaer
        self.BITA = bitta
        self.POLE_IGRY = poleigry
        self.START_coloda = startcoloda
        self.PLAY = True

    def __call__(self, players):
        players, self.PLAY = self.razdacha_cards(players)
        return players, self.PLAY

    def perebor(self, df):
        """
        Функция контроля количества карт игрока
        df - входной датафрейм игрока
        """
        qty_card = (df != 0).sum().sum()
        if qty_card < self.CARDS_4PLAYER:
            situation = False
        else:
            situation = True
        return situation

    def random_card(self, vibor, value_card=0):
        """
        Функция определяет случайный выбор
        из vibor с учетом значения value_card
        """
        vibor_ = vibor.to_numpy()
        idx, jdx = np.where(vibor_ > value_card)
        i = random.randint(0, len(idx) - 1)
        return vibor.index[idx[i]], vibor.columns[jdx[i]]

    def take_cards(self, player, take='full'):
        """
        Функция получения карт из колоды
        take - сколько хочет взять карт, по умолчанию
              выдает до CARDS_4PLAYER(константы)
        player - кто берет карты
        """
        take_card = True
        schet = 0

        while take_card:
            # получаем данные по игроку
            situation = self.perebor(player)

            if situation:
                take_card = False  # на выход

            elif not situation and take_card:
                # делаем случайный выбор
                m, t = self.random_card(self.PLAY_coloda)

                # получаем глобальные номера масти и типа
                idx_m = self.PLAY_coloda.index.tolist().index(m)
                idx_t = self.PLAY_coloda.columns.tolist().index(t)

                # выдача карты из колоды
                player.iloc[idx_m, idx_t] = self.PLAY_coloda.iloc[idx_m, idx_t]
                # списание карты из колоды
                self.PLAY_coloda.iloc[idx_m, idx_t] = 0

                # есть ли карьы в колоде
                if not self.PLAY_coloda.sum().sum(): take_card = False

                schet += 1
                if take == 'full':
                    pass
                elif schet == take:
                    take_card = False  # на выход
        return player

    def control_invariant(self, data):
        """
        проверка инварианта игрового пространства
        для контроля игры
        """
        sum_data = np.zeros_like(data[0])
        for el in data:
            sum_data += el.to_numpy()

        tech_sum = (self.PLAY_coloda + self.BITA + self.POLE_IGRY).to_numpy()
        invariant = sum_data + tech_sum - self.START_coloda.to_numpy()
        if invariant.sum().sum() == 0:
            pass
        else:
            print('Ошибка контроля invariant карт')
            print(invariant)
            self.PLAY = False  # для выхода из игры

    def razdacha_cards(self, players):
        """
        Функция раздачи карт игрокам
        """
        for i in range(len(players)):
            qty_card = (players[i] != 0).sum().sum()
            # если колода не пуста и карт у игрока менее CARDS_4PLAYER
            if self.PLAY_coloda.sum().sum() and qty_card < self.CARDS_4PLAYER:
                print(f'Выдача карт {players[i].name}')
                players[i] = self.take_cards(players[i])
            self.control_invariant(players)
        return players, self.PLAY


class MakeGame:
    def __init__(self,
                 card4plaer,
                 musty,
                 typecard_keys,
                 idx_musty,
                 idx_typecards,
                 startcoloda
                 ):
        """
        Вспомогательный класс к классу class Durack
        для запуска процесса игры через метод go_game()
        """
        self.CARDS_4PLAYER = card4plaer
        self.MUSTY = musty
        self.TYPECARD_KEYS = typecard_keys
        self.IDX_MUSTY = idx_musty
        self.IDX_TYPECARDS = idx_typecards
        self.START_coloda = startcoloda
        self.START_pole = pd.DataFrame(np.zeros(startcoloda.shape),
                                       index=startcoloda.index,
                                       columns=startcoloda.columns).astype(int)
        self.BITA = self.START_pole.copy().astype(int)
        self.POLE_IGRY = self.START_pole.copy().astype(int)
        self.BITA.name = 'Бита'
        self.POLE_IGRY.name = 'Игровое поле'
        self.PLAY = True

    def __call__(self, players: object, playcoloda: object, kozir: object) -> object:
        self.go_game(players, playcoloda, kozir)

    def make_states(self, players):
        """
        Функция создает массив состояний игроков
        """
        state_players = []
        for i in range(len(players)):
            can_step = True
            fin_play = False
            state_players.append([can_step, fin_play])
        return np.array(state_players)

    def get_type(self, player):
        """
        Функция определяет тип игрока
        """
        if player.name.split('_')[0].lower() == 'robot':
            return 'robot'
        else:
            return 'human'

    def show_cards(self, player, show=True):
        """
        Функция преобразования датафрейм игрока
        в список/массива в одномерный список
        При show = True выводи на печать список карт
        выводит:
        for_choose - список карт игрока
        """
        # получаем матрицу карт игрока
        matrix = np.array(player)
        # считываем карты для публикации
        for_choose = []
        for idx_m in range(matrix.shape[0]):
            kz = '-'
            for idx_t in range(matrix.shape[1]):
                if matrix[idx_m][idx_t] != 0:
                    if matrix[idx_m][idx_t] > 100: kz = 'козырь'
                    carta = [player.index[idx_m], player.columns[idx_t], kz]
                    for_choose.append(carta)
        if show:
            # показываем карты игроку
            print(f'Ваши карты {player.name}:')
            for i, cart in enumerate(for_choose):
                txt = ''
                for el in cart:
                    if el != '-': txt += el + ' '
                print(f'{i + 1} - {txt}')
        return for_choose

    def vibor_card(self, df, value):
        """
        Функция определяет возможный список карт
        для выбора от состава df и значения value
        """
        if self.POLE_IGRY.sum().sum() == 0:
            vibor = df
        else:
            # получаем номер масти и номер карты
            [a], [b] = np.where(self.POLE_IGRY.applymap(lambda x: x != 0))

            if self.MUSTY[a] == self.KOZIR:
                vibor = df.apply(lambda x: x[x > value], 0).apply(lambda x: x[x > value], 1)
            else:
                vibor = df.loc[[self.MUSTY[a],
                                self.KOZIR]].apply(lambda x: x[x > value], 0).apply(lambda x: x[x > value], 1)
            vibor.replace(np.nan, 0, inplace=True)
        return vibor

    ##############################################################################
    # HUMAN                                                                    ###
    ##############################################################################
    def human_step(self, player, qty_card, value_card=0):
        """
        Функция выдает ход игрока
        """
        attempt = min(2, qty_card)
        try_card = True
        # получаем датасет возможных карт для хода
        vibor = self.vibor_card(player, value_card)

        schet = 1
        # получаем список карт и показываем по умолчанию
        for_choose = self.show_cards(player)
        # получаем список возможных карт для хода
        available = self.show_cards(vibor, False)

        # просим сделать шаг
        while try_card and schet < attempt + 1:
            print(f'Игрок {player.name}, ваш ход, у вас {attempt - schet + 1} попыток')
            step = input('Введите номер карты или пробел для пропуска хода: ')
            if step == ' ':  # or schet > attempt:  # пропуск хода
                try_card = False
                return step, step
            # команда для сброса игры
            elif step == 'стоп':
                print(f'Игрок {player.name} остановил игру')
                try_card = False
                self.PLAY = False
                return ' ', ' '
            else:
                try:
                    step = int(step)
                    if step in np.arange(1, qty_card + 1):
                        try_card = False
                    else:
                        schet += 1
                        print(f'{player.name} вами введен неверный номер карты, внимательнее')
                except:
                    print(f'{player.name} нужен номер карты или пробел для пропуска хода, внимательнее')
                    schet += 1
                    pass

            # выбор для простого хода
            # если все же ответ, то корректируем на основе value_card
            if not try_card:
                if vibor.sum().sum() == 0:
                    print(f'{player.name} к сожалению у Вас нет варианта для хода')
                    return ' ', ' '
                else:
                    hod = for_choose[step - 1]  # выбор ирока
                    schet += 1
                    step_musty, step_typecards = hod[0], hod[1]
                    # если выбор среди возможного для хода
                    if hod in available:
                        print(f'{player.name} ваш ход {step_musty} {step_typecards} принят')
                        try_card = False
                        return step_musty, step_typecards
                    else:
                        try_card = True
            else:
                pass
        print(f'{player.name} Вы исчерпали свои {attempt + 1} попытки')
        return ' ', ' '

    ##############################################################################

    ##############################################################################
    # ROBOT                                                                    ###
    ##############################################################################
    def random_step(self, player, value_card=0):
        """
        Функция выдает ход робота
        на основе стиля робота
        """
        vibor = self.vibor_card(player, value_card)

        style = player.name.split('(')[1][:-1]

        if vibor.sum().sum() == 0:
            return ' ', ' '
        else:
            if style == 'min':
                return self.min_card(vibor, value_card)
            if style == 'rand':
                return Razdaza.random_card(self, vibor, value_card)

    def min_card(self, vibor, value_card=0):
        """
        Функция определяет минимальный случайный выбор
        из vibor с учетом значения value_card
        """
        vibor_ = vibor.to_numpy()
        mask = vibor_ > value_card
        v_min = vibor_[mask].min()

        idx, jdx = np.where(vibor_ == v_min)
        i, j = random.choice(np.c_[idx, jdx])
        return vibor.index[i], vibor.columns[j]

    ##############################################################################

    def step_player(self, player, type_player='human'):
        """
        Функция выдает шаг игрока
        на основе type_player - робот или человек
        """
        # получаем количество карт
        qty_card = (player != 0).sum().sum()
        # выбор через ответ человекв
        if type_player == 'human':
            print()
            print(f'Ваш ход {player.name}')
            m, t = self.human_step(player, qty_card)
            if m == ' ' and t == ' ':
                print(f'Игрок {player.name} пропустил ход')
                return player
            else:
                pass
        # случайный выбор робота
        if type_player == 'robot':
            m, t = self.random_step(player)

        print(f'{player.name} сделал ход {m}_{t}')
        # получаем глобальные номера масти и типа
        idx_m = self.MUSTY.index(m)
        idx_t = self.TYPECARD_KEYS.index(t)

        # выкладываем карты на поле
        self.POLE_IGRY.iloc[idx_m, idx_t] = player.iloc[idx_m, idx_t]
        # списание карты у игрока
        player.iloc[idx_m, idx_t] = 0
        return player

    def answer_player(self, player, type_player='human'):
        """
        Функция определяет выдает шаг игрока
        на основе type_player - робот или человек
        """
        # получаем номер масти и номер карты
        [a], [b] = np.where(self.POLE_IGRY.applymap(lambda x: x != 0))

        # получаем вес карты
        value_card = self.POLE_IGRY.iloc[a][b]

        # получаем количество карт у игрока
        qty_plcard = (player != 0).sum().sum()
        # случайный выбор робота
        if type_player == 'robot':
            m, t = self.random_step(player, value_card)
        if type_player == 'human':
            print()
            print(f'На поле {self.MUSTY[a]} {self.TYPECARD_KEYS[b]}')
            # получаем список карт и показываем по умолчанию
            m, t = self.human_step(player, qty_plcard, value_card)
        if m == ' ' and t == ' ':
            print(f'Игрок {player.name} берет карту и пропускает ход')
            # игрок берет карту с поля
            player.iloc[a][b] = self.POLE_IGRY.iloc[a][b]
            # убираем карту с поля
            self.POLE_IGRY.iloc[a][b] = 0
            state = False

        else:
            print(f'Игрок {player.name} бьет картой {m}_{t}')
            # получаем глобальные номера масти и типа
            idx_m = self.MUSTY.index(m)
            idx_t = self.TYPECARD_KEYS.index(t)
            # отправляем карту бьющего в биту
            self.BITA.iloc[idx_m][idx_t] = player.iloc[idx_m][idx_t]
            # списание карты у игрока
            player.iloc[idx_m][idx_t] = 0
            # отправляем карту на поле в биту
            self.BITA.iloc[a][b] = self.POLE_IGRY.iloc[a][b]
            # убираем карту с поля
            self.POLE_IGRY.iloc[a][b] = 0
            state = True

        return player, state

    def action_player(self, player, state_player, type_action):
        """
        Функция определяет тип действий игрока
        """
        type_player = self.get_type(player)  # получаем тип игрока
        # Ходит если поле пусто
        if type_action:
            # Ходит или пропускает от состояния state_player[0]
            player = self.step_player(player, type_player)
            # Обновляем состояние в state_player[0] возможности ходить
            if not state_player[0]:  state_player[0] = True
        else:  # Отвечает если на поле лежит карта
            # отвечает и обновляет состояние в state_player[0] возможности ходить
            player, state_player[0] = self.answer_player(player, type_player)
        # Обновляем состояние в state_player[1] закончил ли игру
        state_player[1] = self.fin_play(player)
        return player, state_player

    def fin_play(self, player):
        """
        Функция определяет закончил ли
        игру player
        """
        set_player = player.sum().sum()
        set_coloda = self.PLAY_coloda.sum().sum()
        if not set_player and not set_coloda:
            print(f'Игрок {player.name} закончил игру')
            return True
        else:
            return False

    def go_game(self, players, playcoloda, kozir):
        """
        Функция запускает игры
        """
        qty_players = len(players)

        # считываем количество розданных карт
        self.CARDS_4PLAYER = (players[0] != 0).sum().sum()
        cickle = 1
        fin = 0
        self.PLAY = True
        self.KOZIR = kozir
        self.PLAY_coloda = playcoloda
        # передаем текущий козырь для контроля инварианта игры
        self.START_coloda.loc[self.KOZIR] *= 100

        df_list = [self.BITA, self.PLAY_coloda, self.POLE_IGRY]
        state_players = self.make_states(players)

        while self.PLAY:
            print('cickle ', cickle)
            step = 0
            while step < qty_players and self.PLAY:
                if fin: fin += 1  # для полного выходя из всех циклов в конце текущего
                # проверяем ход или ответ
                if self.POLE_IGRY.sum().sum() == 0:
                    type_action = True  # ходить
                else:
                    type_action = False  # отвечать

                # действие игрока
                players[step], state_players[step] = self.action_player(players[step],
                                                                        state_players[step],
                                                                        type_action)
                # создание метода раздачи карт с текущими значениями игры
                razdacha_cards = Razdaza(self.PLAY_coloda,
                                         self.CARDS_4PLAYER,
                                         self.POLE_IGRY,
                                         self.BITA,
                                         self.START_coloda)
                # выдача карт игроку если нужно
                if (players[step] != 0).sum().sum() < self.CARDS_4PLAYER:
                    players, self.PLAY = razdacha_cards(players)

                # регистрируем если кто окончил игру
                if sum(state_players[:, 1]) == 1:
                    fin += 1

                # если ранее был ответ и игрок взял карту
                some_state = not type_action and not state_players[step][0]

                # если был шаг или some_state или плбедитель,то передаем ход следкющему
                if type_action or some_state or state_players[step][1]:
                    step += 1

                if fin > 0: break  # выход из 1го цикла
            if fin > 0:
                play = False
                break  # выход из 2го цикла

            cickle += 1
            print()
        print()
        winners = str()
        for player, state in zip(players, state_players):
            if state[1]: winners += player.name + ', '
        print(f'Победа у {winners[:-2]}')
        print()

        print('Проверяем карты')
        for player in players:
            print(player.name)
            print(player.head(10).to_string())
            # display(df)
            print()

        print('Проверяем остальное')
        for df in df_list:
            print(df.name)
            print(df.head(10).to_string())
            # display(df)
            print()


class Durack:
    def __init__(self,
                 card4plaer=None,
                 humans=None,
                 robots=None,
                 ):
        """
        Класс для создания игры в карты "Дурак"
        card4plaer - количество карт выдаваемых игроку. Можно не задавать
                    и пройти опрос или задать при создании.
        humans - количество игроков людей. Можно не задавать
                 и пройти опрос или задать при создании.
        robots - количество игроков людей. Можно не задавать
                 и пройти опрос или задать при создании.
        _______________________________________________________
        Для работы необходимо загрузить:
        - библилтеки:
          `import random`
          `import numpy as np`
          `import pandas as pd`
        - вспомогательные классы:
         `Razdaza, MakePlayers, MakeGame`
        Для запуска кода необходимо создать игру и далее методом
        init_game() получить список игроков с картами, игровую колоду
        и козырь:
        `game = Durack(card4plaer=6, humans=1, robots=3)`
        `players, playcoloda, kozir = game.init_game()`
        Далее подать эти данные в метод go_game():
        `game.go_game(players, playcoloda, kozir)`
        Если в игре есть игроки люди, до отвечать на вопросы в игре
        """

        self.__humans = humans
        self.__robots = robots
        self.__CARDS_4PLAYER = card4plaer
        self.__MUSTY = ['Черви', 'Пики', 'Крести', 'Буби']
        self.__DIC_CARDS = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Валет': 11,
                            "Дама": 12, 'Король': 13, 'Туз': 14}
        ########################################################################
        self.__TYPECARD_KEYS = list(self.__DIC_CARDS.keys())
        self.__IDX_MUSTY = np.arange(len(self.__MUSTY))
        self.__IDX_TYPECARDS = np.arange(len(self.__DIC_CARDS))
        self.__VALUE = [[card for card in self.__DIC_CARDS.values()] \
                        for i in range(len(self.__MUSTY))]
        self.__base_coloda = pd.DataFrame(data=self.__VALUE,
                                          index=self.__MUSTY,
                                          columns=self.__DIC_CARDS.keys())
        self.__SHAPE = np.array(self.__base_coloda).shape
        self.__QQUANTY_COLODA = self.__SHAPE[0] * self.__SHAPE[1]
        self.__MAXCARDS_4PLAER = int(np.sqrt(self.__QQUANTY_COLODA))
        self.__START_pole = pd.DataFrame(np.zeros(self.__SHAPE),
                                         index=self.__MUSTY,
                                         columns=self.__DIC_CARDS.keys()).astype(int)
        self.__MINCARDS_4PLAER = 2
        self.__MIN_PLAYERS = 2

        # создание метода запуска игрыв с текущими значениями игры
        self.go_game = MakeGame(self.__CARDS_4PLAYER,
                                 self.__MUSTY,
                                 self.__TYPECARD_KEYS,
                                 self.__IDX_MUSTY,
                                 self.__IDX_TYPECARDS,
                                 self.__base_coloda
                                 )

    def init_game(self):
        """
        Функция инициализации игры
        """
        # создание метода создания игроков с текущими значениями игры
        maker_players = MakePlayers(self.__CARDS_4PLAYER,
                                     self.__humans,
                                     self.__robots,
                                     self.__MINCARDS_4PLAER,
                                     self.__MAXCARDS_4PLAER,
                                     self.__MIN_PLAYERS,
                                     self.__QQUANTY_COLODA,
                                     self.__START_pole
                                     )
        # создаем игпоков, и карт для выдачи обновленное
        players, self.__CARDS_4PLAYER = maker_players()
        print()
        print("Расcаживаем игроков в случайном порядке")
        random.shuffle(players)
        print([player.name for player in players])
        print("rand - робот со случайным выбором из возможных для хода карт")
        print("min - робот выбирает минимальную из возможных для хода карт ")
        print()

        print("Сдаем карты:")
        # обновляем состояние игры
        kozir = random.choice(self.__MUSTY)
        START_coloda = self.__base_coloda.copy().astype(int)
        START_coloda.loc[kozir] = START_coloda.loc[kozir] * 100
        PLAY_coloda = START_coloda.copy().astype(int)
        PLAY_coloda.name = 'Игровая колода'
        BITA = self.__START_pole.copy().astype(int)
        POLE_IGRY = self.__START_pole.copy().astype(int)
        # BITA.name = 'Бита'
        # POLE_IGRY.name = 'Игровое поле'

        # создание метода раздачи карт с текущими значениями игры
        razdacha_cards = Razdaza(PLAY_coloda,
                                 self.__CARDS_4PLAYER,
                                 POLE_IGRY,
                                 BITA,
                                 START_coloda)

        # раздаем карты  игпокам
        players, play = razdacha_cards(players)
        print()
        print(f'Козырь игры {kozir}')
        print()

        return players, PLAY_coloda, kozir


if __name__ == '__main__':
    # Инициализация игры
    game = Durack(card4plaer=3, humans=0, robots=3)
    players, playcoloda, kozir = game.init_game()

    # Запуск игрового цикла
    game.go_game(players, playcoloda, kozir)