## ============================================================
## AVENTURE 1 : SAUVER LE ROYAUME DES LICORNES
## Fichier : game/aventures/licornes.rpy
## ============================================================


## ============================================================
## INTRODUCTION
## ============================================================

label intro_licornes:

    show screen inventaire_hud

    scene bg sky with dissolve

    "Il était une fois, très loin d'ici, un royaume merveilleux appelé {b}Élysia{/b}. 🌈"
    "Dans ce royaume enchanté vivaient des licornes aux crinières arc-en-ciel, des fées lumineuses et des créatures magiques de toutes sortes."
    "La magie d'Élysia venait d'une pierre précieuse extraordinaire : la {b}Pierre de Lumière{/b}."
    "Cette pierre, posée au sommet de la Grande Tour du royaume, donnait ses pouvoirs à toutes les licornes."

    scene bg pierre with dissolve

    "Mais un jour sombre, la terrible sorcière {b}Maléfra{/b} s'empara de la Pierre de Lumière !"
    "Sans elle, les licornes perdaient leur magie une à une. Leurs cornes s'éteignaient, leurs ailes disparaissaient..."
    "Le royaume d'Élysia commençait à s'effacer, comme une bougie qui s'éteint dans le vent."

    scene bg prairie with dissolve

    "C'est alors qu'une petite fée dorée apparut devant toi, alors que tu jouais dans le jardin ce matin-là."

    fee_celeste "Oh, [prenom] ! Je t'en supplie, aide-nous !"

    joueur "Qui es-tu ? Et qu'est-ce qui se passe ?"

    fee_celeste "Je m'appelle Céleste, la gardienne du royaume d'Élysia. La méchante Maléfra a volé notre Pierre de Lumière !"
    fee_celeste "Les licornes perdent leur magie. Si personne ne récupère la Pierre avant le coucher du soleil, le royaume disparaîtra pour toujours !"

    joueur "C'est horrible ! Je dois faire quelque chose !"

    fee_celeste "Tu es brave, [prenom]. Je savais que tu étais la bonne personne !"
    fee_celeste "La tour de Maléfra se trouve au-delà de la Forêt Enchantée et du Pont du Vieux Grok."
    fee_celeste "Prends ce cristal magique."

    $ inventaire.append("Cristal de Céleste 💎")

    fee_celeste "Il t'aidera si tu te trouves en grand danger. Mais attention : il ne peut être utilisé qu'une seule fois !"

    joueur "Merci Céleste ! Je vais sauver les licornes, c'est promis !"

    fee_celeste "Sois prudent(e), [prenom]. Le chemin est semé d'embûches... mais aussi de belles surprises !"

    "Céleste disparut dans un tourbillon d'étincelles d'or. Tu pris une grande inspiration et t'élançais vers la Forêt Enchantée."

    jump foret_enchantee


## ============================================================
## ACTE 1 : LA FORÊT ENCHANTÉE (Choix 1)
## ============================================================

## ── Écran de choix : Forêt Enchantée ──
screen foret_choix_screen():
    zorder 200
    modal True

    ## ── Titre centré ──
    frame:
        xalign 0.5
        yalign 0.07
        background "#000000CC"
        padding (34, 14, 34, 14)
        text "🌿 Quel chemin vas-tu prendre ?" size 42 bold True color "#c8ffb0" outlines [(2, "#000000", 0, 0)] xalign 0.5

    ## ── Moitié gauche : Champignons ──
    button:
        action Return("champignons")
        xpos 0
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF18"

        vbox:
            spacing 0

            add "images/chemin_champignons.png" fit "cover" xsize 960 ysize 760

            frame:
                xsize 960
                ysize 320
                background "#000000BB"
                hover_background "#1e4010EE"
                padding (36, 22, 36, 28)

                vbox:
                    xalign 0.5
                    spacing 18

                    text "🍄 Chemin des Champignons" size 38 bold True color "#7ec850" outlines [(2, "#000000", 0, 0)] xalign 0.5
                    text "Des champignons géants rouges à pois blancs..." size 27 color "#dfffb0" xalign 0.5 text_align 0.5
                    frame:
                        xalign 0.5
                        background "#4a8a20CC"
                        padding (34, 12, 34, 12)
                        text "← Prendre ce chemin" size 30 bold True color "#FFFFFF" xalign 0.5

    ## ── Séparateur central ──
    frame:
        xpos 958
        ypos 0
        xsize 4
        ysize 1080
        background "#FFD70066"

    ## ── Moitié droite : Fleurs ──
    button:
        action Return("fleurs")
        xpos 960
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF18"

        vbox:
            spacing 0

            add "images/chemin_fleur_arc_en_ciel.png" fit "cover" xsize 960 ysize 760

            frame:
                xsize 960
                ysize 320
                background "#000000BB"
                hover_background "#3a1a2aEE"
                padding (36, 22, 36, 28)

                vbox:
                    xalign 0.5
                    spacing 18

                    text "🌸 Sentier des Fleurs" size 38 bold True color "#FF85C2" outlines [(2, "#000000", 0, 0)] xalign 0.5
                    text "Des fleurs arc-en-ciel qui brillent dans la forêt..." size 27 color "#FFE4F5" xalign 0.5 text_align 0.5
                    frame:
                        xalign 0.5
                        background "#FF69B4CC"
                        padding (34, 12, 34, 12)
                        text "Prendre ce chemin →" size 30 bold True color "#FFFFFF" xalign 0.5


