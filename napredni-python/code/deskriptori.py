# 3. Deskriptori

# 3.1 problem sa properties

from weakref import WeakKeyDictionary


class AProperties:
    def __init__(self, broj):
        self._prirodan_broj = 1

    @property
    def prirodan_broj(self):
        return self._prirodan_broj

    @prirodan_broj.setter
    def prirodan_broj(self, broj):
        if not isinstance(broj, int):
            raise ValueError("Broj mora biti ceo")
        if broj <= 0:
            raise ValueError("Broj nije prirodan")
        self._prirodan_broj = broj


class PrirodanBroj():
    def __init__(self):
        self.podrazumevana_vrednost = 1
        self.podaci = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.podaci.get(instance, self.podrazumevana_vrednost)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Broj mora biti ceo")
        if value <= 0:
            raise ValueError("Broj nije prirodan")
        self.podaci[instance] = value


class ADescriptor:
    prirodan_broj = PrirodanBroj()

    def __init__(self, broj):
        self.prirodan_broj = broj

    # nema boiler plate koda u nasoj klasi
    # mozemo na vise mesta da odradimo ustu proveru


if __name__ == '__main__':
    # Test AProperties
    ap = AProperties(100)
    ap.prirodan_broj = 1
    ap.prirodan_broj = 3
    print(ap.prirodan_broj)
    try:
        ap.prirodan_broj = -1
    except ValueError:
        print("Broj nije prirodan")

    # test ADescriptor
    ad = ADescriptor(100)
    ad.prirodan_broj = 1
    ad.prirodan_broj = 3
    print(ad.prirodan_broj)
    try:
        ad.prirodan_broj = -1
    except ValueError:
        print("Broj nije prirodan")
