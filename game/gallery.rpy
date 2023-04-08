init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # A button that contains an image that automatically unlocks.

    g.button       ("cg1")
    g.unlock_image ("cg1")
    g.unlock_image ("cg1_2")

    g.button       ("cg1_a")
    g.unlock_image ("cg1_a")
    g.unlock_image ("cg1_2_a")

    g.button       ("cg2")
    g.unlock_image ("cg2")

    g.button       ("cg2_a")
    g.unlock_image ("cg2_a")

    g.button       ("cg3")
    g.unlock_image ("cg3")

    g.button       ("cg3_a")
    g.unlock_image ("cg3_a")

    g.button       ("cg4")
    g.unlock_image ("cg4")

    g.button       ("cg4_a")
    g.unlock_image ("cg4_a")

    g.button       ("cg5")
    g.unlock_image ("cg5")

    g.button       ("cg5_a")
    g.unlock_image ("cg5_a")

    g.button       ("cg6")
    g.unlock_image ("cg6")

    g.button       ("cg6_a")
    g.unlock_image ("cg6_a")

    g.button       ("cg7")
    g.unlock_image ("cg7")

    g.button       ("cg7_a")
    g.unlock_image ("cg7_a")

    g.button       ("cg8")
    g.unlock_image ("cg8")

    g.button       ("cg8_a")
    g.unlock_image ("cg8_a")

    g.button       ("cg9")
    g.unlock_image ("cg9")

    g.button       ("cg9_a")
    g.unlock_image ("cg9_a")

    g.button       ("cg10")
    g.unlock_image ("cg10")

    g.button       ("cg10_a")
    g.unlock_image ("cg10_a")

    g.button       ("cg11")
    g.unlock_image ("cg11")

    g.button       ("cg11_a")
    g.unlock_image ("cg11_a")

    g.button       ("cg12")
    g.unlock_image ("cg12")

    g.button       ("cg12_a")
    g.unlock_image ("cg12_a")

    g.button       ("cg13")
    g.unlock_image ("cg13")

    g.button       ("cg13_a")
    g.unlock_image ("cg13_a")

    g.button       ("cg14")
    g.unlock_image ("cg14")

    g.button       ("cg14_a")
    g.unlock_image ("cg14_a")

    g.button       ("cg15")
    g.unlock_image ("cg15")

    g.button       ("cg15_a")
    g.unlock_image ("cg15_a")

    g.button       ("cg16")
    g.unlock_image ("cg16")

    g.button       ("cg16_a")
    g.unlock_image ("cg16_a")

    g.button       ("cg17")
    g.unlock_image ("cg17")

    g.button       ("cg17_a")
    g.unlock_image ("cg17_a")

    g.button       ("cg18")
    g.unlock_image ("cg18")

    g.button       ("cg18_a")
    g.unlock_image ("cg18_a")

    g.button       ("hcg1")
    g.unlock_image ("hcg1")
    g.unlock_image ("hcg1_2")
    g.unlock_image ("hcg1_3")

    g.button       ("hcg2")
    g.unlock_image ("hcg2")
    g.unlock_image ("hcg2_2")
    g.unlock_image ("hcg2_3")

    g.button       ("hcg3")
    g.unlock_image ("hcg3")
    g.unlock_image ("hcg3_2")

    g.button       ("hcg4")
    g.unlock_image ("hcg4")
    g.unlock_image ("hcg4_2")
    g.unlock_image ("hcg4_3")
    g.unlock_image ("hcg4_4")
    g.unlock_image ("hcg4_5")
    g.unlock_image ("hcg4_6")

    g.button       ("hcg5")
    g.unlock_image ("hcg5")
    g.unlock_image ("hcg5_2")
    g.unlock_image ("hcg5_3")

    g.locked_button = "gui/gal_locked.png"
  #  g.hover_border = "gui/gal_frame.png"
  #  g.idle_border = "gui/gal_frame.png"

    g.transition = dissolve

    bg_page=1



image gal_locked:
    "gui/gal_locked.png"

