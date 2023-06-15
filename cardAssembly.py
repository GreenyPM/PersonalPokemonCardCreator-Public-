import cv2
import webbrowser
import os

def cardCreator(type, name):
    #img = np.zeros((772,546,3),np.uint8)

    # Card Base
    cardPokemon = cv2.imread('Card Bases\\' + type + ".PNG")
    img = cardPokemon
    #cv2.imshow('Card', img)


    #Pictrue
    personPic = cv2.imread('PeoplePhotos\\Person.png')

    basicEnergy = cv2.imread('Card Bases\\NormalSymbol.PNG')
    typeEnergy = cv2.imread('Card Bases\\' + type + 'Symbol.PNG')

    te_x_offset = 30
    te_y_offset = 477

    if type == "Normal":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (210, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (440,305))
        pic_x_offset = 50
        pic_y_offset = 89
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 30
        be_y_offset = 477
    elif type == "Fire":
        cv2.putText(img, name, (42, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (210, 500), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 500), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Flare", (210, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "20", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (430, 310))
        pic_x_offset = 57
        pic_y_offset = 90
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 460
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Water":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (190, 510), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Water Gun", (190, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "30", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (435, 310))
        pic_x_offset = 53
        pic_y_offset = 88
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 477
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Grass":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (190, 510), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Leaf Blade", (190, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "30", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (435, 310))
        pic_x_offset = 53
        pic_y_offset = 85
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 477
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Fighting":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (190, 510), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Take Down", (190, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "40", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (440, 310))
        pic_x_offset = 52
        pic_y_offset = 87
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 477
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Psychic":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (190, 510), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Confusion", (190, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "30", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (435, 310))
        pic_x_offset = 54
        pic_y_offset = 85
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 477
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Electric":
        cv2.putText(img, name, (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60 HP", (365, 65), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (190, 510), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 520), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Thunder", (190, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "40", (450, 580), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (435, 310))
        pic_x_offset = 52
        pic_y_offset = 87
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 40
        be_y_offset = 477
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 40
        te_y_offset = 550
    elif type == "Steel":
        cv2.putText(img, name, (100, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60", (440, 55), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "HP", (420, 55), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (145, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Iron Head", (145, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "40", (450, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (475, 295))
        pic_x_offset = 35
        pic_y_offset = 70
        basicEnergy = cv2.resize(basicEnergy, (60,50))
        be_x_offset = 30
        be_y_offset = 457
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 30
        te_y_offset = 520
    elif type == "Fairy":
        cv2.putText(img, name, (100, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60", (440, 55), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "HP", (420, 55), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (145, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Petal Dance", (145, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "50", (450, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (480, 291))
        pic_x_offset = 34
        pic_y_offset = 70
        basicEnergy = cv2.resize(basicEnergy, (60, 50))
        be_x_offset = 30
        be_y_offset = 457
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 30
        te_y_offset = 520

    elif type == "Dragon":
        cv2.putText(img, name, (100, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "60", (440, 55), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "HP", (420, 55), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
        cv2.putText(img, "Punch", (145, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "10", (450, 490), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "Draco Meter", (145, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.putText(img, "50", (450, 560), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        personPic = cv2.resize(personPic, (475, 295))
        pic_x_offset = 36
        pic_y_offset = 70
        basicEnergy = cv2.resize(basicEnergy, (60, 50))
        be_x_offset = 30
        be_y_offset = 457
        typeEnergy = cv2.resize(typeEnergy, (60, 50))
        te_x_offset = 30
        te_y_offset = 520
    x_endp = pic_x_offset + personPic.shape[1]
    y_endp = pic_y_offset + personPic.shape[0]
    x_endbe = be_x_offset + basicEnergy.shape[1]
    y_endbe = be_y_offset + basicEnergy.shape[0]
    x_endte = te_x_offset + typeEnergy.shape[1]
    y_endte = te_y_offset + typeEnergy.shape[0]

    imgResult = img.copy()
    imgResult[pic_y_offset:y_endp, pic_x_offset:x_endp] = personPic
    imgResult[be_y_offset:y_endbe, be_x_offset:x_endbe] = basicEnergy
    imgResult[te_y_offset:y_endte, te_x_offset:x_endte] = typeEnergy
    cv2.imwrite("PeoplePhotos\\Card.png", imgResult)
    webbrowser.open("PeoplePhotos\\indexCard.html")
    os.startfile("PeoplePhotos\\Cardback.png", 'print')
    os.startfile("PeoplePhotos\\Card.png", 'print')



#camera.takePicture()
#cv2.putText(img," 'Art' ",(0,450),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,0),3)

#cardCreator("Fairy", "Patrick")