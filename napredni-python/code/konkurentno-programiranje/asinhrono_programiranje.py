import asyncio
import time


# Da li su beskonacne sekvence moguce u Python-u?

# Sve je krenulo sa generatorima (Python 2.2) kao jednostavnim iteratorima.
# Ukoliko se pauziranju generatora pridoda i slanje vrednosti generatoru (send metoda) koji
# nastavlja sa izvrsavanjem od mesta pauziranja, onda se dobije koncept korutine (Python 2.5)


# Korutine - banalno receno funkcije cije se izvrsavanja moze pauzirati (podseca na generator)


def prvi():
    return (yield 33)


def drugi():
    # isrpljuje sve vrednosti generatora prvi
    return (yield from prvi())


def jos_malo_generatora():
    gen = drugi()
    print(gen)
    print(next(gen))
    gen.send(83)


# Event loop (uprosceno) - beskonacna petlja koja osluskuje i ceka neke dogadjaja i na njih reaguje
# na odgovarajuci nacin (GUI programiranje, JavaScript, ...)
# Event loop moze da se ponasa i kao scheduler ako nesto zelimo u posebnoj niti ili procesu da uradimo.
# Obratite paznju da asinhrono programiranje moze da radi i sa samo jednom niti
# (setite se kako radi NodeJS)


# Asinhrono programiranje - programiranje u kome se ne zna unapred tacan redosled izvrsavanja
# Konkurentno programiranje - pisanje koda tako da se delovi nezavisno izvrsavaju, cak i ako ih samo jedna
# nit izvrsava.
# Konkurentnost ne podrazumeva paralelizam.
# Konkurentnost - kompozicija nezavisnih nezavisnih izvrsnih jedinica
# (vise nezavisnih delova koda unutar jedne niti, vise niti, vise procesa)
# Paralelizam - simultano izvrsavanje racunjanja (engl. computation), tj. izvrsnih jedinica
# Paralelno programiranje je podskup konkurentnog izvrsavanja.
# Koliko god mi prizeljkivali da se procesi i/ili niti paralelno izvrsavaju, ako imamo samo jedan CPU
# oni ce se "najvise" (sta ako nemamo opciju multitaskinga na OS-u) konkurentno izvrsavati.

# Kako je sve to izgledalo u Python-u 3.4
# Da ne bi bilo zabune da li je neki generator slucajno postao i korutina,
# generator koji zelimo da bude i korutina bi trebalo da oznacimo sa @asyncio.coroutine

@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1


def dva_asinhrona_brojaca():
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(countdown("A", 2)),
        asyncio.ensure_future(countdown("B", 3))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


# Od Pythona 3.5 async/await uveden.
# Nije potreban dekorator @asyncio.coroutine vec na nivou sintakse
# kljucnom reci async oznacavamo da je nesto korutina.
# Unutar ovako oznacene korutine ne smemo imati yield, samo return i await.
# Sada zaista uvodimo korutinu kao tip, a ne posmatramo samo kao interfejs sto je bilo u prethodnoj verziji Pythona
# Jasna razlika izmedju generatora i generatora koji je namenjen da bude korutina.
# await radi slicno kao yield from, ali prima drugacije objekte
# await prima awaitable objekat (implementira metodu __await__),
# koja vraca iterator, koji nije korutina)
# korutine su awaitable objekti

# yield from VS await - yield from prihavata i generator koji nije korutina

# @asyncio.coroutine - generator-based korutina
# async def - korutina
# upotreba async da ne pomesamo generator-based korutinu i generator


# Zgodno je korisiti ainshrono programiranje kada imamo sledeci scenario.
# U primeru koji sledi simuliramo dugotrajne blokirajuce I/O, odnosno mrezne operacije.
# (!!! Obratiti paznju da se sve izvrsava u jednoj niti)


async def dugotrajna_mrezna_operacije_sinhrona(seconds):
    # nema aktiviranja event loop-a
    time.sleep(seconds)


async def dugotrajna_mrezna_operacije_asinhrona(seconds):
    # aktivira se event loop koji prebacuju naredni zadatak na izvrsavanje
    await asyncio.sleep(seconds)


async def dobavi_prvi_entitet(razmena):
    print("Pocinjem dobavljanje prvog entiteta")
    await razmena(5)
    print("Prvi sadrzaj skinut")


async def dobavi_drugi_entitet(razmena):
    print("Pocinjem svlacenje drugog sadrzaja")
    await razmena(15)
    print("Drugi sadrzaj skinut")


async def dobavi_treci_entitet(razmena):
    print("Pocinjem svlacenje treceg sadrzaja")
    await razmena(10)
    print("Treci sadrzaj skinut")


def napravi_sinhrone_zadatke():
    return [
        asyncio.ensure_future(dobavi_prvi_entitet(dugotrajna_mrezna_operacije_sinhrona)),
        asyncio.ensure_future(dobavi_drugi_entitet(dugotrajna_mrezna_operacije_sinhrona)),
        asyncio.ensure_future(dobavi_treci_entitet(dugotrajna_mrezna_operacije_sinhrona)),
    ]


def napravi_asinhrone_zadatke():
    return [
        asyncio.ensure_future(dobavi_prvi_entitet(dugotrajna_mrezna_operacije_asinhrona)),
        asyncio.ensure_future(dobavi_drugi_entitet(dugotrajna_mrezna_operacije_asinhrona)),
        asyncio.ensure_future(dobavi_treci_entitet(dugotrajna_mrezna_operacije_asinhrona)),
    ]


def dobavi_sve_entitete(napravi_zadatke):
    pocetak = time.time()
    loop = asyncio.get_event_loop()
    tasks = napravi_zadatke()
    loop.run_until_complete(asyncio.wait(tasks))
    kraj = time.time()
    print("Proteklo vreme: %s" % (kraj - pocetak))


def primer_asinhronog_programiranja():
    dobavi_sve_entitete(napravi_sinhrone_zadatke)
    print("===" * 11)
    dobavi_sve_entitete(napravi_asinhrone_zadatke)


if __name__ == '__main__':
    # primer_asinhronog_programiranja()
    # jos_malo_generatora()
    dva_asinhrona_brojaca()

# async/await je API za asinhrono programiranje ali nas ne vezuje za specifican event-loop
# (npr. na nizem nivou, asyncio i curio rade drugacije, a koriste isti API)
# async/await je fleksibilan mehanizam i to je ono sto Python zagovara

