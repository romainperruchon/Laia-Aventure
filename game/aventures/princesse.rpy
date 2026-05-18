## ============================================================
## AVENTURE 2 : PROTÉGER LA PRINCESSE
## Fichier : game/aventures/princesse.rpy
##
## PLAN DE L'HISTOIRE
## ------------------
## Acte 1 — L'Appel du Roi          : Le roi demande de l'aide.
##           Choix : route du Nord (bouclier) ou route de l'Est (alliée Solène).
##
## Acte 2 — La Forêt des Ombres     : Embuscade de gobelins.
##           Choix : combattre ou ruser.
##
## Acte 3 — Le Village en Flammes   : Le dragon Ignar attaque.
##           Choix : sauver les villageois ou foncer vers la tanière.
##
## Acte 4 — La Tanière du Dragon    : Affrontement final avec Ignar.
##           Choix : combattre / négocier / utiliser un objet magique.
##
## Acte 5 — Le Retour               : Résolution selon les actions passées.
##
## FINS
## ----
##   🏆 Fin Parfaite   : Princesse sauvée, dragon vaincu, héros sacré Chevalier
##   🌟 Fin Bonne      : Princesse sauvée, dragon enfui
##   💔 Fin Difficile  : Princesse blessée mais vivante, dragon vaincu
## ============================================================

## Variables propres à cette aventure
default p2_a_bouclier  = False   # Vrai si le bouclier magique a été trouvé
default p2_a_solene    = False   # Vrai si Solène accompagne le héros
default p2_villageois  = False   # Vrai si les villageois ont été secourus
default p2_arya_blessee  = False   # Vrai si la princesse a été blessée pendant l'acte 4


## ============================================================
## INTRODUCTION (sélection du personnage puis démarrage)
## ============================================================

label intro_princesse:

    show screen inventaire_hud

    $ p2_a_bouclier  = False
    $ p2_a_solene    = False
    $ p2_villageois  = False
    $ p2_dragon_mort = False

    scene bg sky with dissolve

    "Il était une fois un royaume prospère nommé {b}Val-Doré{/b}."
    "Ses champs dorés s'étendaient à perte de vue, ses rivières chantaient,\net ses habitants vivaient en paix depuis des générations."
    "Mais cette paix allait être brisée par la créature la plus redoutée du monde connu..."

    scene bg chateau_ext with dissolve

    "Au cœur du royaume se dressait le fier château du {b}Roi Aldric{/b},\ndont la tour la plus haute touchait presque les nuages."
    "Et dans cette tour vivait la {b}Princesse Arya{/b},\ncurieuse, malicieuse, et plus courageuse qu'on ne le disait."

    scene bg foret_sombre with dissolve

    "Mais à l'est, par-delà la Forêt des Ombres,\ndans une tanière creusée au flanc du Mont Cramoisi..."
    "...dormait {b}Ignar{/b}, le Dragon Rouge."
    "Ses écailles brillaient comme des braises.\nSon souffle pouvait réduire un village en cendres en trois battements d'ailes."
    "Cela faisait dix ans qu'il dormait. Mais cette nuit-là... il s'était réveillé."

    jump acte1_appel_du_roi


## ============================================================
## ACTE 1 : L'APPEL DU ROI
## ============================================================

label acte1_appel_du_roi:

    scene bg throne_room with dissolve

    "Le lendemain matin, un messager royal frappait à ta porte avant même le lever du soleil."

    messager "Au nom du Roi Aldric de Val-Doré, je te convoque d'urgence au château !"

    "Tu n'avais jamais reçu un tel honneur. Ni une telle frayeur."
    "Quand tu arrivais dans la grande salle du trône, le roi était debout devant sa chaise,\nle visage gris comme la pierre."

    roi_aldric "Enfin ! {b}[prenom]{/b}... ils m'ont dit que tu étais courageux(se). J'espère que c'est vrai."

    joueur "Votre Majesté... qu'est-il arrivé ?"

    roi_aldric "Ignar. Le Dragon Rouge s'est réveillé cette nuit."
    roi_aldric "Il a survolé les remparts en hurlant, et quand l'aube est venue..."
    roi_aldric "Ma fille, la Princesse Arya... elle a disparu de sa chambre."

    "Un silence de plomb s'abattit sur la salle du trône."

    joueur "Il l'a enlevée ?!"

    roi_aldric "Ses gardes ont retrouvé une écaille rouge sang sur le rebord de la fenêtre."
    roi_aldric "Sa tanière se trouve au Mont Cramoisi, à l'est, après la Forêt des Ombres."
    roi_aldric "Mes chevaliers ont peur. Personne n'ose y aller. Mais toi... on dit que tu n'as peur de rien."

    joueur "Je vais la ramener, Majesté. Je vous le promets."

    roi_aldric "Prends ceci."

    $ inventaire.append("Épée du Roi ⚔️")

    roi_aldric "C'est l'épée de mon père. Elle n'a jamais trahi ses propriétaires."
    roi_aldric "Et prends garde... Ignar est malin. Il ne te fera pas de cadeau."

    "Tu serras la poignée de l'épée et regardas la carte que le messager dépliait sur la table."
    "Deux routes menaient au Mont Cramoisi."

    scene bg chateau_ext with dissolve

    "Devant le portail du château, deux chemins s'ouvraient à toi."
    "Au {b}nord{/b} : la route directe, rapide mais qui traversait les Gorges Sauvages.\nDes voyageurs y avaient trouvé de vieilles armures et des reliques oubliées."
    "À {b}l'est{/b} : la route des villages, plus longue, mais la chevalière {b}Solène{/b}\ny patrouillait depuis des semaines. Elle connaissait la Forêt des Ombres comme sa poche."

    "⚔️ {b}Quelle route prends-tu ?{/b}"

    menu:
        "🧭  La route du Nord — rapide, passer par les Gorges Sauvages":
            jump acte1_route_nord

        "🛤️  La route de l'Est — passer par les villages, rejoindre Solène":
            jump acte1_route_est


## --- Route du Nord : les Gorges Sauvages ---

label acte1_route_nord:

    scene bg grotte with dissolve

    "Tu pris la route du Nord au galop."
    "Les Gorges Sauvages étaient effectivement impressionnantes :\ndes parois de roche noire s'élevaient de chaque côté du sentier,\ncomme deux géants endormis."
    "Au fond d'une alcôve, tu remarquais quelque chose qui brillait faiblement..."
    "Un vieux {b}bouclier{/b} incrusté d'une gemme bleue, appuyé contre la paroi rocheuse.\nPorté par qui ? Depuis quand ? Impossible à dire."

    "Sous le bouclier, gravé dans la pierre, on lisait :\n{i}\"Celui qui protège les autres sera lui-même protégé.\"}{/i}"

    joueur "Un bouclier magique... Il pourrait être utile contre le feu d'un dragon !"

    $ inventaire.append("Bouclier des Gorges 🛡️")
    $ p2_a_bouclier = True

    "Tu attachas le bouclier dans ton dos et continuais ta route."
    "La route du Nord te faisait gagner une demi-journée de voyage."
    "À l'horizon, les premières silhouettes des arbres de la Forêt des Ombres se découpaient sur le ciel."

    "Soudain, une voix t'interpella depuis un rocher."

    solene "Halte ! Qui va là ?"

    joueur "Je suis [prenom] ! J'vais au Mont Cramoisi sauver la Princesse Arya !"

    solene "Vraiment ? Seul(e) comme ça ? Tu es soit très courageux(se)... soit très imprudent(e)."

    "La femme qui sauta du rocher portait une armure bleue et tenait une lance brillante."
    "Elle te jaugea une seconde, puis sourit."

    solene "Je suis {b}Solène{/b}, chevalière de Val-Doré. Je patrouillais justement ces routes."
    solene "Je t'accompagne. Deux valent mieux qu'un face à Ignar."

    $ p2_a_solene = True

    joueur "Avec plaisir, Solène ! Je suis [prenom]."

    solene "J'ai entendu parler de toi. Allons-y, la princesse n'a pas de temps à perdre."

    "Ensemble, vous approchâtes de la lisière de la Forêt des Ombres."

    jump acte1_fin


