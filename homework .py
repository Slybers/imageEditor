#Homework Fondamenti Di Informatica e Laboratorio - Modulo cImage - Ingegneria Informatica 2018/2019 - Giudice Marco MAT.201285
import cImage

def quadrato_grigio(immagine_originale,finestra,larghezza,altezza):
    print("Scegliere l'area da rendere in bianco e nero")
    clicks = finestra.captureClicks(2)
    (x,y)=clicks[0]
    (X,Y)=clicks[1]
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(larghezza,altezza)
    for i in range(altezza):
            for j in range(larghezza):
                pixel_originale = immagine_originale.getPixel(j,i)
                nuova_immagine.setPixel(j,i,pixel_originale)
        
    for a in range(x,X+1):
        for b in range(y,Y+1):
                    pixel=immagine_originale.getPixel(a,b)
                    livello_grigio = ( pixel.getRed() + \
                                        pixel.getGreen() + \
                                        pixel.getBlue() ) // 3
                    grigio=cImage.Pixel(livello_grigio,livello_grigio,
                                                       livello_grigio)
                    nuova_immagine.setPixel(a,b,grigio)

    return nuova_immagine



def blu(immagine_originale,finestra,larghezza,altezza):      
    print("Attendere...")
    nuova_immagine=cImage.EmptyImage(larghezza,altezza)
    for i in range(larghezza):
            for j in range(altezza):
                pixel =immagine_originale.getPixel(i,j)
                livello_blu=pixel.getBlue()
                blu=cImage.Pixel(0,0,livello_blu)
                nuova_immagine.setPixel(i,j,blu)

    return nuova_immagine



def rosso(immagine_originale,finestra,larghezza,altezza):       
    print("Attendere...")
    nuova_immagine=cImage.EmptyImage(larghezza,altezza)
    for i in range(larghezza):
            for j in range(altezza):
                pixel =immagine_originale.getPixel(i,j)
                livello_rosso=pixel.getRed()
                rosso=cImage.Pixel(livello_rosso,0,0)
                nuova_immagine.setPixel(i,j,rosso)

    return nuova_immagine



def verde(immagine_originale,finestra,larghezza,altezza):       
    print("Attendere...")
    nuova_immagine=cImage.EmptyImage(larghezza,altezza)
    for i in range(larghezza):
            for j in range(altezza):
                pixel =immagine_originale.getPixel(i,j)
                livello_verde=pixel.getGreen()
                verde=cImage.Pixel(0,livello_verde,0)
                nuova_immagine.setPixel(i,j,verde)

    return nuova_immagine



def orizzontale(immagine_originale,finestra,larghezza,altezza):
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(larghezza,altezza)
    b=altezza
    for i in range(larghezza):
            for j in range(altezza):
                    pixel = immagine_originale.getPixel(i,j)                
                    nuova_immagine.setPixel(i,b-1,pixel)              
                    b-=1
            b=altezza
    return nuova_immagine



def verticale(immagine_originale,finestra,larghezza,altezza):
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(larghezza,altezza)
    a=larghezza
    b=altezza
    for i in range(larghezza):
            for j in range(altezza):
                    pixel = immagine_originale.getPixel(i,j)                
                    nuova_immagine.setPixel(a-1,j,pixel)
            a-=1            
    return nuova_immagine



def centottanta(immagine_originale,finestra,larghezza,altezza):
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(larghezza,altezza)
    a=larghezza
    b=altezza
    for i in range(larghezza):
            for j in range(altezza):
                    pixel = immagine_originale.getPixel(i,j)                
                    nuova_immagine.setPixel(a-1,b-1,pixel)              
                    b-=1
            a-=1
            b=altezza
    return nuova_immagine



def duecentosettanta(immagine_originale,finestra,larghezza,altezza):
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(altezza,larghezza)
    a=larghezza
    for i in range(larghezza):
            for j in range(altezza):
                    pixel = immagine_originale.getPixel(i,j)                
                    nuova_immagine.setPixel(j,a-1,pixel)
            a-=1    
           
    return nuova_immagine



