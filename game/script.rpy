## ============================================================
## LES AVENTURES MAGIQUES - Script principal
## Jeu narratif pour enfants de 9 ans
## ============================================================

## ============================================================
## IMAGES DE FOND (couleurs unies, pas d'image requise)
## ============================================================

image bg_menu:
    "images/menu_aventure.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg sky:
    "images/sky.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg foret:
    "images/foret.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg sentier_fleurs:
    "images/sentier_fleurs.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg sentier_fleurs2:
    "images/sentier_fleurs2.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg sentier_fleurs_floralie:
    "images/sentier_fleurs_floralie.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg foret_champignons:
    "images/chemin_champignons.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg tour_ext:
    "images/tour_ext.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg tour_int:
    "images/tour_int.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg laboratoire:
    "images/laboratoire.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg escalier:
    "images/escalier.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg porte doree:
    "images/porte_doree.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg ciel victoire laia:
    "images/ciel_victoire_laia.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg ciel victoire kael:
    "images/ciel_victoire_kael.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg noir              = Solid("#000000")
image bg prairie:
    "images/celeste_prairie.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg pierre:
    "images/pierre_lumiere.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg troll dort pont:
    "images/troll_dort_pont.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg troll debout pont:
    "images/troll_debout_pont.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg troll:
    "images/troll.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg salle licorne:
    "images/salle_licorne.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg licorne:
    "images/licorne.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg sommet:
    "images/sommet.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg gnome dort:
    "images/gnome_dort.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg gnome:
    "images/gnome.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg prairie licorne:
    "images/prairie_licornes.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg lumina:
    "images/lumina.png"
    fit "cover"
    xalign 0.5
    yalign 0.5

## Fonds — Aventure 2 : Protéger la princesse
image bg throne_room:
    "images/throne_room.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg village:
    "images/village.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg village_feu:
    "images/village_feu.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg gorges_sauvages:
    "images/gorges_sauvages.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg taniere_dragon    = Solid("#2a0a0a")
image bg ciel_triomphe     = Solid("#e87020")
image bg chateau_ext:
    "images/chateau_ext.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg foret_ombres:
    "images/foret_ombres.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg ignar:
    "images/ignar.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg val_doree:
    "images/val_doree.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg messager_royal:
    "images/messager_royal.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg bouclier:
    "images/bouclier.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg solene:
    "images/solene.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg solene_preval:
    "images/solene_preval.png"
    fit "cover"
    xalign 0.5
    yalign 0.5
image bg gobelins:
    "images/gobelins.png"
    fit "cover"
    xalign 0.5
    yalign 0.5

## ============================================================
## VARIABLES DU JEU
## ============================================================

default inventaire      = []
default prenom          = "Laïa"
default personnage      = "fille"    # "fille" ou "garcon"
default etoile_libre    = False
default pierre_obtenue  = False


## ============================================================
## PERSONNAGES
## ============================================================

define joueur       = Character("[prenom]",     color="#00BFFF", what_color="#E0FFFF", what_outlines=[(2, "#003a50", 0, 0)])
define fee_celeste  = Character("✨ Céleste",   color="#FFD700", what_color="#FFE566", what_outlines=[(2, "#3a2a00", 0, 0)])
define fee_floralie = Character("🌸 Floralie",  color="#FF69B4", what_color="#FFE4E1", what_outlines=[(2, "#3a1020", 0, 0)])
define gnome_pip    = Character("🍄 Pip",       color="#7ec850", what_color="#dfffb0", what_outlines=[(2, "#1a3000", 0, 0)])
define troll_grok   = Character("🧌 Grok",      color="#a0856a", what_color="#F5E8C8", what_outlines=[(2, "#2a1a00", 0, 0)])
define licorne      = Character("🦄 Étoile",    color="#FF85C2", what_color="#FFF0F5", what_outlines=[(2, "#3a1030", 0, 0)])
define sorciere     = Character("🔮 Maléfra",   color="#b060ff", what_color="#e8d0ff", what_outlines=[(2, "#1a0030", 0, 0)])
define reine        = Character("👑 Lumina",    color="#FFD700", what_color="#FFE566", what_outlines=[(2, "#3a2a00", 0, 0)])

## Personnages — Aventure 2 : Protéger la princesse
define roi_aldric   = Character("👑 Roi Aldric",     color="#DAA520", what_color="#FFE566", what_outlines=[(2, "#3a2a00", 0, 0)])
define princesse    = Character("🌸 Arya",            color="#FF85AB", what_color="#FFF0F5", what_outlines=[(2, "#3a1030", 0, 0)])
define solene       = Character("⚔️ Solène",          color="#7ec8e3", what_color="#c0f0ff", what_outlines=[(2, "#003040", 0, 0)])
define dragon       = Character("🐉 Ignar",           color="#c03030", what_color="#ffe0e0", what_outlines=[(2, "#300000", 0, 0)])
define gobelin      = Character("👺 Gobelin",         color="#6aaa30", what_color="#d8ffc0", what_outlines=[(2, "#1a3000", 0, 0)])
define messager     = Character("📜 Messager",        color="#c8a860", what_color="#fff5dc", what_outlines=[(2, "#2a1a00", 0, 0)])


