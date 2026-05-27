"""Annotazioni editoriali italiane per Magnifica Humanitas.

Traduzione delle annotazioni di ``annotations.py``. Ogni voce àncora una nota al
margine a un punto del paragrafo facendo corrispondere un frammento di testo
esatto (``after``) della traduzione ufficiale italiana. I collegamenti puntano
a Wikipedia in italiano quando il titolo è noto, altrimenti a quella inglese
(``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "it") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- INTRODUZIONE ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"L'enciclica del 1891 di {_w('Leone XIII', 'Papa_Leone_XIII')}, documento fondativo della moderna {_w('Dottrina sociale cattolica', 'Dottrina_sociale_della_Chiesa')}, scritta in risposta agli sconvolgimenti del capitalismo industriale. Il titolo è latino e significa <i>{_w('delle cose nuove', 'Rerum_novarum')}</i>. Leone XIV richiama deliberatamente il nome e il progetto del suo predecessore."
    },
    {
        "p": 3, "after": "Dottrina sociale della Chiesa",
        "note": f"Un corpo coerente di insegnamento pontificio e conciliare sulla vita sociale, economica e politica, sviluppato a partire da Leone XIII. I suoi principi fondamentali — dignità, bene comune, sussidiarietà, solidarietà, giustizia — ricorrono in tutta la lettera. Vedi: {_w('Dottrina sociale della Chiesa', 'Dottrina_sociale_della_Chiesa')}."
    },
    {
        "p": 4, "after": "nuove questioni",
        "note": f"<i>Res novae</i> in latino — l'espressione da cui <i>{_w('Rerum novarum', 'Rerum_novarum')}</i> prende il nome. Leone XIV la usa per indicare le pressioni autenticamente nuove che ogni generazione affronta."
    },
    {
        "p": 7, "after": "torre di Babele",
        "note": f"{_w('Genesi 11,1-9', 'Torre_di_Babele')}. Uomini che parlano un'unica lingua si propongono di costruire una torre «con la cima nel cielo» per farsi un nome; Dio li disperde confondendo la loro lingua. Una perenne parabola cristiana della superbia e della frammentazione che segue quando l'agire umano dimentica Dio."
    },
    {
        "p": 7, "after": "ricostruzione delle mura di Gerusalemme",
        "note": f"Il {_w('Libro di Neemia', 'Libro_di_Neemia')} (V secolo a.C.) narra degli esuli ebrei che tornano da {_w('Babilonia', 'Cattività_babilonese')} per ricostruire una Gerusalemme in rovina. Neemia organizza il lavoro famiglia per famiglia, ascolta le lamentele e affronta le opposizioni. Leone lo addita come modello di riparazione distribuita e coordinata — l'opposto dell'unificazione dall'alto di Babele."
    },
    {
        "p": 10, "after": "sinodalità",
        "note": f"Dal greco <i>syn-hodos</i>, «camminare insieme». Una pratica resa centrale da {_w('Papa Francesco', 'Papa_Francesco')}: decisioni ecclesiali raggiunte attraverso un ampio ascolto e un discernimento condiviso anziché per decreto dall'alto. Vedi: {_w('sinodalità', 'Sinodalità')}."
    },
    {
        "p": 11, "after": "Agostino",
        "note": f"{_w('Agostino d\'Ippona', 'Agostino_d\'Ippona')} (354-430), vescovo e filosofo nordafricano, uno dei pensatori più influenti del cristianesimo occidentale. Il «cuore inquieto» è l'incipit delle sue <i>{_w('Confessioni', 'Confessioni_(Agostino)')}</i>, la sua preghiera autobiografica."
    },
    {
        "p": 13, "after": "sussidiarietà",
        "note": f"Principio sociale cattolico: le decisioni spettano al livello più piccolo e locale capace di prenderle; le autorità superiori esistono per <i>sostenere</i> (subsidium) quelle inferiori, non per sostituirle. Sistematizzato per la prima volta da {_w('Pio XI', 'Papa_Pio_XI')} nel 1931. Vedi: {_w('sussidiarietà', 'Sussidiarietà')}."
    },
    {
        "p": 15, "after": "Giubileo Ordinario del 2025",
        "note": f"Nella tradizione cattolica il {_w('Giubileo', 'Giubileo')} è un anno di pellegrinaggio, misericordia e perdono, celebrato ogni 25 anni. Il Giubileo 2025 è stato aperto da {_w('Papa Francesco', 'Papa_Francesco')} con il tema «Pellegrini di speranza»."
    },

    # ---------- CAPITOLO PRIMO ----------
    {
        "p": 17, "after": "Magistero",
        "note": f"L'{_w('autorità di insegnamento', 'Magistero')} ufficiale della Chiesa cattolica, esercitata dal Papa e dai vescovi in comunione con lui. La parola viene dal latino <i>magister</i>, «maestro»."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"«Gioia e speranza» — la Costituzione pastorale del 1965 del {_w('Concilio Vaticano II', 'Concilio_Vaticano_II')} sulla Chiesa nel mondo contemporaneo. Le sue parole d'apertura («Le gioie e le speranze, le tristezze e le angosce degli uomini d'oggi… sono pure le gioie e le speranze… dei discepoli di Cristo») hanno ridefinito il rapporto della Chiesa con la vita secolare. Vedi: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Compendio della Dottrina sociale della Chiesa",
        "note": f"Un {_w('testo di riferimento vaticano del 2004', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')} che raccoglie e sistematizza l'insegnamento sociale della Chiesa da Leone XIII a Giovanni Paolo II. Spesso la prima tappa per rintracciare dove un principio è stato formulato."
    },
    {
        "p": 28, "after": "Laudato si",
        "note": f"{_w('L\'enciclica del 2015 di Papa Francesco', 'Laudato_si\'')} sulla cura della «casa comune» — la crisi ambientale letta come inseparabile da povertà e disuguaglianza. Il titolo viene dal Cantico delle creature di {_w('San Francesco d\'Assisi', 'Francesco_d\'Assisi')} («Laudato si', mi' Signore»)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('L\'enciclica del 2020 di Papa Francesco', 'Fratelli_tutti')} sulla fraternità e l'amicizia sociale. Il titolo è di {_w('San Francesco d\'Assisi', 'Francesco_d\'Assisi')}."
    },
    {
        "p": 30, "after": "Magna Charta",
        "note": f"Lett. «Grande Carta» — il {_w('documento inglese del 1215', 'Magna_Carta', 'en')} fondativo del governo costituzionale. Pio XI la usa metaforicamente per chiamare la <i>Rerum novarum</i> la carta fondativa dell'azione sociale cattolica."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"«Nel quarantesimo anno» — {_w('l\'enciclica del 1931 di Pio XI', 'Quadragesimo_anno')}, scritta nel 40° anniversario della <i>Rerum novarum</i> nel pieno della {_w('Grande depressione', 'Grande_depressione')}. Introdusse il principio di sussidiarietà nella sua forma moderna."
    },
    {
        "p": 32, "after": "diritto naturale",
        "note": f"Una {_w('tradizione filosofica', 'Diritto_naturale')} che va dalla {_w('Roma stoica', 'Stoicismo')} a {_w('Tommaso d\'Aquino', 'Tommaso_d\'Aquino')}: esiste un ordine morale oggettivo, accessibile alla ragione umana, anteriore e indipendente da ogni autorità umana. La Dottrina sociale cattolica vi fonda i diritti umani universali; il sistema internazionale dei diritti del dopoguerra attinse alla stessa corrente. L'alternativa — che i diritti siano semplicemente ciò che i potenti sono disposti a concedere — è precisamente ciò che il pensiero giusnaturalista è costruito per rifiutare."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"«Madre e maestra» — {_w('l\'enciclica del 1961', 'Mater_et_magistra')} di {_w('Giovanni XXIII', 'Papa_Giovanni_XXIII')} che aggiorna la Dottrina sociale cattolica per il mondo del dopoguerra."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"«Pace in terra» — {_w('l\'enciclica del 1963 di Giovanni XXIII', 'Pacem_in_terris')}, scritta pochi mesi dopo la {_w('crisi dei missili di Cuba', 'Crisi_dei_missili_di_Cuba')}. La prima enciclica rivolta a «tutti gli uomini di buona volontà», non solo ai cattolici."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"«Della dignità umana» — la {_w('Dichiarazione sulla libertà religiosa del 1965', 'Dignitatis_humanae')} del Vaticano II, che impegnò formalmente la Chiesa a difendere il diritto civile di ogni persona alla libertà religiosa."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"«Lo sviluppo dei popoli» — {_w('l\'enciclica del 1967', 'Populorum_progressio')} di {_w('Paolo VI', 'Papa_Paolo_VI')}, che definì lo sviluppo stesso «il nuovo nome della pace» e orientò la Dottrina sociale cattolica verso la disuguaglianza globale."
    },
    {
        "p": 35, "after": "Pontificia Commissione Iustitia et Pax",
        "note": f"«Giustizia e pace» — l'ufficio vaticano istituito da Paolo VI nel 1967 per tradurre la Dottrina sociale cattolica in lavoro di politica internazionale. Riorganizzato nel 2017 come {_w('Dicastero per il Servizio dello Sviluppo Umano Integrale', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"«L'ottantesimo che viene» — la {_w('lettera apostolica del 1971', 'Octogesima_adveniens')} di Paolo VI nell'80° anniversario della <i>Rerum novarum</i>, sull'urbanizzazione e sui limiti di ogni singola risposta cattolica alle questioni politiche."
    },
    {
        "p": 36, "after": "strutture di peccato",
        "note": f"Espressione di {_w('Giovanni Paolo II', 'Papa_Giovanni_Paolo_II')} (nella <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) per gli assetti sociali, economici e politici che istituzionalizzano l'ingiustizia. L'espressione sposta il peccato dai soli atti individuali ai sistemi a cui partecipiamo."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"«Compiendo il lavoro» — {_w('l\'enciclica del 1981 di Giovanni Paolo II', 'Laborem_exercens')} sul lavoro umano. Sostenne che il lavoro non è solo una merce ma una dimensione fondamentale della vita umana, e la chiave dell'intera questione sociale."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"«La sollecitudine per le cose sociali» — {_w('l\'enciclica del 1987 di Giovanni Paolo II', 'Sollicitudo_rei_socialis')} che rivisita la <i>Populorum progressio</i> di Paolo VI vent'anni dopo, incentrata sul divario crescente tra nazioni ricche e povere."
    },
    {
        "p": 38, "after": "civiltà dell’amore",
        "note": f"Espressione coniata da {_w('Paolo VI', 'Papa_Paolo_VI')} nel 1975: una visione dell'ordine sociale in cui la carità, non il potere, è il principio organizzatore di economia, politica e cultura. Diventa il tema unificante del Capitolo Quinto."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"«Il centesimo anno» — {_w('l\'enciclica del 1991 di Giovanni Paolo II', 'Centesimus_annus')} nel centenario della <i>Rerum novarum</i>, scritta dopo la caduta del comunismo. Riconosce l'economia di mercato solo nella misura in cui resta subordinata alla legge morale e alla solidarietà."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"«La carità nella verità» — {_w('l\'enciclica del 2009', 'Caritas_in_veritate')} di {_w('Benedetto XVI', 'Papa_Benedetto_XVI')} sullo sviluppo umano integrale, scritta durante la crisi finanziaria globale."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"«La gioia del Vangelo» — {_w('l\'esortazione apostolica del 2013 di Papa Francesco', 'Evangelii_gaudium')}, il documento programmatico del suo pontificato."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"«Ci ha amati» — {_w('l\'enciclica del 2024 di Papa Francesco', 'Dilexit_nos')} sulla devozione al {_w('Sacro Cuore di Gesù', 'Sacro_Cuore')}, la sua ultima grande lettera dottrinale."
    },

    # ---------- CAPITOLO SECONDO ----------
    {
        "p": 50, "after": "Dio trinitario",
        "note": f"La dottrina cristiana centrale della {_w('Trinità', 'Trinità_(cristianesimo)')}: un solo Dio in tre persone — Padre, Figlio e Spirito Santo — eternamente uniti nell'amore. È questa dottrina a rendere il pensiero sociale cattolico relazionale alla radice."
    },
    {
        "p": 52, "after": "dignità ontologica",
        "note": f"Dal greco <i>on</i>, «essere» — la dignità che appartiene a una persona in virtù dell'<i>essere</i>, non del fare, dell'avere o dell'essere riconosciuta. La distinzione è {_w('aristotelico-tomista', 'Tomismo')}: il valore di una persona deriva da ciò che fondamentalmente è (<i>esse</i>), non da proprietà variabili come capacità, successo o posizione sociale."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"«Dignità infinita» — una {_w('dichiarazione del 2024', 'Dignitas_infinita')} del Dicastero per la Dottrina della Fede che afferma la dignità incondizionata di ogni persona umana contro un lungo elenco di violazioni contemporanee."
    },
    {
        "p": 54, "after": "Dichiarazione Universale dei Diritti",
        "note": f"{_w('Adottata dall\'Assemblea generale dell\'ONU', 'Dichiarazione_universale_dei_diritti_umani')} il 10 dicembre 1948 all'indomani della Seconda guerra mondiale. La prima formulazione globale dei diritti che appartengono a ogni persona «semplicemente perché umana»."
    },
    {
        "p": 60, "after": "bene comune",
        "note": f"Un {_w('concetto', 'Bene_comune')} dalle radici filosofiche profonde in {_w('Aristotele', 'Aristotele')} (<i>Politica</i>, Libro III) e {_w('Tommaso d\'Aquino', 'Tommaso_d\'Aquino')}. Crucialmente, <i>non</i> è la somma delle preferenze individuali (la riduzione utilitarista) né semplicemente beni «pubblici» come l'aria pulita; è l'insieme condiviso di condizioni in cui ciascuno può fiorire. È il concetto che distingue il pensiero sociale cattolico tanto dal puro individualismo quanto dal puro collettivismo."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Latino per «cosa pubblica» — la {_w('comunità politica', 'Res_publica')}, l'interesse condiviso di tutti i cittadini. Radice della parola <i>repubblica</i>."
    },
    {
        "p": 82, "after": "sviluppo umano integrale",
        "note": f"{_w('Espressione coniata da Paolo VI', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967): sviluppo di <i>ogni</i> persona e di <i>tutta</i> la persona — materiale, culturale, morale, spirituale. Il criterio con cui l'insegnamento cattolico valuta ogni modello economico."
    },
    {
        "p": 86, "after": "esame di coscienza",
        "note": f"Una tradizionale pratica spirituale cattolica — {_w('una revisione metodica di sé davanti a Dio', 'Esame_di_coscienza')} — derivata in particolare dall'<i>examen</i> {_w('ignaziano', 'Ignatian_spirituality', 'en')}. Qui Leone la trasforma da disciplina personale in disciplina comunitaria per la Chiesa stessa."
    },

    # ---------- CAPITOLO TERZO ----------
    {
        "p": 92, "after": "paradigma tecnocratico",
        "note": f"Espressione di Papa Francesco nella <i>Laudato si'</i> (2015), ereditata da {_w('Romano Guardini', 'Romano_Guardini')} e in risonanza con la critica della tecnica moderna di {_w('Heidegger', 'Martin_Heidegger')}. Non entusiasmo per i congegni, ma l'abitudine mentale più profonda che tratta <i>tutto</i> — natura, persone, istituzioni — come materia prima da misurare, ottimizzare e controllare. Il paradigma riduce l'essere a funzione e il valore a utilità."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Sacerdote e filosofo cattolico italo-tedesco', 'Romano_Guardini')} (1885-1968). La sua opera <i>La fine dell'epoca moderna</i> ammoniva che il potere tecnico aveva superato la formazione morale e spirituale necessaria a esercitarlo. Influenza formativa sul Vaticano II e sulla <i>Laudato si'</i> di Francesco."
    },
    {
        "p": 107, "after": "allineamento",
        "note": f"Termine centrale della contemporanea {_w('sicurezza dell\'IA', 'AI_alignment', 'en')}: il progetto di rendere i sistemi di IA orientati a obiettivi coerenti con i valori umani. Associato a <i>Human Compatible</i> (2019) di {_w('Stuart Russell', 'Stuart_J._Russell', 'en')}, al lavoro del {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, di {_w('Anthropic', 'Anthropic', 'en')} e allo sforzo di «{_w('superallineamento', 'OpenAI', 'en')}» di OpenAI. L'obiezione di Leone non è all'allineamento ma alla domanda a cui l'allineamento da solo non può rispondere: <i>allineato ai valori di chi</i> — e deciso da chi?"
    },
    {
        "p": 115, "after": "transumanesimo",
        "note": f"Un {_w('movimento intellettuale del XX-XXI secolo', 'Transumanesimo')} ({_w('Max More', 'Max_More', 'en')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom', 'en')}, {_w('Ray Kurzweil', 'Ray_Kurzweil', 'en')}) che esorta a usare biotecnologie, IA e altri strumenti per superare i limiti biologici umani — malattia, invecchiamento, soglie cognitive, persino la mortalità. Eredita il progressismo illuminista e la cibernetica del dopoguerra; ha sedi istituzionali nella Silicon Valley e nell'industria della longevità. Tratta il corpo come hardware aggiornabile."
    },
    {
        "p": 115, "after": "postumanesimo",
        "note": f"Una diversa genealogia intellettuale. Il {_w('postumanesimo «critico»', 'Postumanesimo')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) discende dalla filosofia continentale e dalla teoria femminista. Decentra l'umano — rifiutando l'idea di un soggetto umano stabile e autonomo — e sottolinea il nostro intreccio con altre specie, macchine ed ecosistemi. A volte alleato e a volte critico del transumanesimo; i due condividono la disponibilità a relativizzare l'umano, ma per ragioni molto diverse."
    },
    {
        "p": 116, "after": "antropocentrismo",
        "note": f"La {_w('concezione', 'Antropocentrismo')} secondo cui gli esseri umani stanno al centro della considerazione morale. La tradizione cristiana è stata storicamente antropocentrica; Francesco l'ha precisata nella <i>Laudato si'</i> con l'espressione «antropocentrismo situato» — gli esseri umani come creature inserite, non come padroni distaccati. Il postumanesimo rifiuta l'antropocentrismo più nettamente, considerandolo un'illusione illuminista."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Psichiatra austriaco e sopravvissuto ad Auschwitz', 'Viktor_Frankl')} (1905-1997). Il suo <i>{_w('Alla ricerca di un significato della vita', 'Man%27s_Search_for_Meaning', 'en')}</i> sosteneva che la spinta umana più profonda è la ricerca di significato — una libertà che nessuna condizione, per quanto disumana, può estinguere del tutto."
    },
    {
        "p": 122, "after": "Nona di Beethoven",
        "note": f"{_w('Eseguita per la prima volta nel 1824', 'Sinfonia_n._9_(Beethoven)')}; il suo finale corale intona l'«{_w('Inno alla gioia', 'Inno_alla_gioia')}» di Schiller, un canto alla fratellanza universale. Adottato nel 1985 come inno dell'Unione europea."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"Il {_w('dipinto del 1937', 'Guernica_(Picasso)')} di {_w('Picasso', 'Pablo_Picasso')}, realizzato per il Padiglione spagnolo all'Esposizione di Parigi, raffigura il bombardamento nazista della cittadina basca di Guernica durante la guerra civile spagnola. Un monumento dell'arte contro la guerra."
    },
    {
        "p": 122, "after": "Schindler",
        "note": f"Il {_w('film del 1993', 'Schindler%27s_List', 'en')} di {_w('Steven Spielberg', 'Steven_Spielberg')} su {_w('Oskar Schindler', 'Oskar_Schindler')}, l'industriale tedesco che salvò più di mille lavoratori ebrei polacchi dallo sterminio durante la Shoah."
    },
    {
        "p": 123, "after": "Comitato Internazionale della Croce Rossa",
        "note": f"{_w('Fondato a Ginevra nel 1863', 'Comitato_Internazionale_della_Croce_Rossa')} da {_w('Henry Dunant', 'Henry_Dunant')} dopo aver assistito alla carneficina della {_w('battaglia di Solferino', 'Battle_of_Solferino', 'en')}. La sua neutralità operativa — curare i feriti di ogni parte — divenne il seme del diritto internazionale umanitario."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('Pastore battista statunitense', 'Martin_Luther_King')} (1929-1968) e leader centrale del movimento per i diritti civili negli USA, le cui campagne nonviolente contribuirono a porre fine alla segregazione razziale legale."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('Leader sudafricano contro l\'apartheid', 'Nelson_Mandela')} (1918-2013), imprigionato per 27 anni, poi presidente di un Sudafrica post-apartheid. Il suo rifiuto della violenza vendicativa plasmò il processo di {_w('Verità e Riconciliazione', 'Truth_and_Reconciliation_Commission_(South_Africa)', 'en')} del Paese."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('Giornalista e attivista statunitense', 'Dorothy_Day')} (1897-1980), cofondatrice del {_w('Catholic Worker Movement', 'Catholic_Worker_Movement', 'en')}. Unì fede cattolica, povertà volontaria, anarchismo e pacifismo; visse tra i poveri nelle case di ospitalità di Manhattan. Causa di canonizzazione aperta nel 2000."
    },
    {
        "p": 125, "after": "Massimiliano Maria Kolbe",
        "note": f"{_w('Frate francescano conventuale polacco', 'Massimiliano_Kolbe')} (1894-1941). Ad Auschwitz si offrì di prendere il posto di un compagno di prigionia condannato al bunker della fame; morì dopo due settimane. Canonizzato nel 1982 come «martire della carità»."
    },
    {
        "p": 125, "after": "Oscar Romero",
        "note": f"{_w('Arcivescovo di San Salvador', 'Óscar_Romero')} (1917-1980), ucciso all'altare mentre celebrava la Messa per aver ripetutamente denunciato gli squadroni della morte e la repressione militare nella guerra civile salvadoregna. Canonizzato nel 2018."
    },
    {
        "p": 127, "after": "Tommaso",
        "note": f"{_w('Teologo e filosofo domenicano del XIII secolo', 'Tommaso_d\'Aquino')} (1225-1274). La sua <i>{_w('Summa Theologiae', 'Summa_theologiae')}</i> è la più influente sintesi della teologia cristiana nell'Occidente latino; insegnò che la grazia perfeziona la natura anziché distruggerla."
    },
    {
        "p": 128, "after": "prometeici",
        "note": f"Dal mito greco: {_w('Prometeo', 'Prometeo')} rubò il fuoco agli dèi per donarlo all'umanità e fu punito in eterno. Nel pensiero moderno la figura divenne il patrono dell'autoaffermazione tecnologica dell'uomo — {_w('Mary Shelley', 'Mary_Shelley')} sottotitolò <i>{_w('Frankenstein', 'Frankenstein', 'en')}</i> «Il Prometeo moderno»; Marx lodò lo «scatenamento prometeico» delle forze umane; {_w('Hans Jonas', 'Hans_Jonas')}, in <i>Il principio responsabilità</i> (1979), ammonì che la tecnica moderna ha finalmente dato all'ambizione prometeica una portata divina senza una sapienza divina."
    },
    {
        "p": 130, "after": "Agostino",
        "note": f"Nella <i>{_w('Città di Dio', 'La_città_di_Dio')}</i> (inizio V secolo), Agostino legge tutta la storia come l'intreccio di due città — terrena e celeste — costruite da due amori opposti. L'immagine dà il titolo a questo capitolo e unifica il contrasto dell'enciclica tra Babele e Gerusalemme."
    },

    # ---------- CAPITOLO QUARTO ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Teorica politica tedesco-americana', 'Hannah_Arendt')} (1906-1975). Le sue <i>{_w('Origini del totalitarismo', 'Le_origini_del_totalitarismo')}</i> (1951) ed <i>{_w('Eichmann a Gerusalemme', 'La_banalità_del_male')}</i> (1963) mostrarono come i regimi totalitari dipendano dal dissolvere la distinzione stessa tra fatto e finzione."
    },
    {
        "p": 140, "after": "Platone",
        "note": f"{_w('Filosofo greco antico', 'Platone')} (c. 428-348 a.C.). L'immagine della comprensione che si accende come una scintilla attraverso una lunga indagine condivisa è tratta dalla sua {_w('Settima Lettera', 'Seventh_Letter', 'en')} — una difesa dell'apprendimento lento e dialogico contro l'illusione del sapere veloce."
    },
    {
        "p": 148, "after": "Benedetto da Norcia",
        "note": f"{_w('Fondatore del monachesimo occidentale del VI secolo', 'Benedetto_da_Norcia')} (c. 480-547). La sua <i>{_w('Regola', 'Regola_di_san_Benedetto')}</i> intrecciò preghiera e lavoro manuale — <i>ora et labora</i> — e costruì la spiritualità del lavoro che avrebbe plasmato la cultura europea per un millennio."
    },
    {
        "p": 151, "after": "quarta rivoluzione industriale",
        "note": f"{_w('Termine reso popolare da Klaus Schwab', 'Quarta_rivoluzione_industriale')} (fondatore del {_w('Forum economico mondiale', 'Forum_economico_mondiale')}) per la presente fusione di IA, robotica, biotecnologia e mondo fisico — successore delle rivoluzioni a vapore, elettrica e digitale che l'hanno preceduta."
    },
    {
        "p": 163, "after": "mano invisibile",
        "note": f"La {_w('metafora', 'Mano_invisibile')} di {_w('Adam Smith', 'Adam_Smith')} (<i>La ricchezza delle nazioni</i>, 1776): il perseguimento dell'interesse personale in un mercato concorrenziale può, involontariamente, produrre beneficio sociale. Leone si unisce a una lunga schiera di pontefici nel sostenere che questo meccanismo, da solo, non può governare un'economia."
    },

    # ---------- CAPITOLO QUINTO ----------
    {
        "p": 192, "after": "guerra giusta",
        "note": f"La {_w('tradizione cristiana', 'Guerra_giusta')} (Agostino, Tommaso, Vitoria, Suárez) delle condizioni morali in cui la guerra può essere ammissibile — giusta causa, legittima autorità, proporzionalità, ultima istanza. Francesco e ora Leone sostengono che, sotto le armi moderne, tali criteri non possono più essere soddisfatti."
    },
    {
        "p": 193, "after": "industria bellica",
        "note": f"Richiama il «complesso militare-industriale», {_w('espressione coniata dal presidente USA Dwight D. Eisenhower', 'Complesso_militare-industriale')} nel discorso d'addio del 1961, che ammoniva come gli interessi intrecciati di fabbricanti d'armi, apparati militari e politici creino una spinta strutturale verso uno stato di guerra perpetua — esattamente la preoccupazione di Leone qui, sessantacinque anni dopo."
    },
    {
        "p": 194, "after": "Trattato per la proibizione delle armi nucleari",
        "note": f"Un {_w('trattato ONU del 2017', 'Trattato_sulla_proibizione_delle_armi_nucleari')} entrato in vigore nel gennaio 2021. Vieta categoricamente di sviluppare, testare, produrre o possedere armi nucleari. La Santa Sede fu tra i primi firmatari; i nove Stati dotati di armi nucleari hanno tutti rifiutato di aderirvi."
    },
    {
        "p": 198, "after": "agenti morali artificiali",
        "note": f"Un termine della {_w('letteratura sull\'etica delle macchine', 'Machine_ethics', 'en')} (Wendell Wallach e Colin Allen, <i>Moral Machines</i>, 2008) — la proposta che sistemi di IA sufficientemente avanzati possano essere programmati per formulare giudizi etici da sé. L'enciclica risponde con la visione classica: il giudizio morale non è un calcolo ma la risposta di una coscienza a una persona, irriducibile a qualsiasi macchina che segua regole."
    },
    {
        "p": 201, "after": "1989",
        "note": f"L'anno della caduta del {_w('Muro di Berlino', 'Muro_di_Berlino')} e del crollo dei regimi comunisti nell'Europa centro-orientale — che segna la fine della {_w('Guerra fredda', 'Guerra_fredda')} e l'inizio dell'era della «globalizzazione» che Leone critica qui."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Termine tedesco dell\'Ottocento', 'Realpolitik')} per una politica condotta sulla base di interessi pratici e materiali anziché di ideologia o principio morale. Leone la considera una contraffazione del genuino realismo politico."
    },
    {
        "p": 213, "after": "Tolkien",
        "note": f"{_w('Autore inglese', 'J._R._R._Tolkien')} (1892-1973), cattolico devoto, creatore de <i>{_w('Il Signore degli Anelli', 'Il_Signore_degli_Anelli')}</i>. La citazione è di Gandalf, da <i>{_w('Il ritorno del re', 'Il_ritorno_del_re')}</i>: una vocazione definita dal coltivare il pezzo di terra che ci è stato affidato."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Statista cattolico italiano', 'Giorgio_La_Pira')} (1904-1977), più volte sindaco di Firenze e instancabile organizzatore di conferenze di pace dell'era della Guerra fredda, attraverso linee religiose e ideologiche. Beatificato nel 2018."
    },
    {
        "p": 222, "after": "manichee",
        "note": f"Da {_w('Mani', 'Mani_(profeta)')} (216-276 d.C.), fondatore di una {_w('religione dualista persiana', 'Manicheismo')} che leggeva la storia come una battaglia cosmica tra forze uguali e opposte di luce e tenebra. {_w('Agostino', 'Agostino_d\'Ippona')} fu manicheo per nove anni prima di convertirsi; la sua successiva teologia del male come <i>privazione</i> (un'assenza anziché una sostanza) fu costruita contro questo dualismo. La parola oggi indica ogni visione del mondo che divida nettamente la realtà in campi del bene e del male."
    },
    {
        "p": 223, "after": "spirito di Assisi",
        "note": f"Il 27 ottobre 1986 Giovanni Paolo II riunì ad Assisi i leader delle religioni del mondo {_w('per pregare per la pace', 'Day_of_Prayer_for_World_Peace', 'en')} — un precedente di costruzione interreligiosa della pace che Francesco rinnovò più volte durante il suo pontificato."
    },
    {
        "p": 223, "after": "Grande Imam di al-Azhar",
        "note": f"{_w('Ahmad al-Tayyib', 'Ahmad_al-Tayyib')}, capo dell'{_w('università-moschea di al-Azhar', 'Al-Azhar_University', 'en')} del Cairo (la principale autorità dell'islam sunnita). Lui e Papa Francesco firmarono il {_w('Documento sulla fratellanza umana del 2019', 'Document_on_Human_Fraternity', 'en')} ad Abu Dhabi."
    },

    # ---------- CONCLUSIONE ----------
    {
        "p": 230, "after": "Magnificat",
        "note": f"Il {_w('cantico di lode', 'Magnificat')} di {_w('Maria', 'Maria_(madre_di_Gesù)')} in Luca 1,46-55, pregato ogni giorno nei Vespri della Chiesa: «L'anima mia magnifica il Signore… ha rovesciato i potenti dai troni, ha innalzato gli umili». Il titolo dell'enciclica <i>Magnifica Humanitas</i> trae spunto da questo canto."
    },
    {
        "p": 233, "after": "ricapitolazione",
        "note": f"Dal greco <i>anakephalaíōsis</i>, «ricapitolare sotto un capo» (Ef 1,10). Il Padre antico {_w('Ireneo', 'Ireneo_di_Lione')} ne fece l'immagine centrale della salvezza: Cristo raccoglie in sé tutta la creazione, ogni frammento e ogni ferita."
    },
    {
        "p": 234, "after": "Agostino",
        "note": f"Il passo citato è dal {_w('Discorso 272 di Agostino', 'Sermon_272', 'en')}, predicato ai cristiani appena battezzati sull'Eucaristia: «Siate ciò che vedete e ricevete ciò che siete». Una netta affermazione della teologia patristica per cui la Chiesa <i>è</i> il corpo di Cristo — non semplicemente una società che vi si raduna attorno."
    },
    {
        "p": 237, "after": "antropocentrismo situato",
        "note": f"Espressione di Francesco nella <i>{_w('Laudato si\'', 'Laudato_si\'')}</i> (§118): una deliberata correzione dell'antropocentrismo illuminista. Gli esseri umani restano moralmente centrali, ma come creature inserite in e dipendenti da una più ampia rete di vita — non come soggetti distaccati posti sopra una natura inerte. L'invocazione di Leone qui chiude un cerchio aperto nella discussione sul transumanesimo del Capitolo Terzo: l'alternativa a «lasciarsi alle spalle l'umano» non è intronizzare l'umano, ma ricollocarci nella nostra compagnia creaturale."
    },
]