## --- Route de l'Est : rejoindre Solène ---

label acte1_route_est:

    scene bg village with dissolve

    "Tu pris la route de l'Est en longeant les villages endormis."
    "L'aube à peine levée, les coqs chantaient encore. Tout semblait calme... pour l'instant."
    "Dans le deuxième village, tu aperçus une silhouette en armure bleue devant la forge."

    solene "Toi ! C'est toi [prenom] dont on m'a parlé ?"

    joueur "C'est moi. Je cherche la princesse Arya, capturée par Ignar."

    solene "Je le sais. Le roi m'a envoyé un message hier soir."
    solene "Je m'appelle {b}Solène{/b}. Chevalière de Val-Doré. Je connais la Forêt des Ombres et les terres du Mont Cramoisi."
    solene "J'attendais quelqu'un d'assez courageux pour tenter cette mission."

    joueur "Tu m'accompagnes alors ?"

    solene "Essaie de m'en empêcher !"

    $ p2_a_solene = True

    "La forge­ron du village vous regarda partir avec les yeux écarquillés."

    "Avant de quitter le village, la vieille guérisseuse Merna sortit de chez elle et vous appela."

    "Une très vieille dame aux yeux brillants\nvous tendait quelque chose enveloppé dans un linge."

    "\"Prenez ça, les braves. Contre le feu du dragon, rien de mieux que l'eau de la Source Glacée.\""

    $ inventaire.append("Fiole d'Eau Glacée 💧")

    solene "Merci, Merna. Nous en aurons sûrement besoin."

    "Vous reprîtes la route d'un bon pas, la Forêt des Ombres se dessinant à l'horizon."

    jump acte1_fin


## --- Fin de l'Acte 1 ---

label acte1_fin:

    scene bg foret_sombre with dissolve

    "La lisière de la Forêt des Ombres se dressait devant toi comme un mur de ténèbres."
    "Les arbres étaient si grands et si serrés que leurs branches formaient\nun toit opaque au-dessus du sentier."
    "Pas un rayon de soleil ne traversait ce plafond de feuilles sombres."

    if p2_a_solene:
        solene "Je connais ce chemin. Reste près de moi et ne fais pas de bruit."
        solene "Les gobelins d'Ignar patrouillent dans cette forêt. Il les a envoyés pour barrer la route."
        joueur "Des gobelins ? Combien ?"
        solene "Assez pour nous causer des ennuis si on n'est pas prudents."
    else:
        "Tu entras seul(e) dans la forêt, l'épée à la ceinture, le cœur battant fort."
        "Quelque chose bougea dans les buissons sur ta gauche."
        "Puis à droite. Puis derrière."
        "Tu n'étais clairement pas seul(e) ici."

    "Les ombres bougèrent. Des yeux jaunes s'allumèrent entre les troncs."
    "L'Acte 2 approchait... et avec lui, la première vraie épreuve."

    jump acte2_foret_des_ombres


## ============================================================
## ACTE 2 : LA FORÊT DES OMBRES
## ============================================================

label acte2_foret_des_ombres:

    scene bg foret_sombre with dissolve

    "Tu avançais prudemment entre les arbres. Chaque branche craquait sous tes pas\ncomme si la forêt elle-même cherchait à te trahir."
    "Les yeux jaunes dans les buissons se multiplièrent."
    "Puis trois formes trapues et verdâtres bondirent sur le sentier,\nbrandissant des gourdins cloutés et ricanant entre leurs dents pointues."

    gobelin "GRK ! Personne passe ! Ignar dit : personne passe la forêt !"
    gobelin "Vous retournez d'où vous venez... ou on vous fait passer le goût de marcher !"

    "Il y en avait trois en face. Et dans les buissons derrière eux, tu entendais d'autres s'agiter."

    if p2_a_solene:
        solene "(tout bas, sans bouger les lèvres) J'en compte cinq en tout. Trois devant, deux cachés à gauche."
        solene "On peut les combattre ou les semer. Qu'est-ce que tu préfères ?"

        "🌿 {b}Comment voulez-vous gérer les gobelins ?{/b}"

        menu:
            "⚔️  Charger et les combattre directement avec Solène":
                jump acte2_combat_avec_solene

            "🤫  Créer une diversion et contourner en silence":
                jump acte2_diversion_avec_solene

            "🗣️  Tenter de négocier ou de les intimider":
                jump acte2_intimidation

    else:
        "Tu étais seul(e). Trois contre un, avec d'autres dans l'ombre. Pas idéal."
        "Il fallait être malin(e)."

        "🌿 {b}Que fais-tu face aux gobelins ?{/b}"

        menu:
            "⚔️  Dégainer l'Épée du Roi et charger !":
                jump acte2_combat_seul

            "🤫  Ramasser une pierre et la lancer loin derrière eux pour les distraire":
                jump acte2_diversion_seul

            "🗣️  Crier le nom du dragon Ignar pour les terroriser":
                jump acte2_intimidation


## --- Combat avec Solène ---

label acte2_combat_avec_solene:

    "Solène te lança un regard entendu."
    "À trois, deux, un..."

    solene "POUR VAL-DORÉ !"

    "Vous chargeâtes ensemble ! Solène fit voltiger son lance-bouclier,\ndessinant des arcs de lumière bleue qui éblouirent les gobelins."

    if p2_a_bouclier:
        "Tu brandis le Bouclier des Gorges devant toi."
        "Le chef gobelin frappa de toutes ses forces… et recula en hurlant,\nsa main engourdie par le choc magique du bouclier !"
        gobelin "Aïe ! Bouclier brûle ! C'est de la magie ! RETRAITE !"
    else:
        "Tu levais l'Épée du Roi. Sa lame captait la faible lumière qui filtrait\nentre les branches et la renvoyait en éclairs dorés."
        gobelin "L'épée royale ! C'est l'épée du roi ! RETRAITE !"

    "Les gobelins détalèrent en couinant dans tous les sens."
    gobelin "Ignar va pas être content... mais on préfère Ignar fâché que nous morts !"

    "Le silence retomba sur la forêt. Solène souffla."
    solene "Bien joué. Ils n'osent pas affronter l'acier royal."

    jump acte2_apres_gobelins


## --- Diversion avec Solène ---

