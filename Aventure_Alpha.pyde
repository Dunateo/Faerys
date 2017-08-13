





arbreHistoire = [[0,1,2],[1,3,4],[2,9,10],[3,"R1"],[4,5,6],[5,"R2"],[6,7,8],[7,"R3"],[8,"G"],[9,"R4"],[10,11,12],[11,"R5"],[12,13,14],[13,"R6"],[14,"P"]]
MessagesEtapes =[[0,u"Vous vous réveillez subitement. \n Vous êtes seul, étendu au milieu d’une petite clairière bordée d’arbres.  \n Un rapide tour de la clairière vous révèle l’existence d’un mince sentier qui s’engage en serpentant parmi les arbres."],
                 [1,u"Vous prenez le risque de le suivre",u"Vous prenez le risque de le suivre\nVous l’aider à se relever et la calez sur vos épaules et commencez à vous mettre en marche.\nLe chemin que vous suivez est si plein de tournants \nque vous avez perdu tout sens de l’orientation après seulement quelques instants.  \nAlors que vous vous deman-dez si vous avez eu raison de vous fier à ce sentier \nqui vous était offert, vous êtes brusquement alerté par le froissement des broussailles tout près de vous.\nVous avez tout juste le temps de tirer votre épée avant qu’un sanglier massif n’en surgisse pour vous charger"],
                 [2,u"ou partir dans une autre direction en vous aventurant parmi les broussailles",u"ou partir dans une autre direction en vous aventurant parmi les broussailles.\n La végétation est plus épaisse que vous ne l’aviez pensé d’entrée de jeu. \nVous êtes presque tenté de revenir sur vos pas, mais vous n’êtes aucunement certain de retrouver la clairière derrière vous. \nSoudain, des rires cristallins viennent vous frapper les oreilles. \nIls semblent proches, mais ne vous pouvez pas en distinguer l’origine."],
                 [3,u"Vous sortez votre épée",u"Vous sortez votre épée."],
                 ["R1",u"Vous êtes malheureusement trop lent \nGAMEOVER "],
                 [4,u"Vous décidez de courir en l'atirant",u"Vous décidez de courir en l'atirant vous le tuez grâce à un piège \nVous vous servez de votre couteau pour découper la chair du sanglier. \nQuelques instants de tra- vail vous permettent de récupérer suffisamment de viande pour faire trois Repas \nVous vous apprêtez ensuite à poursuivre votre chemin, \nmais c’est pour vous apercevoir que le sentier a totalement disparu \nErrant quelques ins- tants au hasard, vous finissez par entendre une sorte de martèlement, \nléger mais répété."],
                 [5,u"vous rapprocher de l’origine de ce son»"],
                 ["R2",u"Vous arrivez finalement devant une souche d’arbre massive, \nbien que rongée par les champignons et les vers. Assis dessus se trouve un petit homme barbu, \nvêtu d’habits dépenaillés et coiffé d’une sorte de bonnet informe. \nLe petit homme ne vous prête pas la moindre attention et \nvous n’êtes même pas certain qu’il se soit rendu compte de votre arrivée. \nVous êtes perdu"],
                 [6,u"vous préférez prendre une autre direction",u"vous préférez prendre une autre direction \nVous cheminez sans interruption pendant un certain temps, sans autre compagnie que le bruit de vos pas et les sons de la forêt, \navant de déboucher soudain sur une vaste clairière. \nAu-dessus de votre tête, vous pouvez de nouveau voir le ciel azur, \nqui vous était jusque-là dissimulé par l’épais feuillage. \nAu milieu de la clairière se dresse un arbre gigantesque, dont six hommes ne parvien- draient pas à encercler le tronc en se tenant par la main. Il ne semble pas y avoir quoi que ce soit d’autre d’intéressant ici. L’arbre est si grand qu’il doit offrir un bon point de vue sur l’ensemble de la forêt."],
                 [7,u"vous souhaitez y grimper"],
                 ["R3",u"Fort heureusement, le tronc de l’arbre est si rugueux qu’il offre de nombreuses prises. \nLaissant votre sac à dos derrière, vous vous hissez sans trop de difficulté jusqu’à la branche la plus basse, \nsituée à près d’une dizaine de mètres du sol et particulièrement épaisse. \nVous vous y agrippez,\nconvaincu que le reste de l’ascension sera tout aussi aisé, \nmais la branche se dérobe soudain en dessous de vous ! \nIncapable de vous raccrocher à quoi que ce soit, vous chutez."],
                 [8,u"vous préférez quitter la clairière immédiatement"],
                 ["G",u"Vous vous retrouvez à un endroit de la forêt où le feuillage est si épais qu’il \nvous semble presque être sous terre. \nL’atmosphère est feutrée et même le bruit de vos propres \npas ne vous parvient qu’étouffé.\nVous débouchez rapidement sur une vaste clairière baignée de soleil. \nDes fleurs de toutes les couleurs s’étendent devant vous en un tapis ondoyant \nau moindre souffle d’air. \nLe parfum qu’elles diffusent est délicieusement léger. \nAprès un instant, vous remarquez que vous n’êtes pas seul : \nune jeune femme blonde est assise au milieu de la clairière, en train de s’affairer sur \nquel- que chose que vous ne distinguez pas clairement. Des fleurs sont dans ses cheveux, \nautour de son cou et sur ses vêtements.\nvous décidez de rester avec elle "],
                 [9,u"Allez-vous essayez de vous en rapprocher"],
                 ["R4",u"\nVous suivez le bruit des rires. \nVous avez l’impression de vous en rapprocher, car ils se font pro- gressivement plus forts et plus nets \nAlors que vous vous efforcez de traverser un véritable rideau de plantes grimpantes \nqui s’accrochent aux arbres devant vous, celles-ci se resserrent brusquement sur vous, \nvous prenant au piège comme dans une nasse ! \nLes plantes se resserrent progressivement autour de vous, infligeant des dommages croissants. \nLa première fois qu’elles remportent un assaut contre vous \nGAMEOVER"],
                 [10,u"ou prendre une autre direction \n Vous bataillez un certain temps avec la végétation qui obstrue votre chemin, \nmais celle-ci va heureusement en s’amoindrissant. \nUne dizaine de fées minuscules, pas plus grandes que votre main et dotées d’ailes de libellules, \nsont en train de déguster des baies et de boire dans des glands évidés."],
                 [11,u"Allez-vous faire fi de votre expérience récente en vous joignant à elles»."],
                 ["R5",u"Elles vous disent que la nourriture qu’elles consommaient aurait des effets néfas- tes sur vous, \nmais vous invitent à goûter quelques-uns des champignons qui se trouvent là.\nVous mourrez d'une intoxication \nGAMEOVER"],
                 [12,u"ou préférez- vous contourner prudemment la clairière et reprendre votre chemin à travers la forêt».",u"ou préférez- vous contourner prudemment la clairière et reprendre votre chemin à travers la forêt ». \nVous êtes sur le point de la traverser, lorsque vous réalisez que le milieu de \ncette clairière est occupé par un large cercle de champi- gnons."],
                 [13,u"Allez-vous pénétrer à l’intérieur de ce cercle»"],
                 ["R6",u"Un fourmillement vous parcourt le corps une fois que vous avez posé les deux pieds à l’intérieur du cercle de champignons. \nGAMEOVER"],
                 [14,u"ou au contraire le contourner soigneusement et poursuivre votre chemin à travers la forêt"],
                 ["P",u"Le sol est ici tapissé d’une mousse si épaisse qu’elle étouffe tous les sons.\nÀ distance, il vous semble pourtant deviner des bruits d’animaux vous devenez fou \nGAMEOVER"]]


