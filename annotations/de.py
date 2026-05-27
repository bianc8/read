"""Deutsche redaktionelle Annotationen für Magnifica Humanitas.

Übersetzung der Annotationen aus ``annotations.py``. Jeder Eintrag verankert eine
Randnotiz an einer Stelle des Absatzes, indem ein exaktes Textfragment (``after``)
der offiziellen deutschen Übersetzung abgeglichen wird. Die Links verweisen auf
die deutschsprachige Wikipedia, wenn der Titel bekannt ist, andernfalls auf die
englische (``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "de") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- EINLEITUNG ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"Die Enzyklika von 1891 von {_w('Leo XIII.', 'Leo_XIII.')}, das Gründungsdokument der modernen {_w('katholischen Soziallehre', 'Katholische_Soziallehre')}, geschrieben als Antwort auf die Umwälzungen des industriellen Kapitalismus. Der lateinische Titel bedeutet <i>{_w('von den neuen Dingen', 'Rerum_Novarum')}</i>. Leo XIV. greift bewusst den Namen und das Anliegen seines Vorgängers auf."
    },
    {
        "p": 3, "after": "Soziallehre der Kirche",
        "note": f"Ein zusammenhängender Bestand päpstlicher und konziliarer Lehre über das soziale, wirtschaftliche und politische Leben, entwickelt seit Leo XIII. Ihre Grundprinzipien — Würde, Gemeinwohl, Subsidiarität, Solidarität, Gerechtigkeit — durchziehen diesen Brief. Siehe: {_w('katholische Soziallehre', 'Katholische_Soziallehre')}."
    },
    {
        "p": 4, "after": "„Neuerungen“",
        "note": f"<i>Res novae</i> im Lateinischen — der Ausdruck, von dem <i>{_w('Rerum novarum', 'Rerum_Novarum')}</i> seinen Namen hat. Leo XIV. verwendet ihn durchgängig, um die wahrhaft neuen Belastungen zu bezeichnen, mit denen jede Generation konfrontiert ist."
    },
    {
        "p": 7, "after": "Turmbau zu Babel",
        "note": f"{_w('Genesis 11,1-9', 'Turmbau_zu_Babel')}. Menschen, die eine einzige Sprache sprechen, machen sich daran, einen Turm zu bauen „mit einer Spitze bis in den Himmel“, um sich einen Namen zu machen; Gott zerstreut sie, indem er ihre Sprache verwirrt. Ein bleibendes christliches Gleichnis für Hochmut und für die Zersplitterung, die folgt, wenn das menschliche Streben Gott vergisst."
    },
    {
        "p": 7, "after": "Wiederaufbau der Mauern Jerusalems",
        "note": f"Das {_w('Buch Nehemia', 'Buch_Nehemia')} (5. Jh. v. Chr.) erzählt von jüdischen Exilanten, die aus {_w('Babylon', 'Babylonisches_Exil')} zurückkehren, um ein zerstörtes Jerusalem wiederaufzubauen. Nehemia organisiert die Arbeit Familie für Familie, hört auf Beschwerden und stellt sich dem Widerstand. Leo hält ihn als Modell verteilter, koordinierter Wiederherstellung hoch — das Gegenteil der Vereinheitlichung von oben in Babel."
    },
    {
        "p": 10, "after": "Synodalität",
        "note": f"Vom griechischen <i>syn-hodos</i>, „gemeinsam unterwegs sein“. Eine von {_w('Papst Franziskus', 'Franziskus_(Papst)')} ins Zentrum gerückte Praxis: kirchliche Entscheidungen, die durch breites Zuhören und gemeinsame Unterscheidung statt durch Dekret von oben getroffen werden. Siehe: {_w('Synodalität', 'Synodalität')}."
    },
    {
        "p": 11, "after": "Augustinus",
        "note": f"{_w('Augustinus von Hippo', 'Augustinus_von_Hippo')} (354-430), nordafrikanischer Bischof und Philosoph, einer der einflussreichsten Denker des westlichen Christentums. Das „unruhige Herz“ ist der Anfang seiner <i>{_w('Bekenntnisse', 'Confessiones')}</i>, seines autobiographischen Gebets."
    },
    {
        "p": 13, "after": "Subsidiarität",
        "note": f"Katholisches Sozialprinzip: Entscheidungen gehören auf die kleinste, lokalste Ebene, die fähig ist, sie zu treffen; höhere Instanzen existieren, um die unteren zu <i>unterstützen</i> (subsidium), nicht um sie zu ersetzen. Erstmals systematisiert von {_w('Pius XI.', 'Pius_XI.')} im Jahr 1931. Siehe: {_w('Subsidiarität', 'Subsidiarität')}."
    },
    {
        "p": 15, "after": "Ordentlichen Heiligen Jahr 2025",
        "note": f"In der katholischen Tradition ist ein {_w('Heiliges Jahr', 'Heiliges_Jahr')} ein Jahr der Wallfahrt, der Barmherzigkeit und der Vergebung, das alle 25 Jahre begangen wird. Das Heilige Jahr 2025 wurde von {_w('Papst Franziskus', 'Franziskus_(Papst)')} unter dem Motto „Pilger der Hoffnung“ eröffnet."
    },

    # ---------- ERSTES KAPITEL ----------
    {
        "p": 17, "after": "Lehramt",
        "note": f"Die offizielle {_w('Lehrautorität', 'Lehramt')} der katholischen Kirche, ausgeübt vom Papst und den Bischöfen in Gemeinschaft mit ihm. Das Wort kommt vom lateinischen <i>magister</i>, „Lehrer“."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"„Freude und Hoffnung“ — die Pastoralkonstitution von 1965 des {_w('Zweiten Vatikanischen Konzils', 'Zweites_Vatikanisches_Konzil')} über die Kirche in der Welt von heute. Ihre Eröffnungsworte („Freude und Hoffnung, Trauer und Angst der Menschen von heute … sind auch Freude und Hoffnung … der Jünger Christi“) haben das Verhältnis der Kirche zum weltlichen Leben neu bestimmt. Siehe: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Kompendium der Soziallehre der Kirche",
        "note": f"Ein {_w('vatikanisches Referenzwerk von 2004', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')}, das die Soziallehre der Kirche von Leo XIII. bis Johannes Paul II. sammelt und systematisiert. Oft die erste Anlaufstelle, um nachzuzeichnen, wo ein Prinzip formuliert wurde."
    },
    {
        "p": 28, "after": "Laudato si’",
        "note": f"{_w('Die Enzyklika von Papst Franziskus aus dem Jahr 2015', 'Laudato_si’')} über die Sorge für das „gemeinsame Haus“ — die Umweltkrise, gelesen als untrennbar von Armut und Ungleichheit. Der Titel stammt aus dem Sonnengesang des {_w('hl. Franz von Assisi', 'Franz_von_Assisi')} („Sei gepriesen, mein Herr“)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('Die Enzyklika von Papst Franziskus aus dem Jahr 2020', 'Fratelli_tutti')} über Geschwisterlichkeit und soziale Freundschaft. Der Titel stammt vom {_w('hl. Franz von Assisi', 'Franz_von_Assisi')}: „Alle Brüder“."
    },
    {
        "p": 30, "after": "Magna Charta",
        "note": f"Wörtl. „Große Urkunde“ — das {_w('englische Dokument von 1215', 'Magna_Carta')}, grundlegend für das Verfassungswesen. Pius XI. verwendet sie metaphorisch, um die <i>Rerum novarum</i> die Gründungscharta des katholischen Sozialhandelns zu nennen."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"„Im vierzigsten Jahr“ — {_w('die Enzyklika von Pius XI. aus dem Jahr 1931', 'Quadragesimo_anno')}, geschrieben zum 40. Jahrestag der <i>Rerum novarum</i> inmitten der {_w('Weltwirtschaftskrise', 'Weltwirtschaftskrise')}. Führte das Subsidiaritätsprinzip in seiner modernen Form ein."
    },
    {
        "p": 32, "after": "Naturrecht",
        "note": f"Eine {_w('philosophische Tradition', 'Naturrecht')}, die vom {_w('stoischen Rom', 'Stoa')} bis zu {_w('Thomas von Aquin', 'Thomas_von_Aquin')} reicht: Es existiert eine objektive sittliche Ordnung, der menschlichen Vernunft zugänglich, die jeder menschlichen Autorität vorausgeht und von ihr unabhängig ist. Die katholische Soziallehre gründet hierauf die universalen Menschenrechte; das internationale Rechtssystem der Nachkriegszeit schöpfte aus derselben Strömung. Die Alternative — dass Rechte einfach das sind, was die Mächtigen zu gewähren bereit sind — ist genau das, was das naturrechtliche Denken zurückzuweisen bestimmt ist."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"„Mutter und Lehrerin“ — {_w('die Enzyklika von 1961', 'Mater_et_magistra')} von {_w('Johannes XXIII.', 'Johannes_XXIII.')}, welche die katholische Soziallehre für die Nachkriegswelt aktualisiert."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"„Frieden auf Erden“ — {_w('die Enzyklika von 1963 von Johannes XXIII.', 'Pacem_in_terris')}, geschrieben wenige Monate nach der {_w('Kubakrise', 'Kubakrise')}. Die erste Enzyklika, die an „alle Menschen guten Willens“ gerichtet war, nicht nur an die Katholiken."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"„Über die Menschenwürde“ — die {_w('Erklärung über die Religionsfreiheit von 1965', 'Dignitatis_humanae')} des Zweiten Vatikanischen Konzils, die die Kirche förmlich darauf verpflichtete, das bürgerliche Recht jedes Menschen auf Religionsfreiheit zu verteidigen."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"„Die Entwicklung der Völker“ — {_w('die Enzyklika von 1967', 'Populorum_progressio')} von {_w('Paul VI.', 'Paul_VI.')}, die die Entwicklung selbst als „den neuen Namen für den Frieden“ bestimmte und die katholische Soziallehre auf die globale Ungleichheit ausrichtete."
    },
    {
        "p": 35, "after": "Päpstlichen Kommission Iustitia et Pax",
        "note": f"„Gerechtigkeit und Frieden“ — das von Paul VI. 1967 errichtete vatikanische Amt, um die katholische Soziallehre in internationale politische Arbeit zu übersetzen. 2017 reorganisiert als das {_w('Dikasterium für den Dienst zugunsten der ganzheitlichen Entwicklung des Menschen', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"„Das herannahende Achtzigste“ — das {_w('Apostolische Schreiben von 1971', 'Octogesima_adveniens')} von Paul VI. zum 80. Jahrestag der <i>Rerum novarum</i>, über die Verstädterung und die Grenzen einer einzigen katholischen Antwort auf politische Fragen."
    },
    {
        "p": 36, "after": "Strukturen der Sünde",
        "note": f"Begriff von {_w('Johannes Paul II.', 'Johannes_Paul_II.')} (in <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) für soziale, wirtschaftliche und politische Verhältnisse, die Ungerechtigkeit institutionalisieren. Der Ausdruck verlagert die Sünde von rein individuellen Akten auf die Systeme, an denen wir teilhaben."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"„Die menschliche Arbeit verrichtend“ — {_w('die Enzyklika von 1981 von Johannes Paul II.', 'Laborem_exercens')} über die menschliche Arbeit. Sie vertrat, dass Arbeit nicht nur eine Ware ist, sondern eine grundlegende Dimension des menschlichen Lebens und der Schlüssel zur gesamten sozialen Frage."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"„Die Sorge um die soziale Wirklichkeit“ — {_w('die Enzyklika von 1987 von Johannes Paul II.', 'Sollicitudo_rei_socialis')}, die zwanzig Jahre später die <i>Populorum progressio</i> Pauls VI. wieder aufgreift, mit dem Fokus auf der wachsenden Kluft zwischen reichen und armen Nationen."
    },
    {
        "p": 38, "after": "„Zivilisation der Liebe“",
        "note": f"Ausdruck, geprägt von {_w('Paul VI.', 'Paul_VI.')} im Jahr 1975: eine Vision der gesellschaftlichen Ordnung, in der die Liebe, nicht die Macht, das Organisationsprinzip von Wirtschaft, Politik und Kultur ist. Wird zum verbindenden Thema des Fünften Kapitels."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"„Das hundertste Jahr“ — {_w('die Enzyklika von 1991 von Johannes Paul II.', 'Centesimus_annus')} zum hundertjährigen Jubiläum der <i>Rerum novarum</i>, geschrieben nach dem Fall des Kommunismus. Sie bejaht die Marktwirtschaft nur insofern, als sie dem Sittengesetz und der Solidarität untergeordnet bleibt."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"„Liebe in der Wahrheit“ — {_w('die Enzyklika von 2009', 'Caritas_in_veritate')} von {_w('Benedikt XVI.', 'Benedikt_XVI.')} über die ganzheitliche menschliche Entwicklung, geschrieben während der globalen Finanzkrise."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"„Die Freude des Evangeliums“ — {_w('das Apostolische Schreiben von 2013 von Papst Franziskus', 'Evangelii_gaudium')}, das programmatische Dokument seines Pontifikats."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"„Er hat uns geliebt“ — {_w('die Enzyklika von 2024 von Papst Franziskus', 'Dilexit_nos')} über die Verehrung des {_w('Heiligsten Herzens Jesu', 'Herz_Jesu')}, sein letzter großer Lehrbrief."
    },

    # ---------- ZWEITES KAPITEL ----------
    {
        "p": 50, "after": "dreifaltigen Gottes",
        "note": f"Die zentrale christliche Lehre der {_w('Dreifaltigkeit', 'Dreifaltigkeit')}: ein Gott in drei Personen — Vater, Sohn und Heiliger Geist — ewig vereint in der Liebe. Diese Lehre ist es, die das katholische Sozialdenken in seiner Wurzel beziehungshaft macht."
    },
    {
        "p": 52, "after": "ontologische Würde",
        "note": f"Vom griechischen <i>on</i>, „Sein“ — die Würde, die einer Person kraft des <i>Seins</i> zukommt, nicht kraft des Tuns, des Habens oder des Anerkanntwerdens. Die Unterscheidung ist {_w('aristotelisch-thomistisch', 'Thomismus')}: Der Wert eines Menschen entspringt dem, was er fundamental ist (<i>esse</i>), nicht veränderlichen Eigenschaften wie Fähigkeit, Leistung oder gesellschaftlicher Stellung."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"„Unendliche Würde“ — eine {_w('Erklärung von 2024', 'Dignitas_infinita')} des vatikanischen Dikasteriums für die Glaubenslehre, die die bedingungslose Würde jeder menschlichen Person gegen eine lange Liste zeitgenössischer Verletzungen bekräftigt."
    },
    {
        "p": 54, "after": "Allgemeine Erklärung der Menschenrechte",
        "note": f"{_w('Von der UN-Generalversammlung angenommen', 'Allgemeine_Erklärung_der_Menschenrechte')} am 10. Dezember 1948 in der Folge des Zweiten Weltkriegs. Die erste globale Formulierung von Rechten, die jedem Menschen zukommen, „einfach weil er Mensch ist“."
    },
    {
        "p": 60, "after": "Gemeinwohl",
        "note": f"Ein {_w('Begriff', 'Gemeinwohl')} mit tiefen philosophischen Wurzeln bei {_w('Aristoteles', 'Aristoteles')} (<i>Politik</i>, Buch III) und {_w('Thomas von Aquin', 'Thomas_von_Aquin')}. Entscheidend: Es ist <i>nicht</i> die Summe individueller Präferenzen (die utilitaristische Verkürzung) noch bloß „öffentliche“ Güter wie saubere Luft; es ist die gemeinsame Gesamtheit von Bedingungen, unter denen jeder Mensch aufblühen kann. Dieser Begriff unterscheidet das katholische Sozialdenken sowohl vom reinen Individualismus als auch vom reinen Kollektivismus."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Lateinisch für „öffentliche Sache“ — das {_w('Gemeinwesen', 'Res_publica')}, das gemeinsame Anliegen aller Bürger. Wurzel des Wortes <i>Republik</i>."
    },
    {
        "p": 82, "after": "ganzheitlicher menschlicher Entwicklung",
        "note": f"{_w('Prägung Pauls VI.', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967): Entwicklung <i>jedes</i> Menschen und des <i>ganzen</i> Menschen — materiell, kulturell, moralisch, geistlich. Der Maßstab, an dem die katholische Lehre jedes Wirtschaftsmodell misst."
    },
    {
        "p": 86, "after": "Gewissenserforschung",
        "note": f"Eine traditionelle katholische geistliche Praxis — {_w('eine methodische Selbstprüfung vor Gott', 'Gewissenserforschung')} — besonders aus dem {_w('ignatianischen', 'Ignatianische_Spiritualität')} <i>Examen</i> hervorgegangen. Hier wandelt Leo sie von einer persönlichen in eine gemeinschaftliche Disziplin für die Kirche selbst."
    },

    # ---------- DRITTES KAPITEL ----------
    {
        "p": 92, "after": "technokratischen Paradigmas",
        "note": f"Begriff von Papst Franziskus in <i>Laudato si’</i> (2015), übernommen von {_w('Romano Guardini', 'Romano_Guardini')} und im Einklang mit der Kritik der modernen Technik von {_w('Heidegger', 'Martin_Heidegger')}. Nicht Begeisterung für Apparate, sondern die tiefere Geisteshaltung, die <i>alles</i> — Natur, Personen, Institutionen — als Rohmaterial behandelt, das es zu messen, zu optimieren und zu kontrollieren gilt. Das Paradigma reduziert das Sein auf Funktion und den Wert auf Nutzen."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Italienisch-deutscher katholischer Priester und Philosoph', 'Romano_Guardini')} (1885-1968). Sein Werk <i>Das Ende der Neuzeit</i> warnte, dass die technische Macht die moralische und geistliche Bildung überholt habe, die zu ihrer Ausübung nötig ist. Eine prägende Einflussgröße für das Zweite Vatikanische Konzil und für <i>Laudato si’</i> von Franziskus."
    },
    {
        "p": 107, "after": "„Ausrichtung“",
        "note": f"Ein zentraler Begriff der zeitgenössischen {_w('KI-Sicherheit', 'AI_alignment', 'en')}: das Vorhaben, KI-Systeme auf Ziele auszurichten, die mit menschlichen Werten übereinstimmen. Verbunden mit <i>Human Compatible</i> (2019) von {_w('Stuart Russell', 'Stuart_J._Russell', 'en')}, der Arbeit des {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, von {_w('Anthropic', 'Anthropic')} und dem „{_w('Superalignment', 'OpenAI')}“-Bestreben von OpenAI. Leos Einwand richtet sich nicht gegen die Ausrichtung, sondern gegen die Frage, die die Ausrichtung allein nicht beantworten kann: <i>ausgerichtet an wessen Werten</i> — und von wem entschieden?"
    },
    {
        "p": 115, "after": "Transhumanismus",
        "note": f"Eine {_w('intellektuelle Bewegung des 20.-21. Jahrhunderts', 'Transhumanismus')} ({_w('Max More', 'Max_More', 'en')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}), die dazu auffordert, Biotechnologie, KI und andere Werkzeuge einzusetzen, um die biologischen Grenzen des Menschen zu überwinden — Krankheit, Alterung, kognitive Schranken, sogar die Sterblichkeit. Erbt den Fortschrittsglauben der Aufklärung und die Kybernetik der Nachkriegszeit; hat institutionelle Heimstätten im Silicon Valley und in der Langlebigkeitsindustrie. Behandelt den Körper als aufrüstbare Hardware."
    },
    {
        "p": 115, "after": "Posthumanismus",
        "note": f"Eine andere intellektuelle Linie. Der {_w('„kritische“ Posthumanismus', 'Posthumanismus')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) stammt aus der kontinentalen Philosophie und der feministischen Theorie. Er dezentriert den Menschen — verwirft die Idee eines stabilen, autonomen menschlichen Subjekts — und betont unsere Verflechtung mit anderen Arten, Maschinen und Ökosystemen. Mal Verbündeter und mal Kritiker des Transhumanismus; beide teilen die Bereitschaft, den Menschen zu relativieren, jedoch aus sehr unterschiedlichen Gründen."
    },
    {
        "p": 116, "after": "Anthropozentrismus",
        "note": f"Die {_w('Auffassung', 'Anthropozentrismus')}, dass der Mensch im Zentrum des sittlichen Anliegens steht. Die christliche Tradition war historisch anthropozentrisch; Franziskus präzisierte dies in <i>Laudato si’</i> mit dem Ausdruck „situierter Anthropozentrismus“ — der Mensch als eingebundenes Geschöpf, nicht als losgelöster Herr. Der Posthumanismus lehnt den Anthropozentrismus schärfer ab und betrachtet ihn als eine Illusion der Aufklärung."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Österreichischer Psychiater und Auschwitz-Überlebender', 'Viktor_Frankl')} (1905-1997). Sein Werk <i>{_w('… trotzdem Ja zum Leben sagen', 'Man%27s_Search_for_Meaning', 'en')}</i> vertrat, dass der tiefste menschliche Antrieb die Suche nach Sinn ist — eine Freiheit, die keine noch so unmenschliche Bedingung ganz auslöschen kann."
    },
    {
        "p": 122, "after": "Beethovens Neunte",
        "note": f"{_w('Uraufgeführt 1824', 'Sinfonie_Nr._9_(Beethoven)')}; ihr Chorfinale vertont Schillers „{_w('Ode an die Freude', 'An_die_Freude')}“, eine Hymne an die universale Geschwisterlichkeit. 1985 als Hymne der Europäischen Union angenommen."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"Das {_w('Gemälde von 1937', 'Guernica_(Bild)')} von {_w('Picasso', 'Pablo_Picasso')}, geschaffen für den spanischen Pavillon der Pariser Weltausstellung, das die Bombardierung der baskischen Stadt Gernika durch die Nazis während des Spanischen Bürgerkriegs darstellt. Ein Monument der Antikriegskunst."
    },
    {
        "p": 122, "after": "Schindlers Liste",
        "note": f"Der {_w('Film von 1993', 'Schindlers_Liste')} von {_w('Steven Spielberg', 'Steven_Spielberg')} über {_w('Oskar Schindler', 'Oskar_Schindler')}, den deutschen Industriellen, der während des Holocaust mehr als tausend polnisch-jüdische Arbeiter vor der Vernichtung rettete."
    },
    {
        "p": 123, "after": "Internationalen Komitees vom Roten Kreuz",
        "note": f"{_w('1863 in Genf gegründet', 'Internationales_Komitee_vom_Roten_Kreuz')} von {_w('Henry Dunant', 'Henry_Dunant')}, nachdem er das Gemetzel der {_w('Schlacht von Solferino', 'Schlacht_von_Solferino')} miterlebt hatte. Seine operative Neutralität — die Versorgung der Verwundeten auf allen Seiten — wurde zum Keim des humanitären Völkerrechts."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('US-amerikanischer Baptistenpastor', 'Martin_Luther_King')} (1929-1968) und zentrale Führungsgestalt der US-Bürgerrechtsbewegung, dessen gewaltfreie Kampagnen halfen, die gesetzliche Rassentrennung zu beenden."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('Südafrikanischer Anti-Apartheid-Führer', 'Nelson_Mandela')} (1918-2013), 27 Jahre inhaftiert, dann Präsident eines Südafrikas nach der Apartheid. Seine Ablehnung vergeltender Gewalt prägte den {_w('Wahrheits- und Versöhnungsprozess', 'Wahrheits-_und_Versöhnungskommission_(Südafrika)')} des Landes."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('US-amerikanische Journalistin und Aktivistin', 'Dorothy_Day')} (1897-1980), Mitbegründerin der {_w('Catholic-Worker-Bewegung', 'Catholic_Worker_Movement', 'en')}. Verband katholischen Glauben, freiwillige Armut, Anarchismus und Pazifismus; lebte unter den Armen in Häusern der Gastfreundschaft in Manhattan. Seligsprechungsverfahren 2000 eröffnet."
    },
    {
        "p": 125, "after": "Maximilian Maria Kolbe",
        "note": f"{_w('Polnischer Minoriten-Franziskaner', 'Maximilian_Kolbe')} (1894-1941). In Auschwitz bot er sich an, den Platz eines Mithäftlings einzunehmen, der zum Hungerbunker verurteilt war; er starb nach zwei Wochen. 1982 als „Märtyrer der Liebe“ heiliggesprochen."
    },
    {
        "p": 125, "after": "Oscar Romero",
        "note": f"{_w('Erzbischof von San Salvador', 'Óscar_Romero')} (1917-1980), am Altar erschossen, während er die Messe feierte, weil er wiederholt die Todesschwadronen und die militärische Repression im salvadorianischen Bürgerkrieg angeprangert hatte. 2018 heiliggesprochen."
    },
    {
        "p": 127, "after": "Thomas von Aquin",
        "note": f"{_w('Dominikanischer Theologe und Philosoph des 13. Jahrhunderts', 'Thomas_von_Aquin')} (1225-1274). Seine <i>{_w('Summa Theologiae', 'Summa_theologiae')}</i> ist die einflussreichste Synthese der christlichen Theologie im lateinischen Westen; er lehrte, dass die Gnade die Natur vollendet, statt sie zu zerstören."
    },
    {
        "p": 128, "after": "prometheischen",
        "note": f"Aus dem griechischen Mythos: {_w('Prometheus', 'Prometheus')} stahl den Göttern das Feuer, um es der Menschheit zu schenken, und wurde dafür ewig bestraft. Im modernen Denken wurde die Figur zum Schutzpatron der technologischen Selbstbehauptung des Menschen — {_w('Mary Shelley', 'Mary_Shelley')} gab ihrem <i>{_w('Frankenstein', 'Frankenstein')}</i> den Untertitel „Der moderne Prometheus“; Marx pries die „prometheische Entfesselung“ der menschlichen Kräfte; {_w('Hans Jonas', 'Hans_Jonas')} warnte in <i>Das Prinzip Verantwortung</i> (1979), dass die moderne Technik dem prometheischen Ehrgeiz endlich eine gottgleiche Reichweite ohne gottgleiche Weisheit verliehen hat."
    },
    {
        "p": 130, "after": "Augustinus",
        "note": f"In <i>{_w('Vom Gottesstaat', 'De_civitate_Dei')}</i> (Anfang 5. Jh.) liest Augustinus die ganze Geschichte als das Ineinander zweier Städte — der irdischen und der himmlischen —, die von zwei entgegengesetzten Lieben gebaut werden. Das Bild gibt diesem Kapitel seinen Titel und vereint den Gegensatz der Enzyklika zwischen Babel und Jerusalem."
    },

    # ---------- VIERTES KAPITEL ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Deutsch-amerikanische politische Theoretikerin', 'Hannah_Arendt')} (1906-1975). Ihre Werke <i>{_w('Elemente und Ursprünge totaler Herrschaft', 'Elemente_und_Ursprünge_totaler_Herrschaft')}</i> (1951) und <i>{_w('Eichmann in Jerusalem', 'Eichmann_in_Jerusalem')}</i> (1963) zeigten auf, wie totalitäre Regime darauf angewiesen sind, eben die Unterscheidung zwischen Tatsache und Fiktion aufzulösen."
    },
    {
        "p": 140, "after": "Platon",
        "note": f"{_w('Antiker griechischer Philosoph', 'Platon')} (ca. 428-348 v. Chr.). Das Bild des Verstehens, das wie ein Funke durch lange gemeinsame Forschung entzündet wird, stammt aus seinem {_w('Siebten Brief', 'Siebter_Brief')} — einer Verteidigung des langsamen, dialogischen Lernens gegen die Illusion schnellen Wissens."
    },
    {
        "p": 148, "after": "Benedikt von Nursia",
        "note": f"{_w('Begründer des abendländischen Mönchtums im 6. Jahrhundert', 'Benedikt_von_Nursia')} (ca. 480-547). Seine <i>{_w('Regel', 'Regula_Benedicti')}</i> verflocht Gebet und Handarbeit — <i>ora et labora</i> — und baute die Spiritualität der Arbeit auf, die die europäische Kultur ein Jahrtausend lang prägen sollte."
    },
    {
        "p": 151, "after": "„vierten industriellen Revolution“",
        "note": f"{_w('Ein von Klaus Schwab populär gemachter Begriff', 'Vierte_industrielle_Revolution')} (Gründer des {_w('Weltwirtschaftsforums', 'Weltwirtschaftsforum')}) für die gegenwärtige Verschmelzung von KI, Robotik, Biotechnologie und der physischen Welt — Nachfolgerin der dampfbetriebenen, der elektrischen und der digitalen Revolution davor."
    },
    {
        "p": 163, "after": "„unsichtbare Hand“",
        "note": f"Die {_w('Metapher', 'Unsichtbare_Hand')} von {_w('Adam Smith', 'Adam_Smith')} (<i>Der Wohlstand der Nationen</i>, 1776): Das Verfolgen des Eigeninteresses in einem Wettbewerbsmarkt kann unbeabsichtigt gesellschaftlichen Nutzen hervorbringen. Leo reiht sich in eine lange Reihe von Päpsten ein, die vertreten, dass dieser Mechanismus allein keine Wirtschaft regieren kann."
    },

    # ---------- FÜNFTES KAPITEL ----------
    {
        "p": 192, "after": "„gerechten Krieges“",
        "note": f"Die {_w('christliche Tradition', 'Lehre_vom_gerechten_Krieg')} (Augustinus, Thomas, Vitoria, Suárez) der sittlichen Bedingungen, unter denen Krieg zulässig sein kann — gerechter Grund, legitime Autorität, Verhältnismäßigkeit, letztes Mittel. Franziskus und nun Leo vertreten, dass diese Kriterien unter modernen Waffen nicht mehr erfüllt werden können."
    },
    {
        "p": 193, "after": "Rüstungsindustrie",
        "note": f"Verweist auf den „militärisch-industriellen Komplex“, {_w('einen von US-Präsident Dwight D. Eisenhower geprägten Ausdruck', 'Militärisch-industrieller_Komplex')} in seiner Abschiedsrede von 1961, der davor warnte, dass die ineinander verflochtenen Interessen von Waffenherstellern, militärischen und politischen Apparaten einen strukturellen Drang zur dauerhaften Kriegsbereitschaft erzeugen — genau Leos Sorge hier, fünfundsechzig Jahre später."
    },
    {
        "p": 194, "after": "Atomwaffenverbotsvertrags",
        "note": f"Ein {_w('UN-Vertrag von 2017', 'Atomwaffenverbotsvertrag')}, der im Januar 2021 in Kraft trat. Er verbietet kategorisch das Entwickeln, Testen, Herstellen oder Besitzen von Atomwaffen. Der Heilige Stuhl war unter den ersten Unterzeichnern; die neun Atomwaffenstaaten haben alle einen Beitritt abgelehnt."
    },
    {
        "p": 198, "after": "„künstlichen moralischen Agenten“",
        "note": f"Ein Begriff aus der {_w('Literatur zur Maschinenethik', 'Maschinenethik')} (Wendell Wallach und Colin Allen, <i>Moral Machines</i>, 2008) — der Vorschlag, dass hinreichend fortgeschrittene KI-Systeme so programmiert werden könnten, dass sie selbst ethische Urteile fällen. Die Enzyklika antwortet mit der klassischen Sicht: Das moralische Urteil ist keine Berechnung, sondern die Antwort eines Gewissens auf eine Person, unzurückführbar auf irgendeine regelfolgende Maschine."
    },
    {
        "p": 201, "after": "1989",
        "note": f"Das Jahr des Falls der {_w('Berliner Mauer', 'Berliner_Mauer')} und des Zusammenbruchs der kommunistischen Regime in Mittel- und Osteuropa — das das Ende des {_w('Kalten Krieges', 'Kalter_Krieg')} und den Beginn der „Globalisierungs“-Ära markiert, die Leo hier kritisiert."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Deutscher Begriff des 19. Jahrhunderts', 'Realpolitik')} für eine Politik, die auf der Grundlage praktischer und materieller Interessen statt von Ideologie oder sittlichem Prinzip geführt wird. Leo behandelt sie als eine Fälschung des echten politischen Realismus."
    },
    {
        "p": 213, "after": "John Ronald Reuel Tolkien",
        "note": f"{_w('Englischer Autor', 'J._R._R._Tolkien')} (1892-1973), gläubiger Katholik, Schöpfer von <i>{_w('Der Herr der Ringe', 'Der_Herr_der_Ringe')}</i>. Das Zitat stammt von Gandalf, aus <i>{_w('Die Rückkehr des Königs', 'Die_Rückkehr_des_Königs')}</i>: eine Berufung, die im Hegen des Stück Erde besteht, das einem anvertraut wurde."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Italienischer katholischer Staatsmann', 'Giorgio_La_Pira')} (1904-1977), mehrfacher Bürgermeister von Florenz und unermüdlicher Veranstalter von Friedenskonferenzen der Kalten-Kriegs-Ära über religiöse und ideologische Grenzen hinweg. 2018 seliggesprochen."
    },
    {
        "p": 222, "after": "manichäischen",
        "note": f"Von {_w('Mani', 'Mani_(Religionsstifter)')} (216-276 n. Chr.), Begründer einer {_w('persischen dualistischen Religion', 'Manichäismus')}, die die Geschichte als kosmischen Kampf zwischen gleichen und entgegengesetzten Mächten von Licht und Finsternis las. {_w('Augustinus', 'Augustinus_von_Hippo')} war neun Jahre lang Manichäer, bevor er sich bekehrte; seine spätere Theologie des Bösen als <i>Mangel</i> (eine Abwesenheit statt einer Substanz) wurde gegen diesen Dualismus errichtet. Das Wort bezeichnet heute jede Weltsicht, die die Welt sauber in Lager des Guten und des Bösen aufteilt."
    },
    {
        "p": 223, "after": "„Geist von Assisi“",
        "note": f"Am 27. Oktober 1986 versammelte Johannes Paul II. die Führer der Weltreligionen in Assisi, {_w('um für den Frieden zu beten', 'Weltgebetstag_für_den_Frieden')} — ein Präzedenzfall für interreligiöse Friedensarbeit, den Franziskus während seines Pontifikats mehrfach erneuerte."
    },
    {
        "p": 223, "after": "Scheich al-Azhar",
        "note": f"{_w('Ahmad al-Tayyib', 'Ahmad_al-Tayyib')}, Oberhaupt der {_w('Moschee-Universität al-Azhar', 'al-Azhar-Universität')} in Kairo (die führende Autorität des sunnitischen Islam). Er und Papst Franziskus unterzeichneten 2019 in Abu Dhabi das {_w('Dokument über die Geschwisterlichkeit aller Menschen', 'Document_on_Human_Fraternity', 'en')}."
    },

    # ---------- SCHLUSS ----------
    {
        "p": 230, "after": "Magnifikat",
        "note": f"Der {_w('Lobgesang', 'Magnificat')} {_w('Marias', 'Maria_(Mutter_Jesu)')} in Lukas 1,46-55, täglich in der Vesper der Kirche gebetet: „Meine Seele preist die Größe des Herrn … Er stürzt die Mächtigen vom Thron und erhöht die Niedrigen.“ Der Titel der Enzyklika <i>Magnifica Humanitas</i> nimmt seine Anregung aus diesem Gesang."
    },
    {
        "p": 233, "after": "Rekapitulation",
        "note": f"Vom griechischen <i>anakephalaíōsis</i>, „Zusammenfassung unter einem Haupt“ (Eph 1,10). Der frühe Kirchenvater {_w('Irenäus', 'Irenäus_von_Lyon')} machte sie zum zentralen Bild des Heils: Christus sammelt die ganze Schöpfung, jedes Bruchstück und jede Wunde, in sich zurück."
    },
    {
        "p": 234, "after": "Augustinus",
        "note": f"Die zitierte Stelle stammt aus {_w('Augustinus’ Predigt 272', 'Sermon_272', 'en')}, gehalten vor neugetauften Christen über die Eucharistie: „Sei, was du siehst, und empfange, was du bist.“ Eine eindringliche Aussage der patristischen Theologie, dass die Kirche der Leib Christi <i>ist</i> — nicht bloß eine Gesellschaft, die sich um ihn versammelt."
    },
    {
        "p": 237, "after": "situierten Anthropozentrismus",
        "note": f"Ausdruck von Franziskus in <i>{_w('Laudato si’', 'Laudato_si’')}</i> (§118): eine bewusste Korrektur des aufklärerischen Anthropozentrismus. Der Mensch bleibt sittlich zentral, aber als Geschöpf, das in ein weiteres Netz des Lebens eingebunden und von ihm abhängig ist — nicht als losgelöstes Subjekt, das über einer trägen Natur steht. Leos Bezugnahme schließt hier einen Kreis, der in der Erörterung des Transhumanismus im Dritten Kapitel eröffnet wurde: Die Alternative dazu, „den Menschen hinter sich zu lassen“, besteht nicht darin, den Menschen zu inthronisieren, sondern darin, uns wieder in unsere geschöpfliche Gesellschaft einzuordnen."
    },
]