label foret_enchantee:

    scene bg foret with dissolve

    "À l'entrée de la Forêt Enchantée, deux chemins s'offraient à toi."
    "À droite : un sentier bordé de {b}fleurs aux couleurs arc-en-ciel{/b} qui brillaient doucement dans la pénombre."
    "À gauche : un chemin plus large, parsemé de gros {b}champignons{/b} rouges à pois blancs."

    $ choix_foret = renpy.call_screen("foret_choix_screen")

    if choix_foret == "fleurs":
        jump chemin_fleurs
    else:
        jump chemin_champignons


## --- Chemin des fleurs ---

label chemin_fleurs:

    scene bg sentier_fleurs with dissolve

    "Le sentier fleuri sentait bon la vanille et le miel. Les fleurs semblaient s'incliner sur ton passage, comme pour te saluer."

    scene bg sentier_fleurs2 with dissolve

    "Soudain, une petite lumière rose vint tourbillonner autour de toi."

    scene bg sentier_fleurs_floralie with dissolve

    fee_floralie "Bonjour, voyageur(se) ! Je suis {b}Floralie{/b}, la fée des fleurs. 🌸"
    fee_floralie "Tu as l'air bien pressé(e)... Tu vas vers la tour de Maléfra, n'est-ce pas ?"

    joueur "Oui ! Je dois récupérer la Pierre de Lumière pour sauver les licornes !"

    fee_floralie "Tu es courageux(se) ! Je voudrais t'aider. Prends cette {b}Fleur Arc-en-ciel{/b}."

    $ inventaire.append("Fleur Arc-en-ciel 🌈")

    fee_floralie "Elle a un pouvoir extraordinaire : elle apporte la joie à celui qui la sent. Elle peut adoucir même les cœurs les plus durs !"

    joueur "Merci beaucoup, Floralie !"

    fee_floralie "Fais vite ! Et méfie-toi de Grok le Troll... il garde le pont. Mais il adore les jolies choses !"

    scene bg sentier_fleurs2 with dissolve

    "Floralie disparut parmi les fleurs, et tu continuais ton chemin, la fleur magique précieusement rangée dans ta poche."

    jump pont_du_troll


## --- Chemin des champignons ---

label chemin_champignons:

    scene bg foret_champignons with dissolve

    "Les champignons géants formaient comme un tunnel coloré. Certains étaient si grands que tu pouvais te tenir dessous !"
    "Derrière le plus gros champignon, quelqu'un ronflait très fort..."

    scene bg gnome dort with dissolve

    "Tu t'approchais doucement et découvrais un tout petit gnome, profondément endormi, un grand livre de cartes ouvert sur le visage."
    "BOUM ! Tu trébuchas sur une racine et tombas dans les feuilles !"

    gnome_pip "Hein ?! Quoi ! Qui est là ?!"

    "Le gnome sauta sur ses pieds, l'air tout ébouriffé."

    scene bg gnome with dissolve

    gnome_pip "Oh ! Un enfant ! Tu m'as fait une de ces peurs ! Je m'appelle {b}Pip{/b}. 🍄"

    joueur "Désolé(e), Pip ! Je cherche la tour de la sorcière Maléfra."

    gnome_pip "Maléfra ?! Oh là là... Tu vas là-bas tout(e) seul(e) ?"

    joueur "Je dois récupérer la Pierre de Lumière ! Les licornes ont besoin de moi !"

    gnome_pip "Waow... Tu as vraiment du cran, [prenom] ! Tiens, prends cette {b}Carte Magique{/b}."

    $ inventaire.append("Carte Magique 🗺️")

    gnome_pip "C'est une carte des passages secrets de la forêt. Elle indique un chemin caché qui contourne le Pont du Vieux Grok. Très utile pour éviter les embêtements !"
    gnome_pip "Et si tu dois quand même passer par le pont... Grok adore par-dessus tout les {b}devinettes{/b}. Il ne peut pas y résister !"

    joueur "Merci Pip, tu es super !"

    "Pip repartit se terrer dans ses champignons en souriant, et tu continuais ta route vers le Pont du Vieux Grok."

    jump pont_du_troll


## ============================================================
## ACTE 2 : LE PONT DU VIEUX GROK (Choix 2)
## ============================================================

label pont_du_troll:

    scene bg troll dort pont with dissolve

    "Après avoir traversé la forêt, tu arrivais devant un vieux pont de pierre enjambant une rivière bouillonnante."
    "Et là, assis en travers du pont comme s'il faisait une sieste, se trouvait le plus gros troll que tu aies jamais vu !"
    "Il avait une peau verte, des oreilles comme des champignons, et des dents en or qui brillaient quand il souriait."

    scene bg troll debout pont with dissolve

    troll_grok "HALT ! Personne ne passe sur le pont de {b}GROK{/b} sans payer le péage !"

    scene bg troll with dissolve

    joueur "Quel péage ? Je n'ai pas d'argent..."

    troll_grok "Grok n'a pas besoin d'argent ! Grok veut... quelque chose de {i}beau{/i}. Ou alors... une {i}devinette{/i} !"

    if "Fleur Arc-en-ciel 🌈" in inventaire:
        jump troll_avec_fleur
    elif "Carte Magique 🗺️" in inventaire:
        jump troll_avec_carte
    else:
        jump troll_sans_objet