#-----------------------
#fonction qui lit les messages
#-----------------------
def litMessage(n):
    for m in MessagesEtapes:#m allant de l'arbre
        if m[0] == n:#argument
            if len(m)==2:#taille de m == 2
                return [m[1]] # retourne 
            else:
                return [m[1],m[2]]
    return -1
#-----------------------
#fonction qui lit les choix parcours le message étapes  
#-----------------------
def litChoix(n):
    for m in arbreHistoire:
        if m[0] == n:
            if str(m[1])[0:1] == "R":#chaine de caractere que l'on recupere R correspond aux morts
                return ["R",litMessage(m[1])]
            elif str(m[1])[0:1] == "G":#correspond a la victoire 
                return ["G",litMessage(m[1])]
            elif str(m[1])[0:1] == "P":#correspond une impasse 
                return ["P",litMessage(m[1])]
            else:
                return [m[1],m[2],litMessage(m[1]),litMessage(m[2])]
            
            
            
    return -1

noeud = 0
#-----------------------
#fonction 
#-----------------------
def afficheEcran(n):
    global noeud
    msg = litMessage(noeud) #appel de la fonction 
    if msg == -1:
        print("Erreur noeud inconnu :",noeud)
    else:
        choix = litChoix(noeud) #appel de fonction 
        if choix == -1:
            print("Erreur noeud inconnu :",noeud)
        elif choix[0] == "R":
            background(200)
            fill(255,0,0)#rouge
            textSize(20)
            text(choix[1][0],10,50)#(choix,x,y)
            fill(0,0,255)
            textSize(18)
            text(u"Vous recommencer au départ l'histoire !\n\n Appuyer sur la touche entrée",10,470)
        elif choix[0] == "G":
            background(200)
            fill(0,80,255)
            textSize(20)
            text(choix[1][0],10,50)
            fill(0,0,255)
            textSize(18)
            text(u"Bravo ! l'aventure se termine ici !",10,470)
        elif choix[0] == "P":
            background(200)
            fill(255,0,0)
            textSize(20) 
            text(choix[1][0],10,50)
            fill(0,0,255)
            textSize(18)
            text(u"Désolé ! l'aventure se termine ici !",10,470)
        else:
            background(200)
            fill(0)
            textSize(20)
            if len(msg) == 1:
                text(msg[0],10,50)
            else:
                text(msg[1],10,50)
            fill(0,0,255)
            textSize(18)
            text("choix 1 :",10,450)
            text(choix[2][0],10,480)
            text("choix 2 : ",10,550)
            text(choix[3][0],10,570)
