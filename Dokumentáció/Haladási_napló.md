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

## Hatodik hét

Az előző hét folyamán igyekeztem végre sikeresen peft fine-tuneolni a flan-t5-ös modelleket, ami váratlan módon minden
módosítás nélkül egyből sikerült. Erre nem nagyon találtam magyarázatot.

Ezután sokat játszadoztam a training paraméterekkel, illetve chatgpt-vel felduzzasztottam a data.json fájlt ehhez.
Kis tesztelgetés után arra kellett rájönnöm, hogy nem igazán fejlődik a modell. Akárhogy fine-tuneoltam, annak ellenére, hogy csak
pontoznia kellett a modellnek a válaszokat a "scoring guide" alapján, nem igazán érződött a fejlődés.
Végülis utánanéztem más dataseteknek, mit tudnék a promptomon csiszolni, és így létrejött egy második formátum is. 
Illetve most már próbáltam a megbeszélteknek megfelelően úgy alakítani a promptot, hogy a végeredmény a pontszámon felül egy szöveges értékelést is tartalmazzon.
Na ez az új verzió chatgptve nagyon jól működött, azonban a flan-t5el ismét csak nem jutottam túl sokra.

Végső soron a többi datasetet elnézve felmerült bennem a kérdés, hogy nem túl komplex-e egy ilyen feladat egy flan-t5 számára.
Múlt héten meg ezen a héten elég sokat próbálkoztam vele, és kezd gyanús lenni, hogy érdemes lenne átállni az openAI API-jára...


## Tizedik hét

Miután a Flan-T5-XL modelljét nem tudtam fine-tuneolni, az elmúlt két hétben elkezdtem kicsit más irányba tapogatózni.
Jobban beleástam magam a LangChain működésébe, és elkezdett gyanús lenni számomra, hogy valahogy az embeddingek irányába kellene  a későbbiekben továbbhaladnom. Eddig promptokkal próbáltam eldöntetni az LLM-ekkel, hogy egy adott kritérium szerepel-e a válaszokban, azonban találtam modelleket, amik kifejezetten mondatok/szövegek szemantikai összehasonlítására vannak kitalálva.

Így került a kezeim közé a SentenceTransformers framework, annak "all-mpnet-base-v2" modellje, amely teljesen szabadon felhasználható, kicsi, gyors, fent van a huggingfacen, és meglehetősen pontosan működik. A data_v3-ban található tesztadatokkal jelenleg 83.3%-os pontosságot értem el, ez elég jelentős javulás az eddigiekhez képest. A HF_Sentencetransformer.ipynb fájlban találhatóak a próbálkozásaim.

Jelenleg úgy képzelem el az alkalmazást, hogy a tanár által létrehozott tesztfeladatok, illetve a hozzájuk tartozó javítási útmutatók 
elmentődnek valamilyen formátumban a szerveren id-vel, így javításnál könnyedén lekérdezhetők lesznek a kritériumok, nem kell vectore storet használni.

Amivel még nem sokat foglalkoztam az a kódok ellenőrzése. Ennek megoldására is egy "Sentence similarity" modellt képzelek el, amelyet már találtam is néhányat, csak a C++ nyelvet ismerőből van hiány. Azonban ha minden igaz ez a szöveges válaszok ellenőrzéséhez elég hasonlóan működhet majd.

Emmellett elvégeztem két gyorstalpaló kurzust a moodle academy oldalán, így plugin fejlesztésben is történtek előrelépések.

## Tizenegyedik hét

A héten leginkább a moodle plugin fejlesztésével foglalkoztam, amivel egész jól haladtam, azonban beleütköztem néhány nehézségbe. Jelenleg ott tartok, hogy felhasználóként értem hogyan működnek az egyes quizek, és van egy elképzelésem, hogy hogyan is illeszkedik majd a kész rendszerbe az én pluginom. 

A legjobb megoldásnak az tűnik, ha átírom a quiz activityt, aminek azonban hiányzik a dokumentációja a moodle oldaláról. Ezt még nem tudom pontosan hogyan fogom kikerülni, azonban az egyes APIkkal már sokat kísérleteztem. Alapvetően az elején ijesztőnek tűnt számomra az egész rendszer, és bár még a tényleges kódnak nem láttam neki, a héten nagyon sokat tisztult számomra mit és hogyan kell majd csinálnom.


## Tizenkettedik hét

## Tizenharmadik hét

Ezen a héten alapvetően a program moodlebe való integrálásán dolgoztam.
A tanár a zh értékelése során amikor egy válasz kísérlet kommentálására megy, a megjelenő ablakban automatikusan kitöltődik a komment fül
a hiányzó gondolatok megjelölésével, és ez alapján a pontszám is becslésre kerül. Amennyiben a javító a mentés gombra megy, az értékelés mentésre kerül. Ellenkező esetben nem mentődik el semmi, és az ablak újranyitásánál a program ismételten átnézi a választ, és értékel.

A működéshez belenyúltam a php kódba, amely így a review ablak megnyitásánál egy kérést intéz a docker konténerben futó backendhez, amely egy a pontszámot, és a kommentet tartalmazó tömbbel tér vissza. A konténer paraméterként a választ, és az értékelési útmutatót kapja meg, amelyeken koszinuszos összehasonlítást végez a sentencetransformers könyvtár segítségével. Az értékelés pontosságával még nem igazán vagyok elégedett, utolsó héten még legfőbbképpen ezen fogok dolgozni. 