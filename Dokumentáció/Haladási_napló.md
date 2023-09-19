# Haladási napló

### Első hét

Az elmúlt héten leginkáb azzal voltam elfoglalva, hogy a témába beleássam magam. 
Megnéztem a gyorstalpaló kurzus első két heti anyagát, illetve olvasgattam a témában
több cikket is ami ezzel foglalkozik.

Jelenleg még mindig nem egyértelmű számomra, hogy a gyakorlatban hogyan fog megvalósulni a projekt.
Felmerült bennem két kérdés:

    - Lehetséges, hogy több modell ötvözéséből jön majd létre a végső alkalmazás? (egy kérdés/válasz értelmező + egy pontozó LLM)
    - Hogyan fog létrejönni az én datasetem a fine-tuninghoz?

A project lifecycle-t ha követem a következő feladatok várnak rám:
 
    1. Use case meghatározása  (Ez elvileg készen van)
    2. Modell kiválasztása  --> Encoder-only? (BERT)
    3. Prompt engineering, fine-tuning, evaluate   + Dataset összeállítása
    4. Alkalmazás integrálása

Jelenleg azt tervezem, hogy 8 hét alatt végzek az LLM-el, és a maradék időben annak
integrálására fogok koncentrálni.
Reményeim szerint a jövőhét folyamán megtalálom a megfelelő transformer architektúrát,
és elkészítem az első prototípust.

Elkezdtem megírni a specifikációmat is, az LLM leírása már fent van a githubon.
Az önlab keretein belül a megbeszélteknek megfelelően elsősorban erre koncetrálnék.

### Második hét

Az előző alkalom óta elkezdtem kísérletezgetni LLM-ekkel, megcsináltam több tutorialt is,
szereztem némi gyakorlati tapasztalatot fine-tune-olásban. 

Mivel számomra teljesen új maga a python nyelv is, utána kellett néznem több esetben 
a szintaxisnak, illetve több library működésének: pandas, numpy, datasets, evaluate.

Traineléshez kipróbáltam a tensorflowt, illetve a pytorchot is. Egyelőre a pytorch tűnik számomra szimpatikusabbnak,
mivel lehetőség van nativ tuneolásra.

Megismerkedtem az adatok preprocesszálásához használt eszközökkel, mint a padding, trucation, tokenization, mapping.
Kezd összeállni a kép, hogy hogyan is kell elképzelni egy modell fine-tune-olását, azonban még messze a cél.
Egyre inkább látom, hogy valóban vannak mélységei ennek a témának, és nem olyan egyszerű ez a gyakorlatban, 
mint ahogy azt én az elején elképzeltem. 

Beszéltünk róla az első héten, hogy Szerinted érdemes lenne vscode-ot használni a fejlesztéshez, 
azonban egyelőre még nem találtam meg a megfelelő setupot hozzá.
Probálkoztam az egyik tutorialban említett unweave-vel, mivel jelenleg nem áll rendelkezésemre egyetlen gpu sem, 
azonban ez valamiert nem működött. Így a példa-kódokat egyelőre csak google colabban tudtam futtatni.
Amennyiben Te rendelkezel gyakorlattal az unweave használatában, elfogadnék benne némi segítséget... 
Az egészhez még kicsit hozzátartozik, hogy vasárnap végül elegem lett a windowsból, és azóta az ubuntus közösséget gyarapítom. :)

Ma még utána fogok nézni, hogy az egyes modelleket fine-tuneolás után hogyan lehet lementeni, 
majd egy másik alkalmazásban felhasználni.  