## --- Troll : tu as la Fleur ---

label troll_avec_fleur:

    "Tu regardas dans ta poche. La Fleur Arc-en-ciel brillait doucement."

    "🌸 {b}Que fais-tu face au troll ?{/b}"

    menu:
        "🌸  Offrir la Fleur Arc-en-ciel au troll":
            jump troll_fleur_offrir

        "🎵  Chanter une chanson pour le distraire":
            jump troll_chanter_fleur


label troll_fleur_offrir:

    "Tu sortis la fleur arc-en-ciel et la tendis au troll."

    joueur "Regarde comme elle est belle ! Elle sent merveilleusement bon. Je te l'offre si tu me laisses passer !"

    "Grok écarquilla ses grands yeux jaunes. Il se pencha vers la fleur et renifla..."

    troll_grok "Oh... Oh là là... Ça sent tellement bon que Grok a envie de {b}danser{/b} !"

    "Et le troll se mit à tourner sur lui-même en chantonnant, ce qui fit trembler tout le pont !"

    troll_grok "Prends ! PRENDS ! Tu as le droit de passer... Et même plus ! Tiens, prends ça !"

    $ inventaire.remove("Fleur Arc-en-ciel 🌈")
    $ inventaire.append("Clé Dorée ✨")

    troll_grok "C'est la Clé Dorée. Je l'ai trouvée y'a longtemps mais je sais pas à quoi elle sert. Toi t'as l'air malin(e), t'en feras sûrement quelque chose de bien !"

    joueur "Merci, Grok ! Tu es bien plus gentil qu'on ne le dit !"

    troll_grok "Chut ! Ne le dis à personne, Grok a une réputation à tenir !"

    "Tu traversas le pont en souriant."

    jump tour_malefra


label troll_chanter_fleur:

    "Tu pris une grande inspiration et te mis à chanter une chanson joyeuse."
    "Grok leva un sourcil, puis l'autre... et finit par se balancer d'un pied sur l'autre."

    troll_grok "Hm... Pas mal... pas mal du tout..."

    "Mais soudain, le troll aperçut la fleur qui dépassait de ta poche !"

    troll_grok "Hé ! C'est quoi cette chose brillante dans ta poche ?!"

    "Tu n'eus pas le choix : tu sortis la fleur."

    jump troll_fleur_offrir


## --- Troll : tu as la Carte ---

label troll_avec_carte:

    "Tu te souvins de ce que Pip t'avait dit : la carte montrait un chemin secret..."

    "🗺️ {b}Que fais-tu face au troll ?{/b}"

    menu:
        "🗺️  Consulter la Carte Magique pour trouver le passage secret":
            jump troll_carte_passage

        "🧩  Poser une devinette au troll":
            jump troll_devinette


label troll_carte_passage:

    "Tu t'éloignas discrètement du pont et déplias la carte de Pip."
    "Elle indiquait effectivement un passage secret : derrière les grands rochers gris sur la droite, un gué permettait de traverser la rivière à pieds secs !"
    "Tu suivis les indications et traversas sans même croiser le regard de Grok."

    troll_grok "Bizarre... J'ai l'impression d'avoir entendu quelque chose..."

    "Mais tu étais déjà de l'autre côté, riant tout doucement !"

    jump tour_malefra


label troll_devinette:

    troll_grok "Une devinette ?! Oh, Grok {b}ADORE{/b} les devinettes !"

    "Le troll s'assit en tailleur, les yeux brillants d'excitation."

    "🧩 {b}Quelle devinette vas-tu lui poser ?{/b}"

    menu:
        "🌙  « J'ai des milliers de dents mais je ne mords jamais. Qu'est-ce que c'est ? »":
            jump troll_devinette_peigne

        "🌈  « Plus tu en enlèves, plus elle grandit. Qu'est-ce que c'est ? »":
            jump troll_devinette_trou


label troll_devinette_peigne:

    "Grok réfléchit si longtemps que de la fumée sortait de ses oreilles !"

    troll_grok "Euh... euh... des... DENTS DE MONSTRE ??? Non... euh..."

    joueur "Non ! C'est un {b}peigne{/b} !"

    troll_grok "Aaah ! Trop malin(e) ! Grok a perdu ! Tu peux passer !"

    "Le troll s'écarta en bougonnant, mais avec un grand sourire."

    jump tour_malefra


label troll_devinette_trou:

    "Grok fronça ses énormes sourcils verts et réfléchit très fort."

    troll_grok "Euh... un arbre ??? Un bébé troll ???"

    joueur "Non ! C'est un {b}trou{/b} !"

    troll_grok "OH ! C'est trop bien comme devinette ! Grok est impressionné ! Passe, passe !"

    "Le troll s'écarta en applaudissant maladroitement."

    jump tour_malefra


