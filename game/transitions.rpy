init -100 python:
    fdissolve = Dissolve(0.3)
    fstartgame = ImageDissolve("gui/menutrans.png", 1.4, ramplen=60, reverse=True)
    fquitmenu = ImageDissolve("gui/id_circleiris.png", 0.4, ramplen=600, reverse=False)
init python:

    def myshow(name, at_list=[], layer='master', what=None, zorder=0, tag=None, behind=None,atl=None):
        renpy.transition(Dissolve(.3),layer)
        renpy.show(name, at_list, layer, what, zorder, tag, behind,atl)

    config.show = myshow

image imagetextbox:
    contains:
        additive 0.1
        Frame("gui/textbox.png",1,100,1,2)
    #Solid("#000")
   # contains:
      #  alpha 1
      #  Frame("gui/textbox1.png",1,100,1,2)



image white = Solid("#fff")
image black = Solid("#000")

# transitions
define clockwipe = ImageDissolve("transitions/wipe.png", 1.5, ramplen=80)
define wipeup_slow = ImageDissolve("transitions/wipeup.png", 1.5, ramplen=60)
define wipeup_norm = ImageDissolve("transitions/wipeup.png", 0.9, ramplen=120)
define wipedown_norm = ImageDissolve("transitions/wipeup.png", 0.9, ramplen=60, reverse=True)
define wipeup_fast = ImageDissolve("transitions/wipeup.png", 0.5, ramplen=120)
define wiperight_fast = ImageDissolve("transitions/wipeleft.png", 0.8, ramplen=140, reverse=True)
define wipedown_slow = ImageDissolve("transitions/wipeup.png", 1.5, ramplen=60, reverse=True)
define wiperight_slow = ImageDissolve("transitions/wipeleft.png", 1.5, ramplen=140, reverse=True)
define wipeleft_slow = ImageDissolve("transitions/wipeleft.png", 1.5, ramplen=140, reverse=False)
define wipeleft_fast = ImageDissolve("transitions/wipeleft.png", 0.8, ramplen=140, reverse=False)
define wipedown_fast = ImageDissolve("transitions/wipeup.png", 0.45, ramplen=60, reverse=True)
define slow_dissolve = Dissolve(2.0)
define wipe = ImageDissolve("transitions/wipetrans.png", 1.5, ramplen=140, reverse=True)
define wipe_f = ImageDissolve("transitions/wipetrans.png", 0.9, ramplen=140, reverse=True)
define dissolve_f = Dissolve(0.85)
define circleirisin = ImageDissolve("transitions/id_circleiris.png", 1.5, ramplen=80, reverse=False)
define circleirisout = ImageDissolve("transitions/id_circleiris.png", 1.5, ramplen=80, reverse=True)


init -100 python:
    fdissolve = Dissolve(0.3)
    slow_dissolve = Dissolve(1.5)
init python:

    def myshow(name, at_list=[], layer='master', what=None, zorder=0, tag=None, behind=None,atl=None):
        renpy.transition(Dissolve(.3),layer)
        renpy.show(name, at_list, layer, what, zorder, tag, behind,atl)

    config.show = myshow









