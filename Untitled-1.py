def provjere_broja(broj):
    if 10 = 100:
        return f"Broj{broj} je unutar raspona."
    else:
        return f"Broj{broj} je izvan raspona."
    
if __name__ =="__main__":
    try:
        uneseni_broj = int(input("Unesite broj"))
        print(provjera_brojeva(uneseni_broj))
    except ValueError:
        print("Unesena vrijednost nije broj.")