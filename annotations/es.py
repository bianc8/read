"""Anotaciones editoriales españolas para Magnifica Humanitas.

Traducción de las anotaciones de ``annotations.py``. Cada entrada ancla una nota
al margen a un punto del párrafo haciendo coincidir un fragmento de texto exacto
(``after``) de la traducción oficial española. Los enlaces apuntan a Wikipedia
en español cuando el título es conocido; de lo contrario, a la inglesa
(``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "es") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- INTRODUCCIÓN ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"La encíclica de 1891 de {_w('León XIII', 'León_XIII')}, documento fundacional de la moderna {_w('Doctrina social católica', 'Doctrina_social_de_la_Iglesia')}, escrita en respuesta a los trastornos del capitalismo industrial. El título es latín y significa <i>{_w('de las cosas nuevas', 'Rerum_novarum')}</i>. León XIV evoca deliberadamente el nombre y el proyecto de su predecesor."
    },
    {
        "p": 3, "after": "Doctrina social de la Iglesia",
        "note": f"Un cuerpo coherente de enseñanza pontificia y conciliar sobre la vida social, económica y política, desarrollado a partir de León XIII. Sus principios fundamentales — dignidad, bien común, subsidiariedad, solidaridad, justicia — recurren a lo largo de toda la carta. Véase: {_w('Doctrina social de la Iglesia', 'Doctrina_social_de_la_Iglesia')}."
    },
    {
        "p": 4, "after": "nuevos asuntos",
        "note": f"<i>Res novae</i> en latín — la expresión de la que <i>{_w('Rerum novarum', 'Rerum_novarum')}</i> toma su nombre. León XIV la usa para indicar las presiones auténticamente nuevas que cada generación afronta."
    },
    {
        "p": 7, "after": "torre de Babel",
        "note": f"{_w('Génesis 11,1-9', 'Torre_de_Babel')}. Hombres que hablan una sola lengua se proponen construir una torre «cuya cúspide llegue hasta el cielo» para hacerse un nombre; Dios los dispersa confundiendo su lengua. Una perenne parábola cristiana de la soberbia y de la fragmentación que sigue cuando el obrar humano olvida a Dios."
    },
    {
        "p": 7, "after": "reconstrucción de los muros de Jerusalén",
        "note": f"El {_w('Libro de Nehemías', 'Libro_de_Nehemías')} (siglo V a.C.) narra de los exiliados judíos que regresan de {_w('Babilonia', 'Cautiverio_de_Babilonia')} para reconstruir una Jerusalén en ruinas. Nehemías organiza el trabajo familia por familia, escucha las quejas y enfrenta las oposiciones. León lo señala como modelo de reparación distribuida y coordinada — lo opuesto a la unificación desde arriba de Babel."
    },
    {
        "p": 10, "after": "sinodalidad",
        "note": f"Del griego <i>syn-hodos</i>, «caminar juntos». Una práctica que {_w('el papa Francisco', 'Francisco_(papa)')} hizo central: decisiones eclesiales alcanzadas mediante una amplia escucha y un discernimiento compartido, en lugar de por decreto desde arriba. Véase: {_w('sinodalidad', 'Sinodalidad')}."
    },
    {
        "p": 11, "after": "san Agustín",
        "note": f"{_w('Agustín de Hipona', 'Agustín_de_Hipona')} (354-430), obispo y filósofo norteafricano, uno de los pensadores más influyentes del cristianismo occidental. El «corazón inquieto» es el comienzo de sus <i>{_w('Confesiones', 'Confesiones_(Agustín_de_Hipona)')}</i>, su oración autobiográfica."
    },
    {
        "p": 13, "after": "subsidiariedad",
        "note": f"Principio social católico: las decisiones corresponden al nivel más pequeño y local capaz de tomarlas; las autoridades superiores existen para <i>sostener</i> (subsidium) a las inferiores, no para sustituirlas. Sistematizado por primera vez por {_w('Pío XI', 'Pío_XI')} en 1931. Véase: {_w('subsidiariedad', 'Principio_de_subsidiariedad')}."
    },
    {
        "p": 15, "after": "Jubileo ordinario del 2025",
        "note": f"En la tradición católica el {_w('Jubileo', 'Jubileo_(catolicismo)')} es un año de peregrinación, misericordia y perdón, celebrado cada 25 años. El Jubileo de 2025 fue abierto por {_w('el papa Francisco', 'Francisco_(papa)')} con el tema «Peregrinos de esperanza»."
    },

    # ---------- CAPÍTULO PRIMERO ----------
    {
        "p": 17, "after": "Magisterio",
        "note": f"La {_w('autoridad de enseñanza', 'Magisterio_de_la_Iglesia_católica')} oficial de la Iglesia católica, ejercida por el Papa y los obispos en comunión con él. La palabra viene del latín <i>magister</i>, «maestro»."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"«Gozo y esperanza» — la Constitución pastoral de 1965 del {_w('Concilio Vaticano II', 'Concilio_Vaticano_II')} sobre la Iglesia en el mundo contemporáneo. Sus palabras iniciales («Los gozos y las esperanzas, las tristezas y las angustias de los hombres de nuestro tiempo… son a la vez gozos y esperanzas… de los discípulos de Cristo») redefinieron la relación de la Iglesia con la vida secular. Véase: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Compendio de la doctrina social de la Iglesia",
        "note": f"Un {_w('texto de referencia vaticano de 2004', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')} que recoge y sistematiza la enseñanza social de la Iglesia desde León XIII hasta Juan Pablo II. A menudo la primera escala para rastrear dónde se formuló un principio."
    },
    {
        "p": 28, "after": "Laudato si",
        "note": f"{_w('La encíclica de 2015 del papa Francisco', 'Laudato_si%27')} sobre el cuidado de la «casa común» — la crisis ambiental leída como inseparable de la pobreza y la desigualdad. El título viene del Cántico de las criaturas de {_w('san Francisco de Asís', 'Francisco_de_Asís')} («Laudato si', mi' Signore»)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('La encíclica de 2020 del papa Francisco', 'Fratelli_tutti')} sobre la fraternidad y la amistad social. El título es de {_w('san Francisco de Asís', 'Francisco_de_Asís')}: «Todos hermanos»."
    },
    {
        "p": 30, "after": "Magna Charta",
        "note": f"Lit. «Gran Carta» — el {_w('documento inglés de 1215', 'Carta_Magna')} fundacional del gobierno constitucional. Pío XI la usa metafóricamente para llamar a la <i>Rerum novarum</i> la carta fundacional de la acción social católica."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"«En el cuadragésimo año» — {_w('la encíclica de 1931 de Pío XI', 'Quadragesimo_anno')}, escrita en el 40º aniversario de la <i>Rerum novarum</i> en pleno apogeo de la {_w('Gran Depresión', 'Gran_Depresión')}. Introdujo el principio de subsidiariedad en su forma moderna."
    },
    {
        "p": 32, "after": "derecho natural",
        "note": f"Una {_w('tradición filosófica', 'Derecho_natural')} que va de la {_w('Roma estoica', 'Estoicismo')} a {_w('Tomás de Aquino', 'Tomás_de_Aquino')}: existe un orden moral objetivo, accesible a la razón humana, anterior e independiente de toda autoridad humana. La Doctrina social católica funda en él los derechos humanos universales; el sistema internacional de derechos de la posguerra bebió de la misma corriente. La alternativa — que los derechos sean simplemente lo que los poderosos están dispuestos a conceder — es precisamente lo que el pensamiento iusnaturalista está construido para rechazar."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"«Madre y maestra» — {_w('la encíclica de 1961', 'Mater_et_magistra')} de {_w('Juan XXIII', 'Juan_XXIII')} que actualiza la Doctrina social católica para el mundo de la posguerra."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"«Paz en la tierra» — {_w('la encíclica de 1963 de Juan XXIII', 'Pacem_in_terris')}, escrita pocos meses después de la {_w('crisis de los misiles de Cuba', 'Crisis_de_los_misiles_de_Cuba')}. La primera encíclica dirigida a «todos los hombres de buena voluntad», no solo a los católicos."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"«De la dignidad humana» — la {_w('Declaración sobre la libertad religiosa de 1965', 'Dignitatis_humanae')} del Vaticano II, que comprometió formalmente a la Iglesia a defender el derecho civil de toda persona a la libertad religiosa."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"«El desarrollo de los pueblos» — {_w('la encíclica de 1967', 'Populorum_progressio')} de {_w('Pablo VI', 'Pablo_VI')}, que definió el desarrollo mismo como «el nuevo nombre de la paz» y orientó la Doctrina social católica hacia la desigualdad global."
    },
    {
        "p": 35, "after": "Pontificia Comisión Iustitia et Pax",
        "note": f"«Justicia y paz» — la oficina vaticana instituida por Pablo VI en 1967 para traducir la Doctrina social católica en trabajo de política internacional. Reorganizada en 2017 como {_w('Dicasterio para el Servicio del Desarrollo Humano Integral', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"«El octogésimo que llega» — la {_w('carta apostólica de 1971', 'Octogesima_adveniens')} de Pablo VI en el 80º aniversario de la <i>Rerum novarum</i>, sobre la urbanización y los límites de toda respuesta católica única a las cuestiones políticas."
    },
    {
        "p": 36, "after": "estructuras de pecado",
        "note": f"Expresión de {_w('Juan Pablo II', 'Juan_Pablo_II')} (en la <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) para los entramados sociales, económicos y políticos que institucionalizan la injusticia. La expresión desplaza el pecado de los meros actos individuales a los sistemas en los que participamos. Véase: {_w('pecado estructural', 'Structural_sin', 'en')}."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"«Realizando el trabajo» — {_w('la encíclica de 1981 de Juan Pablo II', 'Laborem_exercens')} sobre el trabajo humano. Sostuvo que el trabajo no es solo una mercancía, sino una dimensión fundamental de la vida humana, y la clave de toda la cuestión social."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"«La preocupación por las cosas sociales» — {_w('la encíclica de 1987 de Juan Pablo II', 'Sollicitudo_rei_socialis')} que revisita la <i>Populorum progressio</i> de Pablo VI veinte años después, centrada en la brecha creciente entre naciones ricas y pobres."
    },
    {
        "p": 38, "after": "civilización del amor",
        "note": f"Expresión acuñada por {_w('Pablo VI', 'Pablo_VI')} en 1975: una visión del orden social en la que la caridad, no el poder, es el principio organizador de la economía, la política y la cultura. Se convierte en el tema unificador del Capítulo Quinto."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"«El centésimo año» — {_w('la encíclica de 1991 de Juan Pablo II', 'Centesimus_annus')} en el centenario de la <i>Rerum novarum</i>, escrita tras la caída del comunismo. Reconoce la economía de mercado solo en la medida en que permanece subordinada a la ley moral y a la solidaridad."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"«La caridad en la verdad» — {_w('la encíclica de 2009', 'Caritas_in_veritate')} de {_w('Benedicto XVI', 'Benedicto_XVI')} sobre el desarrollo humano integral, escrita durante la crisis financiera global."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"«La alegría del Evangelio» — {_w('la exhortación apostólica de 2013 del papa Francisco', 'Evangelii_gaudium')}, el documento programático de su pontificado."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"«Nos amó» — {_w('la encíclica de 2024 del papa Francisco', 'Dilexit_nos')} sobre la devoción al {_w('Sagrado Corazón de Jesús', 'Sagrado_Corazón_de_Jesús')}, su última gran carta doctrinal."
    },

    # ---------- CAPÍTULO SEGUNDO ----------
    {
        "p": 50, "after": "Dios trinitario",
        "note": f"La doctrina cristiana central de la {_w('Trinidad', 'Santísima_Trinidad')}: un solo Dios en tres personas — Padre, Hijo y Espíritu Santo — eternamente unidos en el amor. Es esta doctrina la que hace al pensamiento social católico relacional en su raíz."
    },
    {
        "p": 52, "after": "dignidad ontológica",
        "note": f"Del griego <i>on</i>, «ser» — la dignidad que pertenece a una persona en virtud del <i>ser</i>, no del hacer, del tener o del ser reconocida. La distinción es {_w('aristotélico-tomista', 'Tomismo')}: el valor de una persona deriva de lo que fundamentalmente es (<i>esse</i>), no de propiedades variables como la capacidad, el logro o la posición social."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"«Dignidad infinita» — una {_w('declaración de 2024', 'Dignitas_infinita')} del Dicasterio para la Doctrina de la Fe del Vaticano que afirma la dignidad incondicional de toda persona humana frente a una larga lista de violaciones contemporáneas."
    },
    {
        "p": 54, "after": "Declaración Universal de los Derechos del Hombre",
        "note": f"{_w('Adoptada por la Asamblea General de la ONU', 'Declaración_Universal_de_los_Derechos_Humanos')} el 10 de diciembre de 1948, tras la Segunda Guerra Mundial. La primera formulación global de los derechos que pertenecen a toda persona «simplemente por ser humana»."
    },
    {
        "p": 60, "after": "bien común",
        "note": f"Un {_w('concepto', 'Bien_común')} de hondas raíces filosóficas en {_w('Aristóteles', 'Aristóteles')} (<i>Política</i>, Libro III) y {_w('Tomás de Aquino', 'Tomás_de_Aquino')}. Crucialmente, <i>no</i> es la suma de las preferencias individuales (la reducción utilitarista) ni meramente bienes «públicos» como el aire limpio; es el conjunto compartido de condiciones bajo las cuales cada persona puede florecer. Es el concepto que distingue el pensamiento social católico tanto del puro individualismo como del puro colectivismo."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Latín para «cosa pública» — la {_w('comunidad política', 'Res_publica')}, el interés compartido de todos los ciudadanos. Raíz de la palabra <i>república</i>."
    },
    {
        "p": 82, "after": "desarrollo humano integral",
        "note": f"{_w('Expresión acuñada por Pablo VI', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967): desarrollo de <i>cada</i> persona y de <i>toda</i> la persona — material, cultural, moral, espiritual. El criterio con el que la enseñanza católica evalúa todo modelo económico."
    },
    {
        "p": 86, "after": "examen de conciencia",
        "note": f"Una tradicional práctica espiritual católica — {_w('una revisión metódica de sí ante Dios', 'Examen_de_conciencia')} — derivada en particular del <i>examen</i> {_w('ignaciano', 'Ignatian_spirituality', 'en')}. Aquí León la transforma de disciplina personal en disciplina comunitaria para la Iglesia misma."
    },

    # ---------- CAPÍTULO TERCERO ----------
    {
        "p": 92, "after": "paradigma tecnocrático",
        "note": f"Expresión del papa Francisco en la <i>Laudato si'</i> (2015), heredada de {_w('Romano Guardini', 'Romano_Guardini')} y en resonancia con la crítica de la técnica moderna de {_w('Heidegger', 'Martin_Heidegger')}. No entusiasmo por los artilugios, sino el hábito mental más profundo que trata <i>todo</i> — naturaleza, personas, instituciones — como materia prima que medir, optimizar y controlar. El paradigma reduce el ser a función y el valor a utilidad."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Sacerdote y filósofo católico italo-alemán', 'Romano_Guardini')} (1885-1968). Su obra <i>El fin de la Edad Moderna</i> advertía que el poder técnico había superado la formación moral y espiritual necesaria para ejercerlo. Influencia formativa sobre el Vaticano II y sobre la <i>Laudato si'</i> de Francisco."
    },
    {
        "p": 107, "after": "alineación",
        "note": f"Término central de la {_w('seguridad de la IA', 'AI_alignment', 'en')} contemporánea: el proyecto de hacer que los sistemas de IA persigan objetivos coherentes con los valores humanos. Asociado a <i>Human Compatible</i> (2019) de {_w('Stuart Russell', 'Stuart_J._Russell', 'en')}, al trabajo del {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, de {_w('Anthropic', 'Anthropic', 'en')} y al esfuerzo de «{_w('superalineación', 'OpenAI', 'en')}» de OpenAI. La objeción de León no es a la alineación, sino a la pregunta que la alineación por sí sola no puede responder: <i>alineado con los valores de quién</i> — y decidido por quién?"
    },
    {
        "p": 115, "after": "transhumanismo",
        "note": f"Un {_w('movimiento intelectual del siglo XX-XXI', 'Transhumanismo')} ({_w('Max More', 'Max_More')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}) que urge a usar biotecnologías, IA y otras herramientas para superar los límites biológicos humanos — enfermedad, envejecimiento, umbrales cognitivos, incluso la mortalidad. Hereda el progresismo ilustrado y la cibernética de la posguerra; tiene sedes institucionales en Silicon Valley y en la industria de la longevidad. Trata el cuerpo como hardware actualizable."
    },
    {
        "p": 115, "after": "posthumanismo",
        "note": f"Una genealogía intelectual distinta. El {_w('posthumanismo «crítico»', 'Posthumanismo')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) desciende de la filosofía continental y de la teoría feminista. Descentra lo humano — rechazando la idea de un sujeto humano estable y autónomo — y subraya nuestro entrelazamiento con otras especies, máquinas y ecosistemas. A veces aliado y a veces crítico del transhumanismo; ambos comparten la disposición a relativizar lo humano, pero por razones muy distintas."
    },
    {
        "p": 116, "after": "antropocentrismo",
        "note": f"La {_w('concepción', 'Antropocentrismo')} según la cual los seres humanos están en el centro de la consideración moral. La tradición cristiana ha sido históricamente antropocéntrica; Francisco la matizó en la <i>Laudato si'</i> con la expresión «antropocentrismo situado» — los seres humanos como criaturas insertas, no como dueños distantes. El posthumanismo rechaza el antropocentrismo más netamente, considerándolo una ilusión ilustrada."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Psiquiatra austriaco y superviviente de Auschwitz', 'Viktor_Frankl')} (1905-1997). Su <i>{_w('El hombre en busca de sentido', 'El_hombre_en_busca_de_sentido')}</i> sostenía que el impulso humano más profundo es la búsqueda de sentido — una libertad que ninguna condición, por inhumana que sea, puede extinguir del todo."
    },
    {
        "p": 122, "after": "Novena Sinfonía de Beethoven",
        "note": f"{_w('Estrenada en 1824', 'Sinfonía_n.º_9_(Beethoven)')}; su final coral entona el «{_w('Himno a la alegría', 'Oda_a_la_Alegría')}» de Schiller, un canto a la fraternidad universal. Adoptado en 1985 como himno de la Unión Europea."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"El {_w('cuadro de 1937', 'Guernica_(cuadro)')} de {_w('Picasso', 'Pablo_Picasso')}, realizado para el Pabellón español de la Exposición de París, que representa el bombardeo nazi de la villa vasca de Guernica durante la Guerra Civil española. Un monumento del arte contra la guerra."
    },
    {
        "p": 122, "after": "La lista de Schindler",
        "note": f"La {_w('película de 1993', 'La_lista_de_Schindler')} de {_w('Steven Spielberg', 'Steven_Spielberg')} sobre {_w('Oskar Schindler', 'Oskar_Schindler')}, el industrial alemán que salvó a más de mil trabajadores judíos polacos del exterminio durante el Holocausto."
    },
    {
        "p": 123, "after": "Comité Internacional de la Cruz Roja",
        "note": f"{_w('Fundado en Ginebra en 1863', 'Comité_Internacional_de_la_Cruz_Roja')} por {_w('Henry Dunant', 'Henry_Dunant')} tras presenciar la carnicería de la {_w('batalla de Solferino', 'Batalla_de_Solferino')}. Su neutralidad operativa — atender a los heridos de cada bando — se convirtió en la semilla del derecho internacional humanitario."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('Pastor bautista estadounidense', 'Martin_Luther_King')} (1929-1968) y líder central del movimiento por los derechos civiles en EE. UU., cuyas campañas no violentas contribuyeron a poner fin a la segregación racial legal."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('Líder sudafricano contra el apartheid', 'Nelson_Mandela')} (1918-2013), encarcelado durante 27 años, luego presidente de una Sudáfrica post-apartheid. Su rechazo de la violencia vengativa moldeó el proceso de {_w('Verdad y Reconciliación', 'Comisión_para_la_Verdad_y_la_Reconciliación_(Sudáfrica)')} del país."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('Periodista y activista estadounidense', 'Dorothy_Day')} (1897-1980), cofundadora del {_w('Movimiento del Trabajador Católico', 'Movimiento_del_Trabajador_Católico')}. Unió fe católica, pobreza voluntaria, anarquismo y pacifismo; vivió entre los pobres en las casas de hospitalidad de Manhattan. Causa de canonización abierta en 2000."
    },
    {
        "p": 125, "after": "Maximiliano María Kolbe",
        "note": f"{_w('Fraile franciscano conventual polaco', 'Maximiliano_Kolbe')} (1894-1941). En Auschwitz se ofreció a ocupar el lugar de un compañero de prisión condenado al búnker del hambre; murió tras dos semanas. Canonizado en 1982 como «mártir de la caridad»."
    },
    {
        "p": 125, "after": "san Óscar Romero",
        "note": f"{_w('Arzobispo de San Salvador', 'Óscar_Romero')} (1917-1980), asesinado en el altar mientras celebraba la Misa por denunciar repetidamente a los escuadrones de la muerte y la represión militar en la guerra civil salvadoreña. Canonizado en 2018."
    },
    {
        "p": 127, "after": "santo Tomás de Aquino",
        "note": f"{_w('Teólogo y filósofo dominico del siglo XIII', 'Tomás_de_Aquino')} (1225-1274). Su <i>{_w('Summa Theologiae', 'Summa_Theologiae')}</i> es la más influyente síntesis de la teología cristiana en el Occidente latino; enseñó que la gracia perfecciona la naturaleza en lugar de destruirla."
    },
    {
        "p": 128, "after": "prometeicos",
        "note": f"Del mito griego: {_w('Prometeo', 'Prometeo')} robó el fuego a los dioses para dárselo a la humanidad y fue castigado eternamente. En el pensamiento moderno la figura se convirtió en el patrón de la autoafirmación tecnológica del hombre — {_w('Mary Shelley', 'Mary_Shelley')} subtituló <i>{_w('Frankenstein', 'Frankenstein')}</i> «El Prometeo moderno»; Marx alabó el «desencadenamiento prometeico» de las fuerzas humanas; {_w('Hans Jonas', 'Hans_Jonas')}, en <i>El principio de responsabilidad</i> (1979), advirtió que la técnica moderna ha dado finalmente a la ambición prometeica un alcance divino sin una sabiduría divina."
    },
    {
        "p": 130, "after": "San Agustín",
        "note": f"En <i>{_w('La ciudad de Dios', 'La_ciudad_de_Dios')}</i> (inicios del siglo V), Agustín lee toda la historia como el entrelazamiento de dos ciudades — terrena y celestial — construidas por dos amores opuestos. La imagen da el título a este capítulo y unifica el contraste de la encíclica entre Babel y Jerusalén."
    },

    # ---------- CAPÍTULO CUARTO ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Teórica política germano-estadounidense', 'Hannah_Arendt')} (1906-1975). Sus <i>{_w('Los orígenes del totalitarismo', 'Los_orígenes_del_totalitarismo')}</i> (1951) y <i>{_w('Eichmann en Jerusalén', 'Eichmann_en_Jerusalén')}</i> (1963) mostraron cómo los regímenes totalitarios dependen de disolver la distinción misma entre hecho y ficción."
    },
    {
        "p": 140, "after": "Platón",
        "note": f"{_w('Filósofo griego antiguo', 'Platón')} (c. 428-348 a.C.). La imagen de la comprensión que se enciende como una chispa a través de una larga indagación compartida procede de su {_w('Carta Séptima', 'Seventh_Letter', 'en')} — una defensa del aprendizaje lento y dialógico contra la ilusión del saber rápido."
    },
    {
        "p": 148, "after": "san Benito de Nursia",
        "note": f"{_w('Fundador del monacato occidental del siglo VI', 'Benito_de_Nursia')} (c. 480-547). Su <i>{_w('Regla', 'Regla_de_san_Benito')}</i> entretejió oración y trabajo manual — <i>ora et labora</i> — y construyó la espiritualidad del trabajo que moldearía la cultura europea durante un milenio."
    },
    {
        "p": 151, "after": "cuarta revolución industrial",
        "note": f"{_w('Término popularizado por Klaus Schwab', 'Cuarta_revolución_industrial')} (fundador del {_w('Foro Económico Mundial', 'Foro_Económico_Mundial')}) para la actual fusión de IA, robótica, biotecnología y mundo físico — sucesora de las revoluciones a vapor, eléctrica y digital que la precedieron."
    },
    {
        "p": 163, "after": "mano invisible",
        "note": f"La {_w('metáfora', 'Mano_invisible')} de {_w('Adam Smith', 'Adam_Smith')} (<i>La riqueza de las naciones</i>, 1776): la búsqueda del interés propio en un mercado competitivo puede, involuntariamente, producir beneficio social. León se une a una larga estirpe de pontífices al sostener que este mecanismo, por sí solo, no puede gobernar una economía."
    },

    # ---------- CAPÍTULO QUINTO ----------
    {
        "p": 192, "after": "guerra justa",
        "note": f"La {_w('tradición cristiana', 'Guerra_justa')} (Agustín, Tomás, Vitoria, Suárez) de las condiciones morales bajo las cuales la guerra puede ser admisible — justa causa, autoridad legítima, proporcionalidad, último recurso. Francisco y ahora León sostienen que, bajo el armamento moderno, esos criterios ya no pueden cumplirse."
    },
    {
        "p": 193, "after": "industria bélica",
        "note": f"Evoca el «complejo militar-industrial», {_w('expresión acuñada por el presidente de EE. UU. Dwight D. Eisenhower', 'Complejo_militar-industrial')} en su discurso de despedida de 1961, que advertía cómo los intereses entrelazados de los fabricantes de armas, los aparatos militares y políticos crean un impulso estructural hacia un estado de guerra perpetua — exactamente la preocupación de León aquí, sesenta y cinco años después."
    },
    {
        "p": 194, "after": "Tratado sobre la Prohibición de las Armas Nucleares",
        "note": f"Un {_w('tratado de la ONU de 2017', 'Tratado_sobre_la_Prohibición_de_las_Armas_Nucleares')} que entró en vigor en enero de 2021. Prohíbe categóricamente desarrollar, ensayar, producir o poseer armas nucleares. La Santa Sede fue de las primeras firmantes; los nueve Estados dotados de armas nucleares se han negado todos a adherirse."
    },
    {
        "p": 198, "after": "agentes morales artificiales",
        "note": f"Un término de la {_w('literatura sobre ética de las máquinas', 'Machine_ethics', 'en')} (Wendell Wallach y Colin Allen, <i>Moral Machines</i>, 2008) — la propuesta de que sistemas de IA suficientemente avanzados puedan ser programados para formular juicios éticos por sí mismos. La encíclica responde con la visión clásica: el juicio moral no es un cálculo, sino la respuesta de una conciencia a una persona, irreducible a cualquier máquina que siga reglas."
    },
    {
        "p": 201, "after": "1989",
        "note": f"El año de la caída del {_w('Muro de Berlín', 'Muro_de_Berlín')} y del colapso de los regímenes comunistas en Europa central y oriental — que marca el fin de la {_w('Guerra Fría', 'Guerra_Fría')} y el comienzo de la era de la «globalización» que León critica aquí."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Término alemán del siglo XIX', 'Realpolitik')} para una política conducida sobre la base de intereses prácticos y materiales, en lugar de ideología o principio moral. León la considera una falsificación del genuino realismo político."
    },
    {
        "p": 213, "after": "John Ronald Reuel Tolkien",
        "note": f"{_w('Autor inglés', 'J._R._R._Tolkien')} (1892-1973), católico devoto, creador de <i>{_w('El Señor de los Anillos', 'El_Señor_de_los_Anillos')}</i>. La cita es de Gandalf, de <i>{_w('El retorno del Rey', 'El_retorno_del_Rey')}</i>: una vocación definida por cultivar el pedazo de tierra que nos ha sido confiado."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Estadista católico italiano', 'Giorgio_La_Pira')} (1904-1977), varias veces alcalde de Florencia e incansable organizador de conferencias de paz de la era de la Guerra Fría, a través de líneas religiosas e ideológicas. Beatificado en 2018."
    },
    {
        "p": 222, "after": "maniqueas",
        "note": f"De {_w('Mani', 'Mani_(profeta)')} (216-276 d.C.), fundador de una {_w('religión dualista persa', 'Maniqueísmo')} que leía la historia como una batalla cósmica entre fuerzas iguales y opuestas de luz y tiniebla. {_w('Agustín', 'Agustín_de_Hipona')} fue maniqueo durante nueve años antes de convertirse; su posterior teología del mal como <i>privación</i> (una ausencia en lugar de una sustancia) se construyó contra este dualismo. La palabra hoy designa toda visión del mundo que divida netamente la realidad en campos del bien y del mal."
    },
    {
        "p": 223, "after": "espíritu de Asís",
        "note": f"El 27 de octubre de 1986 Juan Pablo II reunió en Asís a los líderes de las religiones del mundo {_w('para orar por la paz', 'Day_of_Prayer_for_World_Peace', 'en')} — un precedente de construcción interreligiosa de la paz que Francisco renovó varias veces durante su pontificado."
    },
    {
        "p": 223, "after": "Gran Imán de al-Azhar",
        "note": f"{_w('Ahmed el-Tayeb', 'Ahmed_el-Tayeb')}, máxima autoridad de la {_w('universidad-mezquita de al-Azhar', 'Universidad_de_Al-Azhar')} de El Cairo (la principal autoridad del islam suní). Él y el papa Francisco firmaron el {_w('Documento sobre la Fraternidad Humana de 2019', 'Document_on_Human_Fraternity', 'en')} en Abu Dabi."
    },

    # ---------- CONCLUSIÓN ----------
    {
        "p": 230, "after": "Magníficat",
        "note": f"El {_w('cántico de alabanza', 'Magníficat')} de {_w('María', 'María_(madre_de_Jesús)')} en Lucas 1,46-55, rezado cada día en las Vísperas de la Iglesia: «Mi alma engrandece al Señor… derribó a los poderosos de sus tronos y enalteció a los humildes». El título de la encíclica <i>Magnifica Humanitas</i> toma su inspiración de este canto."
    },
    {
        "p": 233, "after": "recapitulación",
        "note": f"Del griego <i>anakephalaíōsis</i>, «recapitular bajo una cabeza» (Ef 1,10). El Padre antiguo {_w('Ireneo', 'Ireneo_de_Lyon')} hizo de ella la imagen central de la salvación: Cristo recoge en sí toda la creación, cada fragmento y cada herida."
    },
    {
        "p": 234, "after": "san Agustín",
        "note": f"El pasaje citado es del {_w('Sermón 272 de Agustín', 'Sermon_272', 'en')}, predicado a los cristianos recién bautizados sobre la Eucaristía: «Sed lo que veis y recibid lo que sois». Una neta afirmación de la teología patrística según la cual la Iglesia <i>es</i> el cuerpo de Cristo — no simplemente una sociedad que se reúne en torno a él."
    },
    {
        "p": 237, "after": "antropocentrismo situado",
        "note": f"Expresión de Francisco en la <i>{_w('Laudato si', 'Laudato_si%27')}'</i> (§118): una deliberada corrección del antropocentrismo ilustrado. Los seres humanos permanecen moralmente centrales, pero como criaturas insertas en y dependientes de una más amplia red de vida — no como sujetos distantes situados sobre una naturaleza inerte. La invocación de León aquí cierra un círculo abierto en la discusión sobre el transhumanismo del Capítulo Tercero: la alternativa a «dejar atrás lo humano» no es entronizar lo humano, sino recolocarnos en nuestra compañía creatural."
    },
]