label acte2_diversion_avec_solene:

    solene "Bonne idée. Je vais attirer leur attention à droite.\nToi, file à gauche entre ces deux chênes, tu vois ?"

    joueur "Je vois. Go !"

    "Solène ramassa une grosse branche et la lança bruyamment dans les fourrés à sa droite."

    gobelin "HÉ ! Là-bas ! Y'a quelqu'un !"
    gobelin "CHOPE-LE !"

    "Les cinq gobelins se ruèrent vers les fourrés à droite."
    "Tu courus silencieusement entre les deux chênes, Solène sur tes talons dix secondes plus tard."

    solene "(essoufflée) Parfait. Ils cherchent encore dans les buissons. On a de l'avance !"

    "En chemin, tu remarquais quelque chose d'accroché à un tronc d'arbre :\nune vieille {b}corne de brume{/b} en bois sculpté."
    "Un message y était gravé : {i}\"Pour appeler les alliés de la forêt.\"{/i}"

    $ inventaire.append("Corne de Brume 🎺")

    joueur "Je prends ça. On ne sait jamais."

    jump acte2_apres_gobelins


## --- Combat seul ---

label acte2_combat_seul:

    "Tu dégainas l'Épée du Roi. Sa lame dorée scintilla même dans la pénombre."

    gobelin "Oh... oh non. C'est... c'est l'épée du palais royal !"

    "Les gobelins se regardèrent. Ils reculèrent d'un pas... deux pas..."

    if p2_a_bouclier:
        "Tu levais aussi le Bouclier des Gorges. La gemme bleue s'illumina d'un éclat vif."
        gobelin "Bouclier magique ET épée royale ?! C'est trop ! On se casse !"
        "Les gobelins détaleèrent en hurlant, se bousculant pour fuir plus vite."
    else:
        "Le chef gobelin hésita... puis décida de charger quand même."
        "Le combat fut bref mais intense. Tu reçus un coup de gourdin\nsur l'épaule — aïe — mais tu tins bon."
        "L'épée du roi était si bien équilibrée qu'elle semblait guider ta main toute seule."
        "Deux gobelins s'enfuirent après le premier échange. Le chef suivit de près."
        gobelin "On r'viendra ! Ignar saura que t'es là !"

    jump acte2_apres_gobelins


## --- Diversion seul ---

label acte2_diversion_seul:

    "Tu ramasas discrètement une grosse pierre.\nTu visas, tu lançais... PLOUF ! La pierre atterrit loin dans les fourrés à droite."

    gobelin "HÉ ! Là-bas !"
    gobelin "Vite ! Attrapez-le !"

    "Parfait. Pendant que les gobelins chargeaient dans la mauvaise direction,\ntu te glissais entre les arbres à gauche, rapide et silencieux(se) comme une ombre."
    "Quand tu t'arrêtas enfin, hors d'haleine mais sain(e) et sauf(ve),\ntu entendais encore les gobelins grommeler au loin."
    "Bien joué."

    "En reprenant le sentier, tu trouvais une vieille {b}corne de brume{/b}\naccrachée à un tronc, avec un message gravé :\n{i}\"Pour appeler les alliés de la forêt.\"{/i}"

    $ inventaire.append("Corne de Brume 🎺")

    joueur "Je prends ça. On ne sait jamais."

    jump acte2_apres_gobelins


## --- Intimidation ---

label acte2_intimidation:

    "Tu pris une grande inspiration et criais d'une voix aussi grave que possible :"

    joueur "IGNAR M'A ENVOYÉ PERSONNELLEMENT ! Laissez-moi passer ou je lui dirai que vous m'avez bloqué !"

    "Les gobelins s'arrêtèrent net. Ils se consultèrent en marmonnant."

    gobelin "(à voix basse) ...Ignar va nous griller si on bloque son messager..."
    gobelin "(à voix basse) ...Ouais mais si c'est un mensonge Ignar va nous griller pareil..."
    gobelin "(à voix basse) ...Alors on fait quoi ?"

    "Un long silence."

    gobelin "OK. Vous passez. Mais on vous surveille."

    if p2_a_solene:
        solene "(te chuchotant) Je n'aurais pas osé. Bien joué !"
    else:
        "Tu retins ton souffle jusqu'à être hors de leur vue, puis soufflais un grand coup."

    jump acte2_apres_gobelins


## --- Après les gobelins ---

label acte2_apres_gobelins:

    scene bg foret_sombre with dissolve

    "Les gobelins franchis (ou semés), tu continuais à travers la forêt."
    "Plus tu avançais, plus les arbres devenaient noirs et tordus,\nleurs branches noueuses s'entrelaçant comme des doigts crispés."
    "L'air sentait la fumée."

    if p2_a_solene:
        solene "Attends... cette odeur..."
        joueur "De la fumée ?"
        solene "Du feu. Et pas un feu de cheminée."
    else:
        joueur "Cette odeur... c'est de la fumée ?"

    "Tu escaladas un talus herbeux à la sortie de la forêt et regardas au loin."
    "À l'horizon, dans la direction du village de Preval..."
    "Des {b}flammes orange{/b} s'élevaient dans le ciel du soir."

    if p2_a_solene:
        solene "Preval. Le dragon attaque Preval !"
        solene "C'est le village entre la forêt et le Mont Cramoisi."
        solene "On doit y aller. Ces gens ont besoin d'aide."
    else:
        "Ce devait être Preval, le village que la carte indiquait avant le Mont Cramoisi."
        "Des gens étaient en danger."

    jump acte2_fin


label acte2_fin:

    scene bg village_feu with dissolve

    "Tu courais vers le village en flammes, le cœur serré."
    "L'Acte 3 approchait : le dragon Ignar lui-même t'y attendait peut-être..."

    jump acte3_village_flammes

## ============================================================
## ACTE 3 : LE VILLAGE EN FLAMMES
## ============================================================

label acte3_village_flammes:

    scene bg village_feu with dissolve

    "Tu arrivais en courant à l'entrée de Preval."
    "La moitié du village était en feu. Des villageois couraient en tous sens, affolés.\nDes enfants pleuraient devant leur maison qui brûlait."
    "Et au-dessus de tout ça, battant des ailes comme un cauchemar vivant..."
    "...{b}Ignar{/b}."

    "Le dragon était gigantesque. Ses écailles rouge sang brillaient comme des braises.\nSes yeux jaunes balayaient le village avec une indifférence terrifiante."
    "Et dans sa griffe gauche, bien serrée mais visiblement vivante et furieuse..."

    princesse "LÂCHE-MOI, ESPÈCE DE GRAND LÉZARD MAL ÉLEVÉ !"

    dragon "Silence, petite princesse. Tu es mon otage, pas mon amie."

    princesse "Je vais te mordre si tu ne me lâches pas !"

    dragon "Ha. Tu es drôle. Pour une humaine."

    "Ignar remarqua ta présence. Ses naseaux se dilatèrent."

    dragon "Ah... un(e) autre héros qui vient jouer au brave. Comme c'est touchant."
    dragon "Tu arrives trop tard, petit(e) [prenom]. La princesse reste avec moi."

    "Il cracha une colonne de feu vers le sol devant toi."
    "Les flammes s'élevèrent à trois mètres de hauteur."

    if p2_a_solene:
        solene "On doit choisir vite ! Les villageois sont pris au piège, mais si on ne suit pas Ignar maintenant..."
        joueur "Je sais. Qu'est-ce qu'on fait ?"
    else:
        "Autour de toi, les villageois criaient, coincés entre les flammes."
        "Le dragon pouvait s'envoler à tout moment avec Arya."

    "🔥 {b}Que fais-tu en priorité ?{/b}"

    menu:
        "🏃  Suivre Ignar immédiatement — ne pas le laisser s'échapper !":
            jump acte3_suivre_ignar

        "🏘️  Secourir d'abord les villageois coincés dans les flammes":
            jump acte3_secourir_villageois


