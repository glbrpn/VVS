import curses

classes = ["Строчные-прописные", "Найти-заменить", "Разделить-соединить", "Буква-цифра?-удалить",'Нормализатор']


def character(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("Выберите уровень\n", curses.A_BOLD)
        for i in range(len(classes)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(classes[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1

    
    stdscr.erase()

    if option==0:
        stdscr.addstr(classes[option])
        curses.echo()
        name_bytes = stdscr.getstr()
        name = name_bytes.decode('utf-8') 
        stdscr.addstr("Выберите метод\n", curses.A_BOLD)

        stdscr.getch()
        while c != 10:  # Enter in ascii
            stdscr.erase()
            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                else:
                    attr = attributes['normal']
                stdscr.addstr("{0}. ".format(i + 1))
                stdscr.addstr(classes[i] + '\n', attr)
            c = stdscr.getch()
            if c == curses.KEY_UP and option > 0:
                option -= 1
            elif c == curses.KEY_DOWN and option < len(classes) - 1:
                option += 1


curses.wrapper(character)