## ============================================================
## ÉCRAN INVENTAIRE (affiché en haut à droite pendant le jeu)
## ============================================================

screen inventaire_hud():
    zorder 100
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -12
        yoffset 12
        background "#00000099"
        padding (14, 10, 14, 10)
        vbox:
            spacing 5
            text "🎒 Mon sac" size 21 color "#FFD700" bold True
            if len(inventaire) == 0:
                text "  (vide)" size 17 color "#888888" italic True
            else:
                for objet in inventaire:
                    text ("  • " + objet) size 17 color "#FFFFFF"


## ============================================================
## LABEL START — Menu principal
## ============================================================

label start:

    $ inventaire     = []
    $ etoile_libre   = False
    $ pierre_obtenue = False

    scene bg noir with dissolve

    $ choix_start = renpy.call_screen("start_screen")

    if choix_start == "aventures":

        scene bg_menu with dissolve

        $ choix_av = renpy.call_screen("aventures_screen")
        if choix_av == "licornes":
            jump choisir_personnage_licornes
        elif choix_av == "princesse":
            jump choisir_personnage_princesse
        else:
            jump start
    else:
        $ renpy.call_screen("trophees_screen")
        jump start


## ============================================================
## ÉCRAN TITRE PRINCIPAL (gauche / droite)
## ============================================================

screen start_screen():
    zorder 200
    modal True


    ## Titre du jeu
    frame:
        xalign 0.5
        yalign 0.08
        background "#00000099"
        padding (36, 16, 36, 16)
        text "🌟 Les Aventures Magiques 🌟" size 48 bold True color "#FFD700" outlines [(2, "#1a0a3a", 0, 0)] xalign 0.5

    ## ── Moitié gauche : Jouer ──
    button:
        action Return("aventures")
        xpos 0
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF14"

        vbox:
            xalign 0.5
            yalign 0.52
            spacing 32

            text "🎮" size 130 xalign 0.5
            text "Choisir ton aventure" size 42 bold True color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5
            text "Pars à la découverte\nd'un monde magique !" size 28 color "#C8C8FF" xalign 0.5 text_align 0.5
            frame:
                xalign 0.5
                background "#4040CCAA"
                padding (38, 14, 38, 14)
                text "Jouer →" size 34 bold True color "#FFFFFF" xalign 0.5

    ## Séparateur
    frame:
        xpos 958
        ypos 0
        xsize 4
        ysize 1080
        background "#FFD70066"

    ## ── Moitié droite : Trophées ──
    button:
        action Return("trophees")
        xpos 960
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF14"

        vbox:
            xalign 0.5
            yalign 0.52
            spacing 32

            text "🏆" size 130 xalign 0.5
            text "Voir mes trophées" size 42 bold True color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5

            $ nb_trophees = (1 if persistent.trophee_double_sceau else 0) + (1 if persistent.trophee_amis_licornes else 0)
            text "[nb_trophees] trophée(s) obtenu(s)" size 28 color "#C8C8FF" xalign 0.5

            frame:
                xalign 0.5
                background "#886600AA"
                padding (38, 14, 38, 14)
                text "Consulter →" size 34 bold True color "#FFFFFF" xalign 0.5


## ============================================================
## ÉCRAN SÉLECTION D'AVENTURE (gauche / droite)
## ============================================================