## --- Choix : Suivre Ignar ---

label acte3_suivre_ignar:

    "Tu t'élançais vers le dragon, l'épée levée."

    joueur "Ignar ! Pose la princesse !"

    dragon "Oh, de l'audace. J'aime ça... un tout petit peu."

    "Ignar souffla une seconde boule de feu dans ta direction !"

    if p2_a_bouclier:
        "Tu levas le Bouclier des Gorges instinctivement."
        "Les flammes s'écrasèrent contre la gemme bleue dans un craquement sonore.\nLe bouclier vibra violemment dans ta main mais tint bon !"
        "La gemme bleue se fissura légèrement. Le bouclier avait absorbé le pire."
        joueur "Ça brûle mais je tiens !"
    elif "Fiole d'Eau Glacée 💧" in inventaire:
        "Tu dégainas la fiole et la lançais vers les flammes !"
        "L'eau glacée créa un nuage de vapeur qui dévia une partie du feu."
        "Tu reçus quand même une vague de chaleur intense qui te fit reculer de deux pas."
        joueur "Aïe... mais je suis encore debout !"
    else:
        "Tu plongeais sur le côté, roulant dans la poussière."
        "Les flammes brûlèrent l'air à quelques centimètres de ton visage."
        "Tu te relevais, les sourcils légèrement roussis."
        joueur "C'était chaud..."

    "Ignar renifla, presque amusé."
    dragon "Tu survivras peut-être jusqu'à ma tanière après tout. Intéressant."
    dragon "Je t'attends au Mont Cramoisi... si tu en as le courage."

    "D'un puissant battement d'ailes, il s'envola vers l'est, Arya toujours dans sa griffe."

    princesse "(de loin) [prenom] ! Le Mont Cramoisi ! Trouve la faille dans la paroi nord !"

    dragon "SILENCE !"

    princesse "AÏE ! Lâche mes cheveux !"

    "Ils disparurent dans le ciel cramois."
    "Derrière toi, le village continuait de brûler. Tu n'avais pas aidé les villageois."

    $ p2_villageois = False

    if p2_a_solene:
        solene "Elle nous a donné une information : la faille dans la paroi nord. C'est l'entrée de la tanière."
        solene "...Mais ces villageois... j'aurais voulu qu'on puisse faire quelque chose."
    else:
        "Tu notais mentalement : faille dans la paroi nord. L'entrée de la tanière."
        "Mais le village derrière toi te pesait sur le cœur."

    jump acte3_fin


## --- Choix : Secourir les villageois ---

label acte3_secourir_villageois:

    "Tu tournais le dos au dragon et rugissais aux villageois :"

    joueur "Par ici ! Tout le monde vers la fontaine du centre !"

    "Les villageois commencèrent à se regrouper. Mais des flammes coupaient la rue principale."

    if "Fiole d'Eau Glacée 💧" in inventaire:
        "Tu sortis la fiole d'eau glacée et la brisis sur les flammes qui bloquaient le chemin."
        "L'eau glacée créa une trouée dans le feu — juste assez large et assez longtemps."
        joueur "PASSEZ MAINTENANT ! Vite !"
        "Dix villageois se faufilèrent à travers la trouée avant que les flammes ne se referment."
        $ inventaire.remove("Fiole d'Eau Glacée 💧")
        $ p2_villageois = True

    elif "Corne de Brume 🎺" in inventaire:
        "Tu soufflais dans la Corne de Brume."
        "Un son grave et puissant résonna dans tout le village."
        "Les villageois se figèrent une seconde... puis comprirent et suivirent le son vers toi."
        "Guidés par la corne, ils trouvèrent le chemin dégagé."
        $ p2_villageois = True

    elif p2_a_solene:
        solene "Je connais ce village ! Il y a un puits derrière la forge, les flammes ne l'ont pas atteint !"
        "Solène prit la tête du groupe et guida les villageois par les ruelles de derrière."
        "Tu assurais les arrières, repoussant les flammèches avec ton manteau."
        $ p2_villageois = True

    else:
        "Sans eau ni guide, tu cours de maison en maison en criant."
        "La plupart des villageois parviennent à fuir, mais deux familles restèrent coincées."
        "Tu les rejoignis et les guidais à travers la fumée au jugé, à tâtons."
        "Tout le monde s'en sortit, mais juste."
        $ p2_villageois = True

    "Les villageois étaient saufs. Tu soufflais de soulagement."

    "Mais quand tu lèveras les yeux vers le ciel..."
    "Ignar n'était plus là. Il avait profité de cette minute pour s'envoler."

    dragon "(voix lointaine, depuis le ciel) Brave choix, petit(e) héros(ïne). Les faibles d'abord."
    dragon "Je t'attends dans ma tanière. Si tu oses venir."

    princesse "(de très loin) LA FAILLE NORD ! LA FAILLE DANS LA PAROI NORD !"

    "Sa voix se perdit dans le vent."

    if p2_a_solene:
        solene "Elle a dit la faille nord. C'est l'entrée de la tanière d'Ignar."
        solene "Tu as bien fait de sauver ces gens, [prenom]. Mais maintenant, on ne peut plus perdre de temps."
    else:
        "La faille dans la paroi nord du Mont Cramoisi. Tu le notais dans ta tête."
        "Un vieux villageois te saisit le bras."
        "\"Merci... tu nous as sauvés. Va chercher la princesse. Et méfie-toi : Ignar est en colère.\""

    jump acte3_fin


label acte3_fin:

    scene bg foret_sombre with dissolve

    "Tu quittais le village derrière toi, les jambes lourdes et le cœur battant."
    "Devant, le chemin montait vers le Mont Cramoisi,"
    "dont le sommet rougeoyait d'une lumière orangée dans la nuit qui tombait."

    if p2_a_solene:
        solene "La tanière est encore à une heure de marche. Tu tiens le coup ?"
        joueur "Je tiens. La princesse compte sur nous."
        solene "Alors on court."

    "L'odeur de soufre devenait de plus en plus forte."
    "L'Acte 4 approchait : la tanière d'Ignar."

    jump acte4_taniere

## ============================================================
## ACTE 4 : LA TANIÈRE DU DRAGON
## ============================================================

