"""Polskie adnotacje redakcyjne do Magnifica Humanitas.

Tłumaczenie adnotacji z ``annotations/en.py``. Każdy wpis kotwiczy notę na
marginesie do punktu akapitu poprzez dopasowanie dokładnego fragmentu tekstu
(``after``) oficjalnego polskiego tłumaczenia. Linki kierują do Wikipedii w
języku polskim, gdy tytuł jest znany, w przeciwnym razie do angielskiej
(``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "pl") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- WPROWADZENIE ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"Encyklika {_w('Leona XIII', 'Leon_XIII')} z 1891 r., dokument założycielski współczesnej {_w('katolickiej nauki społecznej', 'Katolicka_nauka_społeczna')}, napisana w odpowiedzi na wstrząsy kapitalizmu przemysłowego. Tytuł jest łaciński i znaczy <i>{_w('o rzeczach nowych', 'Rerum_novarum')}</i>. Leon XIV świadomie nawiązuje do imienia i dzieła swojego poprzednika."
    },
    {
        "p": 3, "after": "nauką społeczną Kościoła",
        "note": f"Spójny zbiór nauczania papieskiego i soborowego o życiu społecznym, gospodarczym i politycznym, rozwijany począwszy od Leona XIII. Jego podstawowe zasady — godność, dobro wspólne, pomocniczość, solidarność, sprawiedliwość — powracają w całym liście. Zob.: {_w('katolicka nauka społeczna', 'Katolicka_nauka_społeczna')}."
    },
    {
        "p": 4, "after": "rzeczach nowych",
        "note": f"<i>Res novae</i> po łacinie — wyrażenie, od którego <i>{_w('Rerum novarum', 'Rerum_novarum')}</i> bierze swoją nazwę. Leon XIV używa go na oznaczenie autentycznie nowych nacisków, jakim stawia czoła każde pokolenie."
    },
    {
        "p": 7, "after": "wieży Babel",
        "note": f"{_w('Rdz 11,1–9', 'Wieża_Babel')}. Ludzie mówiący jednym językiem postanawiają zbudować wieżę „z wierzchołkiem sięgającym nieba”, aby zdobyć sobie imię; Bóg rozprasza ich, mieszając ich mowę. Nieprzemijająca chrześcijańska przypowieść o pysze i o rozproszeniu, które następuje, gdy ludzkie dążenie zapomina o Bogu."
    },
    {
        "p": 7, "after": "odbudowę murów Jerozolimy",
        "note": f"{_w('Księga Nehemiasza', 'Księga_Nehemiasza')} (V wiek p.n.e.) opowiada o żydowskich wygnańcach powracających z {_w('Babilonu', 'Niewola_babilońska')}, by odbudować zrujnowaną Jerozolimę. Nehemiasz organizuje pracę rodzina po rodzinie, wysłuchuje skarg i stawia czoła przeszkodom. Leon ukazuje go jako wzór odbudowy rozproszonej i skoordynowanej — przeciwieństwo odgórnej unifikacji z Babel."
    },
    {
        "p": 10, "after": "synodalności",
        "note": f"Z greckiego <i>syn-hodos</i>, „iść razem”. Praktyka, którą {_w('papież Franciszek', 'Franciszek_(papież)')} uczynił centralną: decyzje kościelne podejmowane przez szerokie słuchanie i wspólne rozeznawanie, a nie przez odgórny dekret. Zob.: {_w('synodalność', 'Synodalność')}."
    },
    {
        "p": 11, "after": "św. Augustynem",
        "note": f"{_w('Augustyn z Hippony', 'Augustyn_z_Hippony')} (354–430), północnoafrykański biskup i filozof, jeden z najbardziej wpływowych myślicieli chrześcijaństwa zachodniego. Słowa o „niespokojnym sercu” to incipit jego <i>{_w('Wyznań', 'Wyznania_(Augustyn)')}</i>, autobiograficznej modlitwy."
    },
    {
        "p": 13, "after": "pomocniczości",
        "note": f"Katolicka zasada społeczna: decyzje należą do najmniejszego, najbardziej lokalnego szczebla zdolnego je podjąć; wyższe władze istnieją po to, by <i>wspierać</i> (subsidium) niższe, a nie je zastępować. Po raz pierwszy usystematyzowana przez {_w('Piusa XI', 'Pius_XI')} w 1931 r. Zob.: {_w('zasada pomocniczości', 'Zasada_pomocniczości')}."
    },
    {
        "p": 15, "after": "Zwyczajnego Roku Jubileuszowego 2025",
        "note": f"W tradycji katolickiej {_w('Jubileusz', 'Rok_jubileuszowy')} to rok pielgrzymowania, miłosierdzia i przebaczenia, obchodzony co 25 lat. Jubileusz 2025 został otwarty przez {_w('papieża Franciszka', 'Franciszek_(papież)')} pod hasłem „Pielgrzymi nadziei”."
    },

    # ---------- ROZDZIAŁ PIERWSZY ----------
    {
        "p": 17, "after": "nauczaniu Papieży",
        "note": f"Mowa o {_w('urzędzie nauczycielskim', 'Magisterium_Kościoła')} (Magisterium) Kościoła katolickiego, sprawowany przez papieża i biskupów w komunii z nim. Słowo pochodzi od łacińskiego <i>magister</i>, „nauczyciel”."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"„Radość i nadzieja” — Konstytucja duszpasterska {_w('Soboru Watykańskiego II', 'Sobór_watykański_II')} o Kościele w świecie współczesnym z 1965 r. Jej słowa otwierające („Radość i nadzieja, smutek i trwoga ludzi współczesnych… są też radością i nadzieją… uczniów Chrystusowych”) na nowo określiły stosunek Kościoła do życia świeckiego. Zob.: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Kompendium nauki społecznej Kościoła",
        "note": f"{_w('Watykańskie kompendium z 2004 r.', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')} zbierające i porządkujące naukę społeczną Kościoła od Leona XIII do Jana Pawła II. Często pierwszy punkt odniesienia przy ustalaniu, gdzie dana zasada została sformułowana."
    },
    {
        "p": 28, "after": "Laudato si’",
        "note": f"{_w('Encyklika papieża Franciszka z 2015 r.', 'Laudato_si’')} o trosce o „wspólny dom” — kryzys ekologiczny odczytany jako nieodłączny od ubóstwa i nierówności. Tytuł pochodzi z Pieśni słonecznej {_w('św. Franciszka z Asyżu', 'Franciszek_z_Asyżu')} („Pochwalony bądź, Panie mój”)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('Encyklika papieża Franciszka z 2020 r.', 'Fratelli_tutti')} o braterstwie i przyjaźni społecznej. Tytuł pochodzi od {_w('św. Franciszka z Asyżu', 'Franciszek_z_Asyżu')}: „Wszyscy bracia”."
    },
    {
        "p": 30, "after": "Magna Charta",
        "note": f"Dosł. „Wielka Karta” — {_w('angielski dokument z 1215 r.', 'Magna_Carta')} założycielski dla rządów konstytucyjnych. Pius XI używa go metaforycznie, nazywając <i>Rerum novarum</i> kartą założycielską katolickiego działania społecznego."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"„W czterdziestym roku” — {_w('encyklika Piusa XI z 1931 r.', 'Quadragesimo_anno')}, napisana w 40. rocznicę <i>Rerum novarum</i> w czasie {_w('wielkiego kryzysu', 'Wielki_kryzys')}. Wprowadziła zasadę pomocniczości w jej nowoczesnej postaci."
    },
    {
        "p": 32, "after": "prawa naturalnego",
        "note": f"{_w('Tradycja filozoficzna', 'Prawo_naturalne')} sięgająca od {_w('rzymskiego stoicyzmu', 'Stoicyzm')} po {_w('Tomasza z Akwinu', 'Tomasz_z_Akwinu')}: istnieje obiektywny porządek moralny, dostępny ludzkiemu rozumowi, uprzedni i niezależny od jakiejkolwiek władzy ludzkiej. Katolicka nauka społeczna fundamentuje tu powszechne prawa człowieka; powojenny międzynarodowy system praw czerpał z tego samego nurtu. Alternatywa — że prawa są po prostu tym, co możni gotowi są przyznać — jest dokładnie tym, co myśl prawnonaturalna ma za zadanie odrzucić."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"„Matka i nauczycielka” — {_w('encyklika z 1961 r.', 'Mater_et_magistra')} {_w('Jana XXIII', 'Jan_XXIII')}, aktualizująca katolicką naukę społeczną na potrzeby świata powojennego."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"„Pokój na ziemi” — {_w('encyklika Jana XXIII z 1963 r.', 'Pacem_in_terris')}, napisana kilka miesięcy po {_w('kryzysie kubańskim', 'Kryzys_kubański')}. Pierwsza encyklika skierowana do „wszystkich ludzi dobrej woli”, nie tylko do katolików."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"„O godności ludzkiej” — {_w('Deklaracja o wolności religijnej z 1965 r.', 'Dignitatis_humanae')} Soboru Watykańskiego II, która formalnie zobowiązała Kościół do obrony obywatelskiego prawa każdej osoby do wolności religijnej."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"„Rozwój ludów” — {_w('encyklika z 1967 r.', 'Populorum_progressio')} {_w('Pawła VI', 'Paweł_VI')}, która sam rozwój określiła jako „nowe imię pokoju” i skierowała katolicką naukę społeczną ku globalnej nierówności."
    },
    {
        "p": 35, "after": "Papieskiej Komisji Iustitia et Pax",
        "note": f"„Sprawiedliwość i pokój” — urząd watykański ustanowiony przez Pawła VI w 1967 r. dla przekładania katolickiej nauki społecznej na pracę w dziedzinie polityki międzynarodowej. Zreorganizowany w 2017 r. jako {_w('Dykasteria ds. Integralnego Rozwoju Człowieka', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"„Nadchodzący osiemdziesiąty” — {_w('list apostolski Pawła VI z 1971 r.', 'Octogesima_adveniens')} w 80. rocznicę <i>Rerum novarum</i>, o urbanizacji i o granicach każdej pojedynczej katolickiej odpowiedzi na kwestie polityczne."
    },
    {
        "p": 36, "after": "strukturami grzechu",
        "note": f"Wyrażenie {_w('Jana Pawła II', 'Jan_Paweł_II')} (w <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) na oznaczenie układów społecznych, gospodarczych i politycznych, które instytucjonalizują niesprawiedliwość. Wyrażenie przenosi grzech z czysto indywidualnych aktów na systemy, w których uczestniczymy. Zob.: {_w('grzech strukturalny', 'Structural_sin', 'en')}."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"„Wykonując pracę” — {_w('encyklika Jana Pawła II z 1981 r.', 'Laborem_exercens')} o pracy ludzkiej. Dowodziła, że praca nie jest jedynie towarem, lecz fundamentalnym wymiarem ludzkiego życia i kluczem do całej kwestii społecznej."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"„Troska o sprawy społeczne” — {_w('encyklika Jana Pawła II z 1987 r.', 'Sollicitudo_rei_socialis')} powracająca do <i>Populorum progressio</i> Pawła VI po dwudziestu latach, skupiona na powiększającej się przepaści między narodami bogatymi a ubogimi."
    },
    {
        "p": 38, "after": "cywilizacji miłości",
        "note": f"Wyrażenie ukute przez {_w('Pawła VI', 'Paweł_VI')} w 1975 r.: wizja ładu społecznego, w którym to miłość, a nie władza, jest zasadą organizującą gospodarkę, politykę i kulturę. Staje się ono tematem jednoczącym Rozdział Piąty."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"„Setny rok” — {_w('encyklika Jana Pawła II z 1991 r.', 'Centesimus_annus')} w stulecie <i>Rerum novarum</i>, napisana po upadku komunizmu. Uznaje gospodarkę rynkową tylko o tyle, o ile pozostaje ona podporządkowana prawu moralnemu i solidarności."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"„Miłość w prawdzie” — {_w('encyklika z 2009 r.', 'Caritas_in_veritate')} {_w('Benedykta XVI', 'Benedykt_XVI')} o integralnym rozwoju człowieka, napisana podczas globalnego kryzysu finansowego."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"„Radość Ewangelii” — {_w('adhortacja apostolska papieża Franciszka z 2013 r.', 'Evangelii_gaudium')}, programowy dokument jego pontyfikatu."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"„Umiłował nas” — {_w('encyklika papieża Franciszka z 2024 r.', 'Dilexit_nos')} o nabożeństwie do {_w('Najświętszego Serca Jezusa', 'Najświętsze_Serce_Jezusa')}, jego ostatni wielki list doktrynalny."
    },

    # ---------- ROZDZIAŁ DRUGI ----------
    {
        "p": 50, "after": "w Trójcy Jedynego",
        "note": f"Centralna doktryna chrześcijańska o {_w('Trójcy', 'Trójca_Święta')}: jeden Bóg w trzech osobach — Ojciec, Syn i Duch Święty — odwiecznie zjednoczonych w miłości. To właśnie ta doktryna czyni katolicką myśl społeczną relacyjną u samych korzeni."
    },
    {
        "p": 52, "after": "godność ontologiczna",
        "note": f"Z greckiego <i>on</i>, „byt” — godność przysługująca osobie z racji samego <i>bycia</i>, a nie czynienia, posiadania czy bycia uznawanym. Rozróżnienie jest {_w('arystotelesowsko-tomistyczne', 'Tomizm')}: wartość osoby płynie z tego, czym ona fundamentalnie jest (<i>esse</i>), a nie ze zmiennych właściwości jak zdolności, osiągnięcia czy pozycja społeczna."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"„Nieskończona godność” — {_w('deklaracja z 2024 r.', 'Dignitas_infinita')} watykańskiej Dykasterii Nauki Wiary, potwierdzająca bezwarunkową godność każdej osoby ludzkiej wobec długiej listy współczesnych jej naruszeń."
    },
    {
        "p": 54, "after": "Powszechna Deklaracja Praw Człowieka",
        "note": f"{_w('Przyjęta przez Zgromadzenie Ogólne ONZ', 'Powszechna_deklaracja_praw_człowieka')} 10 grudnia 1948 r. w następstwie drugiej wojny światowej. Pierwsze globalne sformułowanie praw przysługujących każdej osobie „po prostu dlatego, że jest człowiekiem”."
    },
    {
        "p": 60, "after": "dobro wspólne",
        "note": f"{_w('Pojęcie', 'Dobro_wspólne')} o głębokich korzeniach filozoficznych u {_w('Arystotelesa', 'Arystoteles')} (<i>Polityka</i>, Księga III) i {_w('Tomasza z Akwinu', 'Tomasz_z_Akwinu')}. Co kluczowe, <i>nie</i> jest ono sumą indywidualnych preferencji (redukcja utylitarystyczna) ani po prostu dobrami „publicznymi” jak czyste powietrze; jest wspólnym zespołem warunków, w których każda osoba może rozkwitać. To pojęcie odróżnia katolicką myśl społeczną zarówno od czystego indywidualizmu, jak i od czystego kolektywizmu."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Łacińskie „rzecz publiczna” — {_w('wspólnota polityczna', 'Res_publica')}, wspólna troska wszystkich obywateli. Źródłosłów słowa <i>republika</i>."
    },
    {
        "p": 82, "after": "integralny rozwój człowieka",
        "note": f"{_w('Wyrażenie ukute przez Pawła VI', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967): rozwój <i>każdego</i> człowieka i <i>całego</i> człowieka — materialny, kulturowy, moralny, duchowy. Kryterium, którym nauczanie katolickie ocenia każdy model gospodarczy."
    },
    {
        "p": 86, "after": "rachunkiem sumienia",
        "note": f"Tradycyjna katolicka praktyka duchowa — {_w('metodyczny przegląd siebie przed Bogiem', 'Rachunek_sumienia')} — czerpana zwłaszcza z {_w('ignacjańskiego', 'Duchowość_ignacjańska')} <i>examen</i>. Tutaj Leon przemienia ją z dyscypliny osobistej w dyscyplinę wspólnotową dla samego Kościoła."
    },

    # ---------- ROZDZIAŁ TRZECI ----------
    {
        "p": 92, "after": "paradygmatu technokratycznego",
        "note": f"Wyrażenie papieża Franciszka z <i>Laudato si’</i> (2015), odziedziczone po {_w('Romanie Guardinim', 'Romano_Guardini')} i współbrzmiące z krytyką techniki nowoczesnej {_w('Heideggera', 'Martin_Heidegger')}. Nie entuzjazm dla gadżetów, lecz głębszy nawyk myślowy traktujący <i>wszystko</i> — przyrodę, osoby, instytucje — jako surowiec do mierzenia, optymalizowania i kontrolowania. Paradygmat redukuje byt do funkcji, a wartość do użyteczności."
    },
    {
        "p": 93, "after": "Romana Guardiniego",
        "note": f"{_w('Włosko-niemiecki kapłan i filozof katolicki', 'Romano_Guardini')} (1885–1968). Jego dzieło <i>Koniec czasów nowożytnych</i> ostrzegało, że potęga techniczna wyprzedziła formację moralną i duchową potrzebną do jej dzierżenia. Formacyjny wpływ na Sobór Watykański II i na <i>Laudato si’</i> Franciszka."
    },
    {
        "p": 107, "after": "dostosowania",
        "note": f"Centralny termin współczesnego {_w('bezpieczeństwa AI', 'AI_alignment', 'en')}: projekt sprawienia, by systemy AI dążyły do celów zgodnych z wartościami ludzkimi. Kojarzony z <i>Human Compatible</i> (2019) {_w('Stuarta Russella', 'Stuart_J._Russell', 'en')}, pracą {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, {_w('Anthropic', 'Anthropic', 'en')} oraz wysiłkiem „{_w('superdostosowania', 'OpenAI', 'en')}” OpenAI. Zastrzeżenie Leona nie dotyczy dostosowania, lecz pytania, na które samo dostosowanie nie potrafi odpowiedzieć: <i>dostosowane do czyich wartości</i> — i kto o tym decyduje?"
    },
    {
        "p": 115, "after": "transhumanizm",
        "note": f"{_w('Ruch intelektualny XX–XXI wieku', 'Transhumanizm')} ({_w('Max More', 'Max_More', 'en')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}) wzywający do używania biotechnologii, AI i innych narzędzi do przekraczania ludzkich ograniczeń biologicznych — choroby, starzenia się, progów poznawczych, a nawet śmiertelności. Dziedziczy oświeceniowy progresywizm i powojenną cybernetykę; ma siedziby instytucjonalne w Dolinie Krzemowej i w przemyśle długowieczności. Traktuje ciało jako sprzęt, który można ulepszać."
    },
    {
        "p": 115, "after": "posthumanizm",
        "note": f"Odmienna genealogia intelektualna. {_w('Posthumanizm „krytyczny”', 'Posthumanizm')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) wywodzi się z filozofii kontynentalnej i teorii feministycznej. Decentruje człowieka — odrzucając ideę stabilnego, autonomicznego podmiotu ludzkiego — i podkreśla nasze splątanie z innymi gatunkami, maszynami i ekosystemami. Bywa sojusznikiem i bywa krytykiem transhumanizmu; obydwa łączy gotowość relatywizacji człowieka, lecz z bardzo różnych powodów."
    },
    {
        "p": 116, "after": "antropocentryzm",
        "note": f"{_w('Pogląd', 'Antropocentryzm')}, wedle którego istoty ludzkie stoją w centrum troski moralnej. Tradycja chrześcijańska była historycznie antropocentryczna; Franciszek doprecyzował to w <i>Laudato si’</i> wyrażeniem „antropocentryzm umiejscowiony” — ludzie jako stworzenia osadzone, a nie oderwani panowie. Posthumanizm odrzuca antropocentryzm ostrzej, traktując go jako iluzję oświeceniową."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Austriacki psychiatra i ocalały z Auschwitz', 'Viktor_Frankl')} (1905–1997). Jego <i>{_w('Człowiek w poszukiwaniu sensu', 'Man%27s_Search_for_Meaning', 'en')}</i> dowodził, że najgłębszym ludzkim dążeniem jest poszukiwanie sensu — wolność, której żaden warunek, choćby najbardziej nieludzki, nie może w pełni zgasić."
    },
    {
        "p": 122, "after": "IX Symfonia Beethovena",
        "note": f"{_w('Prawykonana w 1824 r.', 'IX_symfonia_Beethovena')}; jej chóralny finał intonuje „{_w('Odę do radości', 'Oda_do_radości')}” Schillera, hymn do powszechnego braterstwa. Przyjęta w 1985 r. jako hymn Unii Europejskiej."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"{_w('Obraz', 'Guernica_(obraz)')} {_w('Picassa', 'Pablo_Picasso')} z 1937 r., powstały dla Pawilonu Hiszpańskiego na wystawie w Paryżu, przedstawiający nazistowskie bombardowanie baskijskiego miasteczka Guernica podczas hiszpańskiej wojny domowej. Pomnik sztuki antywojennej."
    },
    {
        "p": 122, "after": "Lista Schindlera",
        "note": f"{_w('Film z 1993 r.', 'Lista_Schindlera')} {_w('Stevena Spielberga', 'Steven_Spielberg')} o {_w('Oskarze Schindlerze', 'Oskar_Schindler')}, niemieckim przemysłowcu, który ocalił ponad tysiąc polsko-żydowskich pracowników od zagłady podczas Holokaustu."
    },
    {
        "p": 123, "after": "Międzynarodowego Komitetu Czerwonego Krzyża",
        "note": f"{_w('Założony w Genewie w 1863 r.', 'Międzynarodowy_Komitet_Czerwonego_Krzyża')} przez {_w('Henry’ego Dunanta', 'Henry_Dunant')} po tym, jak był świadkiem rzezi {_w('bitwy pod Solferino', 'Bitwa_pod_Solferino')}. Jego operacyjna neutralność — opieka nad rannymi każdej ze stron — stała się zalążkiem międzynarodowego prawa humanitarnego."
    },
    {
        "p": 124, "after": "Martina Luthera Kinga Jr.",
        "note": f"{_w('Amerykański pastor baptystyczny', 'Martin_Luther_King')} (1929–1968) i centralny przywódca ruchu na rzecz praw obywatelskich w USA, którego pokojowe kampanie pomogły zakończyć prawną segregację rasową."
    },
    {
        "p": 124, "after": "Nelsona Mandeli",
        "note": f"{_w('Południowoafrykański przywódca walki z apartheidem', 'Nelson_Mandela')} (1918–2013), więziony przez 27 lat, następnie prezydent RPA po apartheidzie. Jego odrzucenie przemocy odwetowej ukształtowało krajowy proces {_w('Prawdy i Pojednania', 'Truth_and_Reconciliation_Commission_(South_Africa)', 'en')}."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('Amerykańska dziennikarka i działaczka', 'Dorothy_Day')} (1897–1980), współzałożycielka {_w('Catholic Worker Movement', 'Catholic_Worker_Movement', 'en')}. Łączyła wiarę katolicką, dobrowolne ubóstwo, anarchizm i pacyfizm; żyła wśród ubogich w domach gościnności na Manhattanie. Proces beatyfikacyjny otwarty w 2000 r."
    },
    {
        "p": 125, "after": "Maksymilian Maria Kolbe",
        "note": f"{_w('Polski franciszkanin konwentualny', 'Maksymilian_Maria_Kolbe')} (1894–1941). W Auschwitz zgłosił się, by zająć miejsce współwięźnia skazanego na bunkier głodowy; zmarł po dwóch tygodniach. Kanonizowany w 1982 r. jako „męczennik miłości”."
    },
    {
        "p": 125, "after": "Oscar Romero",
        "note": f"{_w('Arcybiskup San Salvador', 'Óscar_Romero')} (1917–1980), zastrzelony przy ołtarzu podczas sprawowania Mszy za wielokrotne potępianie szwadronów śmierci i represji wojskowych w salwadorskiej wojnie domowej. Kanonizowany w 2018 r."
    },
    {
        "p": 127, "after": "Tomasz z Akwinu",
        "note": f"{_w('Trzynastowieczny teolog i filozof dominikański', 'Tomasz_z_Akwinu')} (1225–1274). Jego <i>{_w('Summa teologiczna', 'Summa_teologiczna')}</i> to najbardziej wpływowa synteza teologii chrześcijańskiej na łacińskim Zachodzie; nauczał, że łaska udoskonala naturę, a nie ją niszczy."
    },
    {
        "p": 128, "after": "prometejskich",
        "note": f"Z mitu greckiego: {_w('Prometeusz', 'Prometeusz')} wykradł ogień bogom, by dać go ludzkości, i został ukarany na wieki. W myśli nowoczesnej postać ta stała się patronem ludzkiej technologicznej samoafirmacji — {_w('Mary Shelley', 'Mary_Shelley')} dała <i>{_w('Frankensteinowi', 'Frankenstein')}</i> podtytuł „Współczesny Prometeusz”; Marks chwalił „prometejskie wyzwolenie” sił ludzkich; {_w('Hans Jonas', 'Hans_Jonas')}, w <i>Zasadzie odpowiedzialności</i> (1979), ostrzegał, że technika nowoczesna dała wreszcie prometejskiej ambicji boski zasięg bez boskiej mądrości."
    },
    {
        "p": 130, "after": "Św. Augustyn",
        "note": f"W <i>{_w('Państwie Bożym', 'Państwo_Boże')}</i> (początek V wieku) Augustyn odczytuje całe dzieje jako splot dwóch miast — ziemskiego i niebieskiego — zbudowanych przez dwie przeciwne miłości. Obraz ten daje temu rozdziałowi tytuł i jednoczy kontrast encykliki między Babel a Jerozolimą."
    },

    # ---------- ROZDZIAŁ CZWARTY ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Niemiecko-amerykańska teoretyczka polityki', 'Hannah_Arendt')} (1906–1975). Jej <i>{_w('Korzenie totalitaryzmu', 'Korzenie_totalitaryzmu')}</i> (1951) i <i>{_w('Eichmann w Jerozolimie', 'Eichmann_w_Jerozolimie._Rzecz_o_banalności_zła')}</i> (1963) ukazały, jak reżimy totalitarne zależą od zacierania samego rozróżnienia między faktem a fikcją."
    },
    {
        "p": 140, "after": "Platon",
        "note": f"{_w('Filozof starogrecki', 'Platon')} (ok. 428–348 p.n.e.). Obraz zrozumienia rozpalanego niczym iskra przez długie wspólne dociekanie pochodzi z jego {_w('Listu siódmego', 'Seventh_Letter', 'en')} — obrony powolnej, dialogicznej nauki przeciw iluzji szybkiej wiedzy."
    },
    {
        "p": 148, "after": "św. Benedykta z Nursji",
        "note": f"{_w('Szóstowieczny założyciel monastycyzmu zachodniego', 'Benedykt_z_Nursji')} (ok. 480–547). Jego <i>{_w('Reguła', 'Reguła_świętego_Benedykta')}</i> splotła modlitwę i pracę fizyczną — <i>ora et labora</i> — i zbudowała duchowość pracy, która miała kształtować kulturę europejską przez tysiąclecie."
    },
    {
        "p": 151, "after": "czwartej rewolucji przemysłowej",
        "note": f"{_w('Termin spopularyzowany przez Klausa Schwaba', 'Czwarta_rewolucja_przemysłowa')} (założyciela {_w('Światowego Forum Ekonomicznego', 'Światowe_Forum_Ekonomiczne')}) na oznaczenie obecnej fuzji AI, robotyki, biotechnologii i świata fizycznego — następczyni rewolucji parowej, elektrycznej i cyfrowej, które ją poprzedziły."
    },
    {
        "p": 163, "after": "niewidzialnej ręce",
        "note": f"{_w('Metafora', 'Niewidzialna_ręka')} {_w('Adama Smitha', 'Adam_Smith')} (<i>Bogactwo narodów</i>, 1776): dążenie do własnego interesu na konkurencyjnym rynku może, w sposób niezamierzony, przynosić korzyść społeczną. Leon dołącza do długiego szeregu papieży dowodzących, że ten mechanizm, wzięty sam w sobie, nie może rządzić gospodarką."
    },

    # ---------- ROZDZIAŁ PIĄTY ----------
    {
        "p": 192, "after": "wojny sprawiedliwej",
        "note": f"{_w('Chrześcijańska tradycja', 'Wojna_sprawiedliwa')} (Augustyn, Tomasz, Vitoria, Suárez) warunków moralnych, w których wojna może być dopuszczalna — słuszna przyczyna, prawowita władza, proporcjonalność, ostateczność. Franciszek, a teraz Leon, dowodzą, że pod bronią nowoczesną kryteria te nie mogą już być spełnione."
    },
    {
        "p": 193, "after": "przemysłu zbrojeniowego",
        "note": f"Nawiązuje do „kompleksu militarno-przemysłowego”, {_w('wyrażenia ukutego przez prezydenta USA Dwighta D. Eisenhowera', 'Kompleks_militarno-przemysłowy')} w mowie pożegnalnej z 1961 r., który ostrzegał, że splecione interesy producentów broni, establishmentu wojskowego i politycznego stworzą strukturalny napęd ku trwałemu stanowi wojennemu — dokładnie troska Leona w tym miejscu, sześćdziesiąt pięć lat później."
    },
    {
        "p": 194, "after": "Traktatu o zakazie broni jądrowej",
        "note": f"{_w('Traktat ONZ z 2017 r.', 'Traktat_o_zakazie_broni_jądrowej')}, który wszedł w życie w styczniu 2021 r. Kategorycznie zakazuje opracowywania, testowania, produkowania i posiadania broni jądrowej. Stolica Apostolska była wśród pierwszych sygnatariuszy; dziewięć państw dysponujących bronią jądrową odmówiło przystąpienia."
    },
    {
        "p": 198, "after": "sztucznych podmiotach moralnych",
        "note": f"Termin z {_w('literatury o etyce maszyn', 'Machine_ethics', 'en')} (Wendell Wallach i Colin Allen, <i>Moral Machines</i>, 2008) — propozycja, że dostatecznie zaawansowane systemy AI mogłyby zostać zaprogramowane do samodzielnego formułowania osądów etycznych. Encyklika odpowiada wizją klasyczną: osąd moralny nie jest obliczeniem, lecz odpowiedzią sumienia na osobę, nieredukowalną do żadnej maszyny postępującej według reguł."
    },
    {
        "p": 201, "after": "1989",
        "note": f"Rok upadku {_w('muru berlińskiego', 'Mur_berliński')} i załamania się reżimów komunistycznych w Europie Środkowej i Wschodniej — wyznaczający koniec {_w('zimnej wojny', 'Zimna_wojna')} i początek ery „globalizacji”, którą Leon tutaj krytykuje."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Dziewiętnastowieczny termin niemiecki', 'Realpolitik')} na oznaczenie polityki prowadzonej na podstawie praktycznych i materialnych interesów, a nie ideologii czy zasady moralnej. Leon traktuje ją jako podróbkę autentycznego realizmu politycznego."
    },
    {
        "p": 213, "after": "John Ronald Reuel Tolkien",
        "note": f"{_w('Angielski pisarz', 'J._R._R._Tolkien')} (1892–1973), gorliwy katolik, twórca <i>{_w('Władcy Pierścieni', 'Władca_Pierścieni')}</i>. Cytat należy do Gandalfa, z <i>{_w('Powrotu króla', 'Powrót_króla')}</i>: powołanie określone przez troskę o powierzony nam skrawek ziemi."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Włoski katolicki mąż stanu', 'Giorgio_La_Pira')} (1904–1977), wielokrotny burmistrz Florencji i niestrudzony organizator konferencji pokojowych ery zimnej wojny, ponad podziałami religijnymi i ideologicznymi. Beatyfikowany w 2018 r."
    },
    {
        "p": 222, "after": "manichejskie",
        "note": f"Od {_w('Maniego', 'Mani_(prorok)')} (216–276 n.e.), założyciela {_w('perskiej religii dualistycznej', 'Manicheizm')}, która odczytywała dzieje jako kosmiczną bitwę między równymi i przeciwnymi siłami światła i ciemności. {_w('Augustyn', 'Augustyn_z_Hippony')} był manichejczykiem przez dziewięć lat przed nawróceniem; jego późniejsza teologia zła jako <i>braku</i> (nieobecności, a nie substancji) została zbudowana przeciw temu dualizmowi. Słowo to oznacza dziś każdy światopogląd, który dzieli świat na czyste obozy dobra i zła."
    },
    {
        "p": 223, "after": "Duch Asyżu",
        "note": f"27 października 1986 r. Jan Paweł II zgromadził w Asyżu przywódców religii świata, {_w('by modlić się o pokój', 'Day_of_Prayer_for_World_Peace', 'en')} — precedens międzyreligijnego budowania pokoju, który Franciszek wielokrotnie odnawiał podczas swojego pontyfikatu."
    },
    {
        "p": 223, "after": "Wielkim Imamem Al-Azharu",
        "note": f"{_w('Ahmad at-Tajjib', 'Ahmad_at-Tajjib')}, zwierzchnik kairskiego {_w('uniwersytetu-meczetu Al-Azhar', 'Uniwersytet_Al-Azhar')} (głównego autorytetu islamu sunnickiego). On i papież Franciszek podpisali {_w('Dokument o ludzkim braterstwie z 2019 r.', 'Document_on_Human_Fraternity', 'en')} w Abu Zabi."
    },

    # ---------- ZAKOŃCZENIE ----------
    {
        "p": 230, "after": "Magnificat",
        "note": f"{_w('Hymn uwielbienia', 'Magnificat')} {_w('Maryi', 'Maria_z_Nazaretu')} w Łk 1,46–55, odmawiany codziennie w Nieszporach Kościoła: „Wielbi dusza moja Pana… strącił władców z tronu, a wywyższył pokornych”. Tytuł encykliki <i>Magnifica Humanitas</i> czerpie natchnienie z tej pieśni."
    },
    {
        "p": 233, "after": "rekapitulacji",
        "note": f"Z greckiego <i>anakephalaíōsis</i>, „streścić pod jedną głową” (Ef 1,10). Wczesny Ojciec {_w('Ireneusz', 'Ireneusz_z_Lyonu')} uczynił to centralnym obrazem zbawienia: Chrystus gromadzi w sobie całe stworzenie, każdy okruch i każdą ranę."
    },
    {
        "p": 234, "after": "św. Augustyn",
        "note": f"Przytoczony fragment pochodzi z {_w('Mowy 272 Augustyna', 'Sermon_272', 'en')}, wygłoszonej do nowo ochrzczonych chrześcijan o Eucharystii: „Bądźcie tym, co widzicie, i przyjmijcie to, czym jesteście”. Dobitne stwierdzenie teologii patrystycznej, wedle której Kościół <i>jest</i> ciałem Chrystusa — a nie jedynie społecznością gromadzącą się wokół niego."
    },
    {
        "p": 237, "after": "antropocentryzmem umiejscowionym",
        "note": f"Wyrażenie Franciszka z <i>{_w('Laudato si’', 'Laudato_si’')}</i> (§118): świadoma korekta oświeceniowego antropocentryzmu. Istoty ludzkie pozostają moralnie centralne, lecz jako stworzenia osadzone w szerszej sieci życia i od niej zależne — a nie jako oderwane podmioty stojące nad bezwładną przyrodą. Przywołanie Leona zamyka tutaj krąg otwarty w omówieniu transhumanizmu w Rozdziale Trzecim: alternatywą wobec „pozostawienia człowieka za sobą” nie jest intronizacja człowieka, lecz ponowne umieszczenie nas w naszej stworzonej wspólnocie."
    },
]
