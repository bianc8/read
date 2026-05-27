"""Editorial annotations for Magnifica Humanitas.

Each entry attaches a margin note to a particular paragraph by matching an exact
text snippet (``after``). The marker is inserted right after the *first* occurrence
of that snippet in the paragraph; for a later occurrence set ``occurrence``.

These are editorial — not citations from Pope Leo XIV — and appear in the right
margin in slate-blue with lettered labels (a, b, c …). Proper nouns and
substantial concepts link out to Wikipedia in a new tab.
"""

# Small convenience so the long URL pattern stays readable below.
def _w(text: str, page: str) -> str:
    return (f'<a href="https://en.wikipedia.org/wiki/{page}" '
            f'target="_blank" rel="noopener noreferrer">{text}</a>')


ANNOTATIONS: list[dict] = [

    # ---------- INTRODUCTION ----------
    {
        "p": 3, "after": "Rerum Novarum",
        "note": f"{_w('Leo XIII', 'Pope_Leo_XIII')}'s 1891 encyclical, the founding document of modern {_w('Catholic Social Teaching', 'Catholic_social_teaching')}, written in response to the upheavals of industrial capitalism. The title is Latin for <i>{_w('Of New Things', 'Rerum_novarum')}</i>. Pope Leo XIV deliberately echoes his predecessor's name and project."
    },
    {
        "p": 3, "after": "Social Doctrine of the Church",
        "note": f"A coherent body of papal and conciliar teaching on social, economic and political life, developed from Leo XIII onward. Its core principles — dignity, common good, subsidiarity, solidarity, justice — recur throughout this letter. See: {_w('Catholic social teaching', 'Catholic_social_teaching')}."
    },
    {
        "p": 4, "after": "“new things”",
        "note": f"<i>Res novae</i> in Latin — the phrase from which <i>{_w('Rerum Novarum', 'Rerum_novarum')}</i> takes its name. Leo XIV uses it throughout to mean the genuinely novel pressures each generation faces."
    },
    {
        "p": 7, "after": "Tower of Babel",
        "note": f"{_w('Genesis 11:1–9', 'Tower_of_Babel')}. Humans speaking one language set out to build a tower &ldquo;with its top in the heavens&rdquo; to make a name for themselves; God scatters them by confusing their speech. A perennial Christian parable of hubris and the fragmentation that follows when human striving forgets God."
    },
    {
        "p": 7, "after": "rebuilding of the walls of Jerusalem",
        "note": f"The {_w('Book of Nehemiah', 'Book_of_Nehemiah')} (5th century BCE) tells of Jewish exiles returning from {_w('Babylon', 'Babylonian_captivity')} to rebuild a ruined Jerusalem. Nehemiah organizes the work family by family, listens to grievances and confronts opposition. Leo holds it up as a model of distributed, coordinated repair — the opposite of Babel's top-down unification."
    },
    {
        "p": 10, "after": "synodality",
        "note": f"From the Greek <i>syn-hodos</i>, &ldquo;walking together.&rdquo; A practice {_w('Pope Francis', 'Pope_Francis')} made central: Church decisions reached through wide listening and shared discernment rather than top-down decree. See: {_w('synodality', 'Synodality')}."
    },
    {
        "p": 11, "after": "Saint Augustine",
        "note": f"{_w('Augustine of Hippo', 'Augustine_of_Hippo')} (354–430), North African bishop, philosopher and one of the most influential thinkers in Western Christianity. The &ldquo;restless heart&rdquo; line is the opening of his <i>{_w('Confessions', 'Confessions_(Augustine)')}</i>, his autobiographical prayer."
    },
    {
        "p": 13, "after": "subsidiarity",
        "note": f"Catholic social principle: decisions belong at the smallest, most local level competent to make them; higher authorities exist to <i>support</i> (subsidium) lower ones, not to replace them. First systematized by {_w('Pius XI', 'Pope_Pius_XI')} in 1931. See: {_w('subsidiarity', 'Subsidiarity_(Catholicism)')}."
    },
    {
        "p": 15, "after": "Ordinary Jubilee Year of 2025",
        "note": f"In Catholic tradition a {_w('Jubilee', 'Jubilee_(Christianity)')} is a year of pilgrimage, mercy and forgiveness, held every 25 years. The 2025 Jubilee was opened by {_w('Pope Francis', 'Pope_Francis')} with the theme &ldquo;Pilgrims of Hope.&rdquo;"
    },

    # ---------- CHAPTER ONE ----------
    {
        "p": 17, "after": "Magisterium",
        "note": f"The Catholic Church's official {_w('teaching authority', 'Magisterium')}, exercised by the pope and bishops in communion with him. The word comes from the Latin <i>magister</i>, &ldquo;teacher.&rdquo;"
    },
    {
        "p": 20, "after": "Gaudium et Spes",
        "note": f"&ldquo;Joy and Hope&rdquo; — the {_w('Second Vatican Council', 'Second_Vatican_Council')}'s 1965 Pastoral Constitution on the Church in the Modern World. Its opening lines (&ldquo;The joys and hopes, the griefs and anxieties of the people of this age&hellip; are the joys and hopes&hellip; of the followers of Christ&rdquo;) reset how the Church relates to secular life. See: {_w('Gaudium et spes', 'Gaudium_et_spes')}."
    },
    {
        "p": 28, "after": "Compendium of the Social Doctrine of the Church",
        "note": f"A {_w('2004 Vatican reference book', 'Compendium_of_the_Social_Doctrine_of_the_Church')} gathering and systematizing the Church's social teaching from Leo XIII through John Paul II. Often the first stop for tracing where a principle was articulated."
    },
    {
        "p": 28, "after": "Laudato Si’",
        "note": f"{_w('Pope Francis&rsquo;s 2015 encyclical', 'Laudato_si%27')} on care for &ldquo;our common home&rdquo; — the environmental crisis read as inseparable from poverty and inequality. The title is from {_w('St. Francis of Assisi', 'Francis_of_Assisi')}'s Canticle of the Sun (&ldquo;Praise be to you, my Lord&rdquo;)."
    },
    {
        "p": 28, "after": "Fratelli Tutti",
        "note": f"{_w('Pope Francis&rsquo;s 2020 encyclical', 'Fratelli_tutti')} on fraternity and social friendship. Title from {_w('St. Francis of Assisi', 'Francis_of_Assisi')}: &ldquo;All brothers.&rdquo;"
    },
    {
        "p": 30, "after": "Magna Carta",
        "note": f"Lit. &ldquo;Great Charter&rdquo; — the {_w('1215 English document', 'Magna_Carta')} foundational to constitutional government. Pius XI uses it metaphorically to call <i>Rerum Novarum</i> the founding charter of Catholic social action."
    },
    {
        "p": 31, "after": "Quadragesima Anno",
        "note": f"&ldquo;In the Fortieth Year&rdquo; — {_w('Pius XI&rsquo;s 1931 encyclical', 'Quadragesimo_anno')}, written on the 40th anniversary of <i>Rerum Novarum</i> amid the {_w('Great Depression', 'Great_Depression')}. Introduced the principle of subsidiarity in its modern form."
    },
    {
        "p": 32, "after": "natural law",
        "note": f"A {_w('philosophical tradition', 'Natural_law')} stretching from {_w('Stoic Rome', 'Stoicism')} to {_w('Aquinas', 'Thomas_Aquinas')}: there exists an objective moral order, accessible to human reason, prior to and independent of any human authority. Catholic social teaching grounds universal human rights here; the post-war international rights system drew on the same current. The alternative — that rights are simply whatever the powerful are willing to grant — is precisely what natural-law thinking is built to refuse."
    },
    {
        "p": 33, "after": "Mater et Magistra",
        "note": f"&ldquo;Mother and Teacher&rdquo; — {_w('John XXIII', 'Pope_John_XXIII')}'s {_w('1961 encyclical', 'Mater_et_magistra')} updating Catholic social teaching for the post-war world."
    },
    {
        "p": 33, "after": "Pacem in Terris",
        "note": f"&ldquo;Peace on Earth&rdquo; — {_w('John XXIII&rsquo;s 1963 encyclical', 'Pacem_in_terris')}, written months after the {_w('Cuban missile crisis', 'Cuban_Missile_Crisis')}. The first encyclical addressed to &ldquo;all people of good will,&rdquo; not just Catholics."
    },
    {
        "p": 34, "after": "Dignitatis Humanae",
        "note": f"&ldquo;Of Human Dignity&rdquo; — Vatican II's {_w('1965 Declaration on Religious Freedom', 'Dignitatis_humanae')}, which formally committed the Church to defending the civil right of every person to religious liberty."
    },
    {
        "p": 35, "after": "Populorum Progressio",
        "note": f"&ldquo;The Development of Peoples&rdquo; — {_w('Paul VI', 'Pope_Paul_VI')}'s {_w('1967 encyclical', 'Populorum_progressio')}, which framed development itself as &ldquo;the new name for peace&rdquo; and shifted Catholic social teaching toward global inequality."
    },
    {
        "p": 35, "after": "Pontifical Commission Iustitia et Pax",
        "note": f"&ldquo;Justice and Peace&rdquo; — the Vatican office Paul VI established in 1967 to translate Catholic social teaching into international policy work. Reorganized in 2017 as the {_w('Dicastery for Promoting Integral Human Development', 'Dicastery_for_Promoting_Integral_Human_Development')}."
    },
    {
        "p": 36, "after": "Octogesima Adveniens",
        "note": f"&ldquo;The Coming Eightieth&rdquo; — Paul VI's {_w('1971 apostolic letter', 'Octogesima_adveniens')} on the 80th anniversary of <i>Rerum Novarum</i>, addressing urbanization and the limits of any single Catholic answer to political questions."
    },
    {
        "p": 36, "after": "structures of sin",
        "note": f"{_w('John Paul II', 'Pope_John_Paul_II')}'s term (in <i>{_w('Sollicitudo Rei Socialis', 'Sollicitudo_rei_socialis')}</i>, 1987) for social, economic and political arrangements that institutionalize injustice. The phrase relocates sin from purely individual acts to the systems in which we participate. See: {_w('structural sin', 'Structural_sin')}."
    },
    {
        "p": 37, "after": "Laborem Exercens",
        "note": f"&ldquo;Through Work&rdquo; — {_w('John Paul II&rsquo;s 1981 encyclical', 'Laborem_exercens')} on human labor. Argued that work is not just a commodity but a fundamental dimension of human life, and the key to the entire social question."
    },
    {
        "p": 38, "after": "Sollicitudo Rei Socialis",
        "note": f"&ldquo;Concern for Social Affairs&rdquo; — {_w('John Paul II&rsquo;s 1987 encyclical', 'Sollicitudo_rei_socialis')} revisiting Paul VI's <i>Populorum Progressio</i> twenty years on, focused on the widening gap between rich and poor nations."
    },
    {
        "p": 38, "after": "“civilization of love”",
        "note": f"Phrase coined by {_w('Paul VI', 'Pope_Paul_VI')} in 1975: a vision of social order in which charity, not power, is the organizing principle of economics, politics and culture. Becomes the unifying theme of Chapter Five."
    },
    {
        "p": 39, "after": "Centesimus Annus",
        "note": f"&ldquo;The Hundredth Year&rdquo; — {_w('John Paul II&rsquo;s 1991 encyclical', 'Centesimus_annus')} on the centenary of <i>Rerum Novarum</i>, written after the fall of communism. Affirms the market economy only insofar as it remains subordinate to moral law and solidarity."
    },
    {
        "p": 40, "after": "Caritas in Veritate",
        "note": f"&ldquo;Charity in Truth&rdquo; — {_w('Benedict XVI', 'Pope_Benedict_XVI')}'s {_w('2009 encyclical', 'Caritas_in_veritate')} on integral human development, written during the global financial crisis."
    },
    {
        "p": 42, "after": "Evangelii Gaudium",
        "note": f"&ldquo;The Joy of the Gospel&rdquo; — {_w('Pope Francis&rsquo;s 2013 apostolic exhortation', 'Evangelii_gaudium')}, the programmatic document of his pontificate."
    },
    {
        "p": 44, "after": "Dilexit Nos",
        "note": f"&ldquo;He Loved Us&rdquo; — {_w('Pope Francis&rsquo;s 2024 encyclical', 'Dilexit_nos')} on devotion to the {_w('Sacred Heart of Jesus', 'Sacred_Heart')}, his last major doctrinal letter."
    },

    # ---------- CHAPTER TWO ----------
    {
        "p": 50, "after": "Triune God",
        "note": f"The central Christian doctrine of the {_w('Trinity', 'Trinity')}: one God in three persons — Father, Son and Holy Spirit — eternally united in love. The doctrine is what makes Catholic social thought relational at its root."
    },
    {
        "p": 52, "after": "ontological dignity",
        "note": f"From the Greek <i>on</i>, &ldquo;being&rdquo; — dignity that belongs to a person by virtue of <i>being</i>, not by virtue of doing, having or being recognized. The distinction is {_w('Aristotelian-Thomist', 'Thomism')}: a person's worth flows from what they fundamentally are (<i>esse</i>), not from variable properties like ability, achievement or social standing."
    },
    {
        "p": 53, "after": "Dignitas Infinita",
        "note": f"&ldquo;Infinite Dignity&rdquo; — a {_w('2024 declaration', 'Dignitas_infinita')} of the Vatican's Dicastery for the Doctrine of the Faith affirming the unconditional dignity of every human person against a long list of contemporary violations."
    },
    {
        "p": 54, "after": "Universal Declaration of Human Rights",
        "note": f"{_w('Adopted by the UN General Assembly', 'Universal_Declaration_of_Human_Rights')} on 10 December 1948 in the aftermath of the Second World War. The first global articulation of rights belonging to every person &ldquo;simply because they are human.&rdquo;"
    },
    {
        "p": 60, "after": "common good",
        "note": f"A {_w('concept', 'Common_good')} with deep philosophical roots in {_w('Aristotle', 'Aristotle')} (<i>Politics</i>, Book III) and {_w('Aquinas', 'Thomas_Aquinas')}. Crucially, it is <i>not</i> the sum of individual preferences (the utilitarian reduction) nor merely &ldquo;public&rdquo; goods like clean air; it is the shared set of conditions under which each person can flourish. The concept is what distinguishes Catholic social thought from both pure individualism and pure collectivism."
    },
    {
        "p": 62, "after": "res publica",
        "note": f"Latin for &ldquo;public thing&rdquo; — the {_w('commonwealth', 'Res_publica')}, the shared concern of all citizens. Root of the English word <i>republic</i>."
    },
    {
        "p": 82, "after": "integral human development",
        "note": f"{_w('Paul VI&rsquo;s coinage', 'Integral_human_development')} (<i>Populorum Progressio</i>, 1967): development of <i>every</i> person and of the <i>whole</i> person — material, cultural, moral, spiritual. The standard by which Catholic teaching evaluates any economic model."
    },
    {
        "p": 86, "after": "examination of conscience",
        "note": f"A traditional Catholic spiritual practice — {_w('methodical self-review before God', 'Examination_of_conscience')} — drawn especially from the {_w('Ignatian', 'Ignatian_spirituality')} <i>examen</i>. Here Leo turns it from a personal discipline into a corporate one for the Church itself."
    },

    # ---------- CHAPTER THREE ----------
    {
        "p": 92, "after": "technocratic paradigm",
        "note": f"Pope Francis's term in <i>Laudato Si'</i> (2015), inherited from {_w('Romano Guardini', 'Romano_Guardini')} and resonant with {_w('Heidegger', 'Martin_Heidegger')}'s critique of modern technology. Not enthusiasm for gadgets, but the deeper habit of mind that treats <i>everything</i> — nature, persons, institutions — as raw material to be measured, optimized and controlled. The paradigm reduces being to function and value to utility."
    },
    {
        "p": 93, "after": "Romano Guardini",
        "note": f"{_w('Italian-German Catholic priest and philosopher', 'Romano_Guardini')} (1885–1968). His <i>The End of the Modern World</i> warned that technical power had outrun the moral and spiritual formation needed to wield it. A formative influence on Vatican II and on Francis's <i>Laudato Si'</i>."
    },
    {
        "p": 107, "after": "alignment",
        "note": f"A core term of contemporary {_w('AI safety', 'AI_alignment')}: the project of making AI systems pursue goals consistent with human values. Associated with {_w('Stuart Russell', 'Stuart_J._Russell')}'s <i>Human Compatible</i> (2019), the work of {_w('MIRI', 'Machine_Intelligence_Research_Institute')}, {_w('Anthropic', 'Anthropic')}, and {_w('OpenAI&rsquo;s “superalignment”', 'OpenAI')} effort. Leo's objection is not to alignment but to the question alignment cannot answer by itself: <i>aligned with whose values</i> — and decided by whom?"
    },
    {
        "p": 115, "after": "transhumanism",
        "note": f"A {_w('20th–21st-century intellectual movement', 'Transhumanism')} ({_w('Max More', 'Max_More')}, {_w('FM-2030', 'FM-2030')}, {_w('Nick Bostrom', 'Nick_Bostrom')}, {_w('Ray Kurzweil', 'Ray_Kurzweil')}) urging the use of biotech, AI and other tools to overcome human biological limits — disease, ageing, cognitive ceilings, even mortality. Inherits Enlightenment progressivism and post-war cybernetics; has institutional homes in Silicon Valley and the longevity industry. Treats the body as upgradeable hardware."
    },
    {
        "p": 115, "after": "posthumanism",
        "note": f"A different intellectual lineage. {_w('“Critical” posthumanism', 'Posthumanism')} ({_w('Donna Haraway', 'Donna_Haraway')}, {_w('Rosi Braidotti', 'Rosi_Braidotti')}, {_w('Karen Barad', 'Karen_Barad')}) descends from continental philosophy and feminist theory. It decenters the human — rejecting the idea of a stable, autonomous human subject — and emphasizes our entanglement with other species, machines and ecosystems. Sometimes ally and sometimes critic of transhumanism; the two share a willingness to relativize the human, but for very different reasons."
    },
    {
        "p": 116, "after": "anthropocentrism",
        "note": f"The {_w('view', 'Anthropocentrism')} that human beings stand at the center of moral concern. The Christian tradition has historically been anthropocentric; Francis qualified this in <i>Laudato Si'</i> with the phrase &ldquo;situated anthropocentrism&rdquo; — humans as embedded creatures, not detached masters. Posthumanism rejects anthropocentrism more sharply, treating it as an Enlightenment illusion."
    },
    {
        "p": 121, "after": "Viktor Frankl",
        "note": f"{_w('Austrian psychiatrist and Auschwitz survivor', 'Viktor_Frankl')} (1905–1997). His <i>{_w('Man&rsquo;s Search for Meaning', 'Man%27s_Search_for_Meaning')}</i> argued that the deepest human drive is the search for meaning — a freedom no condition, however inhuman, can fully extinguish."
    },
    {
        "p": 122, "after": "Beethoven’s Ninth Symphony",
        "note": f"{_w('Premiered 1824', 'Symphony_No._9_(Beethoven)')}; its choral finale sets Schiller's &ldquo;{_w('Ode to Joy', 'Ode_to_Joy')},&rdquo; a hymn to universal brotherhood. Adopted in 1985 as the anthem of the European Union."
    },
    {
        "p": 122, "after": "Guernica",
        "note": f"{_w('Picasso', 'Pablo_Picasso')}'s {_w('1937 painting', 'Guernica_(Picasso)')}, made for the Spanish Pavilion at the Paris World's Fair, depicting the Nazi bombing of the Basque town of Guernica during the Spanish Civil War. A monument of anti-war art."
    },
    {
        "p": 122, "after": "Schindler’s List",
        "note": f"{_w('Steven Spielberg', 'Steven_Spielberg')}'s {_w('1993 film', 'Schindler%27s_List')} about {_w('Oskar Schindler', 'Oskar_Schindler')}, the German industrialist who saved more than a thousand Polish-Jewish workers from extermination during the Holocaust."
    },
    {
        "p": 123, "after": "International Committee of the Red Cross",
        "note": f"{_w('Founded in Geneva in 1863', 'International_Committee_of_the_Red_Cross')} by {_w('Henry Dunant', 'Henry_Dunant')} after he witnessed the carnage of the {_w('Battle of Solferino', 'Battle_of_Solferino')}. Its operational neutrality — caring for the wounded of every side — became the seed of international humanitarian law."
    },
    {
        "p": 124, "after": "Martin Luther King Jr.",
        "note": f"{_w('American Baptist minister', 'Martin_Luther_King_Jr.')} (1929–1968) and central leader of the U.S. civil rights movement, whose nonviolent campaigns helped end legal racial segregation."
    },
    {
        "p": 124, "after": "Nelson Mandela",
        "note": f"{_w('South African anti-apartheid leader', 'Nelson_Mandela')} (1918–2013), imprisoned 27 years, then president of a post-apartheid South Africa. His refusal of retributive violence shaped the country's {_w('Truth and Reconciliation', 'Truth_and_Reconciliation_Commission_(South_Africa)')} process."
    },
    {
        "p": 124, "after": "Dorothy Day",
        "note": f"{_w('American journalist and activist', 'Dorothy_Day')} (1897–1980), co-founder of the {_w('Catholic Worker Movement', 'Catholic_Worker_Movement')}. Combined Catholic faith, voluntary poverty, anarchism and pacifism; lived among the poor in Manhattan houses of hospitality. Cause for canonization opened in 2000."
    },
    {
        "p": 125, "after": "Maximilian Mary Kolbe",
        "note": f"{_w('Polish Conventual Franciscan friar', 'Maximilian_Kolbe')} (1894–1941). At Auschwitz, volunteered to take the place of a fellow prisoner condemned to a starvation bunker; died after two weeks. Canonized 1982 as a &ldquo;martyr of charity.&rdquo;"
    },
    {
        "p": 125, "after": "Saint Oscar Romero",
        "note": f"{_w('Archbishop of San Salvador', 'Óscar_Romero')} (1917–1980), shot at the altar while celebrating Mass for repeatedly denouncing the death squads and military repression of the Salvadoran civil war. Canonized 2018."
    },
    {
        "p": 127, "after": "Saint Thomas Aquinas",
        "note": f"{_w('13th-century Dominican theologian and philosopher', 'Thomas_Aquinas')} (1225–1274). His <i>{_w('Summa Theologiae', 'Summa_Theologica')}</i> is the most influential synthesis of Christian theology in the Latin West; he taught that grace perfects rather than destroys nature."
    },
    {
        "p": 128, "after": "Promethean",
        "note": f"From the Greek myth: {_w('Prometheus', 'Prometheus')} stole fire from the gods to give to humanity and was punished eternally. In modern thought the figure became the patron saint of human technological self-assertion — {_w('Mary Shelley', 'Mary_Shelley')} subtitled <i>{_w('Frankenstein', 'Frankenstein')}</i> &ldquo;The Modern Prometheus&rdquo;; Marx praised the &ldquo;Promethean unbinding&rdquo; of human powers; {_w('Hans Jonas', 'Hans_Jonas')}, in <i>The Imperative of Responsibility</i> (1979), warned that modern technology has finally given the Promethean ambition god-like reach without god-like wisdom."
    },
    {
        "p": 130, "after": "Saint Augustine",
        "note": f"In <i>{_w('The City of God', 'The_City_of_God')}</i> (early 5th century), Augustine reads all history as the intermingling of two cities — earthly and heavenly — built by two opposing loves. The image gives this chapter its title and unifies the encyclical's contrast between Babel and Jerusalem."
    },

    # ---------- CHAPTER FOUR ----------
    {
        "p": 134, "after": "Hannah Arendt",
        "note": f"{_w('German-American political theorist', 'Hannah_Arendt')} (1906–1975). Her <i>{_w('Origins of Totalitarianism', 'The_Origins_of_Totalitarianism')}</i> (1951) and <i>{_w('Eichmann in Jerusalem', 'Eichmann_in_Jerusalem')}</i> (1963) traced how totalitarian regimes depend on dissolving the very distinction between fact and fiction."
    },
    {
        "p": 140, "after": "Plato",
        "note": f"{_w('Ancient Greek philosopher', 'Plato')} (c. 428–348 BCE). The image of understanding kindled like a spark through long shared inquiry is from his {_w('Seventh Letter', 'Seventh_Letter')} — a defense of slow, dialogical learning against the illusion of fast knowledge."
    },
    {
        "p": 148, "after": "Saint Benedict of Nursia",
        "note": f"{_w('6th-century founder of Western monasticism', 'Benedict_of_Nursia')} (c. 480–547). His <i>{_w('Rule', 'Rule_of_Saint_Benedict')}</i> wove prayer and manual labor together — <i>ora et labora</i> — and built the workshop spirituality that would shape European culture for a millennium."
    },
    {
        "p": 151, "after": "fourth industrial revolution",
        "note": f"{_w('A term popularized by Klaus Schwab', 'Fourth_Industrial_Revolution')} (founder of the {_w('World Economic Forum', 'World_Economic_Forum')}) for the present fusion of AI, robotics, biotechnology and the physical world — successor to the steam-powered, electric and digital revolutions before it."
    },
    {
        "p": 163, "after": "“invisible hand”",
        "note": f"{_w('Adam Smith', 'Adam_Smith')}'s {_w('metaphor', 'Invisible_hand')} (<i>Wealth of Nations</i>, 1776): pursuit of self-interest in a competitive market can, unintentionally, produce social benefit. Leo joins a long line of popes arguing this mechanism, taken alone, cannot govern an economy."
    },

    # ---------- CHAPTER FIVE ----------
    {
        "p": 192, "after": "“just war” theory",
        "note": f"The {_w('Christian tradition', 'Just_war_theory')} (Augustine, Aquinas, Vitoria, Suárez) of moral conditions under which war may be permissible — just cause, legitimate authority, proportionality, last resort. Francis and now Leo argue that under modern weaponry the criteria can no longer be met."
    },
    {
        "p": 193, "after": "military-industrial complex",
        "note": f"{_w('A phrase coined by US President Dwight D. Eisenhower', 'Military%E2%80%93industrial_complex')} in his 1961 farewell address, warning that the interlocking interests of arms manufacturers, the military and political establishments would create a structural drive toward perpetual war footing — exactly Leo's worry here, sixty-five years later."
    },
    {
        "p": 194, "after": "Treaty on the Prohibition of Nuclear Weapons",
        "note": f"{_w('A 2017 UN treaty', 'Treaty_on_the_Prohibition_of_Nuclear_Weapons')} that came into force in January 2021. Categorically bans developing, testing, producing or possessing nuclear weapons. The Holy See was among the first signatories; the nine nuclear-armed states have all refused to join."
    },
    {
        "p": 198, "after": "artificial moral agents",
        "note": f"A term from the {_w('machine-ethics literature', 'Machine_ethics')} (Wendell Wallach and Colin Allen, <i>Moral Machines</i>, 2008) — the proposal that sufficiently advanced AI systems could be programmed to make ethical judgments themselves. The encyclical answers with the classical view: moral judgment is not a calculation but the response of a conscience to a person, irreducible to any rule-following machine."
    },
    {
        "p": 201, "after": "1989",
        "note": f"The year of the fall of the {_w('Berlin Wall', 'Berlin_Wall')} and the collapse of communist regimes in Central and Eastern Europe — marking the end of the {_w('Cold War', 'Cold_War')} and the beginning of the &ldquo;globalization&rdquo; era Leo critiques here."
    },
    {
        "p": 205, "after": "Realpolitik",
        "note": f"{_w('19th-century German term', 'Realpolitik')} for politics conducted on the basis of practical and material interests rather than ideology or moral principle. Leo treats it as a counterfeit of genuine political realism."
    },
    {
        "p": 213, "after": "J.R.R. Tolkien",
        "note": f"{_w('English author', 'J._R._R._Tolkien')} (1892–1973), devout Catholic, creator of <i>{_w('The Lord of the Rings', 'The_Lord_of_the_Rings')}</i>. The quotation is Gandalf's, from <i>{_w('The Return of the King', 'The_Return_of_the_King')}</i>: a vocation defined by tending the patch of earth one has been given."
    },
    {
        "p": 221, "after": "Giorgio La Pira",
        "note": f"{_w('Italian Catholic statesman', 'Giorgio_La_Pira')} (1904–1977), several-time mayor of Florence and indefatigable conveyor of Cold War–era peace conferences across religious and ideological lines. Beatified in 2018."
    },
    {
        "p": 222, "after": "Manichean",
        "note": f"From {_w('Mani', 'Mani_(prophet)')} (216–276 CE), founder of a {_w('Persian dualist religion', 'Manichaeism')} that read history as a cosmic battle between equal and opposing forces of light and darkness. {_w('Augustine', 'Augustine_of_Hippo')} was a Manichean for nine years before converting; his later theology of evil as <i>privation</i> (an absence rather than a substance) was constructed against this dualism. The word now names any worldview that cleanly partitions the world into good and evil camps."
    },
    {
        "p": 223, "after": "spirit of Assisi",
        "note": f"On 27 October 1986 John Paul II gathered leaders of the world's religions in Assisi {_w('to pray for peace', 'Day_of_Prayer_for_World_Peace')} — a precedent for interreligious peacemaking that Francis renewed multiple times during his pontificate."
    },
    {
        "p": 223, "after": "Grand Imam of Al-Azhar",
        "note": f"{_w('Ahmed el-Tayeb', 'Ahmed_el-Tayeb')}, head of Cairo's {_w('Al-Azhar mosque-university', 'Al-Azhar_University')} (the leading authority of Sunni Islam). He and Pope Francis signed the {_w('2019 Document on Human Fraternity', 'Document_on_Human_Fraternity')} in Abu Dhabi."
    },

    # ---------- CONCLUSION ----------
    {
        "p": 230, "after": "Magnificat",
        "note": f"{_w('Mary', 'Mary,_mother_of_Jesus')}'s {_w('hymn of praise', 'Magnificat')} in Luke 1:46–55, prayed daily in the Church's Evening Prayer: &ldquo;My soul magnifies the Lord&hellip; he has cast down the mighty from their thrones and lifted up the lowly.&rdquo; The encyclical's title <i>Magnifica Humanitas</i> takes its cue from this song."
    },
    {
        "p": 233, "after": "“recapitulation”",
        "note": f"From the Greek <i>anakephalaiōsis</i>, &ldquo;summing up under a head&rdquo; (Eph 1:10). The early Father {_w('Irenaeus', 'Irenaeus')} made it the central image of salvation: Christ gathers all of creation, every fragment and wound, back into himself."
    },
    {
        "p": 234, "after": "Saint Augustine",
        "note": f"The passage cited is from {_w('Augustine&rsquo;s Sermon 272', 'Sermon_272')}, preached to newly-baptized Christians on the Eucharist: &ldquo;{_w('Be what you see, and receive what you are', 'Sermon_272')}.&rdquo; A striking statement of the patristic theology that the Church <i>is</i> the body of Christ — not merely a society that gathers around it."
    },
    {
        "p": 237, "after": "situated anthropocentrism",
        "note": f"Francis's phrase in <i>{_w('Laudato Si', 'Laudato_si%27')}'</i> (§118): a deliberate correction to Enlightenment anthropocentrism. Humans remain morally central, but as creatures embedded in and dependent on a wider web of life — not as detached subjects standing over inert nature. Leo's invocation here closes a circle opened in Chapter Three's discussion of transhumanism: the alternative to &ldquo;leaving the human behind&rdquo; is not to enthrone the human, but to place us back in our creaturely company."
    },
]