label acte4_taniere:

    scene bg taniere_dragon with dissolve

    "Le Mont Cramoisi vivait à sa réputation : ses parois rougeâtres semblaient\nchauffées de l'intérieur, et le sol vibrait légèrement sous tes pieds."
    "Tu trouvais la faille dans la paroi nord — une crevasse sombre juste assez large\npour passer de profil, dissimulée derrière un rocher."
    "L'air qui en sortait était chaud, chargé de soufre et de fumée."

    if p2_a_solene:
        solene "(voix basse) C'est l'entrée. Ignar ne sait pas encore qu'on est là."
        solene "C'est notre seul avantage. Ne le gâchons pas."
        joueur "(voix basse) D'accord. On entre."
    else:
        joueur "(pour toi-même) C'est maintenant ou jamais."

    "Tu te glissas dans la faille."

    scene bg grotte with dissolve

    "À l'intérieur, une immense caverne s'ouvrait, éclairée par des veines\nde roche en fusion qui couraient le long des murs comme des rivières de feu."
    "Des os de toutes tailles jonchaient le sol. Des pièces d'or et de pierres précieuses\ns'amoncelaient dans les coins, formant des collines scintillantes."
    "Et au centre de la caverne, suspendue à des chaînes d'acier noir fixées\nau plafond de roche... une cage."
    "Dans la cage : la Princesse Arya. Elle était debout, les bras croisés,\nl'air plus agacée qu'effrayée."

    princesse "(vous apercevant) Oh ! Enfin ! J'attendais depuis des heures !"

    joueur "(tout bas) Arya ! Je suis [prenom]. Je viens vous sortir de là !"

    princesse "(murmure) Super. La cage est verrouillée par en haut. La clé est autour du cou d'Ignar."
    princesse "(murmure) Il dort là-bas derrière la montagne d'or. Mais attention, il dort très légèrement."

    "Un grondement sourd résonna dans la caverne. Comme un tonnerre lointain."
    "Puis deux yeux jaunes s'ouvrirent dans l'ombre derrière les piles d'or."

    dragon "...Je savais que tu viendrais."

    "Ignar émergea lentement de derrière son trésor. À cette distance,\nil était encore plus impressionnant que dans le ciel au-dessus de Preval."
    "Sa tête seule était aussi large que ta porte d'entrée à la maison."

    dragon "Courageux(se), [prenom]. Vraiment courageux(se). Ou stupide. Les deux se ressemblent souvent."

    "🐉 {b}Comment vas-tu affronter Ignar ?{/b}"

    menu:
        "⚔️  L'affronter directement — en combat !":
            jump acte4_combat

        "🗣️  Lui parler — essayer de comprendre pourquoi il a enlevé la princesse":
            jump acte4_negocier

        "🔓  Libérer Arya discrètement pendant qu'il parle":
            jump acte4_liberer_arya


## ─────────────────────────────────────────────
## Branche A : COMBAT
## ─────────────────────────────────────────────

label acte4_combat:

    joueur "Rends-moi la princesse, Ignar !"

    dragon "Ah. La méthode directe. J'apprécie l'honnêteté."
    dragon "Mais tu devras me la prendre de force."

    "Ignar inspira profondément. Sa gorge s'illumina d'un rouge incandescent."

    if p2_a_solene:
        solene "À GAUCHE !"
        "Vous plongeâtes chacun d'un côté tandis qu'un jet de flammes trouait l'air\nentre vous comme un couteau de feu."
    else:
        "Tu plongeais sur le côté au dernier moment. Le jet de flammes fit fondre\nle rocher que tu avais quitté une fraction de seconde plus tôt."

    "Ignar chargea. Le sol trembla à chacun de ses pas."

    if p2_a_bouclier:
        "Tu levas le Bouclier des Gorges."
        "Le dragon frappa de sa patte — et le bouclier tint, vibrant comme une cloche,\nenvoyant une onde de choc qui fit reculer Ignar lui-même d'un pas !"
        dragon "Un bouclier enchanté... Intéressant."
        "Tu en profitas pour frapper sa patte de l'Épée du Roi.\nIgnar rugit de surprise plus que de douleur."
        dragon "Tu sais te battre. Je vais devoir faire un effort."
        jump acte4_combat_phase2_fort

    elif "Fiole d'Eau Glacée 💧" in inventaire:
        "Au moment où Ignar ouvrait la gueule pour cracher le feu, tu lançais la fiole\ndirectement dans sa gorge !"
        "Un sifflement monstrueux. De la vapeur jaillit de ses naseaux."
        dragon "GRK... Eau froide... Douleur..."
        "Ignar tituba. Sa flamme s'éteignit momentanément."
        $ inventaire.remove("Fiole d'Eau Glacée 💧")
        "C'était le moment ! Tu te précipitas vers la cage, Épée du Roi en main,\net trancher la chaîne en deux coups précis !"
        jump acte4_cage_ouverte_direct

    elif "Corne de Brume 🎺" in inventaire:
        "Tu soufflais de toutes tes forces dans la Corne de Brume."
        "Le son grave et puissant se répercuta dans toute la caverne,\ns'amplifiant contre les parois de pierre jusqu'à devenir assourdissant."
        dragon "AAARGGH ! Mes oreilles ! Ce SON !"
        "Le dragon se tordait, ses grandes oreilles écailleuses plaquées contre sa tête."
        $ inventaire.remove("Corne de Brume 🎺")
        "Tu profitas de sa confusion pour courir vers la cage !"
        jump acte4_cage_ouverte_direct

    else:
        jump acte4_combat_difficile


label acte4_combat_difficile:

    "Sans objet magique ni allié, le combat était inégal."
    "Tu esquivais, tu courais, tu frappais quand tu pouvais."
    "L'Épée du Roi lacérait ses écailles mais ne semblait guère le blesser."
    "Jusqu'à ce qu'Ignar frappe la cage d'un coup de queue rageur."

    "La cage oscilla violemment. Arya fut projetée contre les barreaux."

    princesse "AÏE !"

    joueur "ARYA !"

    dragon "Ne t'inquiète pas pour elle. Elle est solide. Pour l'instant."
    dragon "Mais si tu continues à m'ennuyer..."

    $ p2_arya_blessee = True

    "Tu serras les dents. Arya se releva, une main sur l'épaule, le visage crispé."
    "Mais elle était toujours debout."
    "Furieux(se), tu chargeais Ignar une dernière fois avec tout ce que tu avais."
    "L'épée s'enfonça entre deux écailles sur sa patte avant."

    dragon "GRRRK !"

    jump acte4_ignar_blesse


label acte4_combat_phase2_fort:

    "Ignar ralentit ses attaques, plus prudent maintenant qu'il t'avait vu\nutiliser le bouclier."
    "Vous tournâtes l'un autour de l'autre dans la caverne."

    if p2_a_solene:
        "Solène feignit une attaque à gauche — Ignar pivota pour la regarder —\ntu en profitas pour frapper sa patte arrière droite de toutes tes forces !"
        dragon "GRK !"
        solene "Encore !"
        "Trois attaques coordonnées plus tard, Ignar reculait vers le fond de la caverne."
    else:
        "Tu repéras un point faible : sous son aile gauche, là où ses écailles étaient plus fines."
        "Il t'attaqua. Tu esquivas et frappas exactement là."
        dragon "GRRK ! Impossible..."
        "Ignar recula d'un pas, puis d'un autre."

    jump acte4_ignar_blesse


label acte4_ignar_blesse:

    dragon "(haletant) Tu... tu es plus fort(e) que tu n'en as l'air."

    "Ignar était blessé. Pas gravement — un dragon ne s'abbat pas si facilement —\nmais suffisamment pour qu'il hésite."

    "🐉 {b}Que fais-tu maintenant qu'Ignar est affaibli ?{/b}"

    menu:
        "⚔️  Continuer à l'attaquer pour le vaincre définitivement":
            jump acte4_victoire_combat

        "🗣️  S'arrêter et lui parler — pourquoi a-t-il enlevé Arya ?":
            jump acte4_ignar_parle


