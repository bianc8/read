"""Annotations éditoriales françaises pour Magnifica Humanitas.

Traduction des annotations de ``annotations/en.py``. Chaque entrée rattache une
note marginale à un point du paragraphe en faisant correspondre un fragment de
texte exact (``after``) de la traduction officielle française. Les liens
pointent vers Wikipédia en français lorsque le titre est connu, sinon vers la
version anglaise (``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "fr") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- INTRODUCTION ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"L'encyclique de 1891 de {_w('Léon XIII', 'Léon_XIII')}, document fondateur de la moderne {_w('Doctrine sociale de l\'Église', 'Doctrine_sociale_de_l\'Église_catholique')}, écrite en réponse aux bouleversements du capitalisme industriel. Le titre est latin et signifie <i>{_w('des choses nouvelles', 'Rerum_novarum')}</i>. Léon XIV reprend délibérément le nom et le projet de son prédécesseur."
    },
    {
        "p": 3, "after": "Doctrine sociale de l’Église",
        "note": f"Un corps cohérent d'enseignement pontifical et conciliaire sur la vie sociale, économique et politique, développé à partir de Léon XIII. Ses principes fondamentaux — dignité, bien commun, subsidiarité, solidarité, justice — reviennent tout au long de la lettre. Voir : {_w('Doctrine sociale de l\'Église', 'Doctrine_sociale_de_l\'Église_catholique')}."
    },
    {
        "p": 4, "after": "questions nouvelles",
        "note": f"<i>Res novae</i> en latin — l'expression dont <i>{_w('Rerum novarum', 'Rerum_novarum')}</i> tire son nom. Léon XIV l'emploie pour désigner les pressions authentiquement nouvelles que chaque génération affronte."
    },
    {
        "p": 7, "after": "tour de Babel",
        "note": f"{_w('Genèse 11, 1-9', 'Tour_de_Babel')}. Des hommes parlant une seule langue entreprennent de bâtir une tour «&nbsp;dont le sommet pénètre les cieux&nbsp;» pour se faire un nom&nbsp;; Dieu les disperse en confondant leur langage. Une parabole chrétienne perpétuelle de l'orgueil et de la fragmentation qui suit lorsque l'agir humain oublie Dieu."
    },
    {
        "p": 7, "after": "reconstruction des murs de Jérusalem",
        "note": f"Le {_w('livre de Néhémie', 'Livre_de_Néhémie')} (Ve siècle av. J.-C.) raconte le retour des exilés juifs de {_w('Babylone', 'Captivité_à_Babylone')} pour reconstruire une Jérusalem en ruines. Néhémie organise le travail famille par famille, écoute les plaintes et affronte les oppositions. Léon en fait un modèle de réparation distribuée et coordonnée — l'opposé de l'unification par le haut de Babel."
    },
    {
        "p": 10, "after": "synodalité",
        "note": f"Du grec <i>syn-hodos</i>, «&nbsp;marcher ensemble&nbsp;». Une pratique rendue centrale par {_w('le pape François', 'François_(pape)')} : des décisions ecclésiales prises par une large écoute et un discernement partagé plutôt que par décret venu d'en haut. Voir : {_w('synodalité', 'Synodalité')}."
    },
    {
        "p": 11, "after": "saint Augustin",
        "note": f"{_w('Augustin d\'Hippone', 'Augustin_d\'Hippone')} (354-430), évêque et philosophe nord-africain, l'un des penseurs les plus influents du christianisme occidental. Le «&nbsp;cœur inquiet&nbsp;» est l'incipit de ses <i>{_w('Confessions', 'Les_Confessions_(Augustin)')}</i>, sa prière autobiographique."
    },
    {
        "p": 13, "after": "subsidiarité",
        "note": f"Principe social catholique : les décisions reviennent au niveau le plus petit et le plus local capable de les prendre ; les autorités supérieures existent pour <i>soutenir</i> (subsidium) les inférieures, non pour les remplacer. Systématisé pour la première fois par {_w('Pie XI', 'Pie_XI')} en 1931. Voir : {_w('subsidiarité', 'Subsidiarité')}."
    },
    {
        "p": 15, "after": "Jubilé ordinaire de 2025",
        "note": f"Dans la tradition catholique, le {_w('Jubilé', 'Jubilé_(catholicisme)')} est une année de pèlerinage, de miséricorde et de pardon, célébrée tous les 25 ans. Le Jubilé 2025 a été ouvert par {_w('le pape François', 'François_(pape)')} sur le thème «&nbsp;Pèlerins d'espérance&nbsp;»."
    },

    # ---------- CHAPITRE PREMIER ----------
    {
        "p": 17, "after": "Magistère",
        "note": f"L'{_w('autorité d\'enseignement', 'Magistère')} officielle de l'Église catholique, exercée par le pape et les évêques en communion avec lui. Le mot vient du latin <i>magister</i>, «&nbsp;maître&nbsp;»."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"«&nbsp;Joie et espérance&nbsp;» — la Constitution pastorale de 1965 du {_w('concile Vatican II', 'Concile_Vatican_II')} sur l'Église dans le monde de ce temps. Ses mots d'ouverture («&nbsp;Les joies et les espoirs, les tristesses et les angoisses des hommes de ce temps… sont aussi les joies et les espoirs… des disciples du Christ&nbsp;») ont redéfini le rapport de l'Église à la vie séculière. Voir : {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Compendium de la Doctrine sociale de l’Église",
        "note": f"Un {_w('ouvrage de référence du Vatican publié en 2004', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')} qui rassemble et systématise l'enseignement social de l'Église de Léon XIII à Jean-Paul II. Souvent la première étape pour retracer où un principe a été formulé."
    },
    {
        "p": 28, "after": "Laudato si",
        "note": f"{_w('L\'encyclique de 2015 du pape François', 'Laudato_si\'')} sur le soin de la «&nbsp;maison commune&nbsp;» — la crise environnementale lue comme inséparable de la pauvreté et de l'inégalité. Le titre vient du Cantique des créatures de {_w('saint François d\'Assise', 'François_d\'Assise')} («&nbsp;Loué sois-tu, mon Seigneur&nbsp;»)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('L\'encyclique de 2020 du pape François', 'Fratelli_tutti')} sur la fraternité et l'amitié sociale. Le titre est de {_w('saint François d\'Assise', 'François_d\'Assise')} : «&nbsp;Tous frères&nbsp;»."
    },
    {
        "p": 30, "after": "Grande Charte",
        "note": f"Litt. «&nbsp;Grande Charte&nbsp;» — le {_w('document anglais de 1215', 'Grande_Charte')} fondateur du gouvernement constitutionnel. Pie XI l'emploie métaphoriquement pour appeler la <i>Rerum novarum</i> la charte fondatrice de l'action sociale catholique."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"«&nbsp;Dans la quarantième année&nbsp;» — {_w('l\'encyclique de 1931 de Pie XI', 'Quadragesimo_anno')}, écrite au 40e anniversaire de <i>Rerum novarum</i> en pleine {_w('Grande Dépression', 'Grande_Dépression')}. Elle introduisit le principe de subsidiarité dans sa forme moderne."
    },
    {
        "p": 32, "after": "droit naturel",
        "note": f"Une {_w('tradition philosophique', 'Droit_naturel')} allant de la {_w('Rome stoïcienne', 'Stoïcisme')} à {_w('Thomas d\'Aquin', 'Thomas_d\'Aquin')} : il existe un ordre moral objectif, accessible à la raison humaine, antérieur et indépendant de toute autorité humaine. La Doctrine sociale catholique y fonde les droits humains universels ; le système international des droits de l'après-guerre puisa au même courant. L'alternative — que les droits soient simplement ce que les puissants veulent bien concéder — est précisément ce que la pensée du droit naturel est faite pour refuser."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"«&nbsp;Mère et maîtresse&nbsp;» — {_w('l\'encyclique de 1961', 'Mater_et_magistra')} de {_w('Jean XXIII', 'Jean_XXIII')} qui actualise la Doctrine sociale catholique pour le monde de l'après-guerre."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"«&nbsp;Paix sur la terre&nbsp;» — {_w('l\'encyclique de 1963 de Jean XXIII', 'Pacem_in_terris')}, écrite quelques mois après la {_w('crise des missiles de Cuba', 'Crise_des_missiles_de_Cuba')}. La première encyclique adressée à «&nbsp;tous les hommes de bonne volonté&nbsp;», et non aux seuls catholiques."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"«&nbsp;De la dignité humaine&nbsp;» — la {_w('Déclaration sur la liberté religieuse de 1965', 'Dignitatis_humanae')} de Vatican II, qui engagea formellement l'Église à défendre le droit civil de toute personne à la liberté religieuse."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"«&nbsp;Le développement des peuples&nbsp;» — {_w('l\'encyclique de 1967', 'Populorum_progressio')} de {_w('Paul VI', 'Paul_VI')}, qui définit le développement lui-même comme «&nbsp;le nouveau nom de la paix&nbsp;» et oriente la Doctrine sociale catholique vers l'inégalité mondiale."
    },
    {
        "p": 35, "after": "Commission pontificale Iustitia et Pax",
        "note": f"«&nbsp;Justice et paix&nbsp;» — l'office vatican institué par Paul VI en 1967 pour traduire la Doctrine sociale catholique en travail de politique internationale. Réorganisé en 2017 en {_w('Dicastère pour le service du développement humain intégral', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"«&nbsp;Le quatre-vingtième qui vient&nbsp;» — la {_w('lettre apostolique de 1971', 'Octogesima_adveniens')} de Paul VI au 80e anniversaire de <i>Rerum novarum</i>, sur l'urbanisation et les limites de toute réponse catholique unique aux questions politiques."
    },
    {
        "p": 36, "after": "structures de péché",
        "note": f"Expression de {_w('Jean-Paul II', 'Jean-Paul_II')} (dans <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) pour les dispositifs sociaux, économiques et politiques qui institutionnalisent l'injustice. L'expression déplace le péché des seuls actes individuels vers les systèmes auxquels nous participons. Voir : {_w('péché structurel', 'Structural_sin', 'en')}."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"«&nbsp;En accomplissant le travail&nbsp;» — {_w('l\'encyclique de 1981 de Jean-Paul II', 'Laborem_exercens')} sur le travail humain. Elle soutint que le travail n'est pas seulement une marchandise mais une dimension fondamentale de la vie humaine, et la clé de toute la question sociale."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"«&nbsp;Le souci des choses sociales&nbsp;» — {_w('l\'encyclique de 1987 de Jean-Paul II', 'Sollicitudo_rei_socialis')} qui revisite la <i>Populorum progressio</i> de Paul VI vingt ans après, centrée sur le fossé croissant entre nations riches et pauvres."
    },
    {
        "p": 38, "after": "civilisation de l’amour",
        "note": f"Expression forgée par {_w('Paul VI', 'Paul_VI')} en 1975 : une vision de l'ordre social où la charité, non le pouvoir, est le principe organisateur de l'économie, de la politique et de la culture. Elle devient le thème unificateur du Chapitre Cinq."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"«&nbsp;La centième année&nbsp;» — {_w('l\'encyclique de 1991 de Jean-Paul II', 'Centesimus_annus')} au centenaire de <i>Rerum novarum</i>, écrite après la chute du communisme. Elle reconnaît l'économie de marché seulement dans la mesure où elle reste subordonnée à la loi morale et à la solidarité."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"«&nbsp;La charité dans la vérité&nbsp;» — {_w('l\'encyclique de 2009', 'Caritas_in_veritate')} de {_w('Benoît XVI', 'Benoît_XVI')} sur le développement humain intégral, écrite pendant la crise financière mondiale."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"«&nbsp;La joie de l'Évangile&nbsp;» — {_w('l\'exhortation apostolique de 2013 du pape François', 'Evangelii_gaudium')}, le document programmatique de son pontificat."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"«&nbsp;Il nous a aimés&nbsp;» — {_w('l\'encyclique de 2024 du pape François', 'Dilexit_nos')} sur la dévotion au {_w('Sacré-Cœur de Jésus', 'Sacré-Cœur')}, sa dernière grande lettre doctrinale."
    },

    # ---------- CHAPITRE DEUX ----------
    {
        "p": 50, "after": "Dieu trinitaire",
        "note": f"La doctrine chrétienne centrale de la {_w('Trinité', 'Trinité_chrétienne')} : un seul Dieu en trois personnes — Père, Fils et Esprit Saint — éternellement unis dans l'amour. C'est cette doctrine qui rend la pensée sociale catholique relationnelle à sa racine."
    },
    {
        "p": 52, "after": "dignité ontologique",
        "note": f"Du grec <i>on</i>, «&nbsp;être&nbsp;» — la dignité qui appartient à une personne en vertu de l'<i>être</i>, non du faire, de l'avoir ou de l'être reconnue. La distinction est {_w('aristotélico-thomiste', 'Thomisme')} : la valeur d'une personne découle de ce qu'elle est fondamentalement (<i>esse</i>), non de propriétés variables comme la capacité, le succès ou la position sociale."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"«&nbsp;Dignité infinie&nbsp;» — une {_w('déclaration de 2024', 'Dignitas_infinita')} du Dicastère pour la doctrine de la foi affirmant la dignité inconditionnelle de chaque personne humaine contre une longue liste de violations contemporaines."
    },
    {
        "p": 54, "after": "Déclaration universelle des droits de l’homme",
        "note": f"{_w('Adoptée par l\'Assemblée générale de l\'ONU', 'Déclaration_universelle_des_droits_de_l\'homme')} le 10 décembre 1948 au lendemain de la Seconde Guerre mondiale. La première formulation mondiale des droits qui appartiennent à toute personne «&nbsp;simplement parce qu'elle est humaine&nbsp;»."
    },
    {
        "p": 60, "after": "bien commun",
        "note": f"Un {_w('concept', 'Bien_commun')} aux racines philosophiques profondes chez {_w('Aristote', 'Aristote')} (<i>Politique</i>, Livre III) et {_w('Thomas d\'Aquin', 'Thomas_d\'Aquin')}. Crucialement, il n'est <i>pas</i> la somme des préférences individuelles (la réduction utilitariste) ni de simples biens «&nbsp;publics&nbsp;» comme l'air pur ; c'est l'ensemble partagé des conditions sous lesquelles chacun peut s'épanouir. C'est le concept qui distingue la pensée sociale catholique de l'individualisme pur comme du collectivisme pur."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Latin pour «&nbsp;chose publique&nbsp;» — la {_w('communauté politique', 'Res_publica')}, l'intérêt partagé de tous les citoyens. Racine du mot <i>république</i>."
    },
    {
        "p": 82, "after": "développement humain intégral",
        "note": f"{_w('Expression forgée par Paul VI', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967) : développement de <i>chaque</i> personne et de <i>tout</i> l'homme — matériel, culturel, moral, spirituel. Le critère par lequel l'enseignement catholique évalue tout modèle économique."
    },
    {
        "p": 86, "after": "examen de conscience",
        "note": f"Une pratique spirituelle catholique traditionnelle — {_w('une révision méthodique de soi devant Dieu', 'Examen_de_conscience')} — issue en particulier de l'<i>examen</i> {_w('ignatien', 'Ignatian_spirituality', 'en')}. Ici Léon la transforme d'une discipline personnelle en discipline communautaire pour l'Église elle-même."
    },

    # ---------- CHAPITRE TROIS ----------
    {
        "p": 92, "after": "paradigme technocratique",
        "note": f"Expression du pape François dans <i>Laudato si'</i> (2015), héritée de {_w('Romano Guardini', 'Romano_Guardini')} et en résonance avec la critique de la technique moderne de {_w('Heidegger', 'Martin_Heidegger')}. Non l'enthousiasme pour les gadgets, mais l'habitude mentale plus profonde qui traite <i>tout</i> — nature, personnes, institutions — comme matière première à mesurer, optimiser et contrôler. Le paradigme réduit l'être à une fonction et la valeur à une utilité."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Prêtre et philosophe catholique italo-allemand', 'Romano_Guardini')} (1885-1968). Son ouvrage <i>La Fin des temps modernes</i> avertissait que la puissance technique avait dépassé la formation morale et spirituelle nécessaire pour l'exercer. Une influence formatrice sur Vatican II et sur <i>Laudato si'</i> de François."
    },
    {
        "p": 107, "after": "alignement",
        "note": f"Terme central de la {_w('sécurité de l\'IA', 'AI_alignment', 'en')} contemporaine : le projet de rendre les systèmes d'IA orientés vers des objectifs cohérents avec les valeurs humaines. Associé à <i>Human Compatible</i> (2019) de {_w('Stuart Russell', 'Stuart_J._Russell', 'en')}, au travail du {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, d'{_w('Anthropic', 'Anthropic', 'en')} et à l'effort de «&nbsp;{_w('superalignement', 'OpenAI', 'en')}&nbsp;» d'OpenAI. L'objection de Léon ne porte pas sur l'alignement mais sur la question à laquelle l'alignement seul ne peut répondre : <i>aligné sur les valeurs de qui</i> — et décidé par qui ?"
    },
    {
        "p": 115, "after": "transhumanisme",
        "note": f"Un {_w('mouvement intellectuel des XXe-XXIe siècles', 'Transhumanisme')} ({_w('Max More', 'Max_More', 'en')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}) qui exhorte à user des biotechnologies, de l'IA et d'autres outils pour dépasser les limites biologiques humaines — maladie, vieillissement, seuils cognitifs, voire la mortalité. Il hérite du progressisme des Lumières et de la cybernétique de l'après-guerre ; il a des assises institutionnelles dans la Silicon Valley et l'industrie de la longévité. Il traite le corps comme un matériel actualisable."
    },
    {
        "p": 115, "after": "posthumanisme",
        "note": f"Une généalogie intellectuelle différente. Le {_w('posthumanisme «&nbsp;critique&nbsp;»', 'Posthumanisme')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) descend de la philosophie continentale et de la théorie féministe. Il décentre l'humain — rejetant l'idée d'un sujet humain stable et autonome — et souligne notre enchevêtrement avec d'autres espèces, machines et écosystèmes. Tantôt allié, tantôt critique du transhumanisme ; les deux partagent la disposition à relativiser l'humain, mais pour des raisons très différentes."
    },
    {
        "p": 116, "after": "anthropocentrisme",
        "note": f"La {_w('conception', 'Anthropocentrisme')} selon laquelle les êtres humains se tiennent au centre de la considération morale. La tradition chrétienne a été historiquement anthropocentrique ; François l'a nuancée dans <i>Laudato si'</i> avec l'expression «&nbsp;anthropocentrisme situé&nbsp;» — les humains comme créatures insérées, non comme maîtres détachés. Le posthumanisme rejette l'anthropocentrisme plus nettement, le considérant comme une illusion des Lumières."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Psychiatre autrichien et survivant d\'Auschwitz', 'Viktor_Frankl')} (1905-1997). Son <i>{_w('Découvrir un sens à sa vie', 'Man%27s_Search_for_Meaning', 'en')}</i> soutenait que la pulsion humaine la plus profonde est la recherche de sens — une liberté qu'aucune condition, si inhumaine soit-elle, ne peut pleinement éteindre."
    },
    {
        "p": 122, "after": "Symphonie de Beethoven",
        "note": f"{_w('Créée en 1824', 'Symphonie_n°_9_de_Beethoven')} ; son final choral met en musique l'«&nbsp;{_w('Ode à la joie', 'Ode_à_la_joie')}&nbsp;» de Schiller, un hymne à la fraternité universelle. Adopté en 1985 comme hymne de l'Union européenne."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"Le {_w('tableau de 1937', 'Guernica_(Picasso)')} de {_w('Picasso', 'Pablo_Picasso')}, réalisé pour le pavillon espagnol de l'Exposition de Paris, représentant le bombardement nazi de la ville basque de Guernica pendant la guerre civile espagnole. Un monument de l'art contre la guerre."
    },
    {
        "p": 122, "after": "La Liste de Schindler",
        "note": f"Le {_w('film de 1993', 'La_Liste_de_Schindler')} de {_w('Steven Spielberg', 'Steven_Spielberg')} sur {_w('Oskar Schindler', 'Oskar_Schindler')}, l'industriel allemand qui sauva plus de mille travailleurs juifs polonais de l'extermination pendant la Shoah."
    },
    {
        "p": 123, "after": "Comité International de la Croix-Rouge",
        "note": f"{_w('Fondé à Genève en 1863', 'Comité_international_de_la_Croix-Rouge')} par {_w('Henry Dunant', 'Henry_Dunant')} après qu'il eut assisté au carnage de la {_w('bataille de Solférino', 'Bataille_de_Solférino')}. Sa neutralité opérationnelle — soigner les blessés de tous les camps — devint le germe du droit international humanitaire."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('Pasteur baptiste américain', 'Martin_Luther_King')} (1929-1968) et chef central du mouvement des droits civiques aux États-Unis, dont les campagnes non violentes contribuèrent à mettre fin à la ségrégation raciale légale."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('Leader sud-africain contre l\'apartheid', 'Nelson_Mandela')} (1918-2013), emprisonné 27 ans, puis président d'une Afrique du Sud post-apartheid. Son refus de la violence vindicative façonna le processus de {_w('Vérité et Réconciliation', 'Commission_de_la_vérité_et_de_la_réconciliation_(Afrique_du_Sud)')} du pays."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('Journaliste et militante américaine', 'Dorothy_Day')} (1897-1980), cofondatrice du {_w('Catholic Worker Movement', 'Catholic_Worker_Movement', 'en')}. Elle unit foi catholique, pauvreté volontaire, anarchisme et pacifisme ; elle vécut parmi les pauvres dans les maisons d'hospitalité de Manhattan. Cause de canonisation ouverte en 2000."
    },
    {
        "p": 125, "after": "Maximilien Marie Kolbe",
        "note": f"{_w('Frère franciscain conventuel polonais', 'Maximilien_Kolbe')} (1894-1941). À Auschwitz, il se porta volontaire pour prendre la place d'un codétenu condamné au bunker de la faim ; il mourut au bout de deux semaines. Canonisé en 1982 comme «&nbsp;martyr de la charité&nbsp;»."
    },
    {
        "p": 125, "after": "Oscar Romero",
        "note": f"{_w('Archevêque de San Salvador', 'Óscar_Romero')} (1917-1980), abattu à l'autel pendant qu'il célébrait la Messe pour avoir dénoncé à plusieurs reprises les escadrons de la mort et la répression militaire de la guerre civile salvadorienne. Canonisé en 2018."
    },
    {
        "p": 127, "after": "Thomas d’Aquin",
        "note": f"{_w('Théologien et philosophe dominicain du XIIIe siècle', 'Thomas_d\'Aquin')} (1225-1274). Sa <i>{_w('Somme théologique', 'Somme_théologique')}</i> est la plus influente synthèse de la théologie chrétienne dans l'Occident latin ; il enseigna que la grâce perfectionne la nature au lieu de la détruire."
    },
    {
        "p": 128, "after": "prométhéens",
        "note": f"Du mythe grec : {_w('Prométhée', 'Prométhée')} déroba le feu aux dieux pour le donner à l'humanité et fut puni éternellement. Dans la pensée moderne, la figure devint le patron de l'auto-affirmation technologique de l'homme — {_w('Mary Shelley', 'Mary_Shelley')} sous-titra <i>{_w('Frankenstein', 'Frankenstein_ou_le_Prométhée_moderne')}</i> «&nbsp;Le Prométhée moderne&nbsp;» ; Marx loua le «&nbsp;déchaînement prométhéen&nbsp;» des forces humaines ; {_w('Hans Jonas', 'Hans_Jonas')}, dans <i>Le Principe responsabilité</i> (1979), avertit que la technique moderne a enfin donné à l'ambition prométhéenne une portée divine sans une sagesse divine."
    },
    {
        "p": 130, "after": "Saint Augustin",
        "note": f"Dans <i>{_w('La Cité de Dieu', 'La_Cité_de_Dieu')}</i> (début du Ve siècle), Augustin lit toute l'histoire comme l'entrelacement de deux cités — terrestre et céleste — bâties par deux amours opposés. L'image donne son titre à ce chapitre et unifie le contraste de l'encyclique entre Babel et Jérusalem."
    },

    # ---------- CHAPITRE QUATRE ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Théoricienne politique germano-américaine', 'Hannah_Arendt')} (1906-1975). Ses <i>{_w('Origines du totalitarisme', 'Les_Origines_du_totalitarisme')}</i> (1951) et <i>{_w('Eichmann à Jérusalem', 'Eichmann_à_Jérusalem')}</i> (1963) montrèrent comment les régimes totalitaires dépendent de la dissolution de la distinction même entre fait et fiction."
    },
    {
        "p": 140, "after": "Platon",
        "note": f"{_w('Philosophe grec antique', 'Platon')} (v. 428-348 av. J.-C.). L'image de la compréhension qui s'allume comme une étincelle au fil d'une longue enquête partagée est tirée de sa {_w('Septième Lettre', 'Seventh_Letter', 'en')} — une défense de l'apprentissage lent et dialogique contre l'illusion du savoir rapide."
    },
    {
        "p": 148, "after": "saint Benoît de Nursie",
        "note": f"{_w('Fondateur du monachisme occidental au VIe siècle', 'Benoît_de_Nursie')} (v. 480-547). Sa <i>{_w('Règle', 'Règle_de_saint_Benoît')}</i> entrelaça prière et travail manuel — <i>ora et labora</i> — et bâtit la spiritualité du travail qui allait façonner la culture européenne pendant un millénaire."
    },
    {
        "p": 151, "after": "quatrième révolution industrielle",
        "note": f"{_w('Un terme popularisé par Klaus Schwab', 'Quatrième_révolution_industrielle')} (fondateur du {_w('Forum économique mondial', 'Forum_économique_mondial')}) pour la présente fusion de l'IA, de la robotique, de la biotechnologie et du monde physique — successeur des révolutions à vapeur, électrique et numérique qui l'ont précédée."
    },
    {
        "p": 163, "after": "main invisible",
        "note": f"La {_w('métaphore', 'Main_invisible')} d'{_w('Adam Smith', 'Adam_Smith')} (<i>La Richesse des nations</i>, 1776) : la poursuite de l'intérêt personnel dans un marché concurrentiel peut, involontairement, produire un bénéfice social. Léon rejoint une longue lignée de papes soutenant que ce mécanisme, à lui seul, ne peut gouverner une économie."
    },

    # ---------- CHAPITRE CINQ ----------
    {
        "p": 192, "after": "guerre juste",
        "note": f"La {_w('tradition chrétienne', 'Guerre_juste')} (Augustin, Thomas, Vitoria, Suárez) des conditions morales sous lesquelles la guerre peut être admissible — juste cause, autorité légitime, proportionnalité, dernier recours. François et maintenant Léon soutiennent que, sous les armes modernes, les critères ne peuvent plus être satisfaits."
    },
    {
        "p": 193, "after": "industrie de guerre",
        "note": f"Évoque le «&nbsp;complexe militaro-industriel&nbsp;», {_w('expression forgée par le président américain Dwight D. Eisenhower', 'Complexe_militaro-industriel')} dans son discours d'adieu de 1961, avertissant que les intérêts entremêlés des fabricants d'armes, des appareils militaires et politiques créeraient une poussée structurelle vers un état de guerre perpétuel — exactement l'inquiétude de Léon ici, soixante-cinq ans plus tard."
    },
    {
        "p": 194, "after": "Traité sur l’interdiction des armes nucléaires",
        "note": f"Un {_w('traité de l\'ONU de 2017', 'Traité_sur_l\'interdiction_des_armes_nucléaires')} entré en vigueur en janvier 2021. Il interdit catégoriquement de développer, tester, produire ou posséder des armes nucléaires. Le Saint-Siège fut parmi les premiers signataires ; les neuf États dotés d'armes nucléaires ont tous refusé d'y adhérer."
    },
    {
        "p": 198, "after": "agents moraux artificiels",
        "note": f"Un terme de la {_w('littérature sur l\'éthique des machines', 'Machine_ethics', 'en')} (Wendell Wallach et Colin Allen, <i>Moral Machines</i>, 2008) — la proposition que des systèmes d'IA suffisamment avancés pourraient être programmés pour porter eux-mêmes des jugements éthiques. L'encyclique répond par la vision classique : le jugement moral n'est pas un calcul mais la réponse d'une conscience à une personne, irréductible à toute machine suivant des règles."
    },
    {
        "p": 201, "after": "1989",
        "note": f"L'année de la chute du {_w('mur de Berlin', 'Mur_de_Berlin')} et de l'effondrement des régimes communistes en Europe centrale et orientale — marquant la fin de la {_w('guerre froide', 'Guerre_froide')} et le début de l'ère de la «&nbsp;mondialisation&nbsp;» que Léon critique ici."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Terme allemand du XIXe siècle', 'Realpolitik')} pour une politique conduite sur la base d'intérêts pratiques et matériels plutôt que d'idéologie ou de principe moral. Léon la considère comme une contrefaçon du réalisme politique authentique."
    },
    {
        "p": 213, "after": "Tolkien",
        "note": f"{_w('Auteur anglais', 'J._R._R._Tolkien')} (1892-1973), catholique fervent, créateur du <i>{_w('Seigneur des anneaux', 'Le_Seigneur_des_anneaux')}</i>. La citation est de Gandalf, dans <i>{_w('Le Retour du roi', 'Le_Retour_du_roi')}</i> : une vocation définie par le soin du lopin de terre qui nous a été confié."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Homme d\'État catholique italien', 'Giorgio_La_Pira')} (1904-1977), plusieurs fois maire de Florence et infatigable organisateur de conférences de paix de l'ère de la guerre froide, par-delà les lignes religieuses et idéologiques. Béatifié en 2018."
    },
    {
        "p": 222, "after": "manichéennes",
        "note": f"De {_w('Mani', 'Mani_(prophète)')} (216-276 apr. J.-C.), fondateur d'une {_w('religion dualiste perse', 'Manichéisme')} qui lisait l'histoire comme une bataille cosmique entre des forces égales et opposées de lumière et de ténèbres. {_w('Augustin', 'Augustin_d\'Hippone')} fut manichéen pendant neuf ans avant de se convertir ; sa théologie ultérieure du mal comme <i>privation</i> (une absence plutôt qu'une substance) fut construite contre ce dualisme. Le mot désigne aujourd'hui toute vision du monde qui partage nettement la réalité en camps du bien et du mal."
    },
    {
        "p": 223, "after": "esprit d’Assise",
        "note": f"Le 27 octobre 1986, Jean-Paul II réunit à Assise les chefs des religions du monde {_w('pour prier pour la paix', 'Day_of_Prayer_for_World_Peace', 'en')} — un précédent de construction interreligieuse de la paix que François renouvela plusieurs fois durant son pontificat."
    },
    {
        "p": 223, "after": "Grand Imam d’al-Azhar",
        "note": f"{_w('Ahmed el-Tayeb', 'Ahmed_el-Tayeb')}, chef de l'{_w('université-mosquée d\'al-Azhar', 'Université_al-Azhar')} du Caire (la principale autorité de l'islam sunnite). Lui et le pape François signèrent le {_w('Document sur la fraternité humaine de 2019', 'Document_on_Human_Fraternity', 'en')} à Abou Dabi."
    },

    # ---------- CONCLUSION ----------
    {
        "p": 230, "after": "Magnificat",
        "note": f"Le {_w('cantique de louange', 'Magnificat')} de {_w('Marie', 'Marie_(mère_de_Jésus)')} en Luc 1, 46-55, prié chaque jour aux Vêpres de l'Église : «&nbsp;Mon âme exalte le Seigneur… il renverse les puissants de leurs trônes et élève les humbles&nbsp;». Le titre de l'encyclique <i>Magnifica Humanitas</i> s'inspire de ce chant."
    },
    {
        "p": 233, "after": "récapitulation",
        "note": f"Du grec <i>anakephalaiôsis</i>, «&nbsp;récapituler sous un chef&nbsp;» (Ep 1, 10). Le Père ancien {_w('Irénée', 'Irénée_de_Lyon')} en fit l'image centrale du salut : le Christ rassemble en lui toute la création, chaque fragment et chaque blessure."
    },
    {
        "p": 234, "after": "saint Augustin",
        "note": f"Le passage cité est du {_w('Sermon 272 d\'Augustin', 'Sermon_272', 'en')}, prêché aux chrétiens nouvellement baptisés sur l'Eucharistie : «&nbsp;Soyez ce que vous voyez et recevez ce que vous êtes&nbsp;». Une affirmation frappante de la théologie patristique selon laquelle l'Église <i>est</i> le corps du Christ — non simplement une société qui se rassemble autour de lui."
    },
    {
        "p": 237, "after": "anthropocentrisme situé",
        "note": f"Expression de François dans <i>{_w('Laudato si', 'Laudato_si\'')}'</i> (§118) : une correction délibérée de l'anthropocentrisme des Lumières. Les humains restent moralement centraux, mais comme créatures insérées dans un réseau de vie plus large et dépendantes de lui — non comme sujets détachés placés au-dessus d'une nature inerte. L'invocation de Léon ici ferme un cercle ouvert dans la discussion du Chapitre Trois sur le transhumanisme : l'alternative à «&nbsp;laisser l'humain derrière soi&nbsp;» n'est pas d'introniser l'humain, mais de nous replacer dans notre compagnie créaturelle."
    },
]