## --- Troll : sans objet spécial ---

label troll_sans_objet:

    "Tu n'avais pas d'objet magique particulier, mais tu devais bien trouver un moyen de passer..."

    "😤 {b}Que tentes-tu ?{/b}"

    menu:
        "🎵  Chanter une berceuse pour endormir le troll":
            jump troll_berceuse

        "💨  Sprinter et passer en courant !":
            jump troll_courir


label troll_berceuse:

    "Tu te mis à chanter la plus douce berceuse que tu connaissais."
    "Grok bâilla... bâilla encore... et ses yeux se fermèrent lentement."

    troll_grok "Grok... Grok a... sommeil... zzzZZZ..."

    "Tu passas sur la pointe des pieds, retenant ta respiration. Un pas... deux pas... trois pas..."
    "CRAAAAC ! Une planche du pont craqua sous ton pied !"

    troll_grok "HM ?! Qui est là ?!"

    "Tu t'élançais en courant ! Le troll essaya de te rattraper, mais il était bien trop lent !"

    troll_grok "Reviens ici ! GROK N'A PAS FINI SA SIESTE !"

    "Tu arrivais de l'autre côté, hors d'haleine mais sain(e) et sauf(ve) !"

    jump tour_malefra


label troll_courir:

    "Tu pris ton élan... et sprinta de toutes tes forces !"
    "Grok fut tellement surpris qu'il resta bouche bée pendant une seconde."

    troll_grok "Hé ! HÉ ! ATTENDS !"

    "Tu courais, courais, courais... et passas le pont juste avant que Grok ne tende son énorme bras !"

    troll_grok "Grok impressionné ! Grok n'a jamais vu quelqu'un courir aussi vite !"

    "Tu n'attendis pas les compliments et continuais à courir vers la tour !"

    jump tour_malefra


## ============================================================
## ACTE 3 : LA TOUR DE MALÉFRA (Choix 3)
## ============================================================

label tour_malefra:

    scene bg tour_ext with dissolve

    "La tour de Maléfra était une horrible construction de pierres noires, couverte de lierre violet et entourée d'un nuage d'orage permanent."
    "Des éclairs silencieux zébraient le ciel autour d'elle. Une lumière violette pulsait à la fenêtre du sommet."
    "Tu observas la tour. Il y avait deux façons d'y entrer."

    "🏰 {b}Comment entrer dans la tour de Maléfra ?{/b}"

    menu:
        "🚪  Entrer discrètement par la grande porte":
            jump entree_grande_porte

        "🪟  Grimper sur le côté jusqu'à une fenêtre entrouverte":
            jump entree_fenetre


## --- Entrée par la grande porte ---

label entree_grande_porte:

    scene bg tour_int with dissolve

    "Tu t'approchas de la grande porte et l'ouvris doucement. Elle n'était pas verrouillée... peut-être un piège ?"
    "À l'intérieur : une longue salle sombre avec des torches violettes. Des armures vides se tenaient le long des murs."
    "Au fond de la salle, deux chemins : un {b}escalier{/b} qui montait, et une petite {b}porte ornée d'une étoile dorée{/b}."

    "⬆️ {b}Que fais-tu ?{/b}"

    menu:
        "⬆️  Monter l'escalier vers le sommet de la tour":
            jump escalier_sommet

        "⭐  Examiner la petite porte à l'étoile dorée":
            jump porte_etoile


## --- Escalier vers le sommet ---

label escalier_sommet:

    scene bg escalier with dissolve

    "Tu montas l'escalier. À chaque étage, des fioles colorées, des grimoires et des cristaux remplissaient les étagères."
    "Au dernier étage, la porte était grande ouverte."

    scene bg pierre with dissolve

    "Et là, sur un piédestal de marbre noir..."
    "La {b}{color=#FFD700}Pierre de Lumière{/color}{/b} ! 💎"
    "Elle brillait de mille feux, pulsant comme un cœur vivant. Même dans cette tour sinistre, elle était magnifique."
    "Mais... où était Maléfra ?"
    "Un bruit de pas résonna dans l'escalier. La sorcière remontait !"

    "⚡ {b}Que fais-tu ?{/b}"

    menu:
        "🤫  Attraper la Pierre et se cacher derrière l'armoire !":
            jump pierre_et_cacher

        "🏃  Attraper la Pierre et descendre en courant !":
            jump pierre_et_courir