screen aventures_screen():
    zorder 200
    modal True

    add "bg_menu"

    ## Titre
    frame:
        xalign 0.5
        yalign 0.07
        background "#00000099"
        padding (34, 14, 34, 14)
        text "✨ Quelle aventure veux-tu vivre ?" size 42 bold True color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5

    ## Bouton retour
    button:
        action Return("retour")
        xpos 30
        ypos 30
        background "#00000099"
        hover_background "#333333CC"
        padding (18, 10, 18, 10)
        text "← Retour" size 26 color "#FFD700" bold True

    ## ── Moitié gauche : Licornes ──
    button:
        action Return("licornes")
        xpos 0
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF14"

        vbox:
            xalign 0.5
            yalign 0.52
            spacing 28

            text "🦄" size 140 xalign 0.5
            text "Sauver le Royaume\ndes Licornes" size 40 bold True color "#FF85C2" outlines [(2, "#000000", 0, 0)] xalign 0.5 text_align 0.5
            text "Aide les licornes d'Élysia\nà retrouver leur magie !" size 27 bold True color "#FFE4F5" outlines [(2, "#000000", 0, 0)] xalign 0.5 text_align 0.5
            frame:
                xalign 0.5
                background "#AA3388AA"
                padding (34, 14, 34, 14)
                text "Partir à l'aventure →" size 30 bold True color "#FFFFFF" xalign 0.5

    ## Séparateur
    frame:
        xpos 958
        ypos 0
        xsize 4
        ysize 1080
        background "#FFD70066"

    ## ── Moitié droite : Princesse ──
    button:
        action Return("princesse")
        xpos 960
        ypos 0
        xsize 960
        ysize 1080
        background "#00000000"
        hover_background "#FFFFFF14"

        vbox:
            xalign 0.5
            yalign 0.52
            spacing 28

            text "👸" size 140 xalign 0.5
            text "Protéger\nla Princesse" size 40 bold True color "#FFB830" outlines [(2, "#000000", 0, 0)] xalign 0.5 text_align 0.5
            text "Défends le château royal\ncontre le dragon Ignar !" size 27 bold True color "#FFFACD" outlines [(2, "#000000", 0, 0)] xalign 0.5 text_align 0.5
            frame:
                xalign 0.5
                background "#AA7700AA"
                padding (34, 14, 34, 14)
                text "Partir à l'aventure →" size 30 bold True color "#FFFFFF" xalign 0.5


## ============================================================
## ÉCRAN TROPHÉES
## ============================================================

screen trophees_screen():
    zorder 200
    modal True

    add "bg_menu"

    ## Bouton retour
    button:
        action Return()
        xpos 30
        ypos 30
        background "#00000099"
        hover_background "#333333CC"
        padding (18, 10, 18, 10)
        text "← Retour" size 28 color "#FFD700" bold True

    ## Titre
    frame:
        xalign 0.5
        yalign 0.09
        background "#00000099"
        padding (34, 14, 34, 14)
        text "🏆 Mes Trophées" size 44 bold True color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5

    ## Contenu
    frame:
        xalign 0.5
        yalign 0.55
        xsize 1100
        background "#00000000"

        vbox:
            xfill True
            spacing 34

            ## ── Aventure 1 ──
            frame:
                xfill True
                background "#00000088"
                padding (30, 22, 30, 22)
                vbox:
                    spacing 18

                    text "🦄 Aventure 1 — Sauver le Royaume des Licornes" size 30 bold True color "#FF85C2" outlines [(2, "#000000", 0, 0)] xalign 0.5

                    if persistent.trophee_double_sceau:
                        frame:
                            xfill True
                            background "#3a2a00CC"
                            padding (20, 14, 20, 14)
                            hbox:
                                spacing 18
                                text "🏆" size 52
                                vbox:
                                    spacing 4
                                    text "Double Sceau des Héros d'Élysia" size 28 bold True color "#FFD700"
                                    text "Récupérer la Pierre ET libérer Étoile la Licorne" size 22 color "#FFE566" italic True
                    else:
                        frame:
                            xfill True
                            background "#1a1a1aCC"
                            padding (20, 14, 20, 14)
                            hbox:
                                spacing 18
                                text "🔒" size 52
                                vbox:
                                    spacing 4
                                    text "Double Sceau des Héros d'Élysia" size 28 bold True color "#555555"
                                    text "Récupérer la Pierre ET libérer Étoile la Licorne" size 22 color "#444444" italic True

                    if persistent.trophee_amis_licornes:
                        frame:
                            xfill True
                            background "#1a3000CC"
                            padding (20, 14, 20, 14)
                            hbox:
                                spacing 18
                                text "🌟" size 52
                                vbox:
                                    spacing 4
                                    text "Sceau des Amis des Licornes" size 28 bold True color "#7ec850"
                                    text "Récupérer la Pierre de Lumière et sauver Élysia" size 22 color "#dfffb0" italic True
                    else:
                        frame:
                            xfill True
                            background "#1a1a1aCC"
                            padding (20, 14, 20, 14)
                            hbox:
                                spacing 18
                                text "🔒" size 52
                                vbox:
                                    spacing 4
                                    text "Sceau des Amis des Licornes" size 28 bold True color "#555555"
                                    text "Récupérer la Pierre de Lumière et sauver Élysia" size 22 color "#444444" italic True

            ## ── Aventure 2 ──
            frame:
                xfill True
                background "#00000088"
                padding (30, 22, 30, 22)
                vbox:
                    spacing 18
                    text "👸 Aventure 2 — Protéger la Princesse" size 30 bold True color "#FFB830" xalign 0.5
                    frame:
                        xfill True
                        background "#1a1a1aCC"
                        padding (20, 14, 20, 14)
                        text "🔓 Aventure bientôt disponible..." size 24 color "#555555" italic True xalign 0.5


