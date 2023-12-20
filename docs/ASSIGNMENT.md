V této úloze budeme pracovat s Vaším vlastním rozvrhem. Předpokládejme rozvrh jednoho konkrétního žáka SPŠE Ječná, tedy Vás. (Uvažujeme tedy rozvrh bez dělení, např. mám-li v pondělí předmět PSS a druhá skupina DS, tak uvažuji že v rozvrhu je jen to PSS). 

Prvním krokem v této úloze je vymyslet, jak rozvrh zachytit pomocí nějakého modelu nebo datové struktury. Například velmi zjednodušeně, budeme-li ignorovat učebny, učitele a nebudeme rozlišovat cvičení a teorii, by to mohlo třeba být takto:

```python
rozvrh = [
    "M", "DS", "DS", "PSS", "PSS", "A", None, "TV", None, None,
    "PIS", "M", "PIS", "PIS", "TP", "A", "CJ", None, None, None,
    "CIT", "CIT", "WA", "DS", "PV", None, "PSS", None, None, None,
    "AM", "M", "WA", "WA", None, "A", "C", "PIS", "TV", None,
    "C",   "A", "M", "PV", "PV", "AM", None, None, None, None 
]
```

Pokud ale chcete alespoň čtyřku, tak to samožejmě zvládnete lépe, tj. s učiteli, učebnami, apod. Možná použijete i třídy a určitě i lepší kolekce. Ten kód výše berme spíš jako rozvcičku, nebo jen pro testování generátorů, viz. dále.

Dále musíte vytvořit kód, který bude mít nejméně tři typy skutečně paralelně běžících procesů/vláken.

1. **Generátor** - Generuje různé varianty zadaného rozvrhu. Například zkouší všechny možné permutace, nebo jen některé variace. Můžete zkoušet prohodit předměty v jednom dni, nebo přesunout výuku více na odpoledne/ráno. Příliš ale neřeší, jestli jsou nové varianty dobré, nebo špatné. Cílem je vygenerovat jich jen co nejvíce. Výsledné varianty se musí vložit do sdíleného prostoru s ostatnímy paralelními částmi programu. Generátorů může být samozřejmě více a mohou být i různé typy.
2. **Hodnotitel** - Ohodnocuje různé varianty rozvrhu, které generátory vytvořily. Hodnotí se pomocí bodů. Za co jsou body, bude uvedeno níže. Hodnotitelů může být také více, a mohou hodnotit shodně nebo se nějak doplňovat, například hodnotitelé pro body plusové a pak hodnotitelé penalizační. Ohodnocené rozvrhy se pak mažou z paměti, vyjma toho nejlepšího. Pokud hodnotitelé zpracují všechny vygenerované varianty, program končí.
3. **Watchdog** - Kontroluje časový timeout. Jakmile program běží více než je Vámi nasavený timeout (defaultně třeba 3min), ukončí se všechny činnosti a vypíše se výsledek i přesto, že všechny varianty nebyly ohodnoceny.

Po ukončení programu se musí na obrazovku vypsat
- Kolik variant bylo vygenerováno
- Kolik variant bylo ohodnoceno
- Které varianty jsou nejlepší
- Kolik variant je lepších, než původně zadaný rozvrh

Kolik je různých variant (permutací)? Víme, že rozvrh má 10 políček x 5 dní, tedy 50 políček celkem. Počet všech permutací, je faktoriál(50), jinými slovy vždy existuje  cca 30414093201713378043612608166064768844377641568960512000000000000 různých variant rozvrhu. Váš program by měl zvládnout alespoň desítky milionů různých variant, čtyřkař možná jen jednotky milionů.

Jak různé varianty generovat? No všechny asi nevygenerujete, takže to chce nějak vybrat. Taková základní strategie je rozdělit to. Třeba po předmětech, po dnech, nebo po n-te hodině a zkusit si třeba všechny permutace pro deset políček v jednom dni (tj. faktorial(10) - nic hrozneho), nebo všechny permutace políček na pozici 1. hodina (tj. faktoriál(5), pohoda) a různě to můžete kombinovat. Ti chytřejší do toho mohou dát i nějakou logiku, třeba využijí teorii grafů, matic, čehokoliv. Pozor ale, ať se Vám ty rozvrhy neopakují ;) to by byl podvod. (neopakování hravě zvládnete, třeba pomoci __eq__/equals() a __hash__/hash() ve spojení s kolekcemi bez opakování)