label pierre_et_cacher:

    "Tu attrapas la Pierre de Lumière et te cachas derrière une grande armoire."

    sorciere "Où est passée ma pierre ?! Qui a osé entrer dans {b}ma{/b} tour ?!"

    "Maléfra tournait dans la pièce, furieuse. Elle était terrifiante : grande, habillée de noir, avec des yeux violets qui lançaient des éclairs."
    "Tu sentis quelque chose de chaud dans ta poche... Le {b}Cristal de Céleste{/b} !"

    if "Cristal de Céleste 💎" in inventaire:
        "Le cristal brilla intensément. Instinctivement, tu le sortis et le tins fort dans ta main."
        joueur "Pour les grands dangers, Céleste m'a dit !"

        "Une explosion de lumière dorée illumina toute la pièce !"

        sorciere "AAAH ! Cette lumière ! Je ne vois plus rien !"

        $ inventaire.remove("Cristal de Céleste 💎")
        $ pierre_obtenue = True

        "Tu t'élançais vers l'escalier et dévalais les marches à toute vitesse !"

        jump fin_bonne

    else:
        "Tu retins ton souffle. Maléfra passait juste devant l'armoire..."
        "... et s'arrêta."

        sorciere "Je sens une présence..."

        "Mais à cet instant, un loud {b}hennissement{/b} retentit depuis le bas de la tour !"

        jump licorne_aide_evasion


label pierre_et_courir:

    "Tu attrapas la Pierre et dévalas l'escalier !"

    sorciere "AU VOLEUR ! REVIENS ICI !"

    "Maléfra lançait des éclairs violets qui te rataient de peu !"
    "BOUM ! Un éclair frappa la rampe juste devant toi. Tu sautes par-dessus !"
    "BOUM ! Un autre éclair... Tu esquivas !"
    "La grande porte ! Tu la poussas et sortis en courant dans la nuit !"

    sorciere "Tu ne perdras rien pour attendre, petit(e) voleur(se) !"

    "Mais tu courais déjà loin dans la forêt, la Pierre de Lumière serrée contre ton cœur."

    $ pierre_obtenue = True

    jump fin_bonne


## --- La petite porte à l'étoile ---

label porte_etoile:

    scene bg porte doree with dissolve

    if "Clé Dorée ✨" in inventaire:
        "Tu tiras sur la poignée... verrouillée. Mais en fouillant dans ton sac, tu trouvas la Clé Dorée !"
        "La clé s'inséra parfaitement dans la serrure. {b}CLIC !{/b}"
        jump chambre_etoile_avec_cle

    else:
        "Tu tiras sur la poignée... la porte était verrouillée !"
        "Mais à travers le bois, tu entendis un son : un tout petit son, comme un cheval qui souffle doucement."

        joueur "Il y a quelqu'un là-dedans ?"

        licorne "Au secours... s'il te plaît..."

        "Une voix faible, comme un tintement de cloches dans le vent."

        joueur "Ne t'inquiète pas ! Je vais te sortir de là !"

        "Tu cherchas une autre solution... Sur le mur en face : des centaines de clés de toutes les tailles !"

        if "Cristal de Céleste 💎" in inventaire:
            "Le Cristal de Céleste vibra légèrement dans ta poche, brillant plus fort en direction d'une petite clé argentée en forme de flocon de neige !"
            "Tu la pris et l'essayas sur la porte. Elle tourna immédiatement !"
        else:
            "Tu en essayas plusieurs... La septième était la bonne !"

        jump chambre_etoile_avec_cle


label chambre_etoile_avec_cle:

    scene bg salle licorne with dissolve

    "Derrière la porte se trouvait une petite pièce ronde joliment décorée... et au milieu, attachée par des chaînes de fumée violette, une magnifique licorne blanche !"

    licorne "Oh ! Tu es venu(e) pour me sauver ?! 🦄"

    joueur "Je suis [prenom] ! Je viens de la part de Céleste. Je cherche la Pierre de Lumière !"

    licorne "La Pierre ! Maléfra l'a cachée dans la chambre du sommet, {b}sous le coussin rouge du grand trône noir{/b}. Fais vite, elle revient bientôt !"

    joueur "Et toi ? Comment je te libère ?"

    licorne "La Clé Dorée... si tu en avais une, elle pourrait briser mes chaînes !"

    if "Clé Dorée ✨" in inventaire:
        $ inventaire.remove("Clé Dorée ✨")
        "Tu posas la Clé Dorée sur les chaînes. Elles se brisèrent dans un nuage de fumée violette !"

        scene bg salle licorne with dissolve

        licorne "Je suis libre ! Oh merci, [prenom] ! Je vais t'aider !"

        $ etoile_libre = True

        "Étoile la Licorne bondit vers l'escalier. Tu la suivais au pas de course."
        jump sommet_avec_etoile

    elif "Cristal de Céleste 💎" in inventaire:
        "Tu n'avais pas de Clé Dorée... mais tu avais le Cristal de Céleste !"
        "Tu le posais contre les chaînes. Une lumière intense jaillit du cristal !"
        "Les chaînes fondirent comme neige au soleil !"

        $ inventaire.remove("Cristal de Céleste 💎")
        $ etoile_libre = True

        scene bg salle licorne with dissolve

        licorne "La magie dorée de Céleste ! Elle brise tous les sortilèges de Maléfra !"

        joueur "Super ! On monte chercher la Pierre ensemble ?"

        licorne "Oui ! Suis-moi !"

        jump sommet_avec_etoile

    else:
        "Tu n'avais pas d'objet magique pour briser les chaînes..."

        licorne "Ne t'inquiète pas ! Va chercher la Pierre. Je me souviendrai de ta bonté, [prenom]."
        licorne "Quand tu auras la Pierre, sa lumière brisera peut-être mes chaînes !"

        "Tu montas seul(e) vers le sommet."
        jump escalier_sommet_info_etoile