init -1:
    ## Transforms
    ## Sprites animation
    $ show_quick_menu = True


    transform c5:
        on show:
            easein .5 alpha 1.0 xoffset 0
        on replace:
            easein .5 xoffset 0
        on hide:
            easeout .5 xoffset 0 alpha 0

    transform c4:
        on show:
            easein .5 alpha 1.0 xoffset -60
        on replace:
            easein .5 xoffset -60
        on hide:
            easeout .5 xoffset -60 alpha 0

    transform c3:
        on show:
            easein .5 alpha 1.0 xoffset -30
        on replace:
            easein .5 xoffset -30
        on hide:
            easeout .5 xoffset -30 alpha 0

    transform c2:
        on show:
            easein .5 alpha 1.0 xoffset 30
        on replace:
            easein .5 xoffset 30
        on hide:
            easeout .5 xoffset 30 alpha 0

    transform c1:
        on show:
            easein .5 alpha 1.0 xoffset 60
        on replace:
            easein .5 xoffset 60
        on hide:
            easeout .5 xoffset 60 alpha 0

    transform fd:
        on show:
            easein .3 alpha 1.0
        on replace:
            easein .3 alpha 1.0
        on hide:
            easein .3 alpha 0.0

    transform tcenter:
        on show:
            xalign .40 yalign 0.2 xpos 550
            easein .5 alpha 1.0 xpos 650
        on replace:
            easein .5 xalign .5 xpos 650
        on hide:
            easeout .5 alpha 0 xalign .5 xpos 550

    transform tcenter2:
        on show:
            xalign .40 yalign 0.2 xpos 450
            easein .5 alpha 1.0 xpos 580
        on replace:
            easein .5 xalign .5 xpos 580
        on hide:
            easeout .5 alpha 0 xalign .5 xpos 450

    transform rtl:
        on show:
            xalign 0.7 yalign 0.2 xpos 600
            easein .5 alpha 1.0 xpos 550
        on replace:
            easein .5 xalign 0.7 xpos 550
        on hide:
            easeout .5 alpha 0 xpos 600


    transform rtr:
        on show:
            xalign 0.85 yalign 0.2 xpos 1450
            easein .5 alpha 1.0 xpos 1550
        on replace:
            easein .5 xalign 0.85 xpos 1550
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0 xpos 1450

    transform rtr_2:
        on show:
            xalign 0.85 yalign 0.2 xpos 1400
            easein .5 alpha 1.0 xpos 1500
        on replace:
            easein .5 xalign 0.85 xpos 1400
        on hide:
            easeout .5 alpha 0 xpos 1500

    transform rtr_ayu:
        on show:
            xalign 0.85 yalign 0.2 xpos 1200
            easein .5 alpha 1.0 xpos 1300
        on replace:
            easein .5 xalign 0.85 xpos 1300
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0 xpos 1200

    transform rtr_hazel:
        on show:
            xalign 0.85 yalign 0.2 xpos 1900
            easein .5 alpha 1.0 xpos 2000
        on replace:
            easein .5 xalign 0.85 xpos 2000
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0 xpos 1900

    transform rtr_hazel2:
        on show:
            xalign 0.85 yalign 0.2 xpos 2000
            easein .5 alpha 1.0 xpos 2100
        on replace:
            easein .5 xalign 0.85 xpos 2100
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0 xpos 2000

    transform rtr_hazel3:
        on show:
            xalign 0.85 yalign 0.2 xpos 2100
            easein .5 alpha 1.0 xpos 2200
        on replace:
            easein .5 xalign 0.85 xpos 2200
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0 xpos 2100

    transform ltl_flip:
        on show:
            xalign 0.40 yalign 0.2 xpos 900
            easein .5 alpha 1.0 xpos 950
        on replace:
            easein .5 xalign 0.0 xpos 950
        on hide:
            easeout .5 alpha 0 xpos 900

    transform ltr:
        on show:
            xalign -0.02 yalign 0.2 xoffset 0
            easein .5 alpha 1.0 xoffset -50
        on replace:
            easein .5 xalign -0.02 xoffset -50
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform ltl:
        on show:
            xalign 0.0 yalign 0.2 xpos 80
            easein .5 alpha 1.0 xpos 50
        on replace:
            easein .5 xalign 0.0 xpos 50
        on hide:
            easeout .5 alpha 0 xpos 80

    transform ltl_2:
        on show:
            xalign 0.0 yalign 0.2 xpos -150
            easein .5 alpha 1.0 xpos -250
        on replace:
            easein .5 xalign 0.0 xpos -250
        on hide:
            easeout .5 alpha 0 xpos -150

    transform ltl_3:
        on show:
            xalign 0.05 yalign 0.2 xpos 450
            easein .5 alpha 1.0 xpos 400
        on replace:
            easein .5 xalign 0.005 xpos 400
        on hide:
            easeout .5 alpha 0 xpos 450

    transform ltl_4:
        on show:
            xalign 0.05 yalign 0.2 xpos 700
            easein .5 alpha 1.0 xpos 650
        on replace:
            easein .5 xalign 0.005 xpos 650
        on hide:
            easeout .5 alpha 0 xpos 700


    transform ltl_marina:
        on show:
            xalign 0.0 yalign 0.2 xpos -40
            easein .5 alpha 1.0 xpos -100
        on replace:
            easein .5 xalign 0.0 xpos -100
        on hide:
            easeout .5 alpha 0 xpos -40

    transform ltl_marina2:
        on show:
            xalign 0.0 yalign 0.2 xpos -350
            easein .5 alpha 1.0 xpos -450
        on replace:
            easein .5 xalign 0.0 xpos -450
        on hide:
            easeout .5 alpha 0 xpos -350

    transform ctl:
        on show:
            xalign .5 yalign 0.2 xoffset 0
            easein .5 alpha 1.0 xoffset -100
        on replace:
            easein .5 xalign .5 xoffset -100
        on hide:
            easeout .5 alpha 0 xalign .5

    transform ctr:
        on show:
            xalign .6 yalign 0.2 xpos 1050
            easein .5 alpha 1.0 xpos 1100
        on replace:
            easein .5 xalign .6  xpos 1100
        on hide:
            easeout .5 alpha 0 xalign .6


    transform ctl2:
        on show:
            xalign 0.2 yalign 0.2 xpos 300
            easein .5 alpha 1.0 xpos 400
        on replace:
            easein .5 xalign 0.2 xpos 400
        on hide:
            easeout .5 alpha 0 xalign .2

    transform ctr2:
        on show:
            xalign .8 yalign 0.2 xpos 1400
            easein .5 alpha 1.0 xpos 1450
        on replace:
            easein .5 xalign .8  xpos 1450
        on hide:
            easeout .5 alpha 0 xalign .6 xpos 1400

    transform rtr2:
        on show:
            xalign 1.0 yalign 0.2 xpos 1900
            easein .5 alpha 1.0 xpos 1860
        on replace:
            easein .5 xalign 1.0 xpos 1860
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0  xpos 1900

    transform ltl2:
        on show:
            xalign 0.0 yalign 0.2 xpos 0
            easein .5 alpha 1.0 xpos -50
        on replace:
            easein .5 xalign 0.0 xpos -50
        on hide:
            easeout .5 alpha 0 xpos 0

    transform rtr3:
        on show:
            xalign 1.0 yalign 0.2 xpos 1900
            easein .5 xalign 1.0 xpos 2000
        on replace:
            easein .5 xalign 1.0 xpos 2000
        on hide:
           # xoffset 45 xalign 1.0
            easeout .5 alpha 0  xpos 1900

    transform ltl3:
        on show:
            xalign 0.0 yalign 0.2 xpos -80
            easein .5 alpha 1.0 xpos -180
        on replace:
            easein .5 xalign 0.0 xpos -180
        on hide:
            easeout .5 alpha 0 xpos -80


    transform jumpx:
        on show:
            easein .2 yoffset 50
            easein .1 yoffset 0
        on replace:
            easein .2 yoffset 50
            easein .1 yoffset 0
        on hide:
            easein .2 yoffset 50
            easein .1 yoffset 0




    transform right_r (x):
        on show:
            xalign 1.1
            easein .5 alpha 1.0 xoffset x
        on replace:
            xalign 1.1
            easein .5 alpha 1.0 xoffset x

        on hide:
            easein .5 alpha 0 xoffset x

    transform left_r (x):
        on show:
            xalign 0
            easein .5 alpha 1.0 xoffset x
        on replace:
            xalign 0
            easein .5 alpha 1.0 xoffset x

        on hide:
            easein .5 alpha 0 xoffset x

    transform vert_r (y):
            easein 0.5 yoffset y

    transform vert_t (t,y):
            easein t xalign 0 yoffset y

    transform right_l:
        on show:
            xalign .9  xoffset -45
            easein .5  xoffset 0
        on replace:
            easein .5 xalign .8
        on hide:
            easeout .5  xoffset -45


    transform center:
        on show:
            easein .5 xalign .5
        on replace:
            easein .5 xalign .5
        on hide:
            easeout .5 xalign .5


    transform slidesmooth(t=.5, x=0, y=0):
        alpha .0 xoffset x yoffset y
        easein t  alpha 1.0 xoffset 0 yoffset 0

    transform slidesmooth2(p=0, t=.5, x=0, y=0):
        alpha .0 xoffset x yoffset y
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0


    transform mm_smooth(p=0, t=.5, x=0, y=0): ##for navigation and main menu
        alpha .0 xoffset x yoffset y
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0
        on replaced:
            easeout t alpha 0
        on hide:
            easeout t alpha 0
        on hover:
            easein .2 xoffset -5
        on idle:
            easeout .2 xoffset 0
        on selected_idle:
            easeout .2 xoffset 0
        on selected_hover:
            easeout .2 xoffset 0

    transform h_smooth(p=0, t=.5, x=0, y=0): ##transform with vertical hover
        alpha .0 xoffset x yoffset y
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0
        on replaced:
            easeout t alpha 0
        on hide:
            easeout t alpha 0
        on hover:
            easein .2 xoffset 5
        on idle:
            easeout .2 xoffset 0
        on selected_idle:
            easeout .2 xoffset 0
        on selected_hover:
            easein .2 xoffset 5



    transform v_smooth(p=0, t=.5, x=0, y=0): ##transform with vertical hover
        alpha .0 xoffset x yoffset y
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0
        on replaced:
            easeout t alpha 0
        on hide:
            easeout t alpha 0
        on hover:
            easein .2 yoffset -3
        on idle:
            easeout .2 yoffset 0
        on selected_idle:
            easeout .2 yoffset 0
        on selected_hover:
            easein .2 yoffset -3

    transform yesno_slide(p=0, t=.5, x=0, y=0): ###for yesno
        alpha .0 xoffset x yoffset y
        pause p
        easein t  alpha 1.0 xoffset 0 yoffset 0
        on hover:
            easein .2 yoffset -10
        on idle:
            easeout .2 yoffset 0

#### KEY BINDINGS ####

init -1600 python:
    renpy.music.register_channel("ambience", "ambient",  loop=True)
    def _toggle_afm():
            _preferences.afm_enable = not _preferences.afm_enable
            renpy.restart_interaction()

    toggle_afm = _toggle_afm

    def _keymap_toggle_afm():
        if renpy.context()._menu:
            return

        _toggle_afm()


##source:http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=6737
init -1100 python:
        config.underlay.append(renpy.Keymap(
          #  helpmenu=(SetVariable("yvalue", 1.0), ShowMenu("help")),
            toggle_afm = _keymap_toggle_afm,))

        config.keymap["toggle_afm"] = [ 'a' ]
     #   config.keymap["helpmenu"] = [ '1' ]
