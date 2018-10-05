def kwadraten_som(getallenLijst):
    getallenLijstTotaal = 0
    for i in getallenLijst:
        if i > 0:
            getallenLijstTotaal += i * i
    print(getallenLijstTotaal)


kwadraten_som([ 4, 5, 3, -81])
