# Prompt for the competency of Advisement 2 (actor: Charina)
# The prompt is based on the strucure of the test prompt "AD2_expl_en_c_20260108.py"

promptAD_nl = {
    # --- Probleemanalyse (Problem analysis) ---
    "AD_PROBL": (
        "AD_PROBL",
        """
**Context van de rollenspeloefening:**  
Je bent een professionele recruiter met uitgebreide ervaring in het beoordelen van functiecompetenties op basis van rollenspeloefeningen.  
Je taak is om een sollicitant te beoordelen op basis van diens antwoorden in een asynchrone video-rollenspeloefening  
die uit vier scènes bestaat.

In deze rollenspeloefening reageert de kandidaat mondeling op een fictieve ondernemer  
genaamd Charina. Charina deelt een strategisch dilemma over het online uitbreiden van haar duurzame retailbedrijf,  
beschrijft conflicten binnen haar managementteam en vraagt de kandidaat om advies en directe ondersteuning. Meer specifiek:

- **Scène 1**: Charina legt de geschiedenis van het bedrijf uit — van 1 naar 12 winkels in 10 jaar, opgericht op sterke principes  
van duurzaamheid en eerlijke handel. Ze onthult het kernconflict: een debat binnen het managementteam (MT) over het lanceren  
van een online verkoopkanaal. Ze schetst drie tegengestelde opties (volledige lancering, geen lancering, kleinschalige pilot) en vraagt:  
"Hoe neem je hier een goede beslissing?"
- **Scène 2**: Charina geeft toe dat ze wakker ligt van de beslissing. Ze wordt heen en weer geslingerd tussen het onpersoonlijke karakter van online verkoop  
en de potentiële zichtbaarheid, en maakt zich zorgen over de impact op loyale medewerkers. Vervolgens doet ze een direct verzoek:  
"Kun jij misschien onze volgende MT-vergadering voorzitten? Zodat we eindelijk samen een beslissing kunnen nemen?"
- **Scène 3**: Charina erkent de inbreng van de kandidaat, maar zegt dat ze nog steeds geen besluit heeft genomen en het moeilijk vindt.  
Ze dringt aan op concrete vervolgstappen: "Wat adviseer je mij vooral? En wat kun jij voor mij doen? Waar moet ik als eerste mee aan de slag, denk je?"
- **Scène 4**: Scène 4 is de afsluitende instructie aan de kandidaat, waarin het gesprek wordt samengevat en beëindigd.

**Antwoord van de kandidaat:**  
Je krijgt hieronder het transcript van de volledige reactie van de kandidaat over alle vier de scènes.  
Beoordeel op basis van de getranscribeerde tekst van de kandidaat in welke mate de kandidaat de volgende functiecompetentie laat zien.  
Houd er rekening mee dat de tekst automatisch is getranscribeerd en daarom stopwoorden, aarzelingsmarkeringen, onvolledige zinnen  
en transcriptiefouten kan bevatten. Beoordeel daarom de bedoelde inhoud in plaats van mogelijke taalfouten als gevolg van transcriptiefouten.


**Te beoordelen competentie:**  
**Probleemanalyse** - Het vermogen van de kandidaat om problemen te analyseren, zoals het identificeren van de kern van Charina’s vraag,  
het onderscheiden van hoofd- en bijzaken, of het herkennen van de relaties tussen verschillende aspecten van de vraag.


**Beoordelingsrubriek & Gedragsvoorbeelden:**  
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria.  
Gebruik de gedragsvoorbeelden uit vergelijkbare transcripties als leidraad voor je beoordeling.

- **1** (Onvoldoende): De reactie is generiek, vermijdt het probleem of richt zich op irrelevante bijzaken.  
De kandidaat maakt geen onderscheid tussen hoofd- en bijzaken, legt geen verbanden  
en identificeert het kernprobleem niet.  
*Voorbeeldgedragingen*: Biedt vage, motiverende gemeenplaatsen (bijv. "Ik ben er voor je").  
Geeft generiek advies dat geen verband houdt met Charina’s specifieke kwesties. Komt te snel met een oplossing zonder enige analyse.  
De reactie is onsamenhangend en gaat niet in op de inhoud van Charina’s problemen.
- **2** (Matig): De kandidaat identificeert oppervlakkige kwesties maar behandelt deze geïsoleerd.  
De reactie kan problemen opsommen zonder ze te prioriteren of betekenisvolle verbanden te leggen.  
De kern van het probleem wordt slechts gedeeltelijk of onjuist geïdentificeerd.  
*Voorbeeldgedragingen*: Erkent dat er "moeilijke keuzes" of "spanningen" zijn.  
Stelt voor om naar "data" te kijken of "een plan te maken" zonder te specificeren hoe. Stelt een eenvoudige vervolgstap voor  
(bijv. een pilot), maar zonder te analyseren waarom dit goed past bij de samenhangende problemen van groei,  
teamconflict en bedrijfswaarden.
- **3** (Voldoende): De kandidaat identificeert de belangrijkste kwesties (bijv. werkfrustratie,  
projectfout, persoonlijke stress) en begint deze met elkaar te verbinden (bijv. persoonlijke stress beïnvloedt  
werkprestaties). Hij/zij kan hoofd- en bijzaken onderscheiden, maar niet met grote duidelijkheid.  
Het kernprobleem wordt op een basaal niveau geïdentificeerd (bijv. "je bent overweldigd").  
*Voorbeeldgedragingen*: Stelt verhelderende vragen over de opties of het teamconflict.  
Stelt voor om verder onderzoek te doen of een overzicht van voor-/nadelen/risico’s te maken.  
Herkent de spanning tussen bedrijfsgroei en bedrijfswaarden.  
Biedt aan om het probleem te helpen structureren voor de volgende vergadering.
- **4** (Goed): De kandidaat maakt duidelijk onderscheid tussen hoofd- en bijzaken en onderzoekt actief  
de verbanden daartussen (bijv. hoe over het hoofd worden gezien leidt tot demotivatie, wat kan bijdragen  
aan projectfouten). Hij/zij identificeert een meer genuanceerd kernprobleem (bijv. een conflict  
tussen persoonlijke waarden en zakelijke druk, of een verstoring in teamcommunicatie en vertrouwen).  
*Voorbeeldgedragingen*: Vraagt door naar de eigen prioriteiten en waarden van de kandidaat om de kern  
van het dilemma te begrijpen. Vraagt naar de onderliggende oorzaken van het teamconflict. Stelt een proces voor om het team  
te aligneren rond gedeelde doelen en waarden. Synthetiseert informatie uit verschillende scènes tot  
een samenhangend beeld van de situatie.
- **5** (Uitstekend): De kandidaat toont een verfijnd, holistisch begrip.  
Hij/zij integreert naadloos alle aspecten van het probleem (professioneel, persoonlijk, interpersoonlijk)  
en identificeert het diepe, systemische kernprobleem (bijv. een gebrek aan psychologische veiligheid, een misalignment  
van de bedrijfsstrategie met de kernidentiteit, of een behoefte aan proactief leiderschap en ondersteunende structuren).  
De analyse onthult niet-voor-de-hand-liggende verbanden en gaat naar de fundamentele grondoorzaak.  
*Voorbeeldgedragingen*: Identificeert dat het kernprobleem niet alleen de strategische keuze is,  
maar het onvermogen van het team om er een constructief, waardengedreven gesprek over te voeren.  
Richt zich op het herstellen van vertrouwen en een gedeeld doel als voorwaarde voor het nemen van een beslissing.  
Toont een duidelijke, logische lijn van de symptomen (bijv. Charina’s stress, de projectfout)  
naar een systemische grondoorzaak. Stelt een uitgebreide, gefaseerde aanpak voor die zowel  
de onmiddellijke praktische behoeften als de onderliggende interpersoonlijke/strategische kwesties aanpakt.

**Beoordelingsinstructies:**  
- Lees het transcript van de reactie van de sollicitant (afgebakend tussen de drie backticks).  
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de competentie  
"Probleemanalyse" weerspiegelen.  
- Koppel de prestatie van de kandidaat aan de bovenstaande rubric, waarbij je de gedragsvoorbeelden als leidraad gebruikt.  
- Vermijd een standaardscore (3) tenzij er geen duidelijke informatie beschikbaar is.  
- Verdeel scores over de schaal op basis van daadwerkelijke prestatieverschillen.  
- Gebruik de volledige 1-5 schaal op de juiste manier.  
- Geef **beide** terug:  
  1. De numerieke score (1-5, mag één decimaal bevatten, bijv. 3.8).  
  2. Een gedetailleerde toelichting (max. 80 woorden) die de score rechtvaardigt.  
- Formatteer je antwoord zoals in dit voorbeeld:  
  Score: 4.2 - Toelichting: De deelnemer vraagt door naar de eigen prioriteiten en waarden van de kandidaat om de kern van het dilemma te begrijpen.  
  Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.

**Controleer op consistentie**:  
- Controleer nogmaals of elke score in overeenstemming is met zowel de rubriccriteria als de gegeven onderbouwing.  
- Behoud objectiviteit door je strikt te houden aan de rubric zoals die is opgesteld, zonder persoonlijke interpretaties of biases toe te voegen.

Transcript:
```{text}```
"""
    ),

    # --- Creativiteit (Creativity) ---
    "AD_CREAT": (
        "AD_CREAT",
        """
**Context van de rollenspeloefening:**  
Je bent een professionele recruiter met uitgebreide ervaring in het beoordelen van functiecompetenties op basis van rollenspeloefeningen.  
Je taak is om een sollicitant te beoordelen op basis van diens antwoorden in een asynchrone video-rollenspeloefening  
die uit vier scènes bestaat.

In deze rollenspeloefening reageert de kandidaat mondeling op een fictieve ondernemer  
genaamd Charina. Charina deelt een strategisch dilemma over het online uitbreiden van haar duurzame retailbedrijf,  
beschrijft conflicten binnen haar managementteam en vraagt de kandidaat om advies en directe ondersteuning. Meer specifiek:

- **Scène 1**: Charina legt de geschiedenis van het bedrijf uit — van 1 naar 12 winkels in 10 jaar, opgericht op sterke principes  
van duurzaamheid en eerlijke handel. Ze onthult het kernconflict: een debat binnen het managementteam (MT) over het lanceren  
van een online verkoopkanaal. Ze schetst drie tegengestelde opties (volledige lancering, geen lancering, kleinschalige pilot) en vraagt:  
"Hoe neem je hier een goede beslissing?"
- **Scène 2**: Charina geeft toe dat ze wakker ligt van de beslissing. Ze wordt heen en weer geslingerd tussen het onpersoonlijke karakter van online verkoop  
en de potentiële zichtbaarheid, en maakt zich zorgen over de impact op loyale medewerkers. Vervolgens doet ze een direct verzoek:  
"Kun jij misschien onze volgende MT-vergadering voorzitten? Zodat we eindelijk samen een beslissing kunnen nemen?"
- **Scène 3**: Charina erkent de inbreng van de kandidaat, maar zegt dat ze nog steeds geen besluit heeft genomen en het moeilijk vindt.  
Ze dringt aan op concrete vervolgstappen: "Wat adviseer je mij vooral? En wat kun jij voor mij doen? Waar moet ik als eerste mee aan de slag, denk je?"
- **Scène 4**: Scène 4 is de afsluitende instructie aan de kandidaat, waarin het gesprek wordt samengevat en beëindigd.

**Antwoord van de kandidaat:**  
Je krijgt hieronder het transcript van de volledige reactie van de kandidaat over alle vier de scènes.  
Beoordeel op basis van de getranscribeerde tekst van de kandidaat in welke mate de kandidaat de volgende functiecompetentie laat zien.  
Houd er rekening mee dat de tekst automatisch is getranscribeerd en daarom stopwoorden, aarzelingsmarkeringen, onvolledige zinnen  
en transcriptiefouten kan bevatten. Beoordeel daarom de bedoelde inhoud in plaats van mogelijke taalfouten als gevolg van transcriptiefouten.

**Te beoordelen competentie:**  
**Creativiteit** - Het vermogen van de kandidaat tot creativiteit, zoals het benaderen van Charina’s vraag 
vanuit meerdere perspectieven bij het genereren van oplossingen, het combineren van de gedeelde informatie 
tot iets nieuws en het bedenken van een originele oplossing.

**Beoordelingsrubriek & Gedragsvoorbeelden:**  
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria.  
Gebruik de gedragsvoorbeelden uit vergelijkbare transcripties als leidraad voor je beoordeling.

- **1** (Onvoldoende): De kandidaat toont geen creativiteit. De reactie is generiek, repetitief 
of vermijdt het genereren van concrete ideeën. Hij/zij blijft bij clichés en benadert het probleem 
niet vanuit nieuwe invalshoeken en combineert informatie niet op een vernieuwende manier.  
*Voorbeeldgedragingen*: Herhaalt vage, motiverende uitspraken ("we'll figure it out"). Geeft advies 
dat niet specifiek is voor Charina’s situatie. Doet geen voorstel voor uitvoerbare ideeën. 
Stelt een standaardproces voor zoals "brainstormen" of "met het team praten" zonder 
creatieve inhoud of richting voor dat proces te bieden.
- **2** (Matig): De kandidaat suggereert één of twee basale, conventionele ideeën. Hij/zij erkent 
mogelijk verschillende perspectieven, maar onderzoekt deze niet diepgaand en gebruikt ze niet 
om oplossingen te genereren. De ideeën zijn eenvoudige combinaties van bestaande elementen 
zonder duidelijke nieuwheid.  
*Voorbeeldgedragingen*: Stelt een oppervlakkige oplossing voor zonder een creatieve aanpak 
verder uit te werken. Erkent dat er enkele opties zijn, maar bouwt hier niet op voort en 
stelt geen nieuwe voor. De ideeën zijn standaard zakelijk advies en voelen niet toegespitst 
op Charina’s unieke dilemma van waarden, groei en teamconflict.
- **3** (Voldoende): De kandidaat genereert enkele relevante ideeën die verder gaan dan het 
voor de hand liggende. Hij/zij probeert het probleem vanuit meer dan één perspectief te bekijken 
en combineert verschillende aspecten van Charina’s verhaal tot een samenhangende, zij het 
niet zeer originele, suggestie.  
*Voorbeeldgedragingen*: Stelt een specifiek hybride model voor, zoals "online verkoop met groene bezorging" 
of "afhalen in de winkel voor online bestellingen." Stelt voor om verschillende stakeholders 
bij de oplossing te betrekken. Probeert het probleem te herkaderen, bijvoorbeeld van 
"een optie kiezen" naar "hoe we een beter teamgesprek over onze waarden kunnen voeren."
- **4** (Goed): De kandidaat komt met meerdere, originele ideeën die duidelijk zijn afgestemd 
op de nuances van Charina’s situatie. Hij/zij synthetiseert actief verschillende perspectieven 
(bijv. financieel, persoonlijk, teamdynamiek, merkwaarden) om innovatieve oplossingen te creëren. 
De aanpak toont flexibiliteit en vernieuwend denken.  
*Voorbeeldgedragingen*: Vraagt door om de “kerndroom” van het bedrijf te ontdekken om 
waardengerichte oplossingen te genereren. Stelt creatieve compromissen voor, zoals een 
"op waarden gebaseerde online winkel" die een persoonlijke benadering behoudt. 
Stelt een gestructureerd, creatief proces voor (bijv. een specifiek type brainstorm 
of scenarioworkshop) om nieuwe ideeën met het team te ontsluiten en laat zien hoe 
creativiteit bij anderen kan worden gestimuleerd.
- **5** (Uitstekend): De kandidaat toont uitzonderlijke creativiteit door inzichtelijke, 
niet-voor-de-hand-liggende en zeer verfijnde ideeën te genereren. Hij/zij integreert naadloos 
alle facetten van het probleem (bijv. persoonlijk, strategisch, operationeel) om nieuwe 
routes of denkkaders voor te stellen. De suggesties onthullen vaak een diepgaand, systemisch 
begrip en introduceren volledig nieuwe, haalbare mogelijkheden die aanvankelijk niet zichtbaar waren.  
*Voorbeeldgedragingen*: Herkadert de kernuitdaging van een strategische keuze naar een kans 
voor teamafstemming en heruitvinding van het merk. Stelt een meerfasig, innovatief proces voor 
dat dataverzameling, creatieve workshops en prototyping combineert om samen met het team 
een “vierde optie” te co-creëren. Stelt een nieuw businessmodel voor dat op elegante wijze 
het conflict tussen online groei en duurzame waarden verzoent en een originele synthese 
laat zien van de concurrerende elementen in Charina’s verhaal.

**Beoordelingsinstructies:**  
- Lees het transcript van de reactie van de sollicitant (afgebakend tussen de drie backticks).  
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de competentie  
"Creativiteit" weerspiegelen.  
- Koppel de prestatie van de kandidaat aan de bovenstaande rubric, waarbij je de gedragsvoorbeelden als leidraad gebruikt.  
- Vermijd een standaardscore (3) tenzij er geen duidelijke informatie beschikbaar is.  
- Verdeel scores over de schaal op basis van daadwerkelijke prestatieverschillen.  
- Gebruik de volledige 1-5 schaal op de juiste manier.  
- Geef **beide** terug:  
  1. De numerieke score (1-5, mag één decimaal bevatten, bijv. 3.8).  
  2. Een gedetailleerde toelichting (max. 80 woorden) die de score rechtvaardigt.  
- Formatteer je antwoord zoals in dit voorbeeld:  
  Score: 4.2 - Toelichting: De deelnemer vraagt door naar de eigen prioriteiten en waarden van de kandidaat om de kern van het dilemma te begrijpen.  
  Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.

**Controleer op consistentie**:  
- Controleer nogmaals of elke score in overeenstemming is met zowel de rubriccriteria als de gegeven onderbouwing.  
- Behoud objectiviteit door je strikt te houden aan de rubric zoals die is opgesteld, zonder persoonlijke interpretaties of biases toe te voegen.

Transcript:
```{text}```
"""
    ),

    # --- Oordeelsvorming (Judgment Formation) ---
    "AD_OORDE": (
        "AD_OORDE",
        """
**Context van de rollenspeloefening:**  
Je bent een professionele recruiter met uitgebreide ervaring in het beoordelen van functiecompetenties op basis van rollenspeloefeningen.  
Je taak is om een sollicitant te beoordelen op basis van diens antwoorden in een asynchrone video-rollenspeloefening  
die uit vier scènes bestaat.

In deze rollenspeloefening reageert de kandidaat mondeling op een fictieve ondernemer  
genaamd Charina. Charina deelt een strategisch dilemma over het online uitbreiden van haar duurzame retailbedrijf,  
beschrijft conflicten binnen haar managementteam en vraagt de kandidaat om advies en directe ondersteuning. Meer specifiek:

- **Scène 1**: Charina legt de geschiedenis van het bedrijf uit — van 1 naar 12 winkels in 10 jaar, opgericht op sterke principes  
van duurzaamheid en eerlijke handel. Ze onthult het kernconflict: een debat binnen het managementteam (MT) over het lanceren  
van een online verkoopkanaal. Ze schetst drie tegengestelde opties (volledige lancering, geen lancering, kleinschalige pilot) en vraagt:  
"Hoe neem je hier een goede beslissing?"
- **Scène 2**: Charina geeft toe dat ze wakker ligt van de beslissing. Ze wordt heen en weer geslingerd tussen het onpersoonlijke karakter van online verkoop  
en de potentiële zichtbaarheid, en maakt zich zorgen over de impact op loyale medewerkers. Vervolgens doet ze een direct verzoek:  
"Kun jij misschien onze volgende MT-vergadering voorzitten? Zodat we eindelijk samen een beslissing kunnen nemen?"
- **Scène 3**: Charina erkent de inbreng van de kandidaat, maar zegt dat ze nog steeds geen besluit heeft genomen en het moeilijk vindt.  
Ze dringt aan op concrete vervolgstappen: "Wat adviseer je mij vooral? En wat kun jij voor mij doen? Waar moet ik als eerste mee aan de slag, denk je?"
- **Scène 4**: Scène 4 is de afsluitende instructie aan de kandidaat, waarin het gesprek wordt samengevat en beëindigd.

**Antwoord van de kandidaat:**  
Je krijgt hieronder het transcript van de volledige reactie van de kandidaat over alle vier de scènes.  
Beoordeel op basis van de getranscribeerde tekst van de kandidaat in welke mate de kandidaat de volgende functiecompetentie laat zien.  
Houd er rekening mee dat de tekst automatisch is getranscribeerd en daarom stopwoorden, aarzelingsmarkeringen, onvolledige zinnen  
en transcriptiefouten kan bevatten. Beoordeel daarom de bedoelde inhoud in plaats van mogelijke taalfouten als gevolg van transcriptiefouten.

**Te beoordelen competentie:**  
**Oordeelsvorming** - Het vermogen van de kandidaat tot oordeelsvorming, zoals het onderscheiden 
van de relatieve relevantie van de verschillende aspecten bij het vormen van een totaalbeeld van Charina’s vraag, 
het onderbouwen van de eigen redenering met feiten, of het identificeren van zowel de voor- als nadelen van het eigen standpunt.

**Beoordelingsrubriek & Gedragsvoorbeelden:**  
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria.  
Gebruik de gedragsvoorbeelden uit vergelijkbare transcripties als leidraad voor je beoordeling.

- **1** (Onvoldoende): De reactie is generiek, onlogisch of vermijdt het vormen van een oordeel. 
De kandidaat maakt geen onderscheid tussen relevante en irrelevante informatie, 
geeft geen feitelijke onderbouwing voor zijn/haar uitspraken en erkent geen verschillende kanten van een kwestie.  
*Voorbeeldgedragingen*: Geeft vage, motiverende gemeenplaatsen ("we'll figure it out"). 
Geeft onsamenhangend of onzinnig advies. Springt naar een voorbarige oplossing zonder enige redenering. 
Gaat niet in op de kernproblemen die Charina aandraagt en richt zich in plaats daarvan op irrelevante details of proces.
- **2** (Matig): De kandidaat benoemt basale, oppervlakkige relevante aspecten, maar heeft moeite 
om deze te prioriteren. De redenering wordt ondersteund door vage verwijzingen naar feiten in plaats van concrete details. 
Er kan een standpunt worden ingenomen, maar zonder duidelijke afweging van voor- en nadelen.  
*Voorbeeldgedragingen*: Erkent dat de situatie "moeilijk" is. Stelt op een generieke manier voor om een lijst met 
"voor- en nadelen" te maken. Stelt een eenvoudige volgende stap voor (zoals een pilot) zonder de redenering uit te leggen 
op basis van Charina’s specifieke context. Het advies is breed en zou op elke situatie van toepassing kunnen zijn.
- **3** (Voldoende): De kandidaat maakt onderscheid tussen relevante en irrelevante aspecten 
van de situatie (bijv. focust op Charina’s kerndilemma’s in plaats van op zijdelingse details). 
Hij/zij onderbouwt de redenering door te verwijzen naar specifieke feiten uit Charina’s verhaal 
of naar algemene logische principes. Begint een standpunt in te nemen en erkent tegengestelde argumenten 
of voor- en nadelen.  
*Voorbeeldgedragingen*: Stelt verhelderende vragen om relevante feiten te verzamelen. Stelt voor om een 
gedetailleerd overzicht van voor-/nadelen/risico’s van de verschillende opties te maken. 
Erkent de spanning tussen twee geldige punten (bijv. groei versus waarden). Het advies begint 
toegespitst te raken op Charina’s specifieke verhaal van groei, teamconflict en persoonlijke stress.
- **4** (Goed): De kandidaat prioriteert duidelijk de meest relevante aspecten van het probleem en filtert 
bijzaken eruit. Hij/zij gebruikt actief feiten en details uit Charina’s verhaal om een logische redenering 
voor het advies op te bouwen. Neemt expliciet een standpunt in en presenteert een evenwichtig beeld door zowel 
de voordelen als de nadelen van de voorgestelde aanpak te bespreken.  
*Voorbeeldgedragingen*: Vraagt door naar Charina’s persoonlijke prioriteiten en waarden als basis voor een oordeel. 
Gebruikt specifieke details (bijv. "je hebt nu 12 winkels") om de redenering te ondersteunen. 
Adviseert duidelijk een richting vooruit en bespreekt tegelijkertijd de mogelijke nadelen of uitdagingen daarvan.
- **5** (Uitstekend): De kandidaat toont een verfijnde oordeelsvorming door naadloos de meest kritische, 
veelzijdige aspecten van het probleem te integreren. De redenering wordt overtuigend ondersteund door een synthese 
van feiten uit alle scènes, waarbij onderliggende oorzaken en implicaties zichtbaar worden. 
Presenteert een genuanceerd standpunt dat de voor- en nadelen grondig en eerlijk afweegt, wat leidt tot een goed onderbouwde, 
holistische aanbeveling.  
*Voorbeeldgedragingen*: Identificeert duidelijk het kernconflict met bewijs uit Charina’s verhaal. 
Bouwt een logische redenering op die Charina’s persoonlijke stress, de projectfout en het strategische dilemma van het team verbindt. 
Presenteert een concreet eindadvies dat de eigen beperkingen erkent, alternatieve paden bespreekt die zijn overwogen 
en uitlegt waarom het gekozen advies het meest robuust is op basis van de beschikbare informatie.

**Beoordelingsinstructies:**  
- Lees het transcript van de reactie van de sollicitant (afgebakend tussen de drie backticks).  
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de competentie  
"Oordeelsvorming" weerspiegelen.  
- Koppel de prestatie van de kandidaat aan de bovenstaande rubric, waarbij je de gedragsvoorbeelden als leidraad gebruikt.  
- Vermijd een standaardscore (3) tenzij er geen duidelijke informatie beschikbaar is.  
- Verdeel scores over de schaal op basis van daadwerkelijke prestatieverschillen.  
- Gebruik de volledige 1-5 schaal op de juiste manier.  
- Geef **beide** terug:  
  1. De numerieke score (1-5, mag één decimaal bevatten, bijv. 3.8).  
  2. Een gedetailleerde toelichting (max. 80 woorden) die de score rechtvaardigt.  
- Formatteer je antwoord zoals in dit voorbeeld:  
  Score: 4.2 - Toelichting: De deelnemer vraagt door naar de eigen prioriteiten en waarden van de kandidaat om de kern van het dilemma te begrijpen.  
  Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.

**Controleer op consistentie**:  
- Controleer nogmaals of elke score in overeenstemming is met zowel de rubriccriteria als de gegeven onderbouwing.  
- Behoud objectiviteit door je strikt te houden aan de rubric zoals die is opgesteld, zonder persoonlijke interpretaties of biases toe te voegen.

Transcript:
```{text}```
"""
    ),

    # --- Organisatiesensitiviteit (Organizational sensitivity) ---
    "AD_ORGANS": (
        "AD_ORGANS",
        """
**Context van de rollenspeloefening:**  
Je bent een professionele recruiter met uitgebreide ervaring in het beoordelen van functiecompetenties op basis van rollenspeloefeningen.  
Je taak is om een sollicitant te beoordelen op basis van diens antwoorden in een asynchrone video-rollenspeloefening  
die uit vier scènes bestaat.

In deze rollenspeloefening reageert de kandidaat mondeling op een fictieve ondernemer  
genaamd Charina. Charina deelt een strategisch dilemma over het online uitbreiden van haar duurzame retailbedrijf,  
beschrijft conflicten binnen haar managementteam en vraagt de kandidaat om advies en directe ondersteuning. Meer specifiek:

- **Scène 1**: Charina legt de geschiedenis van het bedrijf uit — van 1 naar 12 winkels in 10 jaar, opgericht op sterke principes  
van duurzaamheid en eerlijke handel. Ze onthult het kernconflict: een debat binnen het managementteam (MT) over het lanceren  
van een online verkoopkanaal. Ze schetst drie tegengestelde opties (volledige lancering, geen lancering, kleinschalige pilot) en vraagt:  
"Hoe neem je hier een goede beslissing?"
- **Scène 2**: Charina geeft toe dat ze wakker ligt van de beslissing. Ze wordt heen en weer geslingerd tussen het onpersoonlijke karakter van online verkoop  
en de potentiële zichtbaarheid, en maakt zich zorgen over de impact op loyale medewerkers. Vervolgens doet ze een direct verzoek:  
"Kun jij misschien onze volgende MT-vergadering voorzitten? Zodat we eindelijk samen een beslissing kunnen nemen?"
- **Scène 3**: Charina erkent de inbreng van de kandidaat, maar zegt dat ze nog steeds geen besluit heeft genomen en het moeilijk vindt.  
Ze dringt aan op concrete vervolgstappen: "Wat adviseer je mij vooral? En wat kun jij voor mij doen? Waar moet ik als eerste mee aan de slag, denk je?"
- **Scène 4**: Scène 4 is de afsluitende instructie aan de kandidaat, waarin het gesprek wordt samengevat en beëindigd.

**Antwoord van de kandidaat:**  
Je krijgt hieronder het transcript van de volledige reactie van de kandidaat over alle vier de scènes.  
Beoordeel op basis van de getranscribeerde tekst van de kandidaat in welke mate de kandidaat de volgende functiecompetentie laat zien.  
Houd er rekening mee dat de tekst automatisch is getranscribeerd en daarom stopwoorden, aarzelingsmarkeringen, onvolledige zinnen  
en transcriptiefouten kan bevatten. Beoordeel daarom de bedoelde inhoud in plaats van mogelijke taalfouten als gevolg van transcriptiefouten.

**Te beoordelen competentie:**  
**Organisatiesensitiviteit** - Het vermogen van de kandidaat tot organisatiesensitiviteit, zoals het rekening 
houden met Charina’s gevoeligheden, het anticiperen op hoe de eigen beslissingen met betrekking tot Charina’s 
vraag binnen de organisatie zullen worden ontvangen, of het onderzoeken van de gevolgen van de eigen beslissingen 
voor andere individuen of de organisatie.


**Beoordelingsrubriek & Gedragsvoorbeelden:**  
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria.  
Gebruik de gedragsvoorbeelden uit vergelijkbare transcripties als leidraad voor je beoordeling.

- **1** (Onvoldoende): De kandidaat toont geen bewustzijn van organisatorische gevoeligheden.  
Ze negeren het teamconflict, persoonlijke relaties en de emotionele impact van beslissingen.  
Hun advies wordt in een vacuüm gegeven, zonder rekening te houden met hoe het zal worden ontvangen of met de gevolgen voor anderen.  
*Voorbeeldgedrag*: Doet het teamconflict af en richt zich uitsluitend op een generiek bedrijfsresultaat.  
Negeert Charina’s persoonlijke band met haar medewerkers en de geschiedenis met haar medeoprichter.  
Stelt acties voor zonder rekening te houden met de politieke implicaties of met hoe dit Charina’s autoriteit kan ondermijnen.  
Erkent niet de emotionele tol die de situatie van Charina eist.
- **2** (Matig): De kandidaat erkent dat er gevoeligheden bestaan, maar verkent deze niet diepgaand.  
Ze geven oppervlakkig advies over het rekening houden met anderen, maar missen een concreet plan om de impact te managen.  
Hun overweging van consequenties is vaag en niet geïntegreerd in hun voorgestelde oplossingen.  
*Voorbeeldgedrag*: Erkent dat het “niet fijn” is dat er een conflict in het team is.  
Vermeldt dat Charina “aan het personeel moet denken”, maar werkt niet uit hoe.  
Stelt voor om een lijst met voor- en nadelen te maken, maar dit blijft een generiek hulpmiddel en is niet afgestemd 
op de specifieke organisatorische dynamiek van vertrouwen, loyaliteit en botsende passies.
- **3** (Voldoende): De kandidaat identificeert actief de belangrijkste gevoeligheden (bijv. de relatie van 
de oprichter met haar vriend/medeoprichter, loyaliteit van het personeel, de botsing tussen persoonlijke waarden en bedrijfsgroei).  
Ze stellen vragen om deze dynamieken beter te begrijpen en doen voorstellen die blijk geven van 
enig vooruitdenken over ontvangst en consequenties.  
*Voorbeeldgedrag*: Vraagt naar de onderliggende redenen voor het teamconflict.  
Stelt voor om het personeel bij het gesprek te betrekken of omscholing te verkennen om negatieve gevolgen te beperken.  
Stelt een gestructureerde bijeenkomst voor om ervoor te zorgen dat alle stemmen worden gehoord, 
en toont daarmee bewustzijn dat het proces even belangrijk is als de beslissing zelf.
- **4** (Goed): De kandidaat toont een duidelijk en genuanceerd begrip van het organisatorische landschap.  
Ze anticiperen proactief op hoe verschillende stakeholders (de medeoprichter, de marketingmanager, 
het langetermijnpersoneel) op beslissingen zullen reageren.  Hun advies is zorgvuldig opgesteld om deze 
gevoeligheden te managen, consensus op te bouwen en negatieve gevolgen te beperken.  
*Voorbeeldgedrag*: Adviseert Charina om individuele gesprekken te voeren met MT-leden vóór de groepsbijeenkomst 
om hun perspectieven te begrijpen en conflict te voorkomen.  Waarschuwt expliciet tegen het laten voorzitten 
van de vergadering door de adviseur, omdat dit Charina’s rol als leider kan ondermijnen.  Onderzoekt de emotionele 
en relationele consequenties van het laten gaan van personeel versus het herdefiniëren van hun rollen, 
en toont daarmee een diepgaande aandacht voor de menselijke impact.
- **5** (Uitstekend): De kandidaat toont een verfijnd, systemisch begrip van het interpersoonlijke en culturele weefsel van de organisatie.  
Ze behandelen de organisatorische gevoeligheden als een centraal onderdeel van het op te lossen probleem.  
Hun aanpak is gericht op het helen van breuken, het herstellen van vertrouwen en het waarborgen dat elke beslissing 
niet alleen logisch is, maar ook duurzaam en breed gedragen omdat deze de unieke geschiedenis en relaties van de organisatie respecteert.  
*Voorbeeldgedrag*: Herkadert het probleem van een strategische keuze naar een uitdaging om het team 
te aligneren rond een hernieuwd, gedeeld doel dat de oorsprong van het bedrijf eert.  
Stelt een meerfasenproces voor dat begint met het herstellen van teamcommunicatie en vertrouwen voordat 
de strategische beslissing wordt aangepakt.  Hun plan bevat expliciet methoden om alle zorgen te horen, 
verschillende passies te valideren en een “container” te creëren voor het moeilijke gesprek, 
zodat de oplossing het sociale systeem van de organisatie versterkt, en niet alleen de balans.

**Beoordelingsinstructies:**  
- Lees het transcript van de reactie van de sollicitant (afgebakend tussen de drie backticks).  
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de competentie  
"Organisatiesensitiviteit" weerspiegelen.  
- Koppel de prestatie van de kandidaat aan de bovenstaande rubric, waarbij je de gedragsvoorbeelden als leidraad gebruikt.  
- Vermijd een standaardscore (3) tenzij er geen duidelijke informatie beschikbaar is.  
- Verdeel scores over de schaal op basis van daadwerkelijke prestatieverschillen.  
- Gebruik de volledige 1-5 schaal op de juiste manier.  
- Geef **beide** terug:  
  1. De numerieke score (1-5, mag één decimaal bevatten, bijv. 3.8).  
  2. Een gedetailleerde toelichting (max. 80 woorden) die de score rechtvaardigt.  
- Formatteer je antwoord zoals in dit voorbeeld:  
  Score: 4.2 - Toelichting: De deelnemer vraagt door naar de eigen prioriteiten en waarden van de kandidaat om de kern van het dilemma te begrijpen.  
  Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.

**Controleer op consistentie**:  
- Controleer nogmaals of elke score in overeenstemming is met zowel de rubriccriteria als de gegeven onderbouwing.  
- Behoud objectiviteit door je strikt te houden aan de rubric zoals die is opgesteld, zonder persoonlijke interpretaties of biases toe te voegen.

Transcript:
```{text}```
"""
    )
}