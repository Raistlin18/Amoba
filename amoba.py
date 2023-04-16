import string


def tabla_minta1(megadott_meret, tipp1, board, foglalt):
    if int(tipp1[0]) > len(board):
        print('Nem megfelelő értéket adtál meg')
    if int(tipp1[1]) > len(board):
        print('Nem megfelelő értéket adtál meg')
    elif not foglalt[int(tipp1[0]) - 1][int(tipp1[1]) - 1]:
        foglalt[int(tipp1[0]) - 1][int(tipp1[1]) - 1] = True
        for sor in range(megadott_meret):
            for oszlop in range(megadott_meret):
                if oszlop == int(tipp1[1]) - 1 and sor == int(tipp1[0]) - 1:
                    board[sor][oszlop] = ' X'
                    print('|X |', end='')
                else:
                    print('|' + board[sor][oszlop] + '|', end='')
            print()
    else:
        print("A hely már foglalt, válassz másikat.")
        return False
    return True

def tabla_minta2(megadott_meret, tipp2, board, foglalt):
    if int(tipp2[0]) > len(board):
        print('Nem megfelelő értéket adtál meg')
    if int(tipp2[1]) > len(board):
        print('Nem megfelelő értéket adtál meg')
    elif not foglalt[int(tipp2[0]) - 1][int(tipp2[1]) - 1]:
        foglalt[int(tipp2[0]) - 1][int(tipp2[1]) - 1] = True
        for sor in range(megadott_meret):
            for oszlop in range(megadott_meret):
                if oszlop == int(tipp2[1]) - 1 and sor == int(tipp2[0]) - 1:
                    board[sor][oszlop] = ' O'
                    print('|O |', end='')
                else:
                    print('|' + board[sor][oszlop] + '|', end='')
            print()
    else:
        print("A hely már foglalt, válassz másikat.")
        return False
    return True

def nyeres_ellenorzes(tabla, jel):
    for i in range(len(tabla)-4):
        for j in range(len(tabla[i])-4):
            eredmeny = all(tabla[i][j] == tabla[i][j + k] for k in range(1,5))
            if eredmeny == True:
                print(f'{jel} NYERT!!! GRATULÁLOK!!!!!!')
                return eredmeny
            eredmeny = all(tabla[i][j] == tabla[i+k][j] for k in range(1,5))
            if eredmeny == True:
                print(f'{jel} NYERT!!! GRATULÁLOK!!!!!!')
                return eredmeny
            eredmeny = all(tabla[i][j] == tabla[i + k][j + k] for k in range(1, 5))
            if eredmeny == True:
                print(f'{jel} NYERT!!! GRATULÁLOK!!!!!!')
                return eredmeny
            eredmeny = all(tabla[i][j + 4] == tabla[i + k][j + 4 - k] for k in range(1, 5))
            if eredmeny == True:
                print(f'{jel} NYERT!!! GRATULÁLOK!!!!!!')
                return eredmeny
    return False

def main():
    meret = int(input('\nMekkora pályán szeretnél játszani (5x5...9x9)?\nCsak egy számot adj meg: '))
    print('\n')
    oszlop_lista = string.digits[1:meret + 1]
    sor_lista = string.digits[1:meret + 1]
    oszlop_szamok = string.digits[1:meret + 1]
    board = [[sor_lista[i] + oszlop_lista[j] for j in range(meret)] for i in range(meret)]
    print('| ' + ' | '.join(oszlop_szamok) + '|', end='\n')
    for sor in range(meret):
        for oszlop in range(meret):
            print('|' + board[sor][oszlop] + '|', end='')
        print()
    print('\nAMŐBA!\n')
    nev_1 = input('Add meg az 1-es játékos nevét: ')
    print('Nagyszerű, te vagy az "X"-el')
    nev_2 = input('Add meg a 2-es játékos nevét: ')
    print('Nagyszerű, te vagy a "O"-el')
    foglalt = [[False for j in range(meret)] for i in range(meret)]
    gyozelem = False
    while not gyozelem:
        tipp_1 = input(f'\n{nev_1} Add meg a sort "X"-nek (Kilépés: exit) : ')
        if tipp_1 == 'exit':
            break
        print('\n')
        tabla_minta1(meret, tipp_1, board, foglalt)
        nyeres_ellenorzes(board, nev_1)
        if nyeres_ellenorzes(board, nev_1) == True:
            break
        tipp_2 = input(f'\n{nev_2} Add meg a sort "O"-nek (Kilépés:exit) : ')
        if tipp_2 == 'exit':
            break
        print('\n')
        tabla_minta2(meret, tipp_2, board, foglalt)
        nyeres_ellenorzes(board, nev_2)
        if nyeres_ellenorzes(board, nev_2) == True:
            break
    print('VÉGE!!!')

