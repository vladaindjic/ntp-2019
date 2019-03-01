# 1. Magicne metode

# 1.1. Iterator
class PrimerIterator:
    def __init__(self, start=0, stop=10):
        self.pocetak = start
        self.brojac = self.pocetak - 1
        self.kraj = stop
        if self.kraj < self.pocetak:
            raise ValueError("Kraj mora biti veci od pocetka")

    # magicna metoda koja vraca iterabilni objekat
    def __iter__(self):
        return self

    # iterator protokol
    def __next__(self):
        if self.brojac <= self.kraj:
            self.brojac += 1
            return self.brojac
        raise StopIteration()


def iterator():
    pi = PrimerIterator(10, 20)
    it = iter(pi)
    print("Ovo je iterabilni objekat: %s" % it)
    # iterate ove the iterator
    print("Rucno preuzimamo sledeci element: %d" % next(it))
    for i in it:
        print("FOR PETLJA: %d" % i)
    try:
        print(next(it))
    except StopIteration:
        print("Iterabilni objekat je ispraznjen")


# 1.2 Generator
class PrimerGeneratora:
    def __init__(self, start=0, stop=10):
        self.pocetak = start
        self.brojac = self.pocetak
        self.kraj = stop
        if self.kraj < self.pocetak:
            raise ValueError("Kraj mora biti veci od pocetka")

    # generator
    def __iter__(self):
        while self.brojac < self.kraj:
            yield self.brojac
            self.brojac += 1


def generator():
    pi = PrimerIterator(10, 20)
    it = iter(pi)
    print("Ovo je iterabilni objekat: %s" % it)
    # iterate ove the iterator
    print("Rucno preuzimamo sledeci element: %d" % next(it))
    for i in it:
        print("FOR PETLJA: %d" % i)
    try:
        print(next(it))
    except StopIteration:
        print("Generator je ispraznjen")


# 1.3 __contains__ -> operator in
# 1.4 __getitem__ -> operator []

# 1.5.1 __getattr__,
# 1.5.2 __setattr__ (self.name -> self.__dict__[name] = value)
# 1.5.3 __delattr__ (del object.name)
# 1.5.4 __getattribute__ (self.__dict__[name], MRO, __getattr__)

# Operatori
# 1.6.1 Matematicki operator (__add__, __sub__, __mul__, __iadd__,...)
# 1.6.2 Operatori poredjenja (__eq__, __ne__, __lt__, __le__, __gt__, __ge__)
#   dekorator total_ordering implementira nedostajuce operatore poredjenja


def main():
    iterator()
    generator()
    pass


if __name__ == '__main__':
    main()