screen gallery():

    tag menu

    use game_menu(_("Gallery")):


        frame:
            style_group "gal"
            background None
            xalign .5
            $ next_bg_page = bg_page + 1
            $ prev_bg_page = bg_page - 1
            xoffset -50
            yoffset 140


            grid 3 2:
                    spacing 50
                    xalign 0.5
                    #xfill True

                    # Call make_button to show a particular button.

                    if persistent.adult==True:
                        add g.make_button("cg1_a", im.Scale("adult/cg1_a.png", 384, 216))
                    else:
                        add g.make_button("cg1", im.Scale("cg/cg1.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg2_a", im.Scale("adult/cg2_a.png", 384, 216))
                    else:
                        add g.make_button("cg2", im.Scale("cg/cg2.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg3_a", im.Scale("adult/cg3_a.png", 384, 216))
                    else:
                        add g.make_button("cg3", im.Scale("cg/cg3.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg4_a", im.Scale("adult/cg4_a.png", 384, 216))
                    else:
                        add g.make_button("cg4", im.Scale("cg/cg4.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg5_a", im.Scale("adult/cg5_a.png", 384, 216))
                    else:
                        add g.make_button("cg5", im.Scale("cg/cg5.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg6_a", im.Scale("adult/cg6_a.png", 384, 216))
                    else:
                        add g.make_button("cg6", im.Scale("cg/cg6.png", 384, 216))

        hbox:
            xalign .5
            #xalign .5
            yoffset -40
            style_prefix "gal"
            spacing 20
            textbutton _("Previous Page")# action SetVariable('bg_page', prev_bg_page )
            textbutton _("Page 1")
            textbutton _("Next Page") action ShowMenu('gallery1')


screen gallery1():

    tag menu

    use game_menu(_("Gallery")):


        frame:
            style_group "gal"
            background None
            xalign .5
            $ next_bg_page = bg_page + 1
            $ prev_bg_page = bg_page - 1
            xoffset -50
            yoffset 140


            grid 3 2:
                    spacing 50
                    xalign 0.5
                    #xfill True

                    # Call make_button to show a particular button.

                    if persistent.adult==True:
                        add g.make_button("cg7_a", im.Scale("adult/cg7_a.png", 384, 216))
                    else:
                        add g.make_button("cg7", im.Scale("cg/cg7.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg8_a", im.Scale("adult/cg8_a.png", 384, 216))
                    else:
                        add g.make_button("cg8", im.Scale("cg/cg8.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg9_a", im.Scale("adult/cg9_a.png", 384, 216))
                    else:
                        add g.make_button("cg9", im.Scale("cg/cg9.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg10_a", im.Scale("adult/cg10_a.png", 384, 216))
                    else:
                        add g.make_button("cg10", im.Scale("cg/cg10.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg11_a", im.Scale("adult/cg11_a.png", 384, 216))
                    else:
                        add g.make_button("cg11", im.Scale("cg/cg11.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg12_a", im.Scale("adult/cg12_a.png", 384, 216))
                    else:
                        add g.make_button("cg12", im.Scale("cg/cg12.png", 384, 216))


        hbox:
            xalign .5
            #xalign .5
            yoffset -40
            style_prefix "gal"
            spacing 20
            textbutton _("Previous Page") action ShowMenu('gallery')
            textbutton _("Page 2")
            textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]

screen gallery2():

    tag menu

    use game_menu(_("Gallery")):


        frame:
            style_group "gal"
            background None
            xalign .5
            $ next_bg_page = bg_page + 1
            $ prev_bg_page = bg_page - 1
            xoffset -50
            yoffset 140


            grid 3 2:
                    spacing 50
                    xalign 0.5
                    #xfill True

                    # Call make_button to show a particular button.

                    if persistent.adult==True:
                        add g.make_button("cg13_a", im.Scale("adult/cg13_a.png", 384, 216))
                    else:
                        add g.make_button("cg13", im.Scale("cg/cg13.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg14_a", im.Scale("adult/cg14_a.png", 384, 216))
                    else:
                        add g.make_button("cg14", im.Scale("cg/cg14.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg15_a", im.Scale("adult/cg15_a.png", 384, 216))
                    else:
                        add g.make_button("cg15", im.Scale("cg/cg15.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg16_a", im.Scale("adult/cg16_a.png", 384, 216))
                    else:
                        add g.make_button("cg16", im.Scale("cg/cg16.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg17_a", im.Scale("adult/cg17_a.png", 384, 216))
                    else:
                        add g.make_button("cg17", im.Scale("cg/cg17.png", 384, 216))
                    if persistent.adult==True:
                        add g.make_button("cg18_a", im.Scale("adult/cg18_a.png", 384, 216))
                    else:
                        add g.make_button("cg18", im.Scale("cg/cg18.png", 384, 216))


        hbox:
            xalign .5
            #xalign .5
            yoffset -40
            style_prefix "gal"
            spacing 20
            textbutton _("Previous Page") action ShowMenu('gallery1')
            textbutton _("Page 3")
            if persistent.adult==True:
                textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
            else:
                textbutton _("Next Page") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]

screen gallery3():

    tag menu

    use game_menu(_("Gallery")):


        frame:
            style_group "gal"
            background None
            xalign .5
            $ next_bg_page = bg_page + 1
            $ prev_bg_page = bg_page - 1
            xoffset -50
            yoffset 140


            grid 3 2:
                    spacing 50
                    xalign 0.5
                    #xfill True

                    # Call make_button to show a particular button.

                    add g.make_button("hcg1", im.Scale("adult/hcg1.png", 384, 216))
                    add g.make_button("hcg2", im.Scale("adult/hcg2.png", 384, 216))
                    add g.make_button("hcg3", im.Scale("adult/hcg3.png", 384, 216))
                    add g.make_button("hcg4", im.Scale("adult/hcg4.png", 384, 216))
                    add g.make_button("hcg5", im.Scale("adult/hcg5.png", 384, 216))
                    label _(" ")




        hbox:
            xalign .5
            #xalign .5
            yoffset -40
            style_prefix "gal"
            spacing 20
            textbutton _("Previous Page") action ShowMenu('gallery2')
            textbutton _("Page 4")
            textbutton _("Next Page") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]



init -2:

    # Make all the main menu buttons be the same size.
#    style mm_button:
#        size_group "mm"


    style gal_button is navigation_button

    style gal_button_text is quick_button_text
