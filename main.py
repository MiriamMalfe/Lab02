import translator as tr

t = tr.Translator()  #t è un oggetto di classe Translator


while(True):
    t.printMenu()  #stampa i menu richiamando metodo della classe translator


    txtIn = input("Scegliere azione: ")

    match txtIn:
        case "1":
            parola = input("Inserire la parola da aggiungere: ").lower()
            traduzione = input("Inserire traduzione corrispondente: ").lower()
            definizione = parola+" "+traduzione
            t.handleAdd(definizione)

        case "2":
            parola = input("Inserire la parola da cercare: ").lower()
            t.handleTranslate(parola)

        case "3":
            pass
        case "4":
            pass
        case "5":
            break