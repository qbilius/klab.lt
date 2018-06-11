---
title: LJMS vasara 2011 m.
event: LJMS vasaros stovykla
venue: Molėtų astronomijos observatorija (Lithuania)
date: 2011-07-31 17:00:00
categories: Lectures
datestamp: 2011-08-02 14:54:40
links:
    slides: http://neuromokslai.files.wordpress.com/2011/08/ljms_vasara2011_regos_sistemos_modeliavimas.pdf
---

Atsakymai į paskaitos metu neatsakytus klausimus
================================================

**Perceptronas: kam reikalinga g(x) (25-26 skaidrės)? Gal užtektų tiesiog g(x) = x?**

Yra kelios priežastys naudoti sudėtingesnę funkciją. Iš vienos pusės, neuroniniuose tinkluose kažkiek bandoma išlaikyti panašumą į biologinius neuroninius tinklus. O neuronai turi tam tikras ribas, kiek kartų per sekundę jie gali perduoti impulsą. Jei *g(x)* būtų lygu *x*, tada jokių tokių ribų nebūtų. Todėl praktikoje naudojama, pavyzdžiui, *[Heaviside step funkcija](http://en.wikipedia.org/wiki/Heaviside_step_function)* arba *[sigmoidinė funkcija](http://en.wikipedia.org/wiki/Sigmoid_function)*, kurios turi viršutinę ribą. Iš kitos pusės, jeigu leisim išvesčiai augti be apribojimų, tai dar gali būti, kad visas neuroninis tinklas taps nestabilus ir nepavyks jo ištreniruoti (pasiekti lokalaus minimumo).

**Neurono selektyvumo pokytis (48 skaidrė) – kodėl neurono selektyvumas sumažėja P stimului (šuniukui) ir išauga N stimului (raganosiui)? Juk jeigu P ir N stimulai rodomi greta vienas kito laike, neuronas turėtų išlikti selektyvus P stimului ir, be to, tapti selektyvus N stimului.**

Atkreipkime dėmesį į eksperimento dizainą (47 skaidrė, B). Neuronui parenkami du stimulai: P (*prefered*) stimulas (šuniukas), į kurį neuronas reaguoja aktyviau nei į N (*non-prefered*) stimulą (raganosį). Tada P stimulas asocijuojamas laike su dvigubai didesniu N stimulu, ir atvirkščiai. Vadinasi, neuronas išmoksta traktuoti vidutinio dydžio P stimulą ir didelį N stimulą kaip tą patį objektą.  Testuojant naudojami tik pastarieji, dvigubai didesni stimulai. Ko galima tikėtis? Kad neuronas, kuris šiaip jau mėgsta P stimulus, dabar aktyviai reaguos ir į didelį N stimulą. Taip pat – kad tas pats neuronas, šiaip jau nemėgstantis N stimulų, ims menkiau reaguoti ir į didelį P stimulą.