#-----------------------
#fonction qui crée la fenetre de 1400 pixels par 800 pixels
#tourne 1 
#-----------------------
def setup():
    global debutJeu#variable global modifiable sans appel 
    size(1400,800)
    fill(0)#background blanc
    img = loadImage("menu.png") #on definit img comme étant l'image que l'on veut 
    image(img,0,0,1400,800) #(variable, x, y, recadrage)
    debutJeu = True
#-----------------------
#tourne tant que elle n'est pas stoppé
#-----------------------
def draw():
    return   #retourne c'est un stop   
#-----------------------
#fonction touche 
#-----------------------    
def keyPressed():
    global noeud 
    global debutJeu
    if keyCode == 10 and debutJeu: #10 en ascii enter ou line feed 
        debutJeu = False #on passe donc au jeu 
        noeud = 0 
    if not(debutJeu):
        choix = litChoix(noeud) #appel de la fonction
        if choix == -1:
                print("Erreur noeud inconnu :",noeud)
        elif key == "1":
            noeud = choix[0]
        elif key == "2":#touche 2 donne le choix 2 le noeud avance donc 
            noeud = choix[1]
        elif keyCode == 10 and choix[0] == "R":  #recommence le jeu 
            noeud = 0
        afficheEcran(noeud)#appel fonction 
            
    
    