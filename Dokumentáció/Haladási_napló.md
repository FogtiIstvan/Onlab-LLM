# Haladási napló

## Első hét

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

## Második hét

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

## Harmadik hét

Ezen a héten elkezdtem összeállítani a promptok formátumát, amit később a fine-tuneoláshoz használni fogok.
Ehhez elsősorban a chatgpt-vel kísérletezgettem, one-shot után pedig már tök jó eredményeket kaptam.
Csináltam few-shotot is, azzal már az ismeretlen feladatok is egészen helyesen lettek pontozva.

Ezután elkezdtem más modellekkel is kísérletezni huggingfacen:

    - google/flan-t5-base/xxl --> a base verzióval nem kaptam eredményeket, xxl-el már volt output, közelítőleg helyes.
    - bert-base-uncased / xlm-roberta-base / roberta-->  volt output, egészen jó. xlm-roberta tud magyarul is.
    - gpt2 --> nem volt output

Az eddigi próbálkozások alapján a (encoder-only) Bert alapú modellek a legjobbak. Kíváncsi vagyok, ha 
rendelkezem majd nagyobb adathalmazzal melyik hogyan fog teljesíteni. Az eddig használt adatok megtalálhatók githubon 
a data.json fájlban, illetve a átláthatobb formátumban az example fájlokban is.

A mai nap folyamán szeretném még a githubra már feltöltött jegyzetfüzetet befejezni, és legalább a flan-t5-ön lefuttatni a 
traininget. 

Ezen kívül ezen a héten különösebb kérdés nem merült fel bennem, a következő lépések is tiszták számomra. Cél lehet jövőhétig a 
bert típusú, és a flan-t5 modellek tesztelése (), esetleg egy gradio tesztfelület elkészítése is hozzá. Ezzel együtt tovább bővíteném
a datasetet is, első lépésbe angol nyelvű, később akár a xlm-bert model számára magyar nyelvű kérdésekkel is. 

## Negyedik hét

Elmaradt

## Ötödik hét

Ezen a héten már tényleg sokat kísérletezgettem a modellekkel, első sorban a flan-t5, illetve a bert alapú modellek
fine-tuneolásával.
Jelen állás szerint a modell feladata egyszerűen osztályozni, azaz egy pontszámot adni a válaszra,
a megadott kérdés, illetve pontozási útmutató kontextusában.

### prompts_flan_t5_base.ipynb

Ebben a fájlban játszadoztam az adatok preprocesszálásával. Elkészült a tokenize függvény, amit a későbbiekben is hazsnálni fogok.
A base modellen kívül kipróbáltam a large modellt is, az xl már ahhoz is túl nagy volt, hogy letöltsem, pontosabban nagyon sokáig tartott volna.
A base modell egyébként egész jó válaszokat adott, full fine-tune után 49%os volt a hibafüggvény.

### prompts_bert_based.ipynb, roberta_fine_tune.ipynb

Ezután kísérletezgettem a Bert alapú modellekkel is. A sima bert nem igazán működött jól,
még azt sem találta el, hogy számjegynek kellene lennie a scorenak.
A roberta ehhez képest egész jól teljesített, meg is próbáltam fine-tuneolni, azonban nem jártam sikerrel:
"TypeError: RobertaModel.forward() got an unexpected keyword argument 'labels'"
Több próbálkozás, és hibaüzenet után idáig jutottam el, azonban ennél már feladtam, és úgy döntöttem mepróbálkozom a flan-t5 large modelljének peftes tuneolásával
(https://hackernoon.com/fine-tuning-roberta-for-topic-classification)

### flan_t5_large_peft.ipynb

Ebben a fájlban találhatók az ehhez kapcsolódó próbálkozásaim, ami szintén nem járt sikerrel. Valamilyen oknál fogva
a google colab mindig úgy döntött, hogy összeomlik trainelésnél, még akkor is, ha csak a base modellel próbálkoztam.

