#unesi boju napisane rijeci

#modul za graficko sucelje
import tkinter
#modul za nasumicne brojeve
import random

#lista mogucih boja
boje = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
#pocetni bodovi
bodovi = 0
#zadano vrijeme
preostalo_vrijeme = 30

#funkcija koja zapocinje igru
def zapocni_igru(event):

    #provjeri je li preostalo vrijeme 30
    if preostalo_vrijeme == 30:
        #zapocni odbrojavanje
        odbrojavanje()
        
    #odaberi sljedecu boju
    sljedeca_boja()

#funkcija koja odabere i pokaze sljedecu boju
def sljedeca_boja():

    #globalne varijable za koristenje u drugim funkcijama
    global bodovi
    global preostalo_vrijeme

    #ako je igra u tijeku...
    if preostalo_vrijeme > 0:

        #postavi polje u aktivno stanje (za pisanje)
        txt_polje.focus_set()

        #ako je unesena boja jednaka boji teksta
        if txt_polje.get().lower() == boje[1].lower():
            #dodaj 1 bod
            bodovi += 1

        #ocisti prijasnji unos u polje
        txt_polje.delete(0, tkinter.END)
        #promijesaj listu boja
        random.shuffle(boje)
        #uzmi tekst iz liste boje i obojaj ga nasumicnom bojom
        label.config(fg=str(boje[1]), text=str(boje[0]))
        #azuriraj bodove na njihovom polju
        bodovi_label.config(text="bodovi: " + str(bodovi))

#funkcija za odbrojavanje
def odbrojavanje():

    #globalna varijabla za koristenje u ostalim funkcijama
    global preostalo_vrijeme

    #ako je igra u tijeku...
    if preostalo_vrijeme > 0:

        #smanji preostalo vrijeme za sekundu
        preostalo_vrijeme -= 1
        #azuriraj label za vrijeme
        vrijeme_label.config(text="Time left: " + str(preostalo_vrijeme))
        #pokreni funkciju opet za 1 sekundu
        vrijeme_label.after(1000, odbrojavanje)
    
#stvori prozor s grafickim suceljem
prozor = tkinter.Tk()
#naslov
prozor.title("Pogodi boju")
#postavi velicinu prozora
prozor.geometry("375x200")

#label za upute igre
instructions = tkinter.Label(prozor, text="Upisi ime boje kojom je napisan tekst", font=('Helvetica', 12))
instructions.pack()

#dodaj label za prikaz bodova
bodovi_label = tkinter.Label(prozor, text="Pritisni enter za start", font=('Helvetica', 12))
bodovi_label.pack()

#dodaj label za prikaz preostalog vremena
vrijeme_label = tkinter.Label(prozor, text="Preostalo vrijeme: " + str(preostalo_vrijeme), font=('Helvetica', 12))
vrijeme_label.pack()

#dodaj label za prikaz obojane rijeci
label = tkinter.Label(prozor, font=('Helvetica', 60))
label.pack()

#dodaj polje za upisivanje odgovora
txt_polje = tkinter.Entry(prozor)
#pokreni zapocni_igru kada pritisnemo enter
prozor.bind('<Return>', zapocni_igru)
txt_polje.pack()
#postavi aktivni fokus na polje
txt_polje.focus_set()

#otvori prozor u petlji da se ne ugasi dok nije igra gotova
prozor.mainloop()