image splash:
    "gui/splash.png"
image mm_logo:
    "gui/logo.png"
image mm_logo1:
    "gui/logo.png"
        
label splashscreen:
    scene black
    $ renpy.pause(0.5)

    show splash with fade
    $ renpy.pause(1.0)

    hide splash with fade
    $ renpy.pause(1.0)
    
    show mm_logo with fade
    $ renpy.pause(2.0)
    
    return