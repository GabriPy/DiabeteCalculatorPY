import tkinter as tk
from tkinter import messagebox


def show_main():
    main_frame.pack()
    correzione_frame.pack_forget()
    insulina_frame.pack_forget()
    settings_frame.pack_forget()


def show_correzione():
    main_frame.pack_forget()
    correzione_frame.pack()
    insulina_frame.pack_forget()
    settings_frame.pack_forget()


def show_insulina():
    main_frame.pack_forget()
    correzione_frame.pack_forget()
    insulina_frame.pack()
    settings_frame.pack_forget()


def show_settings():
    main_frame.pack_forget()
    correzione_frame.pack_forget()
    insulina_frame.pack_forget()
    settings_frame.pack()


def calculate_correzione():
    glicemia = int(glicemia_entry.get())

    if scelta_var.get() == 0:
        unita_insulina = correzione_giorno(glicemia)
    else:
        unita_insulina = correzione_notte(glicemia)

    stringa_unita_insulina = str(unita_insulina)

    arrotondato_unita_insulina = round(float(stringa_unita_insulina), 1)

    result_label_correzione["text"] = "Le unità che devi fare per correggere sono: " + \
        str(arrotondato_unita_insulina)


def calculate_insulina():
    carboidrati = int(carboidrati_entry.get())
    unita_insulina = carboidrati // assorbimento_carboidrati

    stringa_unita_insulina = str(unita_insulina)

    arrotondato_unita_insulina = round(float(stringa_unita_insulina), 1)

    result_label_insulina["text"] = "Devi fare " + \
        str(arrotondato_unita_insulina) + " unità."


def update_settings():
    global fattore_giornaliero, fattore_notturno
    fattore_giornaliero = float(fattore_giornaliero_entry.get())
    fattore_notturno = float(fattore_notturno_entry.get())
    messagebox.showinfo("Modifica Fattore Correzione",
                        "Il fattore correzione è stato aggiornato.")


def back_to_main():
    main_frame.pack()
    correzione_frame.pack_forget()
    insulina_frame.pack_forget()
    settings_frame.pack_forget()


def correzione_giorno(glicemia):
    return glicemia / fattore_giornaliero


def correzione_notte(glicemia):
    return glicemia / fattore_notturno


# Valori di configurazione
fattore_giornaliero = 35
fattore_notturno = 40
assorbimento_carboidrati = 8

# Creazione della finestra principale
window = tk.Tk()
window.title("Programma diabetico")

# Frame principale
main_frame = tk.Frame(window)
main_frame.pack(padx=200)

window.update_idletasks()  # Aggiorna la finestra per ottenere le dimensioni corrette
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"+{x}+{y}")


correzione_button = tk.Button(main_frame, text="Correzione", font=(
    "Arial", 12), command=show_correzione)
correzione_button.pack(pady=10)

insulina_button = tk.Button(main_frame, text="Insulina", font=(
    "Arial", 12), command=show_insulina)
insulina_button.pack(pady=10)

settings_button = tk.Button(main_frame, text="Impostazioni", font=(
    "Arial", 12), command=show_settings)
settings_button.pack(pady=10)

# Frame per la correzione
correzione_frame = tk.Frame(window)

glicemia_label = tk.Label(
    correzione_frame, text="Inserisci la glicemia:", font=("Arial", 12))
glicemia_label.grid(row=0, column=0, pady=10)

glicemia_entry = tk.Entry(correzione_frame, font=("Arial", 12))
glicemia_entry.grid(row=0, column=1)

scelta_var = tk.IntVar()

scelta_frame = tk.Frame(correzione_frame)
scelta_frame.grid(row=1, column=0, columnspan=2, pady=10)

giorno_button = tk.Radiobutton(
    scelta_frame, text="Giorno", variable=scelta_var, value=0, font=("Arial", 12))
giorno_button.pack()

notte_button = tk.Radiobutton(
    scelta_frame, text="Notte", variable=scelta_var, value=1, font=("Arial", 12))
notte_button.pack()

calculate_correzione_button = tk.Button(
    correzione_frame, text="Calcola", command=calculate_correzione, font=("Arial", 12))
calculate_correzione_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label_correzione = tk.Label(
    correzione_frame, text="", font=("Arial", 12))
result_label_correzione.grid(row=3, column=0, columnspan=2, pady=10)

back_button_correzione = tk.Button(
    correzione_frame, text="Indietro", command=back_to_main, font=("Arial", 12))
back_button_correzione.grid(row=4, column=0, columnspan=2, pady=10)

# Frame per l'insulina
insulina_frame = tk.Frame(window)

carboidrati_label = tk.Label(
    insulina_frame, text="Inserisci i carboidrati:", font=("Arial", 12))
carboidrati_label.grid(row=0, column=0, pady=10)

carboidrati_entry = tk.Entry(insulina_frame, font=("Arial", 12))
carboidrati_entry.grid(row=0, column=1)

calculate_insulina_button = tk.Button(
    insulina_frame, text="Calcola", command=calculate_insulina, font=("Arial", 12))
calculate_insulina_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label_insulina = tk.Label(insulina_frame, text="", font=("Arial", 12))
result_label_insulina.grid(row=2, column=0, columnspan=2, pady=10)

back_button_insulina = tk.Button(
    insulina_frame, text="Indietro", command=back_to_main, font=("Arial", 12))
back_button_insulina.grid(row=3, column=0, columnspan=2, pady=10)

# Frame per le impostazioni
settings_frame = tk.Frame(window)

fattore_giornaliero_label = tk.Label(
    settings_frame, text="Fattore correzione giorno:", font=("Arial", 12))
fattore_giornaliero_label.grid(row=0, column=0, pady=10)

fattore_giornaliero_entry = tk.Entry(settings_frame, font=("Arial", 12))
fattore_giornaliero_entry.grid(row=0, column=1)

fattore_notturno_label = tk.Label(
    settings_frame, text="Fattore correzione notte:", font=("Arial", 12))
fattore_notturno_label.grid(row=1, column=0, pady=10)

fattore_notturno_entry = tk.Entry(settings_frame, font=("Arial", 12))
fattore_notturno_entry.grid(row=1, column=1)

update_settings_button = tk.Button(
    settings_frame, text="Aggiorna", command=update_settings, font=("Arial", 12))
update_settings_button.grid(row=2, column=0, columnspan=2, pady=10)

back_button_settings = tk.Button(
    settings_frame, text="Indietro", command=back_to_main, font=("Arial", 12))
back_button_settings.grid(row=3, column=0, columnspan=2, pady=10)

# Visualizzazione iniziale
show_main()

# Avvio dell'applicazione
window.mainloop()