## ============================================================
## ÉCRAN DE CHOIX DU PERSONNAGE (cartes gauche / droite)
## ============================================================

screen choisir_personnage_screen():
    zorder 200
    modal True

    add "bg_menu"

    ## Titre
    frame:
        xalign 0.5
        yalign 0.08
        background "#00000000"
        text "Qui veux-tu être dans cette aventure ?" size 36 bold True color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5

    ## Conteneur des deux cartes
    hbox:
        xalign 0.5
        yalign 0.52
        spacing 60

        ## ── Carte Laïa (gauche) ──
        button:
            action [
                SetVariable("prenom",     "Laïa"),
                SetVariable("personnage", "fille"),
                Return("laia")
            ]
            xsize 340
            ysize 460
            background "#00000000"
            hover_background "#00000000"

            frame:
                xsize 340
                ysize 460
                background Frame("#3a1a6aCC", 20, 20)
                hover_background Frame("#6a3aafCC", 20, 20)
                padding (20, 20, 20, 20)

                vbox:
                    xalign 0.5
                    spacing 18

                    ## Emoji grand format
                    text "👧" size 100 xalign 0.5

                    ## Nom
                    text "Laïa" size 38 bold True color "#FF85C2" outlines [(2, "#000000", 0, 0)] xalign 0.5

                    ## Séparateur
                    frame:
                        xsize 260
                        ysize 2
                        xalign 0.5
                        background "#FFD70088"

                    ## Description
                    text "Courageuse\net curieuse" size 24 color "#FFE4F5" xalign 0.5 text_align 0.5

                    ## Tags
                    hbox:
                        xalign 0.5
                        spacing 8
                        frame:
                            background "#FF69B455"
                            padding (8, 4, 8, 4)
                            text "✨ Magie" size 18 color "#FF85C2"
                        frame:
                            background "#FF69B455"
                            padding (8, 4, 8, 4)
                            text "💜 Amitié" size 18 color "#FF85C2"

                    ## Bouton-indicateur
                    frame:
                        xalign 0.5
                        background "#FF69B4AA"
                        padding (20, 8, 20, 8)
                        text "Choisir →" size 22 bold True color "#FFFFFF" xalign 0.5

        ## ── Carte Kaël (droite) ──
        button:
            action [
                SetVariable("prenom",     "Kaël"),
                SetVariable("personnage", "garcon"),
                Return("kael")
            ]
            xsize 340
            ysize 460
            background "#00000000"
            hover_background "#00000000"

            frame:
                xsize 340
                ysize 460
                background Frame("#1a2a6aCC", 20, 20)
                hover_background Frame("#2a4aafCC", 20, 20)
                padding (20, 20, 20, 20)

                vbox:
                    xalign 0.5
                    spacing 18

                    text "👦" size 100 xalign 0.5

                    text "Kaël" size 38 bold True color "#7ec8ff" outlines [(2, "#000000", 0, 0)] xalign 0.5

                    frame:
                        xsize 260
                        ysize 2
                        xalign 0.5
                        background "#FFD70088"

                    text "Aventurier\net débrouillard" size 24 color "#D0EEFF" xalign 0.5 text_align 0.5

                    hbox:
                        xalign 0.5
                        spacing 8
                        frame:
                            background "#4488FF55"
                            padding (8, 4, 8, 4)
                            text "⚔️ Courageux" size 18 color "#7ec8ff"
                        frame:
                            background "#4488FF55"
                            padding (8, 4, 8, 4)
                            text "🌟 Futé" size 18 color "#7ec8ff"

                    frame:
                        xalign 0.5
                        background "#4488FFAA"
                        padding (20, 8, 20, 8)
                        text "Choisir →" size 22 bold True color "#FFFFFF" xalign 0.5


## ============================================================
## CHOIX DU PERSONNAGE
## ============================================================

label choisir_personnage_licornes:

    "Avant de commencer, {b}choisis ton personnage{/b} !"

    $ choix = renpy.call_screen("choisir_personnage_screen")

    "[prenom], c'est parti pour l'aventure ! ✨"
    jump intro_licornes

label choisir_personnage_princesse:

    "Avant de commencer, {b}choisis ton personnage{/b} !"

    $ choix = renpy.call_screen("choisir_personnage_screen")

    "[prenom], c'est parti pour l'aventure ! ✨"
    jump intro_princesse

## ============================================================
## AVENTURE 1 : voir game/aventures/licornes.rpy
## ============================================================
## Les labels suivants sont définis dans aventures/licornes.rpy :
##   intro_licornes, foret_enchantee, chemin_fleurs, chemin_champignons,
##   pont_du_troll, tour_malefra, fin_parfaite, fin_bonne,
##   epilogue_parfait, epilogue_bon, menu_fin, ...
