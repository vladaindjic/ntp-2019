# Jezici specifični za domen (engl. Domain Specific Languages)
- Jezici koji se koriste za iskazivanje rešenja problema tačno određenog domena.
- Manje ili više pokrivaju domen problema. U idealnom slučaju ga pokrivaju tačno.
- Mogu biti vizuelni i tekstualni (mi ćemo se fokusirati na ove druge).
- Tekstualni DSL-ovi se obično prevode na jezik opšte namene (engl. 
*general purpose language*). GPL se dalje prevodi na 
mašinski jezik, koji se izvršava na ciljnoj hardverskoj arhitekturi.

## Programski prevodioci
- Proces prevođenja DSL-a na GPL (*General Purpose Language*) obavlja programski prevodilac.
- Programski prevodioci su programi koji program iskazan jezikom višeg nivoa
(u našem slučaju DSL-om) 
prevode na ekvivalentan program iskazan jezikom nižeg nivoa
(u našem slučaju GPL-om).
- Programski prevodioci se obično sastoje iz dva dela: prednjeg i zadnjeg.
- Prednji deo obavlja: sintaksnu i semantičku analizu, generisanje međukoda i optimizaciju istog.
- Zadnji deo obavlja: generisanje koda i eventualno optimizaciju koda.
- Mi ćemo se na ovom kursu pretežno baviti sintaksnom analizom.
- Programske prevodioce ćemo pisati [textX alatom](http://textx.github.io/textX/stable/).

## Sintaksna analiza
- Proces u kome se proverava korektnost programa u skladu sa sintaksnim pravilima.
- Sintaksa pravila se iskazuju uglavnom nekom vrstom Bakus-Naurove forme
- Rezultat sintaksne analize je (apstraktno) sintaksno stablo
- Sintaksna analiza se drugačije naziva parsiranje.
- Obavljaju je parseri.
- Parsiranje može biti: silazno (engl. *top-down*) i uzlazno (engl. *bottom-up*).

### Silazno parsiranje
- Silazno parsirinje kreće od početnog neterminalnog simbola
gramatike, koji predstavlja korenski čvor apstraktnog stabla sintakse. Spuštajući se
niz stablo, primenjuje pravila izvođenja sa namerom da dođe do terminalnih simbola
koji odgovaraju sekvenci karaktera izvornog koda.
- Ne podržavaju levu rekurziju. 
- Na SPP-u smo sami pisali silazni parser.

### Uzlazno parsiranje
- Uzlazno parsiranje kreće od niza terminalnih simbola, koji
odgovaraju ulaznoj sekvenci karaktera izvornog koda. Pokušava da ih zameni sa
odgovarajućim neterminalnim simbolima, penjući se uz apstraktno stablo sintakse sve
do korenskog čvora. Ovaj čvor predstavlja početni neterminalni simbol gramatike
- Podržavaju levu rekurziju.
- Kao primer uzlaznih parsera, najčešće se navode LR parseri, za koje je
karakteristično da sekvencu terminalnih simbola čitaju sa leva na desno (engl. *Left-to-right*)
gradeći najviše desno izvođenje u obrnutom redosledu (engl. *Right-most derivation in
reverse*)
- Drugi naziv za LR parsere je *Shift-Reduce*. Kao što im samo ime kaže, koriste dva tipa operacija shift i reduce.
- Na PP-u smo koristili Flex i Bison.
- Koga zanimaju LR parseru, može da pogleda [parglare](http://www.igordejanovic.net/parglare/grammar_language/).

## textX
- textX koristi PEG parser (posebna vrsta silaznog parsera).
- Bitan redosled navođenja izbora. 
- Prilikom pisanje PEG gramatike potrebno je razmišljati
kao parser.
- Ove gramatike nisu deklarativne prirode. 
- Nije dovoljno samo navesti šta parser treba da uradi, već i kako.
- Rezultat rada textX parsera je sintaksno stablo iskazano Python objektima.
- Pogledati primere koda.

## Literatura
- http://textx.github.io/textX/stable/
- http://www.igordejanovic.net/parglare/stable/
- http://textx.github.io/textX/stable/tutorials/hello_world/
- http://textx.github.io/textX/stable/tutorials/robot/
- http://textx.github.io/textX/stable/tutorials/entity/
- https://github.com/textX/textX
- https://github.com/textX/textX/blob/master/examples/expression/calc_processors.py