## Jak různé varianty hodnotit? 
```
Principem hodnocení je to, abychom mohli rozvrhy porovnat, 
a vybrat z nich nejlepší. Tedy chce to takové hodnocení, 
které bude vyjádřené číslem a ideálně žádné dva rozvrhy ho nebudou mít stejné.
 (Pozn. pro jedničkáře, když existuje 3x10^64 variant, bude asi dost těžké, aby to žádné dva neměli stejné). Hodnocení bude samozřejmě z velké části na Vás, ale z části musíte nějak implementovat následující pravidla 1. až 7., vytvořit dvě vlastní unikátní pravidla 8. a 9. a nakonec se poprat i s wellbeing ovýmpravidlem 10. Bude se tedy hodnotit takto:
```
1. Každému políčku v rozvrhu určete bonus/malus za to, když tam hodina je/není. Například pátek 9. hodina je pro někoho +100 bodů, pro někoho -100 bodů. Hodně se to liší, pokud chodíte do zaměstnání, nebo jste student. Také ranní hodiny jsou někdy oblíbené a někdy ne, apod. Nakonec každé políčko bude mít nějaký bonus/penále.

2. Pokud v je stejný předmět vícekrát v jeden den a není to vícehodinovka, tak to je špatně. Cvičení a teorie ale v jeden den být mohou. Také úplně štastně a rozumné, když cvičení předchází teorii.

3. Pokud musím mezi hodinami přecházet do jiného patra je to špatně, pokud do jiné učebny, je to taky špatně ale pokud je to na stejném patře, tak to není tak hrozné.

4. Obědy se vydávají mezi 5. a 8. hodinou, takže každý den jedna z hodin číslo 5., 6., 7. nebo 8. musí být volná na oběd.

5. Denně by se mělo učit ideálně tak 5-6 hodin, víc je špatně, 8 je strop, 9 je problém a 10 snad ani není ani legální.

6. Když je cvičení dvouhodinové, tříhodinové tak ty hodiny musí být u sebe v jednom dni.

7. Matematika a profilové předměty by se neměli učit ani první hodinu, ani po obědové pauze, za to musí být body dolu.

8. (Vaše vlastní pravidlo #1, jeho princip musí být zřejmý z dokumentace.)

9. (Vaše vlastní pravidlo #2, jeho princip musí být zřejmý i bez dokumentace.)

10. Wellbeing pravilo - Musi reflektovat Váš wellbeing, napr. pokud nemate/mate radi urcite ucebny/ucitele/predmety. Napr. nemam rad ucitele A, B a C, tak rozvrh ktery obsahuje dny, kde uci jen tihle tri dostane penale. Nebo naopak, pokud mam rad ucitele X a rozvrh vysel tak, ze ho potkam kazdy den alespon 1x je to lepsi, nez kdyz ho napr. 3 dny v kuse nepotkam.

**Dobré rady a doporučení**: Při implementaci doporučujeme nezůstávat jen u třech vláken (generátor, hodnotitel a watchdog), ale zkuste si udělat třeba tři hodnotele, kteří hodnotí paralerně, nebo více generátorů variant rozvrhu podle různých strategií. Zvažte také využítí znalostí z kapitol o generátorech a korutinách. Důrazně doporučujeme využít OOP/dedičnost a vyjímky pro architekturu celého díla. Dílo musí být rozumě rozděleno do samostatných modulů/souborů a složek/package. Samozřejmě ho můžete vytvořit v libovolném programovacím jazyce. Hlídejte si, kde je main() pro spuštění a kde pro unit testy. Nezapomeňte zpracovat soubor README a popsat jak se program zapne, jak se ovládá. Silně doporučujeme používat vhodné datové struktury, které usnadní napsání celého algoritmu, ale je to na Vás... 

**Varování**: Upozorňujeme, že tato úloha není týmová ale samostatná a lze ji napsat mnoha způsoby. Je velmi nepravděpodobné, že dva žáci budou mít stejný program, nebo jakoukoli jeho část a proto se vyvarujte inspiracím ze zdrojových kódů spolužáků, týmové spolupráci, nebo generátorům kódu a předejděte tak případným plagiátům. Pokud použijete cizí kód, například ten, který naše automatická kontrola dokáže vygooglit nebo ho najde na githubu, uveďte vždy zdroj v dokumentaci a raději i README. Pokud pouzijete generativni umelou inteligenci, napiste ktery kod je generovany - pri kontrole se nesmi stat, ze nebudete vlastnimu kodu rozumet, to by bylo vnimano jako podvod.

**Kritéria hodnocení:**

Spuštění programu musí alespoň na 5 sec zatížit všechna procesorová jádra běžného školního PC.
Program musí obsahovat alespoň jedno synchronizační primitivum, které je účelně použito a jednotlivé paralelní částí musí nějak sdílet/komunikovat informace.
Program musí být spustitelný bez vývojového prostředí (tj.nebude spouštěn v PyCharm ani VStudio) na školním PC. Nelze tedy použít technologie a knihovny, které nelze ve škole instalovat/nasadit.
Pri splneni kriterii bude prace hodnocena na stupnici 1 az 5 podle kriterii kvality, pri nesplneni, nebo podvodu bude hodnocena znamkou 5, bez vyhodnoceni kriterii.