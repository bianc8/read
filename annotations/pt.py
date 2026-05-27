"""Anotações editoriais em português para Magnifica Humanitas.

Tradução das anotações de ``annotations/en.py``. Cada entrada ancora uma nota
de margem a um ponto do parágrafo, fazendo corresponder um fragmento de texto
exato (``after``) da tradução oficial portuguesa. As ligações apontam para a
Wikipédia em português quando o título é conhecido, caso contrário para a
inglesa (``lang="en"``).
"""


def _w(text: str, page: str, lang: str = "pt") -> str:
    return (f'<a href="https://{lang}.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- INTRODUÇÃO ----------
    {
        "p": 3, "after": "Rerum novarum",
        "note": f"A encíclica de 1891 de {_w('Leão XIII', 'Papa_Leão_XIII')}, documento fundador da moderna {_w('Doutrina social católica', 'Doutrina_social_da_Igreja')}, escrita em resposta aos abalos do capitalismo industrial. O título é latim e significa <i>{_w('das coisas novas', 'Rerum_novarum')}</i>. Leão XIV evoca deliberadamente o nome e o projeto do seu predecessor."
    },
    {
        "p": 3, "after": "Doutrina social da Igreja",
        "note": f"Um corpo coerente de ensinamento pontifício e conciliar sobre a vida social, económica e política, desenvolvido a partir de Leão XIII. Os seus princípios fundamentais — dignidade, bem comum, subsidiariedade, solidariedade, justiça — repetem-se ao longo de toda a carta. Ver: {_w('Doutrina social da Igreja', 'Doutrina_social_da_Igreja')}."
    },
    {
        "p": 4, "after": "«novas questões»",
        "note": f"<i>Res novae</i> em latim — a expressão de que <i>{_w('Rerum novarum', 'Rerum_novarum')}</i> toma o nome. Leão XIV usa-a para designar as pressões autenticamente novas que cada geração enfrenta."
    },
    {
        "p": 7, "after": "torre de Babel",
        "note": f"{_w('Génesis 11, 1-9', 'Torre_de_Babel')}. Homens que falam uma única língua propõem-se construir uma torre «cujo cimo atinja os céus» para se fazerem um nome; Deus dispersa-os confundindo a sua fala. Uma perene parábola cristã da soberba e da fragmentação que se segue quando o agir humano esquece Deus."
    },
    {
        "p": 7, "after": "reconstrução das muralhas de Jerusalém",
        "note": f"O {_w('Livro de Neemias', 'Livro_de_Neemias')} (séc. V a.C.) narra os exilados judeus que regressam da {_w('Babilónia', 'Cativeiro_da_Babilónia')} para reconstruir uma Jerusalém em ruínas. Neemias organiza o trabalho família por família, ouve as queixas e enfrenta a oposição. Leão apresenta-o como modelo de reparação distribuída e coordenada — o oposto da unificação imposta de cima de Babel."
    },
    {
        "p": 10, "after": "sinodalidade",
        "note": f"Do grego <i>syn-hodos</i>, «caminhar juntos». Uma prática que {_w('Papa Francisco', 'Papa_Francisco')} tornou central: decisões eclesiais alcançadas através de uma ampla escuta e de um discernimento partilhado, e não por decreto vindo de cima. Ver: {_w('sinodalidade', 'Sinodalidade')}."
    },
    {
        "p": 11, "after": "Santo Agostinho",
        "note": f"{_w('Agostinho de Hipona', 'Agostinho_de_Hipona')} (354-430), bispo e filósofo norte-africano, um dos pensadores mais influentes do cristianismo ocidental. O «coração inquieto» é o início das suas <i>{_w('Confissões', 'Confissões_(Agostinho)')}</i>, a sua oração autobiográfica."
    },
    {
        "p": 13, "after": "subsidiariedade",
        "note": f"Princípio social católico: as decisões competem ao nível mais pequeno e local capaz de as tomar; as autoridades superiores existem para <i>apoiar</i> (subsidium) as inferiores, não para as substituir. Sistematizado pela primeira vez por {_w('Pio XI', 'Papa_Pio_XI')} em 1931. Ver: {_w('subsidiariedade', 'Subsidiariedade')}."
    },
    {
        "p": 15, "after": "Jubileu Ordinário de 2025",
        "note": f"Na tradição católica, o {_w('Jubileu', 'Jubileu_(cristianismo)')} é um ano de peregrinação, misericórdia e perdão, celebrado de 25 em 25 anos. O Jubileu de 2025 foi aberto por {_w('Papa Francisco', 'Papa_Francisco')} com o tema «Peregrinos de esperança»."
    },

    # ---------- CAPÍTULO PRIMEIRO ----------
    {
        "p": 17, "after": "Magistério",
        "note": f"A {_w('autoridade de ensino', 'Magistério')} oficial da Igreja católica, exercida pelo Papa e pelos bispos em comunhão com ele. A palavra vem do latim <i>magister</i>, «mestre»."
    },
    {
        "p": 20, "after": "Gaudium et spes",
        "note": f"«Alegria e esperança» — a Constituição pastoral de 1965 do {_w('Concílio Vaticano II', 'Concílio_Vaticano_II')} sobre a Igreja no mundo contemporâneo. As suas palavras de abertura («As alegrias e as esperanças, as tristezas e as angústias dos homens de hoje… são também as alegrias e as esperanças… dos discípulos de Cristo») redefiniram a relação da Igreja com a vida secular. Ver: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Compêndio da Doutrina Social da Igreja",
        "note": f"Um {_w('texto de referência do Vaticano de 2004', 'Compendium_of_the_Social_Doctrine_of_the_Church', 'en')} que reúne e sistematiza o ensinamento social da Igreja de Leão XIII a João Paulo II. Muitas vezes a primeira etapa para localizar onde um princípio foi formulado."
    },
    {
        "p": 28, "after": "Laudato si",
        "note": f"{_w('A encíclica de 2015 do Papa Francisco', 'Laudato_si%27')} sobre o cuidado da «casa comum» — a crise ambiental lida como inseparável da pobreza e da desigualdade. O título vem do Cântico das criaturas de {_w('São Francisco de Assis', 'Francisco_de_Assis')} («Louvado sejas, meu Senhor»)."
    },
    {
        "p": 28, "after": "Fratelli tutti",
        "note": f"{_w('A encíclica de 2020 do Papa Francisco', 'Fratelli_tutti')} sobre a fraternidade e a amizade social. O título é de {_w('São Francisco de Assis', 'Francisco_de_Assis')}: «Todos irmãos»."
    },
    {
        "p": 30, "after": "Magna Charta",
        "note": f"Lit. «Grande Carta» — o {_w('documento inglês de 1215', 'Magna_Carta')} fundador do governo constitucional. Pio XI usa-a metaforicamente para chamar à <i>Rerum novarum</i> a carta fundadora da ação social católica."
    },
    {
        "p": 31, "after": "Quadragesimo anno",
        "note": f"«No quadragésimo ano» — {_w('a encíclica de 1931 de Pio XI', 'Quadragesimo_anno')}, escrita no 40.º aniversário da <i>Rerum novarum</i> em plena {_w('Grande Depressão', 'Grande_Depressão')}. Introduziu o princípio da subsidiariedade na sua forma moderna."
    },
    {
        "p": 32, "after": "direito natural",
        "note": f"Uma {_w('tradição filosófica', 'Direito_natural')} que vai da {_w('Roma estoica', 'Estoicismo')} a {_w('Tomás de Aquino', 'Tomás_de_Aquino')}: existe uma ordem moral objetiva, acessível à razão humana, anterior e independente de qualquer autoridade humana. A Doutrina social católica nela funda os direitos humanos universais; o sistema internacional de direitos do pós-guerra bebeu da mesma corrente. A alternativa — que os direitos sejam apenas aquilo que os poderosos estão dispostos a conceder — é precisamente o que o pensamento jusnaturalista é construído para recusar."
    },
    {
        "p": 33, "after": "Mater et magistra",
        "note": f"«Mãe e mestra» — {_w('a encíclica de 1961', 'Mater_et_magistra')} de {_w('João XXIII', 'Papa_João_XXIII')} que atualiza a Doutrina social católica para o mundo do pós-guerra."
    },
    {
        "p": 33, "after": "Pacem in terris",
        "note": f"«Paz na terra» — {_w('a encíclica de 1963 de João XXIII', 'Pacem_in_terris')}, escrita poucos meses após a {_w('crise dos mísseis de Cuba', 'Crise_dos_mísseis_de_Cuba')}. A primeira encíclica dirigida a «todos os homens de boa vontade», e não apenas aos católicos."
    },
    {
        "p": 34, "after": "Dignitatis humanae",
        "note": f"«Da dignidade humana» — a {_w('Declaração sobre a liberdade religiosa de 1965', 'Dignitatis_humanae')} do Vaticano II, que comprometeu formalmente a Igreja a defender o direito civil de cada pessoa à liberdade religiosa."
    },
    {
        "p": 35, "after": "Populorum progressio",
        "note": f"«O desenvolvimento dos povos» — {_w('a encíclica de 1967', 'Populorum_progressio')} de {_w('Paulo VI', 'Papa_Paulo_VI')}, que definiu o próprio desenvolvimento como «o novo nome da paz» e orientou a Doutrina social católica para a desigualdade global."
    },
    {
        "p": 35, "after": "Pontifícia Comissão Iustitia et Pax",
        "note": f"«Justiça e Paz» — o organismo do Vaticano que Paulo VI instituiu em 1967 para traduzir a Doutrina social católica em trabalho de política internacional. Reorganizado em 2017 como {_w('Dicastério para o Serviço do Desenvolvimento Humano Integral', 'Dicastery_for_Promoting_Integral_Human_Development', 'en')}."
    },
    {
        "p": 36, "after": "Octogesima adveniens",
        "note": f"«O octogésimo que vem» — a {_w('carta apostólica de 1971', 'Octogesima_adveniens')} de Paulo VI no 80.º aniversário da <i>Rerum novarum</i>, sobre a urbanização e os limites de qualquer resposta católica única às questões políticas."
    },
    {
        "p": 36, "after": "estruturas de pecado",
        "note": f"Expressão de {_w('João Paulo II', 'Papa_João_Paulo_II')} (na <i>{_w('Sollicitudo rei socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) para os arranjos sociais, económicos e políticos que institucionalizam a injustiça. A expressão desloca o pecado dos atos puramente individuais para os sistemas em que participamos. Ver: {_w('pecado estrutural', 'Structural_sin', 'en')}."
    },
    {
        "p": 37, "after": "Laborem exercens",
        "note": f"«Realizando o trabalho» — {_w('a encíclica de 1981 de João Paulo II', 'Laborem_exercens')} sobre o trabalho humano. Sustentou que o trabalho não é apenas uma mercadoria, mas uma dimensão fundamental da vida humana e a chave de toda a questão social."
    },
    {
        "p": 38, "after": "Sollicitudo rei socialis",
        "note": f"«A solicitude pelas coisas sociais» — {_w('a encíclica de 1987 de João Paulo II', 'Sollicitudo_rei_socialis')} que revisita a <i>Populorum progressio</i> de Paulo VI vinte anos depois, centrada no fosso crescente entre nações ricas e pobres."
    },
    {
        "p": 38, "after": "civilização do amor",
        "note": f"Expressão cunhada por {_w('Paulo VI', 'Papa_Paulo_VI')} em 1975: uma visão da ordem social em que a caridade, e não o poder, é o princípio organizador da economia, da política e da cultura. Torna-se o tema unificador do Capítulo Quinto."
    },
    {
        "p": 39, "after": "Centesimus annus",
        "note": f"«O centésimo ano» — {_w('a encíclica de 1991 de João Paulo II', 'Centesimus_annus')} no centenário da <i>Rerum novarum</i>, escrita após a queda do comunismo. Reconhece a economia de mercado apenas na medida em que permaneça subordinada à lei moral e à solidariedade."
    },
    {
        "p": 40, "after": "Caritas in veritate",
        "note": f"«A caridade na verdade» — {_w('a encíclica de 2009', 'Caritas_in_veritate')} de {_w('Bento XVI', 'Papa_Bento_XVI')} sobre o desenvolvimento humano integral, escrita durante a crise financeira global."
    },
    {
        "p": 42, "after": "Evangelii gaudium",
        "note": f"«A alegria do Evangelho» — {_w('a exortação apostólica de 2013 do Papa Francisco', 'Evangelii_gaudium')}, o documento programático do seu pontificado."
    },
    {
        "p": 44, "after": "Dilexit nos",
        "note": f"«Ele amou-nos» — {_w('a encíclica de 2024 do Papa Francisco', 'Dilexit_nos')} sobre a devoção ao {_w('Sagrado Coração de Jesus', 'Sagrado_Coração_de_Jesus')}, a sua última grande carta doutrinal."
    },

    # ---------- CAPÍTULO SEGUNDO ----------
    {
        "p": 50, "after": "Deus trinitário",
        "note": f"A doutrina cristã central da {_w('Trindade', 'Santíssima_Trindade')}: um só Deus em três pessoas — Pai, Filho e Espírito Santo — eternamente unidos no amor. É esta doutrina que torna o pensamento social católico relacional na sua raiz."
    },
    {
        "p": 52, "after": "dignidade ontológica",
        "note": f"Do grego <i>on</i>, «ser» — a dignidade que pertence a uma pessoa em virtude do <i>ser</i>, e não do fazer, do ter ou do ser reconhecida. A distinção é {_w('aristotélico-tomista', 'Tomismo')}: o valor de uma pessoa decorre daquilo que fundamentalmente é (<i>esse</i>), e não de propriedades variáveis como a capacidade, o êxito ou a posição social."
    },
    {
        "p": 53, "after": "Dignitas infinita",
        "note": f"«Dignidade infinita» — uma {_w('declaração de 2024', 'Dignitas_infinita')} do Dicastério para a Doutrina da Fé do Vaticano que afirma a dignidade incondicional de cada pessoa humana contra uma longa lista de violações contemporâneas."
    },
    {
        "p": 54, "after": "Declaração Universal dos Direitos do Homem",
        "note": f"{_w('Adotada pela Assembleia Geral da ONU', 'Declaração_Universal_dos_Direitos_Humanos')} a 10 de dezembro de 1948, no rescaldo da Segunda Guerra Mundial. A primeira formulação global dos direitos que pertencem a cada pessoa «simplesmente por ser humana»."
    },
    {
        "p": 60, "after": "bem comum",
        "note": f"Um {_w('conceito', 'Bem_comum')} com raízes filosóficas profundas em {_w('Aristóteles', 'Aristóteles')} (<i>Política</i>, Livro III) e {_w('Tomás de Aquino', 'Tomás_de_Aquino')}. Crucialmente, <i>não</i> é a soma das preferências individuais (a redução utilitarista) nem meros bens «públicos» como o ar limpo; é o conjunto partilhado de condições em que cada pessoa pode florescer. É o conceito que distingue o pensamento social católico tanto do puro individualismo como do puro coletivismo."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Latim para «coisa pública» — a {_w('comunidade política', 'Res_publica')}, o interesse partilhado de todos os cidadãos. Raiz da palavra <i>república</i>."
    },
    {
        "p": 82, "after": "desenvolvimento humano integral",
        "note": f"{_w('Expressão cunhada por Paulo VI', 'Integral_human_development', 'en')} (<i>Populorum progressio</i>, 1967): desenvolvimento de <i>cada</i> pessoa e de <i>toda</i> a pessoa — material, cultural, moral, espiritual. O critério pelo qual o ensinamento católico avalia qualquer modelo económico."
    },
    {
        "p": 86, "after": "exame de consciência",
        "note": f"Uma prática espiritual católica tradicional — {_w('uma revisão metódica de si diante de Deus', 'Exame_de_consciência')} — derivada em particular do <i>examen</i> {_w('inaciano', 'Espiritualidade_inaciana')}. Aqui Leão transforma-a de disciplina pessoal em disciplina comunitária para a própria Igreja."
    },

    # ---------- CAPÍTULO TERCEIRO ----------
    {
        "p": 92, "after": "paradigma tecnocrático",
        "note": f"Expressão do Papa Francisco na <i>Laudato si'</i> (2015), herdada de {_w('Romano Guardini', 'Romano_Guardini')} e em ressonância com a crítica da técnica moderna de {_w('Heidegger', 'Martin_Heidegger')}. Não o entusiasmo por engenhocas, mas o hábito mental mais profundo que trata <i>tudo</i> — natureza, pessoas, instituições — como matéria-prima a medir, otimizar e controlar. O paradigma reduz o ser a função e o valor a utilidade."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Sacerdote e filósofo católico italo-alemão', 'Romano_Guardini')} (1885-1968). A sua obra <i>O fim da época moderna</i> alertava que o poder técnico tinha ultrapassado a formação moral e espiritual necessária para o exercer. Influência formadora no Vaticano II e na <i>Laudato si'</i> de Francisco."
    },
    {
        "p": 107, "after": "alinhamento",
        "note": f"Termo central da contemporânea {_w('segurança da IA', 'AI_alignment', 'en')}: o projeto de fazer com que os sistemas de IA prossigam objetivos coerentes com os valores humanos. Associado a <i>Human Compatible</i> (2019) de {_w('Stuart Russell', 'Stuart_J._Russell', 'en')}, ao trabalho do {_w('MIRI', 'Machine_Intelligence_Research_Institute', 'en')}, da {_w('Anthropic', 'Anthropic', 'en')} e ao esforço de «{_w('superalinhamento', 'OpenAI', 'en')}» da OpenAI. A objeção de Leão não é ao alinhamento, mas à pergunta a que o alinhamento, por si só, não pode responder: <i>alinhado com os valores de quem</i> — e decidido por quem?"
    },
    {
        "p": 115, "after": "transumanismo",
        "note": f"Um {_w('movimento intelectual dos séculos XX-XXI', 'Transumanismo')} ({_w('Max More', 'Max_More', 'en')}, {_w('FM-2030', 'FM-2030', 'en')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}) que exorta a usar a biotecnologia, a IA e outras ferramentas para superar os limites biológicos humanos — doença, envelhecimento, limiares cognitivos, mesmo a mortalidade. Herda o progressismo iluminista e a cibernética do pós-guerra; tem sedes institucionais no Silicon Valley e na indústria da longevidade. Trata o corpo como hardware atualizável."
    },
    {
        "p": 115, "after": "pós-humanismo",
        "note": f"Uma genealogia intelectual diferente. O {_w('pós-humanismo «crítico»', 'Pós-humanismo')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti', 'en')}, {_w('Karen Barad', 'Karen_Barad', 'en')}) descende da filosofia continental e da teoria feminista. Descentra o humano — rejeitando a ideia de um sujeito humano estável e autónomo — e sublinha o nosso entrelaçamento com outras espécies, máquinas e ecossistemas. Por vezes aliado e por vezes crítico do transumanismo; os dois partilham a disponibilidade para relativizar o humano, mas por razões muito diferentes."
    },
    {
        "p": 116, "after": "antropocentrismo",
        "note": f"A {_w('conceção', 'Antropocentrismo')} segundo a qual os seres humanos estão no centro da consideração moral. A tradição cristã foi historicamente antropocêntrica; Francisco precisou-a na <i>Laudato si'</i> com a expressão «antropocentrismo situado» — os seres humanos como criaturas inseridas, não como senhores distantes. O pós-humanismo rejeita o antropocentrismo de modo mais nítido, considerando-o uma ilusão iluminista."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Psiquiatra austríaco e sobrevivente de Auschwitz', 'Viktor_Frankl')} (1905-1997). O seu <i>{_w('Em Busca de Sentido', 'Man%27s_Search_for_Meaning', 'en')}</i> sustentava que o impulso humano mais profundo é a busca de sentido — uma liberdade que nenhuma condição, por mais desumana, pode extinguir por completo."
    },
    {
        "p": 122, "after": "Nona Sinfonia de Beethoven",
        "note": f"{_w('Estreada em 1824', 'Sinfonia_n.º_9_(Beethoven)')}; o seu final coral entoa o «{_w('Hino à Alegria', 'Ode_an_die_Freude')}» de Schiller, um canto à fraternidade universal. Adotado em 1985 como hino da União Europeia."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"O {_w('quadro de 1937', 'Guernica_(Picasso)')} de {_w('Picasso', 'Pablo_Picasso')}, realizado para o Pavilhão Espanhol da Exposição de Paris, que retrata o bombardeamento nazi da cidade basca de Guernica durante a Guerra Civil de Espanha. Um monumento da arte contra a guerra."
    },
    {
        "p": 122, "after": "A Lista de Schindler",
        "note": f"O {_w('filme de 1993', 'A_Lista_de_Schindler')} de {_w('Steven Spielberg', 'Steven_Spielberg')} sobre {_w('Oskar Schindler', 'Oskar_Schindler')}, o industrial alemão que salvou mais de mil trabalhadores judeus polacos do extermínio durante o Holocausto."
    },
    {
        "p": 123, "after": "Comité Internacional da Cruz Vermelha",
        "note": f"{_w('Fundado em Genebra em 1863', 'Comité_Internacional_da_Cruz_Vermelha')} por {_w('Henry Dunant', 'Henry_Dunant')} depois de ter assistido à carnificina da {_w('batalha de Solferino', 'Batalha_de_Solferino')}. A sua neutralidade operacional — cuidar dos feridos de todos os lados — tornou-se a semente do direito internacional humanitário."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('Pastor batista norte-americano', 'Martin_Luther_King_Jr.')} (1929-1968) e líder central do movimento pelos direitos civis nos EUA, cujas campanhas não violentas ajudaram a pôr fim à segregação racial legal."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('Líder sul-africano contra o apartheid', 'Nelson_Mandela')} (1918-2013), preso durante 27 anos, depois presidente de uma África do Sul pós-apartheid. A sua recusa da violência vingativa moldou o processo de {_w('Verdade e Reconciliação', 'Comissão_da_Verdade_e_Reconciliação_(África_do_Sul)')} do país."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('Jornalista e ativista norte-americana', 'Dorothy_Day')} (1897-1980), cofundadora do {_w('Catholic Worker Movement', 'Catholic_Worker_Movement', 'en')}. Uniu fé católica, pobreza voluntária, anarquismo e pacifismo; viveu entre os pobres nas casas de hospitalidade de Manhattan. Causa de canonização aberta em 2000."
    },
    {
        "p": 125, "after": "Maximiliano Maria Kolbe",
        "note": f"{_w('Frade franciscano conventual polaco', 'Maximiliano_Maria_Kolbe')} (1894-1941). Em Auschwitz, ofereceu-se para tomar o lugar de um companheiro de prisão condenado ao bunker da fome; morreu ao fim de duas semanas. Canonizado em 1982 como «mártir da caridade»."
    },
    {
        "p": 125, "after": "Óscar Romero",
        "note": f"{_w('Arcebispo de San Salvador', 'Óscar_Romero')} (1917-1980), morto ao altar enquanto celebrava a Missa por ter denunciado repetidamente os esquadrões da morte e a repressão militar na guerra civil salvadorenha. Canonizado em 2018."
    },
    {
        "p": 127, "after": "São Tomás de Aquino",
        "note": f"{_w('Teólogo e filósofo dominicano do séc. XIII', 'Tomás_de_Aquino')} (1225-1274). A sua <i>{_w('Summa Theologiae', 'Suma_Teológica')}</i> é a mais influente síntese da teologia cristã no Ocidente latino; ensinou que a graça aperfeiçoa a natureza em vez de a destruir."
    },
    {
        "p": 128, "after": "prometeicos",
        "note": f"Do mito grego: {_w('Prometeu', 'Prometeu')} roubou o fogo aos deuses para o dar à humanidade e foi punido eternamente. No pensamento moderno, a figura tornou-se o patrono da autoafirmação tecnológica do homem — {_w('Mary Shelley', 'Mary_Shelley')} subtitulou <i>{_w('Frankenstein', 'Frankenstein')}</i> «O Prometeu moderno»; Marx louvou o «desencadeamento prometeico» das forças humanas; {_w('Hans Jonas', 'Hans_Jonas')}, em <i>O princípio responsabilidade</i> (1979), alertou que a técnica moderna deu finalmente à ambição prometeica um alcance divino sem uma sabedoria divina."
    },
    {
        "p": 130, "after": "Santo Agostinho",
        "note": f"Na <i>{_w('Cidade de Deus', 'A_Cidade_de_Deus')}</i> (início do séc. V), Agostinho lê toda a história como o entrelaçamento de duas cidades — terrena e celeste — construídas por dois amores opostos. A imagem dá o título a este capítulo e unifica o contraste da encíclica entre Babel e Jerusalém."
    },

    # ---------- CAPÍTULO QUARTO ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('Teórica política teuto-americana', 'Hannah_Arendt')} (1906-1975). As suas <i>{_w('Origens do Totalitarismo', 'As_Origens_do_Totalitarismo')}</i> (1951) e <i>{_w('Eichmann em Jerusalém', 'Eichmann_em_Jerusalém')}</i> (1963) mostraram como os regimes totalitários dependem de dissolver a própria distinção entre facto e ficção."
    },
    {
        "p": 140, "after": "Platão",
        "note": f"{_w('Filósofo grego antigo', 'Platão')} (c. 428-348 a.C.). A imagem da compreensão que se acende como uma centelha através de uma longa investigação partilhada é tirada da sua {_w('Sétima Carta', 'Seventh_Letter', 'en')} — uma defesa da aprendizagem lenta e dialógica contra a ilusão do saber rápido."
    },
    {
        "p": 148, "after": "São Bento de Núrsia",
        "note": f"{_w('Fundador do monaquismo ocidental do séc. VI', 'Bento_de_Núrsia')} (c. 480-547). A sua <i>{_w('Regra', 'Regra_de_São_Bento')}</i> entrelaçou oração e trabalho manual — <i>ora et labora</i> — e construiu a espiritualidade do trabalho que viria a moldar a cultura europeia durante um milénio."
    },
    {
        "p": 151, "after": "quarta revolução industrial",
        "note": f"{_w('Termo tornado popular por Klaus Schwab', 'Quarta_Revolução_Industrial')} (fundador do {_w('Fórum Económico Mundial', 'Fórum_Económico_Mundial')}) para a presente fusão de IA, robótica, biotecnologia e mundo físico — sucessora das revoluções a vapor, elétrica e digital que a precederam."
    },
    {
        "p": 163, "after": "mão invisível",
        "note": f"A {_w('metáfora', 'Mão_invisível')} de {_w('Adam Smith', 'Adam_Smith')} (<i>A Riqueza das Nações</i>, 1776): a busca do interesse pessoal num mercado concorrencial pode, involuntariamente, produzir benefício social. Leão junta-se a uma longa fila de pontífices ao sustentar que este mecanismo, por si só, não pode governar uma economia."
    },

    # ---------- CAPÍTULO QUINTO ----------
    {
        "p": 192, "after": "guerra justa",
        "note": f"A {_w('tradição cristã', 'Guerra_justa')} (Agostinho, Tomás, Vitória, Suárez) das condições morais em que a guerra pode ser admissível — justa causa, autoridade legítima, proporcionalidade, último recurso. Francisco e agora Leão sustentam que, sob o armamento moderno, tais critérios já não podem ser cumpridos."
    },
    {
        "p": 193, "after": "indústria bélica",
        "note": f"Evoca o «complexo militar-industrial», {_w('expressão cunhada pelo presidente dos EUA Dwight D. Eisenhower', 'Complexo_militar-industrial')} no seu discurso de despedida de 1961, que alertava que os interesses entrelaçados dos fabricantes de armas, dos aparelhos militares e políticos criariam um impulso estrutural para um estado de guerra perpétua — exatamente a preocupação de Leão aqui, sessenta e cinco anos depois."
    },
    {
        "p": 194, "after": "Tratado sobre a proibição de armas nucleares",
        "note": f"Um {_w('tratado da ONU de 2017', 'Tratado_sobre_a_Proibição_das_Armas_Nucleares')} que entrou em vigor em janeiro de 2021. Proíbe categoricamente desenvolver, testar, produzir ou possuir armas nucleares. A Santa Sé foi dos primeiros signatários; os nove Estados dotados de armas nucleares recusaram todos aderir."
    },
    {
        "p": 198, "after": "agentes morais artificiais",
        "note": f"Um termo da {_w('literatura sobre ética das máquinas', 'Machine_ethics', 'en')} (Wendell Wallach e Colin Allen, <i>Moral Machines</i>, 2008) — a proposta de que sistemas de IA suficientemente avançados possam ser programados para formular juízos éticos por si próprios. A encíclica responde com a visão clássica: o juízo moral não é um cálculo, mas a resposta de uma consciência a uma pessoa, irredutível a qualquer máquina que siga regras."
    },
    {
        "p": 201, "after": "1989",
        "note": f"O ano da queda do {_w('Muro de Berlim', 'Muro_de_Berlim')} e do colapso dos regimes comunistas na Europa central e oriental — que marca o fim da {_w('Guerra Fria', 'Guerra_Fria')} e o início da era da «globalização» que Leão critica aqui."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('Termo alemão do séc. XIX', 'Realpolitik')} para uma política conduzida com base em interesses práticos e materiais em vez de ideologia ou princípio moral. Leão considera-a uma contrafação do genuíno realismo político."
    },
    {
        "p": 213, "after": "Tolkien",
        "note": f"{_w('Autor inglês', 'J._R._R._Tolkien')} (1892-1973), católico devoto, criador de <i>{_w('O Senhor dos Anéis', 'O_Senhor_dos_Anéis')}</i>. A citação é de Gandalf, em <i>{_w('O Regresso do Rei', 'O_Regresso_do_Rei')}</i>: uma vocação definida pelo cultivo do pedaço de terra que nos foi confiado."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Estadista católico italiano', 'Giorgio_La_Pira')} (1904-1977), várias vezes presidente da câmara de Florença e incansável organizador de conferências de paz da era da Guerra Fria, através de linhas religiosas e ideológicas. Beatificado em 2018."
    },
    {
        "p": 222, "after": "maniqueístas",
        "note": f"De {_w('Mani', 'Mani_(profeta)')} (216-276 d.C.), fundador de uma {_w('religião dualista persa', 'Maniqueísmo')} que lia a história como uma batalha cósmica entre forças iguais e opostas de luz e trevas. {_w('Agostinho', 'Agostinho_de_Hipona')} foi maniqueu durante nove anos antes de se converter; a sua posterior teologia do mal como <i>privação</i> (uma ausência e não uma substância) foi construída contra este dualismo. A palavra designa hoje qualquer visão do mundo que divida nitidamente a realidade em campos do bem e do mal."
    },
    {
        "p": 223, "after": "espírito de Assis",
        "note": f"A 27 de outubro de 1986, João Paulo II reuniu em Assis os líderes das religiões do mundo {_w('para rezar pela paz', 'Day_of_Prayer_for_World_Peace', 'en')} — um precedente de construção inter-religiosa da paz que Francisco renovou várias vezes durante o seu pontificado."
    },
    {
        "p": 223, "after": "Grande Imã de al-Azhar",
        "note": f"{_w('Ahmed al-Tayeb', 'Ahmed_al-Tayeb')}, chefe da {_w('universidade-mesquita de al-Azhar', 'Al-Azhar_University', 'en')} do Cairo (a principal autoridade do islão sunita). Ele e o Papa Francisco assinaram o {_w('Documento sobre a Fraternidade Humana de 2019', 'Document_on_Human_Fraternity', 'en')} em Abu Dhabi."
    },

    # ---------- CONCLUSÃO ----------
    {
        "p": 230, "after": "Magnificat",
        "note": f"O {_w('cântico de louvor', 'Magnificat')} de {_w('Maria', 'Maria_(mãe_de_Jesus)')} em Lucas 1, 46-55, rezado todos os dias nas Vésperas da Igreja: «A minha alma engrandece o Senhor… derrubou os poderosos dos seus tronos e exaltou os humildes». O título da encíclica <i>Magnifica Humanitas</i> inspira-se neste cântico."
    },
    {
        "p": 233, "after": "recapitulação",
        "note": f"Do grego <i>anakephalaíōsis</i>, «recapitular sob uma cabeça» (Ef 1, 10). O Padre antigo {_w('Ireneu', 'Ireneu_de_Lião')} fez dela a imagem central da salvação: Cristo reúne em si toda a criação, cada fragmento e cada ferida."
    },
    {
        "p": 234, "after": "Santo Agostinho",
        "note": f"A passagem citada é do {_w('Sermão 272 de Agostinho', 'Sermon_272', 'en')}, pregado aos cristãos recém-batizados sobre a Eucaristia: «Sede o que vedes e recebei o que sois». Uma afirmação marcante da teologia patrística segundo a qual a Igreja <i>é</i> o corpo de Cristo — e não simplesmente uma sociedade que se reúne em torno dele."
    },
    {
        "p": 237, "after": "antropocentrismo situado",
        "note": f"Expressão de Francisco na <i>{_w('Laudato si', 'Laudato_si%27')}'</i> (§118): uma correção deliberada do antropocentrismo iluminista. Os seres humanos permanecem moralmente centrais, mas como criaturas inseridas numa mais ampla teia de vida e dela dependentes — não como sujeitos distantes postos acima de uma natureza inerte. A invocação de Leão aqui fecha um círculo aberto na discussão sobre o transumanismo do Capítulo Terceiro: a alternativa a «deixar para trás o humano» não é entronizar o humano, mas recolocar-nos na nossa companhia de criaturas."
    },
]
