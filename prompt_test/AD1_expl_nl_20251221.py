# prompts have the following structure: 
# for each competence, the first prompt is about providing verbal explanation (number + explanation),
# the second prompt is about numerical annotation only.

# Define general instructions for competence annotation

promptAD = {
    # --- Probleemanalyse (Problem analysis) ---
    "AD_PROBL": (
        "AD_PROBL",
        """
        **Context van de rollenspel-oefening:**
Je bent een professionele recruiter. Je taak is om een sollicitant te evalueren op basis van hun antwoorden 
in een rollenspel-oefening. In deze oefening reageert de kandidaat verbaal op een fictieve collega genaamd Lara, 
verspreid over vier scènes. Lara deelt professionele frustraties, fouten bij klantprojecten, emotionele uitputting, 
en persoonlijke financiële zorgen, en vraagt de kandidaat om ondersteuning en advies. Samengevat:

- **Scène 1**: Lara uit frustratie over het over het hoofd worden gezien op het werk, het uitvoeren van repetitieve taken, 
en het gebrek aan groeimogelijkheden. Ze vraagt om advies.
- **Scène 2**: Lara bekent dat ze twee klantprojecten verkeerd heeft aangepakt, wat heeft geleid tot kostenproblemen en klantontevredenheid. 
Ze is bang om het aan de teamleider te vertellen en vraagt of de kandidaat namens haar kan spreken.
- **Scène 3**: Lara onthult emotionele uitputting en financiële stress vanwege de chronische ziekte van haar dochter. 
Ze vraagt zich af of ze extra verlof kan krijgen of dat de kandidaat enkele taken kan overnemen.
- **Scène 4**: Lara voelt zich iets beter maar nog steeds overweldigd. Ze vraagt de kandidaat om concreet advies 
over wat ze hierna moet doen.

**Reactie van de kandidaat**:
Je krijgt het transcript van de volledige reactie van de kandidaat over alle vier de scènes hieronder. 
De reacties van de kandidaat voor elke scène zijn samengevoegd tot één tekst en gescheiden 
door een puntkomma (;). Elke puntkomma duidt het begin van de reactie van de kandidaat op een nieuwe scène aan.

De tekst is automatisch getranscribeerd, dus kan vulwoorden, aarzelingstekens, 
onvolledige zinnen en transcriptiefouten bevatten. 
Evalueer de bedoelde inhoud in plaats van mogelijke taal- of transcriptiefouten.

**Competentie om te evalueren:**  
**Probleemanalyse** - Het vermogen van de kandidaat om de complexe, veelzijdige situatie 
die Lara presenteert te ontleden, de kernproblemen, hun onderlinge verbanden en relatieve belangrijkheid te identificeren.

**Evaluatierubriek & Gedragsvoorbeelden**:
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria. 
Gebruik de gedragsvoorbeelden uit soortgelijke transcripts als leidraad voor je beoordeling.

- **1** (Slecht): De reactie is algemeen, vermijdt het probleem of richt zich op irrelevante nevenproblemen. 
De kandidaat onderscheidt hoofd- van bijzaken niet, legt geen verbanden en identificeert het kernprobleem niet.
*Voorbeeldgedrag*: Geeft vage, motiverende uitspraken ("Ik ben er voor je"). 
Geeft algemeen advies dat niet gerelateerd is aan Lara's specifieke problemen. 
Komt te snel met een oplossing zonder analyse. De reactie is onsamenhangend en gaat niet in op de kern van Lara's problemen.
- **2** (Redelijk): De kandidaat identificeert oppervlakkige problemen maar behandelt ze geïsoleerd. 
De reactie kan problemen opsommen zonder ze te prioriteren of betekenisvolle verbanden te leggen. 
Het kernprobleem wordt slechts gedeeltelijk of onjuist geïdentificeerd.
*Voorbeeldgedrag*: Erkent dat er "moeilijke keuzes" of "spanningen" zijn. 
Stelt voor om naar "data" te kijken of een "plan te maken" zonder te specificeren hoe. 
Stelt een eenvoudige volgende stap voor (bijv. een pilot) zonder te analyseren waarom dit passend is voor de samenhangende problemen van groei, teamconflict en bedrijfswaarden.
- **3** (Voldoende): De kandidaat identificeert de belangrijkste problemen (bijv. werkfrustratie, 
projectfout, persoonlijke stress) en begint ze met elkaar te verbinden (bijv. persoonlijke stress beïnvloedt 
werkprestaties). Ze kunnen hoofd- en bijzaken onderscheiden, maar niet met hoge duidelijkheid. 
Het kernprobleem wordt op basisniveau geïdentificeerd (bijv. "je bent overweldigd").
*Voorbeeldgedrag*: Stelt verduidelijkende vragen over de opties of het teamconflict. 
Stelt verder onderzoek of het maken van een overzicht van voor- en nadelen/risico's voor. 
Erkent de spanning tussen bedrijfsontwikkeling en waarden van het bedrijf. 
Biedt aan om het probleem te structureren voor de volgende vergadering.
- **4** (Goed): De kandidaat onderscheidt duidelijk hoofd- van bijzaken en onderzoekt actief 
de verbanden tussen hen (bijv. hoe over het hoofd gezien worden leidt tot demotivatie, wat kan 
bijdragen aan projectfouten). Ze identificeren een genuanceerder kernprobleem (bijv. een conflict 
tussen persoonlijke waarden en bedrijfsdruk, of een breuk in teamcommunicatie en vertrouwen).
*Voorbeeldgedrag*: Peilt naar de eigen prioriteiten en waarden van de kandidaat om de kern 
van het dilemma te begrijpen. Vraagt naar de onderliggende oorzaken van het teamconflict. 
Stelt een proces voor om het team op één lijn te krijgen rond gedeelde doelen en waarden. 
Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.
- **5** (Uitstekend): De kandidaat toont een verfijnd, holistisch begrip. 
Ze integreren naadloos alle aspecten van het probleem (professioneel, persoonlijk, interpersoonlijk) 
en identificeren de diepe, systemische kern (bijv. gebrek aan psychologische veiligheid, een misalignement 
tussen bedrijfsstrategie en kernidentiteit, of een behoefte aan proactief leiderschap en ondersteuningsstructuren). 
Hun analyse onthult niet voor de hand liggende verbanden en komt tot de fundamentele oorzaak.
*Voorbeeldgedrag*: Identificeert dat het kernprobleem niet alleen de strategische keuze is, 
maar het onvermogen van het team om een constructief, op waarden gebaseerd gesprek te voeren. 
Richt zich op het herstellen van vertrouwen en gedeeld doel als voorwaarde voor besluitvorming. 
Toont een duidelijke, logische lijn van de symptomen (Lara's stress, de projectfout) 
naar een systemische kernoorzaak. Stelt een uitgebreide, gefaseerde aanpak voor die zowel 
de onmiddellijke praktische behoeften als de onderliggende interpersoonlijke/strategische problemen aanpakt.

**Evaluatie-instructies**:
- Lees het transcript van de reactie van de kandidaat (tussen de triple backticks). 
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de 
competentie "Probleemanalyse" weerspiegelt.
- Koppel de prestaties van de kandidaat aan de rubriek hierboven, gebruikmakend van de gedragsvoorbeelden als leidraad.
- Vermijd standaardiseren naar een gemiddelde (3) tenzij er geen duidelijke informatie beschikbaar is.
- Verspreid scores over de schaal op basis van daadwerkelijke prestatieverschillen. 
- Gebruik de volledige 1-5 schaal correct.
- Geef **beide** terug:
  1. De numerieke beoordeling (1-5, kan één decimaal bevatten, bijv. 3.8).
  2. Een korte uitleg (max 80 woorden) ter rechtvaardiging van de beoordeling.
- Formatteer je antwoord zoals dit voorbeeld:
  Beoordeling: 4.2 - Uitleg: De deelnemer peilt naar de eigen prioriteiten en waarden van de kandidaat om de kern van het dilemma te begrijpen. 
Synthetiseert informatie uit verschillende scènes tot een samenhangend beeld van de situatie.

Transcript:
```{text}```
"""
    ),

    # --- Creativiteit (Creativity) ---
    "AD_CREAT": (
        "AD_CREAT",
        """
        **Context van de rollenspel-oefening:**
Je bent een professionele recruiter. Je taak is om een sollicitant te evalueren op basis van hun antwoorden 
in een rollenspel-oefening. In deze oefening reageert de kandidaat verbaal op een fictieve collega genaamd Lara, 
verspreid over vier scènes. Lara deelt professionele frustraties, fouten bij klantprojecten, emotionele uitputting, 
en persoonlijke financiële zorgen, en vraagt de kandidaat om ondersteuning en advies. Samengevat:

- **Scène 1**: Lara uit frustratie over het over het hoofd worden gezien op het werk, het uitvoeren van repetitieve taken, 
en het gebrek aan groeimogelijkheden. Ze vraagt om advies.
- **Scène 2**: Lara bekent dat ze twee klantprojecten verkeerd heeft aangepakt, wat heeft geleid tot kostenproblemen en klantontevredenheid. 
Ze is bang om het aan de teamleider te vertellen en vraagt of de kandidaat namens haar kan spreken.
- **Scène 3**: Lara onthult emotionele uitputting en financiële stress vanwege de chronische ziekte van haar dochter. 
Ze vraagt zich af of ze extra verlof kan krijgen of dat de kandidaat enkele taken kan overnemen.
- **Scène 4**: Lara voelt zich iets beter maar nog steeds overweldigd. Ze vraagt de kandidaat om concreet advies 
over wat ze hierna moet doen.

**Reactie van de kandidaat**:
Je krijgt het transcript van de volledige reactie van de kandidaat over alle vier de scènes hieronder. 
De reacties van de kandidaat voor elke scène zijn samengevoegd tot één tekst en gescheiden 
door een puntkomma (;). Elke puntkomma duidt het begin van de reactie van de kandidaat op een nieuwe scène aan.

De tekst is automatisch getranscribeerd, dus kan vulwoorden, aarzelingstekens, 
onvolledige zinnen en transcriptiefouten bevatten. 
Evalueer de bedoelde inhoud in plaats van mogelijke taal- of transcriptiefouten.

**Competentie om te evalueren:**  
**Creativiteit** - Het vermogen van de kandidaat om nieuwe, diverse en goed geïntegreerde ideeën te genereren 
als reactie op de complexe, veelzijdige problemen van Lara.

**Evaluatierubriek & Gedragsvoorbeelden**:
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria. 
Gebruik de gedragsvoorbeelden uit soortgelijke transcripts als leidraad voor je beoordeling.

- **1** (Slecht): De kandidaat toont geen creativiteit. Hun reactie is algemeen, repetitief, 
of vermijdt het genereren van concrete ideeën. Ze blijven bij clichés en benaderen het probleem niet 
van nieuwe invalshoeken of combineren informatie niet op een originele manier.
*Voorbeeldgedrag*: Herhaalt vage motiverende uitspraken ("we'll figure it out"). Geeft advies dat niet specifiek is voor Lara's situatie. 
Doet geen voorstel voor uitvoerbare ideeën. Stelt een standaardproces voor zoals "brainstormen" of "met het team praten" zonder creatieve inhoud of richting.

- **2** (Redelijk): De kandidaat stelt één of twee basisideeën voor, conventioneel van aard. Ze erkennen mogelijk verschillende perspectieven 
maar verkennen deze niet diepgaand of gebruiken ze niet om oplossingen te genereren. 
Hun ideeën zijn simpele combinaties van bestaande elementen zonder significante originaliteit.
*Voorbeeldgedrag*: Stelt een oppervlakkige oplossing voor zonder uit te leggen hoe een creatieve benadering werkt. 
Erkent dat er opties zijn, maar bouwt hier niet op voort of suggereert geen nieuwe. De ideeën zijn standaard bedrijfsadvies 
en voelen niet afgestemd op Lara's unieke dilemma van waarden, groei en teamconflict.

- **3** (Voldoende): De kandidaat genereert enkele relevante ideeën die verder gaan dan het voor de hand liggende. 
Ze proberen het probleem vanuit meerdere perspectieven te bekijken en combineren verschillende aspecten van Lara's verhaal tot 
een samenhangende, zij het niet uiterst originele suggestie.
*Voorbeeldgedrag*: Stelt een specifiek hybride model voor, zoals "online verkoop met groene levering" of "afhalen in de winkel voor 
online bestellingen." Betrekt verschillende belanghebbenden bij de oplossing. Probeert het probleem te herformuleren, bijvoorbeeld 
van "kiezen voor een optie" naar "hoe een betere teamgesprek voeren over onze waarden".

- **4** (Goed): De kandidaat produceert meerdere originele ideeën die duidelijk afgestemd zijn op de nuances van Lara's situatie. 
Ze synthetiseren actief verschillende perspectieven (bijv. financieel, persoonlijk, teamdynamiek, merkwaarden) om innovatieve oplossingen te creëren. 
Hun aanpak toont flexibiliteit en nieuwe denkwijze.
*Voorbeeldgedrag*: Peilt naar de "kernvisie" van het bedrijf om waardegerichte oplossingen te genereren. Stelt creatieve compromissen voor, 
zoals een "waarden-gebaseerde online winkel" met persoonlijke touch. Stelt een gestructureerd creatief proces voor (bijv. specifieke 
brainstorm of scenario workshop) om nieuwe ideeën met het team te genereren.

- **5** (Uitstekend): De kandidaat toont uitzonderlijke creativiteit door inzichtelijke, niet voor de hand liggende en hooggesofisticeerde ideeën te genereren. 
Ze integreren naadloos alle facetten van het probleem (persoonlijk, strategisch, operationeel) om nieuwe paden of frameworks voor te stellen. 
Hun suggesties tonen een diep, systemisch begrip en introduceren geheel nieuwe, haalbare mogelijkheden.
*Voorbeeldgedrag*: Herformuleert de kernuitdaging van een strategische keuze naar een kans voor teamalignment en merkinnovatie. 
Stelt een multi-fase proces voor dat data-analyse, creatieve workshops en prototyping combineert om een "vierde optie" co-creatief te ontwikkelen. 
Stelt een nieuw bedrijfsmodel voor dat online groei en duurzame waarden elegant verenigt.

**Evaluatie-instructies**:
- Lees het transcript van de reactie van de kandidaat (tussen de triple backticks). 
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de 
competentie "Creativiteit" weerspiegelt.
- Koppel de prestaties van de kandidaat aan de rubriek hierboven, gebruikmakend van de gedragsvoorbeelden als leidraad.
- Vermijd standaardiseren naar een gemiddelde (3) tenzij er geen duidelijke informatie beschikbaar is.
- Verspreid scores over de schaal op basis van daadwerkelijke prestatieverschillen. 
- Gebruik de volledige 1-5 schaal correct.
- Geef **beide** terug:
  1. De numerieke beoordeling (1-5, kan één decimaal bevatten, bijv. 3.8).
  2. Een korte uitleg (max 80 woorden) ter rechtvaardiging van de beoordeling.
- Formatteer je antwoord zoals dit voorbeeld:
  Beoordeling: 4.2 - Uitleg: De deelnemer stelt een gestructureerd creatief proces voor (bijv. specifieke brainstorm 
  of scenario workshop) om nieuwe ideeën met het team te genereren, waardoor creativiteit bij anderen wordt gestimuleerd.


Transcript:
```{text}```
"""
    ),

    # --- Oordeelsvorming (Judgment Formation) ---
    "AD_OORDE": (
        "AD_OORDE",
        """
        **Context van de rollenspel-oefening:**
Je bent een professionele recruiter. Je taak is om een sollicitant te evalueren op basis van hun antwoorden 
in een rollenspel-oefening. In deze oefening reageert de kandidaat verbaal op een fictieve collega genaamd Lara, 
verspreid over vier scènes. Lara deelt professionele frustraties, fouten bij klantprojecten, emotionele uitputting, 
en persoonlijke financiële zorgen, en vraagt de kandidaat om ondersteuning en advies. Samengevat:

- **Scène 1**: Lara uit frustratie over het over het hoofd worden gezien op het werk, het uitvoeren van repetitieve taken, 
en het gebrek aan groeimogelijkheden. Ze vraagt om advies.
- **Scène 2**: Lara bekent dat ze twee klantprojecten verkeerd heeft aangepakt, wat heeft geleid tot kostenproblemen en klantontevredenheid. 
Ze is bang om het aan de teamleider te vertellen en vraagt of de kandidaat namens haar kan spreken.
- **Scène 3**: Lara onthult emotionele uitputting en financiële stress vanwege de chronische ziekte van haar dochter. 
Ze vraagt zich af of ze extra verlof kan krijgen of dat de kandidaat enkele taken kan overnemen.
- **Scène 4**: Lara voelt zich iets beter maar nog steeds overweldigd. Ze vraagt de kandidaat om concreet advies 
over wat ze hierna moet doen.

**Reactie van de kandidaat**:
Je krijgt het transcript van de volledige reactie van de kandidaat over alle vier de scènes hieronder. 
De reacties van de kandidaat voor elke scène zijn samengevoegd tot één tekst en gescheiden 
door een puntkomma (;). Elke puntkomma duidt het begin van de reactie van de kandidaat op een nieuwe scène aan.

De tekst is automatisch getranscribeerd, dus kan vulwoorden, aarzelingstekens, 
onvolledige zinnen en transcriptiefouten bevatten. 
Evalueer de bedoelde inhoud in plaats van mogelijke taal- of transcriptiefouten.

**Competentie om te evalueren:**  
**Oordeelsvorming** - Het vermogen van de kandidaat om een goed onderbouwd, evenwichtig (zowel voor- als nadelen) 
en op feiten gebaseerd oordeel te vormen in reactie op Lara's complexe situatie.

**Evaluatierubriek & Gedragsvoorbeelden**:
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria. 
Gebruik de gedragsvoorbeelden uit soortgelijke transcripts als leidraad voor je beoordeling.

- **1** (Slecht): De reactie is algemeen, onsamenhangend, of vermijdt het vormen van een oordeel. 
De kandidaat onderscheidt relevante van irrelevante informatie niet, levert geen feitelijke onderbouwing, 
en erkent geen verschillende kanten van een kwestie.
*Voorbeeldgedrag*: Geeft vage, motiverende uitspraken ("we'll figure it out"). Geeft onsamenhangend of onzinnig advies. 
Komt te vroeg met een oplossing zonder redenering. Behandelt de kernproblemen van Lara niet, richt zich op irrelevante details of processen.
- **2** (Redelijk): De kandidaat identificeert basale, oppervlakkige relevante aspecten maar heeft moeite 
om deze te prioriteren. Hun redenering wordt ondersteund door vage verwijzingen naar feiten in plaats van concrete details. 
Ze kunnen een standpunt aangeven zonder duidelijke afweging van voor- en nadelen.
*Voorbeeldgedrag*: Erkent dat de situatie "moeilijk" is. Stelt voor om een lijst van "voor- en nadelen" te maken op een algemene manier. 
Stelt een eenvoudige volgende stap voor (bijv. een pilot) zonder uitleg te geven op basis van Lara's specifieke context. Het advies is breed en toepasbaar op elke situatie.
- **3** (Voldoende): De kandidaat onderscheidt relevante van irrelevante aspecten 
van de situatie (bijv. focust op Lara's kernproblemen in plaats van tangentiële details). 
Ze onderbouwen hun redenering met verwijzingen naar specifieke feiten uit Lara's verhaal of algemene logische principes. 
Ze beginnen een standpunt in te nemen en erkennen tegenargumenten of voor- en nadelen.
*Voorbeeldgedrag*: Stelt verduidelijkende vragen om relevante feiten te verzamelen. Stelt een gedetailleerd overzicht van voor- 
en nadelen/risico's voor de verschillende opties voor. Erkent de spanning tussen twee geldige punten (bijv. groei versus waarden). 
Hun advies wordt afgestemd op Lara's specifieke verhaal van groei, teamconflict en persoonlijke stress.
- **4** (Goed): De kandidaat prioriteert duidelijk de meest relevante aspecten van het probleem en filtert nevenzaken eruit. 
Ze gebruiken actief feiten en details uit Lara's verhaal om een logische argumentatie voor hun advies op te bouwen. 
Ze geven expliciet hun standpunt aan en presenteren een gebalanceerd beeld door zowel de voordelen 
als nadelen van hun voorgestelde aanpak te bespreken.
*Voorbeeldgedrag*: Peilt naar Lara's persoonlijke prioriteiten en waarden om een oordeel te vormen. 
Gebruikt specifieke details (bijv. "je hebt nu 12 winkels") om hun redenering te ondersteunen. Geeft duidelijk een pad vooruit aan, 
terwijl ook mogelijke nadelen of uitdagingen besproken worden.
- **5** (Uitstekend): De kandidaat toont een verfijnd oordeel door naadloos de meest kritieke, veelzijdige aspecten van het probleem te integreren. 
Hun redenering wordt overtuigend ondersteund door een synthese van feiten uit alle scènes, onthult onderliggende oorzaken en implicaties. 
Ze presenteren een genuanceerd standpunt dat voor- en nadelen grondig en eerlijk evalueert, leidend tot een goed onderbouwde, holistische aanbeveling.
*Voorbeeldgedrag*: Identificeert het kernconflict duidelijk met bewijs uit Lara's verhaal. Bouwt een logische argumentatie die Lara's 
persoonlijke stress, projectfout en strategisch dilemma van het team verbindt. Presenteert een concrete eindaanbeveling die 
de beperkingen erkent, alternatieve paden bespreekt en verklaart waarom het gekozen advies het meest robuust is op basis van beschikbare informatie.

**Evaluatie-instructies**:
- Lees het transcript van de reactie van de kandidaat (tussen de triple backticks). 
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de 
competentie "Oordeelsvorming" weerspiegelt.
- Koppel de prestaties van de kandidaat aan de rubriek hierboven, gebruikmakend van de gedragsvoorbeelden als leidraad.
- Vermijd standaardiseren naar een gemiddelde (3) tenzij er geen duidelijke informatie beschikbaar is.
- Verspreid scores over de schaal op basis van daadwerkelijke prestatieverschillen. 
- Gebruik de volledige 1-5 schaal correct.
- Geef **beide** terug:
  1. De numerieke beoordeling (1-5, kan één decimaal bevatten, bijv. 3.8).
  2. Een korte uitleg (max 80 woorden) ter rechtvaardiging van de beoordeling.
- Formatteer je antwoord zoals dit voorbeeld:
  Beoordeling: 4.2 - Uitleg: De deelnemer peilt naar persoonlijke prioriteiten om een oordeel te vormen. Gebruikt specifieke details om 
  hun redenering te ondersteunen. Geeft duidelijk een pad vooruit aan terwijl ook mogelijke nadelen of uitdagingen besproken worden.

Transcript:
```{text}```
"""
    ),

    # --- Organisatiesensitiviteit (Organizational sensitivity) ---
    "AD_ORGANS": (
        "AD_ORGANS",
        """
        **Context van de rollenspel-oefening:**
Je bent een professionele recruiter. Je taak is om een sollicitant te evalueren op basis van hun antwoorden 
in een rollenspel-oefening. In deze oefening reageert de kandidaat verbaal op een fictieve collega genaamd Lara, 
verspreid over vier scènes. Lara deelt professionele frustraties, fouten bij klantprojecten, emotionele uitputting, 
en persoonlijke financiële zorgen, en vraagt de kandidaat om ondersteuning en advies. Samengevat:

- **Scène 1**: Lara uit frustratie over het over het hoofd worden gezien op het werk, het uitvoeren van repetitieve taken, 
en het gebrek aan groeimogelijkheden. Ze vraagt om advies.
- **Scène 2**: Lara bekent dat ze twee klantprojecten verkeerd heeft aangepakt, wat heeft geleid tot kostenproblemen en klantontevredenheid. 
Ze is bang om het aan de teamleider te vertellen en vraagt of de kandidaat namens haar kan spreken.
- **Scène 3**: Lara onthult emotionele uitputting en financiële stress vanwege de chronische ziekte van haar dochter. 
Ze vraagt zich af of ze extra verlof kan krijgen of dat de kandidaat enkele taken kan overnemen.
- **Scène 4**: Lara voelt zich iets beter maar nog steeds overweldigd. Ze vraagt de kandidaat om concreet advies 
over wat ze hierna moet doen.

**Reactie van de kandidaat**:
Je krijgt het transcript van de volledige reactie van de kandidaat over alle vier de scènes hieronder. 
De reacties van de kandidaat voor elke scène zijn samengevoegd tot één tekst en gescheiden 
door een puntkomma (;). Elke puntkomma duidt het begin van de reactie van de kandidaat op een nieuwe scène aan.

De tekst is automatisch getranscribeerd, dus kan vulwoorden, aarzelingstekens, 
onvolledige zinnen en transcriptiefouten bevatten. 
Evalueer de bedoelde inhoud in plaats van mogelijke taal- of transcriptiefouten.

**Competentie om te evalueren:**  
**Organisatiesensitiviteit** - Het empathisch vermogen van de kandidaat, het bewustzijn van en rekening houden met 
interpersoonlijke dynamiek, onuitgesproken regels, en de potentiële impact van hun beslissingen 
op verschillende mensen en afdelingen binnen Lara's organisatie.

**Evaluatierubriek & Gedragsvoorbeelden**:
Beoordeel de kandidaat op een schaal van 1 tot 5 op basis van de volgende criteria. 
Gebruik de gedragsvoorbeelden uit soortgelijke transcripts als leidraad voor je beoordeling.

- **1** (Slecht): De kandidaat toont geen bewustzijn van organisatiesensitiviteiten. 
Ze negeren het teamconflict, persoonlijke relaties en de emotionele impact van beslissingen. 
Hun advies wordt gegeven in een vacuüm, zonder rekening te houden met de ontvangst of gevolgen voor anderen.
*Voorbeeldgedrag*: Negeert het teamconflict en focust alleen op generieke bedrijfsresultaten. 
Negeert Lara's persoonlijke band met het personeel en de geschiedenis met haar medeoprichter. 
Stelt acties voor zonder rekening te houden met politieke implicaties of hoe dit Lara's autoriteit kan ondermijnen. Negeert de emotionele tol die de situatie voor Lara heeft.
- **2** (Redelijk): De kandidaat erkent dat er sensitiviteiten bestaan maar verkent deze niet diepgaand. 
Ze geven oppervlakkig advies over rekening houden met anderen, maar missen een concreet plan om de impact te beheren. 
Hun afweging van gevolgen is vaag en niet geïntegreerd in de voorgestelde oplossing.
*Voorbeeldgedrag*: Erkent dat het "niet leuk" is dat er conflict is in het team. Vermeldt dat Lara "aan het personeel moet denken" 
maar gaat niet in op hoe. Stelt een lijst van voor- en nadelen voor, maar dit is een algemeen hulpmiddel, niet afgestemd op de specifieke 
organisatorische dynamiek van vertrouwen, loyaliteit en conflicterende belangen.
- **3** (Voldoende): De kandidaat identificeert actief belangrijke sensitiviteiten (bijv. de relatie van de oprichter met haar vriend/medeoprichter, 
loyaliteit van het personeel, clash tussen persoonlijke waarden en bedrijfsontwikkeling). 
Ze stellen vragen om deze dynamiek beter te begrijpen en stellen stappen voor die enige vooruitziende blik tonen over ontvangst en gevolgen.
*Voorbeeldgedrag*: Vraagt naar de onderliggende redenen van het teamconflict. Stelt voor het personeel bij het gesprek te betrekken of retraining 
te verkennen om negatieve gevolgen te verminderen. Stelt een gestructureerde vergadering voor om ervoor te zorgen dat alle stemmen gehoord worden, 
toont bewustzijn dat het proces net zo belangrijk is als de beslissing zelf.
- **4** (Goed): De kandidaat toont een duidelijk en genuanceerd begrip van het organisatorische landschap. 
Ze anticiperen proactief hoe verschillende stakeholders (medeoprichter, marketingmanager, langdurig personeel) 
zullen reageren op beslissingen. Hun advies is zorgvuldig opgesteld om deze sensitiviteiten te beheren, consensus op te bouwen, en negatieve gevolgen te beperken.
*Voorbeeldgedrag*: Adviseert Lara individuele gesprekken te voeren met MT-leden vóór de groepsvergadering om hun perspectieven te begrijpen 
en conflicten te voorkomen. Waarschuwt expliciet dat de adviseur de vergadering niet moet leiden, omdat dit Lara's leiderschapsrol kan ondermijnen. 
Peilt naar de emotionele en relationele gevolgen van het ontslaan van personeel versus het aanpassen van hun rollen, toont diepgaande consideratie voor menselijke impact.
- **5** (Uitstekend): De kandidaat toont een verfijnd, systemisch begrip van het interpersoonlijke en culturele weefsel van de organisatie. 
Ze behandelen organisatiesensitiviteiten als een centraal onderdeel van het probleem dat opgelost moet worden. Hun aanpak is ontworpen om scheuren te helen, 
vertrouwen te herstellen, en ervoor te zorgen dat beslissingen niet alleen logisch, maar ook duurzaam en breed gedragen zijn omdat ze de unieke 
geschiedenis en relaties van de organisatie respecteren.
*Voorbeeldgedrag*: Herformuleert het probleem van een strategische keuze naar een uitdaging om het team op één lijn te krijgen rond een vernieuwd 
gedeeld doel dat de oorsprong van het bedrijf eert. Stelt een meerfasig proces voor dat begint met het herstellen van teamcommunicatie en vertrouwen 
voordat strategische beslissingen worden genomen. Het plan bevat expliciet methoden om alle zorgen te horen, verschillende belangen te valideren, 
en een "container" te creëren voor moeilijke gesprekken, zodat de oplossing het sociale systeem van de organisatie versterkt, niet alleen de balans.

**Evaluatie-instructies**:
- Lees het transcript van de reactie van de kandidaat (tussen de triple backticks). 
- Richt je op verbale gedragingen en de analytische inhoud van de reactie die de 
competentie "Organisatiesensitiviteit" weerspiegelt.
- Koppel de prestaties van de kandidaat aan de rubriek hierboven, gebruikmakend van de gedragsvoorbeelden als leidraad.
- Vermijd standaardiseren naar een gemiddelde (3) tenzij er geen duidelijke informatie beschikbaar is.
- Verspreid scores over de schaal op basis van daadwerkelijke prestatieverschillen. 
- Gebruik de volledige 1-5 schaal correct.
- Geef **beide** terug:
  1. De numerieke beoordeling (1-5, kan één decimaal bevatten, bijv. 3.8).
  2. Een korte uitleg (max 80 woorden) ter rechtvaardiging van de beoordeling.
- Formatteer je antwoord zoals dit voorbeeld:
  Beoordeling: 4.2 - Uitleg: De deelnemer peilt naar de emotionele en relationele gevolgen van het ontslaan van personeel versus het aanpassen 
  van hun rollen, toont diepgaande consideratie voor de menselijke impact.

Transcript:
```{text}```
"""
    )
}