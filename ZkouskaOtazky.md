# cv1 - vyhladit histogram
# cv2 - sledování obrazu
# cv3 - Převod do barevných prostorů + geometrické operace (zvětšení, zkosení, rotace podle úhlu)
# cv4 - Transformace jasu
![transformaceJasu](https://user-images.githubusercontent.com/46580540/170105374-e12eb5a4-91c2-4276-860e-48eff5e5da33.png)


# cv5 - Filtrace šumu
## Průměrování
![noiseMean](https://user-images.githubusercontent.com/46580540/170126797-5fb00d81-fc9d-4bd7-b9d1-f40bca73eee5.png)

## Median
![noiseMedian](https://user-images.githubusercontent.com/46580540/170126929-c293b391-24ca-4440-a436-8757b9024f42.png)

## Rotující maska
- oprava velkoplošných chyb bez vlivu na zbytek obrazu,
jednoduché vyhlazení bez poškození hran. 
![noiseRotatingMask](https://user-images.githubusercontent.com/46580540/170127841-a8279db1-245d-4d6a-bab2-244baa9a7480.png)


# cv6 - Hranové detektory

## Laplace
![edgeLaplace](https://user-images.githubusercontent.com/46580540/170127195-00a7f442-df3a-4be2-acb7-eb06190de464.png)

## Sobel
![noiseSobel](https://user-images.githubusercontent.com/46580540/170127371-78bb18a5-8eea-446d-afab-e8150f97c3bb.png)

## Canny
- nejprve potřeba redukovat noise
![edgesCanny](https://user-images.githubusercontent.com/46580540/170128042-eb72fb74-d3a4-4fee-a6cb-cd6975bbdc59.png)


# cv7 - Segmentace

# cv8 - Morfologické operace -> bin obraz
https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
## Dilatace 
- samostatně k zaplnění malých děr, úzkých zálivů a pro další
složitější operace, zvětšuje objekty, pro zachování původních rozměrů >>>
kombinace s erozí 
![binDilatace](https://user-images.githubusercontent.com/46580540/170106837-7fc97ad2-8ed6-483b-9577-a63de5b398a8.png)


## Uzavření
- Uzavření >>> dilatace následovaná erozí
- Uzavření spojí objekty, které jsou blízko u sebe, zaplní malé díry a vyhladí
obrys tím, že zaplní úzké zálivy
![binUzavreni](https://user-images.githubusercontent.com/46580540/170107325-6085ce8b-36b4-449b-b77f-c8a8ba6d42a7.png)


## Eroze 
- zjednodušení struktury objektů, složitější objekt se rozdělí na několik jednodušších
![binEroze](https://user-images.githubusercontent.com/46580540/170105973-87ab9f34-987d-4bc4-8903-92e8f8db2247.png)

## Otevření
- Otevření >>> eroze následovaná dilatací
-  Otevření oddělí objekty spojené úzkou šíjí a tak zjednoduší strukturu objektů
![binOtevreni](https://user-images.githubusercontent.com/46580540/170106417-800cfab0-498e-41e5-a29b-5b76fe778ab5.png)


# cv9 - Morfologické operace -> grayscale obraz
## Šedotónová delatace
## Šedotónová eroze
## Šedotónové Otevření
## Šedotónové Uzavření

# cv10 - Skeletizace a rozvodí


