# RijksBot: van idee tot goedgekeurde Wikidata-bot
**Hoe het Rijksmuseum Wikidata-items veilig en gecontroleerd updatet**

Wat begon als een technisch idee — het automatisch bijwerken van Rijksmuseum-links op bestaande Wikidata-items — groeide uit tot een avontuur door de wereld van open data, community-processen en wiki-syntax.  

## Het probleem

Op Wikidata staan al duizenden objecten uit de collectie van het Rijksmuseum. Veel van deze items bevatten echter een verouderde of ontbrekende URL, waardoor de koppeling met de officiële Rijksmuseum-data niet volledig is. Dit beperkt de vindbaarheid en het gebruik van de data voor onderzoek, visualisaties en andere toepassingen.  

RijksBot pakt dit aan door bestaande Wikidata-items bij te werken: de nieuwe, persistente Rijksmuseum-URL wordt toegevoegd, en waar nodig vult de bot enkele ondersteunende gegevens aan. Zo wordt bijvoorbeeld het objectnummer toegevoegd als deze ontbreekt. Op die manier zijn de items volledig en correct gemodelleerd, terwijl bestaande informatie behouden blijft.

## Wat doet RijksBot precies?

RijksBot voegt altijd het Rijksmuseum ID (`P13234`) toe aan bestaande Wikidata-items. Daarnaast vult de bot, waar nodig, een paar ondersteunende gegevens aan: de collectie (`P195`), het Rijksmuseum objectnummer (`P217`) en de locatie (`P276`). Deze extra gegevens zorgen ervoor dat elk item correct en volledig gemodelleerd is volgens de richtlijnen van Wikidata en de verwachtingen van het Rijksmuseum, zonder bestaande informatie te overschrijven.

Zo blijven de items volledig, correct en consistent, en kunnen onderzoekers en geïnteresseerden gemakkelijker gebruikmaken van de data.

## Veilig testen in de sandbox

Voordat RijksBot op de “echte” Wikidata draaide, werd alles uitgebreid getest in de veilige testomgeving van Wikidata ([test.wikidata.org](https://test.wikidata.org/)).  

Hiermee werd gecontroleerd dat het script correct functioneert, de structuur van Wikidata wordt gerespecteerd en dat er geen roekeloze bewerkingen plaatsvinden. Deze tests waren cruciaal om vertrouwen te winnen bij de community en de reviewers.

## De officiële botaanvraag en community-feedback

De botaanvraag werd ingediend op **Wikidata:Requests for permissions/Bot/RijksBot** waarin duidelijk staat beschreven wat RijksBot doet, hoe vaak hij draait en welke wijzigingen hij doorvoert, inclusief een link naar de code.

De snelle en constructieve reacties van Wikipedianen maakten het proces een stuk vlotter. Dankzij hun aanwijzingen over de zichtbaarheid van de aanvraag en de formulering van de beschrijving werd het proces aanzienlijk eenvoudiger en overzichtelijker.

## Resultaat en impact

Na goedkeuring door de community heeft RijksBot inmiddels **5367 Wikidata-items bijgewerkt**.  

De bot draait nu veilig en gecontroleerd: het Rijksmuseum ID wordt toegevoegd als het nog niet aanwezig is, en de ondersteunende gegevens worden alleen aangevuld waar dat nodig is. Zo blijven de items volledig en correct, terwijl bestaande informatie intact blijft.

Een speciale dank aan de Wikipedianen: hun snelle en constructieve feedback maakte dit project mogelijk en veel efficiënter.

En dit is nog maar het begin. Dankzij wat er nu is opgezet, kan RijksBot in de toekomst eenvoudig meer Wikidata-items bijwerken en eventueel andere eigenschappen toevoegen, zodat de data voor onderzoekers en geïnteresseerden nog waardevoller wordt.

## Conclusie

RijksBot laat zien hoe technische innovatie, open samenwerking en zorgvuldige toetsing binnen de Wikidata-community samenkomen.  

Voor wie een eigen bot overweegt: onderschat het proces niet, maar laat je niet afschrikken — het resultaat is betrouwbare data en een gecontroleerde, transparante samenwerking met de community.

Meer weten over RijksBot en de technische achtergrond? Bekijk onze [GitHub-repository](https://github.com/Jeroen-DeMeester/rijks-wikidata-bot).

RijksBot is opgezet als een flexibel systeem: in de toekomst kan het eenvoudig meer Wikidata-items bijwerken en extra eigenschappen toevoegen, waardoor de data voor onderzoekers en geïnteresseerden nog waardevoller wordt.