label acte4_victoire_combat:

    if p2_a_solene:
        solene "Ensemble ! Pour Val-Doré !"
        "Vous chargeâtes ensemble une dernière fois."
    else:
        "Tu réunis tout ton courage et chargeais une dernière fois."

    dragon "NON ! RECULEZ !"

    "Ignar tenta de s'envoler. Ses grandes ailes déployées firent tourbillonner\nla poussière et souffler les flammes des veines de roche."
    "Mais il était trop blessé pour porter la cage et fuir en même temps."
    "Il lâcha la chaîne de la cage qui s'écrasa dans un tas d'or."

    princesse "OUF."

    "Ignar plongea vers la faille nord et s'enfuit dans la nuit du Mont Cramoisi,\nlaissant derrière lui un filet de fumée et ses rugissements qui s'éloignaient."

    $ p2_dragon_mort = True

    jump acte4_cage_ouverte


## ─────────────────────────────────────────────
## Branche B : NÉGOCIER
## ─────────────────────────────────────────────

label acte4_negocier:

    joueur "Attends ! Avant qu'on se batte... pourquoi ?"

    dragon "...Pourquoi quoi ?"

    joueur "Pourquoi avoir enlevé la princesse ? Les dragons dorment pendant des années.\nTu te réveilles et la première chose que tu fais, c'est enlever quelqu'un ?"

    "Ignar s'arrêta. Ses yeux jaunes clignotèrent."

    dragon "...Personne ne me pose jamais cette question."

    princesse "(depuis la cage) Moi je lui ai posé plein de fois ! Il ne répond jamais !"

    dragon "Parce que les humains ne m'écoutent jamais !"

    "Un silence. La caverne crépitait doucement."

    dragon "Quand j'ai dormi, mon territoire était libre. Mes montagnes m'appartenaient."
    dragon "En dix ans... les humains ont construit leurs routes, leurs villages, jusqu'à mes frontières."
    dragon "Ils s'approchent chaque saison un peu plus. J'ai eu peur."

    joueur "Peur ?"

    dragon "Un vieux dragon seul contre tout un royaume. Oui. Peur."
    dragon "J'ai enlevé la princesse pour avoir... un moyen de parler."
    dragon "Pour que le roi m'écoute enfin."

    princesse "Tu aurais pu juste... envoyer un message."

    dragon "Les humains brûlent mes messagers."

    princesse "...D'accord, c'est un peu notre faute aussi."

    joueur "Si je te promets que le roi t'écoutera... tu la libères ?"

    "Ignar te fixa longuement."

    dragon "Ta parole de héros vaut quelque chose ?"

    joueur "Elle vaut l'épée que tu vois dans ma main."

    "Un très long silence. Puis Ignar inclina sa tête massive et sortit la clé\nde la cage de sous une de ses écailles."

    "Il la posa doucement sur le sol devant toi."

    dragon "Va. Libère-la. Et... dis à ton roi que je veux parler."

    $ p2_dragon_mort = False

    jump acte4_cage_cle


## ─────────────────────────────────────────────
## Branche C : LIBÉRER ARYA EN DOUCE
## ─────────────────────────────────────────────

label acte4_liberer_arya:

    "Pendant qu'Ignar te regardait, tu fis un signe discret à Arya."
    "Elle comprit immédiatement — cette fille était vraiment maligne."

    if p2_a_solene:
        "Tu lanças un regard à Solène. Elle hocha la tête imperceptiblement."
        solene "Dis-moi, Ignar... pourquoi avoir choisi cette princesse en particulier ?"
        "Pendant que Solène monopolisait l'attention du dragon,\ntu te glissas discrètement entre les piles d'or."
        dragon "Parce qu'elle est l'héritière du trône. Le roi ne peut pas ignorer ça."
        solene "Intéressant. Et si le roi t'avait juste envoyé une lettre ?"
        dragon "Les humains brûlent mes messagers. Alors j'ai..."
    else:
        "Tu pris la parole pour l'occuper."
        joueur "Dis-moi, Ignar... tu dors dix ans et tu te réveilles et là tu enlèves quelqu'un.\nC'est vraiment ton plan ?"
        dragon "Mon plan était de forcer le roi à parler avec moi."
        joueur "Et ça marche souvent, comme méthode ?"
        dragon "...Pas vraiment, non."

    "Tu atteignis le dessous de la cage. La chaîne était fixée par un anneau.\nPas de clé nécessaire — juste un anneau que tu pouvais soulever avec ta lame."

    "Du plat de l'Épée du Roi, tu soulevais l'anneau doucement, doucement..."

    "CLONG !"

    "La chaîne se décrocha. La cage tomba dans un tas d'or avec un bruit d'enfer."

    dragon "HÉ !"

    princesse "MAINTENANT ON COURT !"

    "Arya sauta hors de la cage à moitié ouverte et courut vers la faille nord."

    if p2_a_solene:
        solene "J'assure les arrières — FILEZ !"

    "Ignar rugit et s'élança vers vous."
    "Son souffle de feu balaya la caverne — mais vous étiez déjà dans la faille !"

    "La chaleur te frôla la nuque. Quelques mèches de tes cheveux s'enflammèrent brièvement."
    "Mais vous étiez dehors."

    $ p2_dragon_mort = False

    jump acte4_evasion_directe


## ─────────────────────────────────────────────
## Issues communes
## ─────────────────────────────────────────────

label acte4_cage_ouverte_direct:

    "La cage s'ouvrit. Arya en sortit d'un bond."

    princesse "Bien joué ! On sort d'ici !"

    "Ignar se relevait, secoué et furieux."

    dragon "REVENEZ !"

    if p2_a_solene:
        solene "COUREZ !"

    "Vous foncâtes vers la faille nord. Un jet de feu rasa le plafond au-dessus de vous."
    "Vous sortîtes dans la nuit fraîche du Mont Cramoisi."

    $ p2_dragon_mort = False
    jump acte4_dehors


label acte4_cage_cle:

    "Tu ouvris la cage avec la clé."

    princesse "Enfin ! J'en avais assez de ces barreaux."

    joueur "Tu vas bien ?"

    princesse "Je suis furieuse, j'ai faim et j'ai les cheveux qui sentent la fumée.\nMais oui, ça va."

    "Ignar regardait la scène, immobile."

    dragon "N'oublie pas ta promesse, [prenom]."

    joueur "Je n'oublierai pas."

    $ p2_dragon_mort = False
    jump acte4_dehors


label acte4_ignar_parle:

    dragon "Tu veux parler maintenant ? Très bien."
    dragon "Mon territoire rétrécit chaque année. Les humains avancent. Je suis seul."
    dragon "J'avais besoin... d'être entendu."

    joueur "Libère la princesse et je te promets que le roi t'écoutera."

    "Ignar considéra cela un long moment."

    dragon "...D'accord."

    "Il lâcha la chaîne. La cage descendit doucement."

    $ p2_dragon_mort = False
    jump acte4_cage_cle