label escalier_sommet_info_etoile:

    scene bg sommet with dissolve

    "Le coussin rouge du trône... tu le soulevais et là :"
    "La {b}{color=#FFD700}Pierre de Lumière{/color}{/b} ! Elle brillait comme un petit soleil ! 💎"

    "Au moment où tu la saisis, sa lumière explosa dans toute la tour !"

    licorne "(d'en bas) Mes chaînes ! Elles se brisent ! La lumière de la Pierre les dissout !"

    sorciere "QUI OSE TOUCHER À MA PIERRE ?!"

    "Maléfra apparut dans un tourbillon de fumée noire !"

    sorciere "Un enfant ! Dans {b}ma{/b} tour ! Et mes chaînes qui disparaissent ?!"

    "Un fracas retentit ! Étoile venait de monter l'escalier en bondissant !"

    licorne "[prenom] ! Monte sur mon dos, {b}vite !{/b}"

    $ etoile_libre = True
    $ pierre_obtenue = True

    "Tu sautes sur le dos d'Étoile. La licorne déploya ses ailes — elle avait retrouvé sa magie au contact de la Pierre !"

    sorciere "NOOOON ! IMPOSSIBLE !"

    "Étoile s'élança vers la fenêtre et plongea dans le ciel étoilé !"

    jump fin_parfaite


## --- Sommet de la tour avec Étoile ---

label sommet_avec_etoile:

    scene bg sommet with dissolve

    "Au sommet de la tour, vous trouvâtes la Pierre de Lumière sous le coussin rouge du trône noir, exactement là où Étoile l'avait dit."
    "Mais à peine tu la touchas qu'un grondement terrible résonna dans toute la tour !"

    sorciere "QUI OSE TOUCHER À MA PIERRE ?!"

    "Maléfra apparut dans un tourbillon de fumée noire !"

    sorciere "Toi ! Un petit enfant ! Et mon Étoile s'est enfuie !"

    licorne "Je ne suis {b}pas{/b} ta licorne, Maléfra ! Tu ne m'as jamais appartenu !"

    "Maléfra leva son bâton magique pour frapper..."

    licorne "[prenom] ! Monte sur mon dos, {b}vite !{/b}"

    $ pierre_obtenue = True

    "Tu bondis sur le dos d'Étoile. La licorne déploya ses ailes — elle avait retrouvé sa magie au contact de la Pierre !"

    sorciere "NOOOON ! IMPOSSIBLLE !"

    "Étoile s'élança vers la fenêtre et plongea dans le ciel !"

    jump fin_parfaite


## --- Entrée par la fenêtre ---

label entree_fenetre:

    "Tu trouvas une liane solide sur le côté de la tour et commençais à grimper."
    "C'était haut... très haut... mais tu ne lâchas pas !"
    "Tu atteignis enfin une fenêtre entrouverte au milieu de la tour et te glissas à l'intérieur."

    scene bg laboratoire with dissolve

    "La pièce était un laboratoire magique : des chaudrons bouillonnants, des étagères de fioles, des livres de sorts qui volaient tout seuls... une porte mène à une autre salle, tu y vas"

    scene bg salle licorne

    "Tu arrives dans une salle ronde et tu vois, attachée par des chaînes de fumée violette... une licorne !"

    licorne "Oh ! Attention, ne touche à rien... tu ne sais pas ce que ces potions peuvent faire ! 🦄"

    joueur "Je suis [prenom] ! Je viens sauver les licornes ! Qui es-tu ?"

    licorne "Je suis {b}Étoile{/b}. Maléfra me retient prisonnière depuis qu'elle a volé la Pierre de Lumière."

    joueur "Je dois trouver la Pierre ! Tu sais où elle est ?"

    licorne "Elle est tout en haut, dans la chambre du trône, {b}sous le coussin rouge{/b}. Mais Maléfra peut revenir d'une seconde à l'autre !"

    "⚡ {b}Que décides-tu ?{/b}"

    menu:
        "🏃  Monter chercher la Pierre rapidement":
            jump monter_pierre_fenetre

        "🔑  Chercher d'abord comment libérer Étoile":
            jump liberer_etoile_fenetre


label monter_pierre_fenetre:

    scene bg sommet with dissolve

    "Tu grimpa l'escalier en courant. La chambre du trône était juste au-dessus."
    "La Pierre de Lumière était là, sur son coussin rouge. Tu tendis la main..."

    sorciere "Je t'attendais !"

    "Maléfra sortit de derrière le rideau, son bâton pointé vers toi !"

    sorciere "Tu croyais vraiment pouvoir me voler ma Pierre aussi facilement ?!"

    "Tu reculais vers la fenêtre..."

    if "Cristal de Céleste 💎" in inventaire:
        "Le cristal de Céleste brûlait dans ta poche. C'était le moment !"

        joueur "Céleste m'a donné ça pour les grands dangers !"

        "Tu lanças le cristal au sol. Une explosion de lumière dorée aveugla Maléfra !"

        $ inventaire.remove("Cristal de Céleste 💎")
        $ pierre_obtenue = True

        sorciere "Mes yeux ! Je ne vois rien ! NOOOON !"

        "Tu saisis la Pierre de Lumière et dévalas l'escalier !"

        jump fin_bonne

    else:
        "Pas d'objet magique... mais soudain, un grand fracas retentit dans le laboratoire en dessous !"

        licorne "(d'en bas) Maléfra ! J'ai renversé tous tes chaudrons par accident ! 😅"

        sorciere "MES POTIONS ! MES PRÉCIEUSES POTIONS !"

        "Maléfra se précipita à l'étage en dessous. Tu en profitais pour attraper la Pierre et descendre !"

        $ pierre_obtenue = True

        jump fin_bonne


