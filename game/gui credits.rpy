
#image text_b = ParameterizedText(font=gui.interface_font,text_align=.5,outlines=[(1,gui.quick_button_text_idle_outline, 1,1),(1,gui.quick_button_text_idle_outline, 0,0)])
image black_alpha = Solid("#00000066")

label credits:

    stop ambience fadeout 1.0
    stop music fadeout 1.0
    scene black with slow_dissolve
    window hide dissolve

    $ renpy.pause(1.0)

    play music "bgm/succubus_pensive_loop.ogg" fadein 1.0
    scene skyn with Dissolve(1.0)
    #show mm_logo with Dissolve(1.0)

    $ renpy.pause(2.5, hard=True)
    show black_alpha with Dissolve(2.0)
  #  scene black behind mm_logo with Dissolve(3.0)
    show text (
        "{size=60}Story and writing:\n{/size}"
         "{size=60}[credits_writer]{/size}"
        ) with Dissolve(2.0):
            xalign 0.1 yalign .5
    $ renpy.pause(2.5, hard=True)
  #  scene black behind mm_logo with Dissolve(3.0)
    show text (
        "{size=60}Character art:\n{/size}"
         "{size=60}[credits_artist]{/size}"
        ) with Dissolve(2.0):
            xalign 0.9 yalign .5
    $ renpy.pause(2.5, hard=True)
  #  scene black behind mm_logo  with Dissolve(3.0)
    show text (
        "{size=60}Background art:\n{/size}"
         "{size=60}[credits_bg_artist]{/size}"
        ) with Dissolve(2.0):
            xalign 0.1 yalign .5
    $ renpy.pause(2.5, hard=True)
  #  scene bg_sky_night behind mm_logo  with Dissolve(3.0)
    show text (
        "{size=60}Music:\n{/size}"
        "{size=60}[credits_music]{/size}"
        ) with Dissolve(2.0):
            xalign 0.9 yalign .5
    $ renpy.pause(2.5, hard=True)
    show text (
        "{size=60}Production:\n{/size}"
         "{size=60}[credits_production]{/size}"
        ) with Dissolve(2.0):
            xalign 0.1 yalign .5
    $ renpy.pause(2.5, hard=True)
    show text (
        "{size=60}[credits_thanks]{/size}"
        ) with Dissolve(2.0):
        xalign 0.5 yalign .5
    $ renpy.pause(5.0, hard=True)

    if credits_thanks1 == None:
        jump credits_end
    else:
        show text (
            "{size=60}[credits_thanks1]{/size}"
            ) with Dissolve(2.0):
                xalign 0.5 yalign .5
        $ renpy.pause(2.5, hard=True)

    if credits_header2 == None:
        jump credits_end
    else:
        show text (
            "{size=60}[credits_header2]\n{/size}"
            "{size=60}[credits_thanks2]{/size}"
            ) with Dissolve(2.0):
                xalign 0.9 yalign .5
        $ renpy.pause(2.5, hard=True)
    if credits_header3 == None:
        jump credits_end
    else:
        show text (
            "{size=60}[credits_header3]\n{/size}"
            "{size=60}[credits_thanks3]{/size}"
            ) with Dissolve(2.0):
                xalign 0.1 yalign .5
        $ renpy.pause(2.5, hard=True)

label credits_end:


    stop music fadeout 5.0
    $ renpy.pause(2.5, hard=True)

    scene black with Dissolve (4.0)

    stop music fadeout 3.0
    pause 5

return
