# cv1 - vyhladit histogram
# cv2 - sledování obrazu
# cv3 - Převod do barevných prostorů + geometrické operace (zvětšení, zkosení, rotace podle úhlu)
# cv4 - Transformace jasu

# cv5 - Filtrace šumu
## Rotující maska
- oprava velkoplošných chyb bez vlivu na zbytek obrazu,
jednoduché vyhlazení bez poškození hran. 
# cv6 - Hranové detektory
# cv7 - Segmentace
# cv8 - Morfologické operace -> bin obraz
## Dilatace 
- samostatně k zaplnění malých děr, úzkých zálivů a pro další
složitější operace, zvětšuje objekty, pro zachování původních rozměrů >>>
kombinace s erozí 
## Eroze 
- zjednodušení struktury objektů, složitější objekt se rozdělí na několik jednodušších

## Otevření
- Otevření >>> eroze následovaná dilatací
-  Otevření oddělí objekty spojené úzkou šíjí a tak zjednoduší strukturu objektů

## Uzavření
- Uzavření >>> dilatace následovaná erozí
- Uzavření spojí objekty, které jsou blízko u sebe, zaplní malé díry a vyhladí
obrys tím, že zaplní úzké zálivy

# cv9 - Morfologické operace -> grayscale obraz
## Šedotónová delatace
## Šedotónová eroze
## Šedotónové Otevření
## Šedotónové Uzavření

# cv10 - Skeletizace a rozvodí