label acte4_evasion_directe:

    scene bg chateau_ext with dissolve

    "Vous court{i}iez{/i} dans la nuit, dévalant les pentes du Mont Cramoisi."
    "Derrière vous, les rugissements d'Ignar résonnaient entre les rochers\nmais s'éloignaient peu à peu."
    "Il ne vous suivit pas. Peut-être trop blessé dans son orgueil pour courir après vous."

    jump acte4_fin


label acte4_dehors:

    scene bg chateau_ext with dissolve

    "Vous vous retrouvâtes sous le ciel étoilé du Mont Cramoisi."

    if p2_a_solene:
        solene "(essoufflée) Ça... ça s'est passé."
        joueur "On a la princesse."
        solene "On a la princesse."

    princesse "Je m'appelle Arya. Et je ne suis pas du genre à attendre d'être sauvée."
    princesse "Mais cette fois... merci. Vraiment."

    joueur "Ravie de voir que tu vas bien, Arya."

    princesse "On rentre à Val-Doré ?"

    joueur "On rentre."

    jump acte4_fin


label acte4_fin:

    "Le chemin du retour s'ouvrait devant vous."
    "La princesse était libre. La mission avait réussi."
    "Mais comment le roi et le royaume accueilleraient-ils votre retour\ndépendrait de tout ce que vous aviez fait... et de tout ce que vous n'aviez pas pu faire."

    jump acte5_retour

## ============================================================
## ACTE 5 : LE RETOUR À VAL-DORÉ
## ============================================================

label acte5_retour:

    scene bg sky with dissolve

    "L'aube se levait sur Val-Doré quand vous aperçûtes enfin les tours du château."
    "La lumière dorée du soleil naissant faisait briller les remparts\ncomme si le royaume lui-même vous accueillait."

    princesse "Je n'aurais jamais cru être contente de voir ces murs."

    if p2_a_solene:
        solene "Moi, si. Allons rendre la princesse à son père."

    "Les gardes aux portes écarquillèrent les yeux en vous voyant arriver."
    "Quelques minutes plus tard, le château entier était en émoi."
    "Des serviteurs couraient dans tous les couloirs. Des cloches sonnaient."
    "Et le Roi Aldric descendit lui-même les grand escalier de marbre\nau pas de course — chose que tout le monde dit qu'il ne faisait jamais."

    roi_aldric "Arya !"

    princesse "Papa !"

    "Le roi serra sa fille dans ses bras si fort qu'il en tremblait."
    "Puis il se redressa, les yeux brillants, et te regarda."

    roi_aldric "[prenom]... tu l'as ramenée."

    joueur "Comme promis, Majesté."

    "Le roi prit une longue inspiration."

    roi_aldric "Je dois tout entendre. Chaque détail. Mais d'abord..."

    "Il regarda la princesse de la tête aux pieds."

    roi_aldric "Est-ce qu'elle va bien ?"

    if p2_arya_blessee:
        jump acte5_arya_blessee_decouverte
    else:
        jump acte5_arya_sauve_entiere


label acte5_arya_blessee_decouverte:

    "Arya fit une grimace en déplaçant son épaule."
    "Une ecchymose violacée s'étendait depuis son cou jusqu'à sa clavicule."

    roi_aldric "(voix tendue) Qu'est-ce que... qui a fait ça ?"

    princesse "Le dragon m'a projetée contre les barreaux pendant le combat. Ce n'est pas grave."

    roi_aldric "Ce n'est pas grave ?!"

    princesse "Papa. J'ai eu plus mal en tombant de cheval l'an dernier. [prenom] m'a sauvée."

    "Le roi se tourna vers toi. Son visage était partagé entre la gratitude et la peine."

    roi_aldric "Elle est vivante grâce à toi... mais elle est blessée."
    roi_aldric "Je ne peux pas... faire comme si tout allait parfaitement bien."

    joueur "Je comprends, Majesté. Je regrette de n'avoir pas pu faire mieux."

    roi_aldric "Non. Tu as risqué ta vie. C'est moi qui aurais dû envoyer mes chevaliers plutôt\nqu'un(e) seul(e) héros(ïne)."

    jump fin_princesse_difficile


label acte5_arya_sauve_entiere:

    princesse "En pleine forme. Juste les cheveux qui sentent la fumée."

    roi_aldric "(soupirant de soulagement) Dieux merci."

    if p2_villageois:
        jump acte5_villageois_mentionnes
    else:
        jump acte5_sans_villageois


label acte5_villageois_mentionnes:

    "Un messager pénétra dans la grande salle en courant."

    messager "Majesté ! Des villageois de Preval sont arrivés aux portes de la ville.\nIls demandent à voir le héros [prenom] en personne !"

    roi_aldric "Qu'ils entrent."

    "Une dizaine de villageois entrèrent dans la salle du trône, dont plusieurs enfants."
    "Ils étaient encore noircis de suie, mais leurs visages rayonnaient."
    "Un vieil homme s'avança le premier et s'inclina profondément devant toi."

    "\"[prenom]... tu nous as sauvés. Le dragon avait mis le feu à nos maisons,\net toi tu t'es arrêté(e) pour nous aider.\""
    "\"Tu aurais pu courir après la princesse. Tu as choisi de nous protéger d'abord.\""
    "\"Nous ne l'oublierons jamais.\""

    "Des larmes coulaient sur les joues du vieil homme."
    "Les enfants t'offraient de petites fleurs des champs cueillies en chemin."

    joueur "Je ne pouvais pas vous laisser."

    roi_aldric "(ému) C'est cela, la vraie noblesse."

    jump fin_princesse_parfaite


label acte5_sans_villageois:

    "Un messager entra discrètement et murmura quelque chose à l'oreille du roi."
    "Le visage d'Aldric se rembrunit légèrement."

    roi_aldric "(à voix basse) Le village de Preval a brûlé cette nuit. Des familles ont tout perdu."
    roi_aldric "Les secours royaux sont en chemin, mais..."

    "Il te regarda."

    roi_aldric "Tu as dû faire un choix difficile. La princesse ou le village."

    joueur "Je regrette de ne pas avoir pu faire les deux."

    roi_aldric "Un héros ne peut être partout à la fois. Je comprends."

    jump fin_princesse_bonne


## ============================================================
## FIN DIFFICILE — Princesse blessée
## ============================================================

label fin_princesse_difficile:

    scene bg throne_room with dissolve

    "Le médecin royal soigna rapidement la blessure d'Arya.\nRien de grave : une ecchymose profonde et quelques jours de repos."

    princesse "Je vais bien, [prenom]. Vraiment. Ne t'en veux pas."

    joueur "Je t'avais promis de te ramener saine et sauve."

    princesse "Tu m'as ramenée. C'est déjà énorme."

    roi_aldric "Ma fille a raison. Avec un seul héros contre un dragon... \nle simple fait qu'elle soit vivante relève du prodige."
    roi_aldric "Le royaume te doit une dette, [prenom]."

    if not p2_dragon_mort:
        roi_aldric "Et ce dragon... tu dis qu'il voulait parler ?"
        joueur "Il a peur que son territoire disparaisse. Il voulait être entendu."
        roi_aldric "(songeur) ...Peut-être que j'ai eu tort de l'ignorer pendant toutes ces années."

    scene bg noir with dissolve

    "💔 {b}{size=+6}FIN DIFFICILE : Le Prix du Courage{/size}{/b} 💔"
    " "
    "La princesse Arya fut soignée et se rétablit complètement en quelques jours."
    "Elle garda toujours une petite cicatrice sur l'épaule — et elle refusa\nqu'on la cache. {i}\"C'est la marque de mon aventure\"{/i}, disait-elle."
    " "
    "[prenom] reçut la Médaille du Mérite Royal."
    "Pas la plus haute distinction... mais gagnée au prix d'un courage réel."
    " "
    "{color=#FFD700}Et quelque part au Mont Cramoisi, Ignar dormit à nouveau.{/color}"
    "{color=#FFD700}Peut-être pour toujours. Peut-être jusqu'à la prochaine fois.{/color}"
    " "
    "{i}(Rejoue pour découvrir comment protéger Arya et sauver les villageois !){/i}"
    " "
    "{b}🏅 Tu as obtenu la Médaille du Mérite Royal.{/b}"

    jump menu_fin_princesse