def novanta(immagine_originale,finestra,larghezza,altezza):
    print("Attendere...")
    nuova_immagine = cImage.EmptyImage(altezza,larghezza)
    b=altezza
    for i in range(larghezza):
            for j in range(altezza):
                    pixel = immagine_originale.getPixel(i,j)                
                    nuova_immagine.setPixel(b-1,i,pixel)
                    b-=1
            b=altezza
                   
    return nuova_immagine


                                                                                
def trasformazione(file_immagine,funzione):
    immagine_originale = cImage.Image(file_immagine)
    larghezza = immagine_originale.getWidth()
    altezza = immagine_originale.getHeight()
    finestra = cImage.ImageWin("Immagine originale",larghezza,altezza)
    immagine_originale.draw(finestra)

    nuova_immagine = funzione(immagine_originale,finestra,larghezza,altezza)
        
    larghezza = nuova_immagine.getWidth()
    altezza = nuova_immagine.getHeight()
    finestra_2 = cImage.ImageWin("Nuova immagine",larghezza,altezza)
    print("Finito!")
    nuova_immagine.draw(finestra_2)
    continua=input(f"Vuoi eseguire un'altra operazione?\n")
    if "si" in continua or "s" in continua or "y" in continua or "yes" in continua:
        finestra.master.destroy()
        finestra.quit()
        finestra_2.master.destroy()
        finestra_2.quit()
        immagine_diversa=input(f"Vuoi cambiare immagine?\n")
        if "si" in immagine_diversa or "s" in immagine_diversa or "y" in immagine_diversa or "yes" in immagine_diversa:
            immagine=input(f'Quale immagine vuoi modificare?(Solo .gif)\n')
            if ".gif" not in immagine:
                immagine=immagine+".gif"
                main(immagine)
        else:
            main(file_immagine)
    else:
        print("Premere sulle immagini per uscire.")
        finestra_2.exitOnClick()
        finestra.exitOnClick()


def main(immagine):
    operazione=int(input(f"Scegliere l'operazione da compiere\nDigitare:\n1 per convertire in toni di grigio una porzione dell’immagine\n2 per convertire l’immagine originale in toni di rosso,verde o blu\n3 per specchiare l'immagine\n4 per ruotare l'immagine\n"))
    if operazione == 1:
        trasformazione(immagine,quadrato_grigio)
    else:
        if operazione == 3:
            verso=input(f"Specchiare l'immagine in orizzontale o in verticale?\n")
            if "orizzontale" in verso:
                trasformazione(immagine,orizzontale)
            else:
               trasformazione(immagine,verticale)
       
        else:
            if operazione == 2:
                colore=input(f'Scegliere il colore\n')
                if "blu" in colore:
                    trasformazione(immagine,blu)
                else:
                    if "verde" in colore:
                        trasformazione(immagine,verde)
                    else:
                        if "rosso" in colore:
                            trasformazione(immagine,rosso)
            else:
                if operazione == 4:
                    verso=input(f'Senso orario o antiorario?\n')
                    

                    gradi=input(f"Di quanti gradi vuoi ruotare l'immagine?(90°,180°,270°)\n")
                    if "orario" in verso:
                        
                        if gradi == "90" or gradi == "novanta":
                            trasformazione(immagine,novanta)
                        else:
                            if gradi == "180" or gradi == "centottanta":
                                trasformazione(immagine,centottanta)
                            else:
                                if gradi =="270" or gradi == "duecentosettanta":
                                    trasformazione(immagine,duecentosettanta)
                    else:
                        if "antiorario" in verso:
                            
                            if gradi == "90" or gradi == "novanta":
                                trasformazione(immagine,duecentosettanta)
                            else:
                                if gradi == "180" or gradi == "centottanta":
                                    trasformazione(immagine,centottanta)
                                else:
                                    if gradi =="270" or gradi == "duecentosettanta":
                                        trasformazione(immagine,novanta)
                            
                
        
immagine=input(f'Quale immagine vuoi modificare?(Solo .gif)\n')
if ".gif" not in immagine:
    immagine=immagine+".gif"
main(immagine)