label liberer_etoile_fenetre:

    scene bg laboratoire with dissolve

    "Tu cherchas un moyen de briser les chaînes qui retenaient Étoile."
    "Les chaînes étaient faites de magie noire... peut-être qu'une autre magie pourrait les dissoudre ?"

    if "Cristal de Céleste 💎" in inventaire:
        "Tu posais le Cristal de Céleste contre les chaînes. Elles fondirent instantanément, comme de la neige au soleil !"

        licorne "Je suis libre ! Oh, merci [prenom] ! La magie dorée dissout toujours les sortilèges noirs !"

        $ inventaire.remove("Cristal de Céleste 💎")
        $ etoile_libre = True

        "Étoile retrouva ses forces. Ensemble, vous montâtes vers le sommet."

        jump sommet_avec_etoile

    elif "Fleur Arc-en-ciel 🌈" in inventaire:
        "Tu effleuras les chaînes avec la Fleur Arc-en-ciel. Ses couleurs se répandirent le long des chaînes, les faisant éclater !"

        licorne "La magie de la forêt ! Elle rompt les sortilèges des sorcières !"

        $ inventaire.remove("Fleur Arc-en-ciel 🌈")
        $ etoile_libre = True

        joueur "Étoile ! On monte chercher la Pierre ensemble ?"

        licorne "Oui ! Vite !"

        jump sommet_avec_etoile

    else:
        "Tu n'avais pas d'objet magique pour briser les chaînes..."

        licorne "Attends ! Regarde ce grimoire ouvert sur la table. Il y a un contre-sort !"

        "Tu lus à voix haute : {i}\"Lumière du soir, brise les liens, libère ce qui est captif !\"}{/i}"
        "Rien ne se passa d'abord... puis les chaînes commencèrent à vibrer et à craqueler..."

        licorne "Ça marche ! Continue, n'arrête pas !"

        "Tu répétas les mots avec encore plus de conviction. Les chaînes explosèrent dans un nuage de lumière !"

        licorne "Je suis libre !! Tu l'as fait, [prenom] !"

        $ etoile_libre = True

        "Main dans la crinière, vous montâtes vers le sommet."

        jump sommet_avec_etoile


## --- Étoile aide à s'échapper ---

label licorne_aide_evasion:

    "Un hennissement retentissant ! Étoile avait réussi à briser partiellement ses chaînes et faisait une diversion !"

    licorne "[prenom] ! COURS ! Prends la Pierre et cours !"

    sorciere "TOI ! Tu oses me résister, Étoile ?!"

    "Maléfra se tourna vers le bas de la tour. Tu en profitais pour saisir la Pierre de Lumière et te précipiter vers l'escalier !"
    "Tu dévalas toutes les marches, traversas la grande salle et plongeais dans la nuit."

    licorne "(au loin) Va, [prenom] ! Sauve le royaume ! Je trouverai le moyen de m'enfuir. On se retrouvera bientôt, promis !"

    $ pierre_obtenue = True

    "Tu serras la Pierre contre ton cœur et courus vers la forêt, les larmes aux yeux mais le cœur résolu."

    jump fin_bonne


## ============================================================
## FINS DE L'AVENTURE
## ============================================================

## --- FIN PARFAITE : Pierre récupérée ET Étoile libérée ---

label fin_parfaite:

    $ pierre_obtenue = True

    scene bg ciel_victoire with dissolve

    "Étoile volait haut, très haut dans le ciel, te portant sur son dos."
    "La Pierre de Lumière brillait entre tes mains, illuminant les nuages de mille couleurs. 💎"
    "En dessous, le royaume d'Élysia reprenait vie : les fleurs regermaient, les ruisseaux chantaient, les licornes bondissaient en faisant jaillir des étoiles sous leurs sabots."

    licorne "[prenom]... merci. Sans toi, je serais encore prisonnière de Maléfra. 🦄"

    joueur "C'est toi qui m'as aidé(e) autant que je t'ai aidée ! On est une vraie équipe !"

    licorne "Une équipe... J'aime ça. Est-ce qu'on peut être amis/amies pour toujours ?"

    joueur "Pour toujours et à jamais !"

    scene bg prairie licorne with dissolve

    "Vous atterrîtes dans une grande prairie fleurie au cœur d'Élysia."
    "Toutes les licornes du royaume vous galopent libres, brillant de tous leurs feux."

    scene bg prairie with dissolve

    fee_celeste "Tu l'as fait, [prenom] ! Tu as sauvé le royaume et tu as libéré Étoile ! C'est plus que ce qu'on espérait ! 🌟"

    scene bg lumina with dissolve

    "La Reine des Licornes, Lumina, s'avança majestueusement et toucha ton front de sa corne dorée."

    reine "Au nom d'Élysia, je te décerne le {b}Double Sceau des Héros{/b}. Tu seras toujours le/la bienvenu(e) dans notre royaume."
    reine "Et Étoile sera ta licorne gardienne... pour la vie !"

    hide screen inventaire_hud

    jump epilogue_parfait


