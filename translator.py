class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("------------------------")
        print("Translator Alien-Italian")
        print("------------------------")
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcar")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("------------------------")


    def handleAdd(self, definizione):
        self.aperto = open("dictionary.txt", "r") #apro dizionario in lettura
        defi = definizione.split(" ") #defi è una lista che contiene le parole
        dizionario = {} #creo dizionario vuoto
        for line in self.aperto:   #per ogni riga del dictionary.txt:
            line.strip("\n")  #tolgo a capo
            line = line.split(" ")  #creo la linea (lista) composta dalla riga del dictionary.txt senza spazi
            dizionario[line[0]] = [] #per ogni key (line[0]) del dizionario creo una lista vuota dove ci aggiungerò man mano le traduzioni
            for i in range(len(line)): #per  ogni parola nel range lunghezza lista delle traduzioni
                if i > 0:  #se la parola non è la key quindi è in posizione 1 (>0):
                    dizionario[line[0]].append(line[i].strip("\n"))  #aggiungo alla key la traduzione (senza a capo)
        print(dizionario)
        lettere = True #variabile usata per capire se ho solo lettere
        for i in defi: #per ogni parola in defi
            if i.isalpha():  #controllo che le parole siano composte da solo lettere
                pass #non faccio niente
            else:  #altrimenti
                lettere = False  #la variabile bool cambia

        if lettere == True:  #se ci sono solo lettere:
            trovato = 0  #variabile che indica se la key esiste già
            #caso in cui la key sia presente già nel dizionario e devo aggiungere la traduzione
            if defi[0] in dizionario: #se la key c'è già:
                for i in dizionario[defi[0]]:  #per ogni traduzione associata alla key:
                    if i == defi[1]: #se la traduzione esiste già esco dal ciclo e aggiorno il bool dicendo che c'è gia
                        trovato = 1
                        break #esco dal ciclo
                if trovato == 0: #se la traduzione non c'è già la aggiungo alla key
                    for i in range(1, len(defi)-1): #per ogni traduzione nella lista che va dalla prima traduzione fino alla fine
                        dizionario[defi[0]].append(defi[i]) #appendo la nuova traduzione
                                                            #definizione = "ciao caro carissimo brutto"
                                                            #defi = ["ciao"]["caro"]
            else:  #caso in cui la key non sia presente già nel dizionario
                dizionario[defi[0]] = [] #creo la nuova key a cui associo la lista vuota elle traduzioni
                for i in range(1, len(defi)):  #per ogni traduzione nel range della lunghezza della lista traduzioni:
                    dizionario[defi[0]].append(defi[i])  #ci aggiungo la nuova traduzione
            self.aperto.close()  #chiudo il dictionary.txt che era aperto in lettura
            self.riscrivi = open("dictionary.txt", "w")  #apro il dictionary.txt in scrittura

            #sovrascrivo il dizionario sul file txt
            for k in dizionario: #PER OGNI CHIAV DEL DIZIONARIO:
                stringa = ""  #creo la stringa che andrò a scrivere nel file perchè ci posso scrivere solo delle stringhe
                stringa = k  #stringa = key , poi ora ci aggiungo le traduzioni
                for i in dizionario[k]:  #scorro le traduzioni associate alla key
                    stringa = stringa+" "+i  #stringa si aggiorna e diventa: key traduzione1 traduzione2 ....
                stringa = stringa+"\n"  #aggiungo alla stringa a capo   (LA STRINGA SI RIFERISCE ALLA SINGOLA KEY E AI SUOI VALORI ASSOCIATI)
                self.riscrivi.write(stringa)  #riscrivo la stringa nel file
            self.riscrivi.close()   #chiudo dictionary.txt aperto in scrittura --> lo chiudo perchè così ho subito le parole salvate e le posso cercare subito
        else:
            print("Errore: hai inserito caratteri non consentiti")  #se invece non ci sono solo lettere significa che ci sono caratteri non consentiti --> stampo errore



    def handleTranslate(self, parola):
        self.aperto = open("dictionary.txt", "r")  #apro il file dictionary.txt in lettura
        trovata = 0  #bool per sapere se la parola che cerco esiste
        for line in self.aperto:  #per ogni riga del file:
            line.strip("\n")  #rimuovo a capo
            line = line.split(" ")   #rimuovo gli spazi
            if line[0] == parola: #se la parola che cerco coincide con la parola (quindi controllo che ciò che cerco esista)
                trovata = 1   #aggiorno il bool e gli dico che l'ho trovata
                stringa = "La traduzione è: "   #inizio a creare la stringa che stamperò
                for i in range(1, len(line)):   #per ogni parola nel range delle traduzioni
                    stringa = stringa+" "+line[i]  #aggiorno la stringa--> stringa = La traduzione è: traduzione1, .....
                print(stringa)  #stampo la stringa con le traduzioni
        if trovata == 0:  #se invece la parola non esiste e cioè non l'ho trovata:
            print("Traduzione non esistente")   #comunico all'utente che la parola cercata non esiste

    def handleWildCard(self,query):
        aperto = open("dictionary.txt", "r")   #apro il dizionario in lettura
        lista = list(query)   #dalla query che mi da l'utente ci creo una lista di lettere

        c=0  #variabile che mi conta il numero dei punti interrogativi che ha messo l'utente nella query
        for i in lista:   #per ogni lettera nella lista di lettere:
            if i == "?":  #se la lettera è il punto interrogativo:
                c = c+1   #aggiorno la variabile contatore dei punti interrogativi

        if c==0:   #se non ho punti interrogativi restituisco la traduzione corrispondente alla parola inserita dall'utente
            self.handleTranslate(query)
        if c==1:    #se ho un punto interrogativo:
            diz = {}   #creo un dizionario vuoto che mi serve per associare la parola inserita dall'utente a tutte le possibili traduzioni
            for line in aperto:  #per ogni riga del dictionary.txt
                line.strip("\n")  #tolgo a capo
                line = line.split(" ") #tolgo gli spazi così da avere una lista di parole
                line[0] = list(line[0])  #creo una lista di lettere per le parole (non le traduzioni) del  dizionario

                k = 0   #uso una variabile per vedere quante lettere sono uguali tra le due parole (di lista e di line)
                if len(lista) == len(line[0]):   #se la lunghezza della parola del file corrisponde alla lunghezza della pparola inserita dall'utente
                    for i in range(len(lista)):   #scorro le lettere della parola inserita dall'utente
                        if lista[i] == line[0][i]:  #se la lettera della parola dell'utente è uguale alla lettera nella stessa posizione della lista line
                            k = k+1   #aggiorno la variabile
                    if k == len(lista)-1:  #se le due parole hanno la stessa lunghezza
                        diz[query] = []   #creo un dizionario vuoto dove come key ho la parola inserita dall'utente e come valore la lista delle possibili traduzione
                        for i in range(1, len(line)):  #per ogni lettera (traduzione) nella parola del file
                            diz[query].append(line[i])  #aggiungo al dizionario la traduzione

            for x in diz:  #per ogni traduzione associata alla parola inserita stampo le possibili traduzioni
               print(diz[x].strip("\n"))

        else:
            print("Errore: hai inserito troppi punti interrogativi")   #stampo errore se si ha inserito più di un punto interrogativo

    def printDiz(self):
        aperto = open("dictionary.txt", "r")
        for l in aperto:
            print(l)