## ============================================================
## FIN BONNE — Arya sauvée, village non secouru
## ============================================================

label fin_princesse_bonne:

    scene bg throne_room with dissolve

    roi_aldric "La princesse est saine et sauve. C'est l'essentiel."
    roi_aldric "Pour les habitants de Preval, le trésor royal couvrira la reconstruction."

    princesse "Et [prenom] a fait face à Ignar seul(e). Tu sais ce que ça représente ?"

    roi_aldric "Je le sais, Arya."

    "Le roi se leva de son trône et descendit les marches vers toi."
    "Il posa sa main sur ton épaule."

    roi_aldric "Je te nomme {b}Protecteur(trice) de Val-Doré{/b}. Ce titre est rare."
    roi_aldric "Il signifie que les portes de ce château te seront toujours ouvertes."

    if not p2_dragon_mort:
        roi_aldric "Quant à Ignar... j'enverrai des émissaires. Il est temps que les dragons\net les hommes apprennent à se parler."
        princesse "C'est ce qu'il voulait depuis le début."

    scene bg noir with dissolve

    "🌟 {b}{size=+6}FIN BONNE : Le Protecteur de Val-Doré{/size}{/b} 🌟"
    " "
    "La Princesse Arya rentra chez elle saine et sauve."
    "Le village de Preval fut reconstruit en moins d'un an grâce aux fonds royaux."
    " "
    "{color=#FFD700}[prenom] reçut le titre de Protecteur(trice) de Val-Doré.{/color}"
    "{color=#FFD700}Dorénavant, son nom était gravé dans la pierre à l'entrée du château.{/color}"
    " "
    if not p2_dragon_mort:
        "{i}Le roi envoya des négociateurs au Mont Cramoisi.{/i}"
        "{i}Ignar accepta de parler. C'était un début.{/i}"
    " "
    "{i}(Rejoue pour sauver les villageois et décrocher la Fin Parfaite !){/i}"
    " "
    "{b}⭐ Tu as obtenu le titre de Protecteur(trice) de Val-Doré !{/b}"

    jump menu_fin_princesse


## ============================================================
## FIN PARFAITE — Arya sauvée + villageois secourus
## ============================================================

label fin_princesse_parfaite:

    scene bg throne_room with dissolve

    roi_aldric "Princesse sauvée. Villageois protégés. Dragon... géré."
    roi_aldric "En une seule nuit."

    "Le roi secoua la tête, entre l'incrédulité et l'admiration."

    roi_aldric "Dans toute l'histoire de Val-Doré, je ne connais pas un seul chevalier\nqui ait accompli autant en si peu de temps."

    princesse "Ce n'est pas un chevalier, Papa."
    princesse "C'est {b}[prenom]{/b}. Et c'est bien mieux."

    if p2_a_solene:
        solene "Si je peux me permettre, Majesté... [prenom] mérite plus qu'une médaille."

    roi_aldric "Je suis d'accord, Solène."

    "Le roi quitta la salle. Il revint quelques minutes plus tard\navec une épée à la lame dorée et un manteau d'hermine blanche."

    roi_aldric "[prenom]... mets-toi à genoux, s'il te plaît."

    "Tu t'agenouillas. Le silence dans la grande salle était total."

    roi_aldric "Par les pouvoirs qui me sont conférés en tant que Roi de Val-Doré..."
    roi_aldric "Je te nomme {b}Chevalier(ère) du Cœur de Val-Doré{/b} — la plus haute distinction\nde ce royaume, réservée à ceux qui protègent à la fois les grands et les humbles."

    "Il posa l'épée dorée sur ton épaule droite, puis sur l'épaule gauche."

    roi_aldric "Relève-toi, Chevalier(ère) [prenom]."

    "Tu te relevas. Arya t'applaudit la première. Solène suivit.\nPuis tous les gens dans la salle, serviteurs compris."

    if not p2_dragon_mort:
        roi_aldric "Et pour Ignar... tu m'as dit qu'il voulait parler ?"
        joueur "Il a peur. Son territoire rétrécit. Il voulait être entendu."
        roi_aldric "Alors je l'écouterai. C'est aussi le rôle d'un roi."
        princesse "C'est la première bonne décision que tu prends depuis longtemps, Papa."
        roi_aldric "Arya..."
        princesse "Je t'aime quand même."

    scene bg ciel_triomphe with dissolve

    "Ce soir-là, Val-Doré fêta jusqu'à l'aube."
    "Les cloches sonnèrent, les feux d'artifice illuminèrent le ciel,\net les villageois de Preval — qui avaient tout perdu la nuit d'avant —\ndansèrent quand même, parce que quelqu'un avait pensé à eux."

    scene bg noir with dissolve

    "🏆 ⭐ 🏆 {b}{size=+6}FIN PARFAITE{/size}{/b} 🏆 ⭐ 🏆"
    " "
    "{b}Le Chevalier(ère) du Cœur de Val-Doré !{/b}"
    " "
    "La Princesse Arya fut sauvée, les villageois de Preval aussi."
    "Et pour la première fois depuis des siècles, un dragon et un roi\ns'assirent à la même table pour parler."
    " "
    "{color=#FFD700}[prenom] devint la légende de Val-Doré.{/color}"
    "{color=#FFD700}Les enfants apprirent son histoire à l'école. Les bardes chantèrent ses exploits.{/color}"
    "{color=#FFD700}Et la Princesse Arya resta la meilleure amie de [prenom] pour toujours.{/color}"
    " "
    "{i}Quant à Ignar... il ne brûla plus jamais un seul village.{/i}"
    "{i}Il devint même, dit-on, le gardien officiel des frontières nord de Val-Doré.{/i}"
    "{i}Pour un salaire en or et en moutons rôtis.{/i}"
    " "
    "{b}{color=#FFD700}🏆 Tu as obtenu le titre de Chevalier(ère) du Cœur de Val-Doré — Récompense Suprême ! 🏆{/color}{/b}"

    jump menu_fin_princesse


## ============================================================
## MENU DE FIN DE L'AVENTURE PRINCESSE
## ============================================================

label menu_fin_princesse:

    "Que veux-tu faire ?"

    menu:
        "🔄  Rejouer cette aventure":
            $ inventaire      = []
            $ p2_arya_blessee  = False
            jump intro_princesse

        "🏠  Retourner au menu principal":
            $ inventaire      = []
            $ p2_arya_blessee  = False
            jump start

    return


