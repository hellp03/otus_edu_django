from lototron import Lototron

def main():

    loto=Lototron()
    while not loto.get_start_info():
        pass
    loto.make_cards()
    if loto.start_game():
        for i in loto.winner:
            print(i, ' - Win!')

if __name__ == '__main__':
    main()