## --- FIN BONNE : Pierre récupérée, Étoile non libérée ---

label fin_bonne:

    scene bg sky with dissolve

    "Tu courus, courus, courus jusqu'à sortir de la forêt, la Pierre de Lumière serrée contre ton cœur."
    "Dans une clairière ensoleillée, tu t'arrêtais enfin et regardas la Pierre."
    "Elle brillait si fort qu'on aurait dit une petite étoile dans tes mains."

    scene bg prairie with dissolve

    fee_celeste "Tu l'as fait, [prenom] ! Tu l'as vraiment fait ! ✨"

    fee_celeste "La Pierre de Lumière ! Les licornes vont retrouver leur magie ! Le royaume est sauvé !"

    "Au même instant, des lumières dorées et roses apparurent dans tout le ciel. Les licornes d'Élysia retrouvaient leurs pouvoirs une à une."

    joueur "Céleste... il y a une licorne prisonnière dans la tour. Elle s'appelle Étoile. Je n'ai pas pu la libérer cette fois."

    fee_celeste "Je sais, [prenom]. Mais grâce à toi, le royaume est sauvé ! Étoile sera libérée très bientôt, maintenant que la Pierre est de retour."
    fee_celeste "Tu es un(e) vrai(e) héros/héroïne, [prenom] !"

    scene bg lumina with dissolve

    "La Reine des Licornes, Lumina, descendit du ciel et s'inclina devant toi."
    "Elle posa délicatement sa corne sur ton front."

    reine "Le {b}Sceau des Amis des Licornes{/b}... Pour [prenom], qui a sauvé Élysia avec courage ! 🌟"

    hide screen inventaire_hud

    jump epilogue_bon


## ============================================================
## ÉPILOGUES
## ============================================================

label epilogue_parfait:

    $ persistent.trophee_double_sceau = True

    scene bg noir with dissolve

    "⭐ ⭐ ⭐ {b}{size=+8}FIN MAGIQUE{/size}{/b} ⭐ ⭐ ⭐"
    " "
    "{b}Le Double Héros d'Élysia !{/b}"
    " "
    "Grâce à toi, la Pierre de Lumière est de retour et {b}Étoile la Licorne est libre{/b} !"
    "Tu as réussi l'aventure de la façon la plus merveilleuse qui soit."
    " "
    "{color=#FFD700}Étoile et [prenom] devinrent les meilleurs amis du monde.{/color}"
    "{color=#FFD700}Ensemble, ils vécurent de nombreuses autres aventures dans le royaume d'Élysia.{/color}"
    " "
    "{i}Quant à Maléfra... elle se retrouva seule dans sa tour, sans plus aucun pouvoir.{/i}"
    "{i}Peut-être qu'un jour elle comprendrait que l'amitié est plus puissante que la magie noire...{/i}"
    " "
    "{b}{color=#FFD700}🏆 Tu as obtenu le Double Sceau des Héros d'Élysia — Récompense Suprême ! 🏆{/color}{/b}"

    jump menu_fin


label epilogue_bon:

    $ persistent.trophee_amis_licornes = True

    scene bg noir with dissolve

    "🌟 {b}{size=+8}FIN : Le Héros du Royaume{/size}{/b} 🌟"
    " "
    "Le royaume d'Élysia fut sauvé grâce à ton courage !"
    "La Pierre de Lumière retrouva sa place, et les licornes fleurirent à nouveau."
    " "
    "{color=#FFD700}Étoile la Licorne fut libérée quelques jours plus tard par les fées du royaume.{/color}"
    "{color=#FFD700}Elle n'oublia jamais [prenom] et l'attendit chaque nuit sous les étoiles...{/color}"
    " "
    "{i}Peut-être que [prenom] reviendra la retrouver dans une prochaine aventure ?{/i}"
    " "
    "{b}{color=#FFD700}🌟 Tu as obtenu le Sceau des Amis des Licornes ! 🌟{/color}{/b}"
    " "
    "{i}(Rejoue l'aventure pour découvrir la Fin Magique !){/i}"

    jump menu_fin


## ============================================================
## MENU DE FIN
## ============================================================

label menu_fin:

    " "
    "Que veux-tu faire ?"

    menu:
        "🔄  Rejouer (pour explorer d'autres chemins !)":
            $ inventaire     = []
            $ etoile_libre   = False
            $ pierre_obtenue = False
            jump choisir_personnage

        "🏠  Retourner au menu principal":
            $ inventaire     = []
            $ etoile_libre   = False
            $ pierre_obtenue = False
            jump start

    return

