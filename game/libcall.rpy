# CGs
image cg1 = "cg/cg1.png"
image cg1_2 = "cg/cg1_2.png"
image cg2 = "cg/cg2.png"
image cg3 = "cg/cg3.png"
image cg4 = "cg/cg4.png"
image cg4_2 = "cg/cg4_2.png"
image cg5 = "cg/cg5.png"
image cg5_2 = "cg/cg5_2.png"
image cg6 = "cg/cg6.png"
image cg6_2 = "cg/cg6_2.png"
image cg7 = "cg/cg7.png"
image cg8 = "cg/cg8.png"
image cg9 = "cg/cg9.png"
image cg10 = "cg/cg10.png"
image cg10_2 = "cg/cg10_2.png"
image cg11 = "cg/cg11.png"
image cg12 = "cg/cg12.png"
image cg13 = "cg/cg13.png"
image cg13_2 = "cg/cg13_2.png"
image cg14 = "cg/cg14.png"
image cg14_2 = "cg/cg14_2.png"
image cg15 = "cg/cg15.png"
image cg16 = "cg/cg16.png"
image cg17 = "cg/cg17.png"
image cg18 = "cg/cg18.png"

init:
    image cg4_grey = im.Grayscale("cg/cg4.png")
    image cg4_2_grey = im.Grayscale("cg/cg4_2.png")
    image cg12_g = im.Grayscale("cg/cg12.png")
    image cg11_g = im.Grayscale("cg/cg11.png")
    image cg5_g = im.Grayscale("cg/cg5.png")
    image cg5_2_g = im.Grayscale("cg/cg5_2.png")

label h_ayu:
    hide ayu
    return

label h_marina:
    hide marina
    return

label s_hayu:
    show hazel at ltl_marina
    show ayu at rtr_ayu
    return

label s_ayha:
    show ayu at ltl_marina
    show hazel flip at rtr_hazel
    return

label s_hama:
    show hazel flip at rtr_hazel
    show marina at ltl_marina
    return

label s_hayuco:
    show hazel at ltl_2
    show ayu at tcenter2
    show cosmos at rtr_2
    return

label s_hayuhi:
    show hazel at ltl_2
    show ayu at tcenter2
    show hifumi at rtr_ayu
    return

label s_mayuhi:
    show marina at ltl_marina2
    show ayu at tcenter2
    show hifumi at rtr_ayu
    return

label s_mayuco:
    show marina at ltl_marina2
    show ayu at tcenter2
    show cosmos at rtr_2
    return

label s_cahi:
    show cosmos at ltl_marina
    show ayu at tcenter2
    show hifumi at rtr_ayu
    return

label s_hayma:
    show hazel at ltl_2
    show ayu at tcenter2
    show marina flip at rtr_hazel3
    return

label s_hahia:
    show hazel at ltl_2
    show hifumi at tcenter2
    show ayu at rtr_2
    return

label s_aymahi:
    show marina at ltl_marina
    show ayu at tcenter2
    show hifumi at rtr_2
    return

label s_hahima:
    show hazel flip at rtr_hazel3
    show hifumi at tcenter2
    show marina at ltl_marina2
    return

label s_hicomaa:
    show hifumi at ltl_2
    show cosmos at tcenter2
    show marina flip at rtr_hazel3
    return

label s_hiayma:
    show hifumi at ltl_2
    show ayu at tcenter2
    show marina flip at rtr_hazel3
    return

label s_mh:
    show marina at ltl_marina
    show hifumi at rtr_ayu
    return

label s_ayucostef:
    show ayu at ltl_2
    show cosmos at tcenter2
    show steffy at rtr_2
    return

label s_elicostef:
    show lizzie flip at ltl_3
    show cosmos at tcenter2
    show steffy at rtr_2
    return

label s_mariliz:
    show lizzie at rtr_ayu
    show marina at ltl_marina
    return

label s_alina:
    show alice at rtr_ayu
    show marina at ltl_marina
    return

label s_ayuyulice:
    show alice at rtr_2
    show yue at tcenter
    show ayu at ltl_2
    return

label s_ayulice:
    show alice at rtr_ayu
    show ayu at ltl2
    return

label s_stefyu:
    show steffy at rtr_ayu
    show ayu at ltl_marina
    return

label s_lizyu:
    show lizzie at rtr_ayu
    show ayu at ltl2
    return

label s_lismos:
    show cosmos at rtr_ayu
    show lizzie flip at ltl_4
    return

label s_stefmos:
    show cosmos at rtr_ayu
    show steffy at ltl
    return

label s_stefeli:
    show steffy at rtr_ayu
    show lizzie flip at ltl_flip
    return

label s_steffy:
    show steffy at tcenter2
    return

label s_lizzie:
    show lizzie at tcenter2
    return

label s_ayu:
    show ayu at tcenter2
    return

label s_yue:
    show yue at tcenter
    return

label s_hifumi:
    show hifumi at tcenter2
    return

label s_hazel:
    show hazel at tcenter2
    return

label s_cosmos:
    show cosmos at tcenter
    return

label s_alice:
    show alice at tcenter
    return

label s_marina:
    show marina at tcenter2
    return

label s_marinaflip:
    show marina flip at tcenter2
    return

label s_yh:
    show yue at ltl2
    show hazel flip at rtr_hazel
    return

label s_ac:
    show cosmos at ltl2
    show ayu at rtr_ayu
    return

label s_yalice:
    show yue at ltl2
    show alice at rtr_ayu
    return

label s_yc:
    show yue at ltl2
    show ayu at rtr_ayu
    return

label s_yuco:
    show yue at ltl2
    show cosmos at rtr_ayu
    return

label s_ca:
    show ayu at ltl2
    show cosmos at rtr_ayu
    return

label s_hc:
    show hazel at ltl2
    show cosmos at rtr_ayu
    return

label s_hico:
    show cosmos at ltl2
    show hifumi at rtr_ayu
    return

label s_hm:
    show marina at ltl_marina
    show hifumi at rtr_ayu
    return

label s_hahi:
    show hazel at ltl_marina
    show hifumi at rtr_ayu
    return

label s_ha:
    show ayu at ltl_marina
    show hifumi at rtr_ayu
    return

label s_yueha:
    show yue at ltl_marina
    show hazel flip at rtr_hazel
    return

label s_ya:
    show ayu at ltl_marina
    show yue at rtr_ayu
    return

label s_yhi:
    show yue at ltl_marina
    show hifumi at rtr_ayu
    return

label s_ym:
    show marina at ltl_marina
    show yue at rtr_ayu
    return

label s_yco:
    show cosmos at ltl_marina
    show yue at rtr_ayu
    return

label s_haco:
    show hazel at ltl_marina
    show cosmos at rtr_ayu
    return

label s_maha:
    show hazel at ltl_marina
    show marina flip at rtr_hazel
    return

label s_stefha:
    show hazel at ltl_marina
    show steffy at rtr_ayu
    return

label s_hifma:
    show hifumi at ltl_marina
    show marina flip at rtr_hazel
    return

label s_hazm:
    show marina at ltl_marina
    show hazel flip at rtr2
    return

label s_hifha:
    show hifumi at ltl_marina
    show hazel flip at rtr2
    return

label s_ch:
    show cosmos at ltl_marina
    show hifumi at rtr_ayu
    return

label s_cha:
    show cosmos at ltl_marina
    show hazel flip at rtr2
    return

label s_cm:
    show marina at ltl2
    show cosmos at rtr_ayu
    return

label s_my:
    show marina at ltl2
    show yue at rtr_ayu
    return

label s_am2:
    show ayu at rtr_ayu
    show marina at ltl_marina
    return

label s_ma:
    show ayu at ltl2
    show marina flip at rtr_hazel2
    return

label s_am:
    show marina at ltl_marina
    show ayu at rtr_ayu
    return

label s_amm:
    show marina at ltl_marina2
    show ayu at rtr_ayu
    return

label s_ah:
    show ayu at ltl_marina
    show hifumi at rtr_ayu
    return

label s_stefumi:
    show steffy at ltl_marina
    show hifumi at rtr_ayu
    return

label s_stefumin:
    show steffy at rtr_ayu
    show hifumi at ltl_marina
    return

label s_stefuel:
    show steffy at ltl_2
    show hifumi at tcenter2
    show lizzie at rtr
    return

label s_stefuzel:
    show steffy at ltl_2
    show hifumi at tcenter2
    show hazel flip at rtr_hazel2
    return

label s_yalm:
    show marina at ltl_2
    show alice at tcenter2
    show yue at rtr
    return

label s_yusteco:
    show yue at ltl_2
    show steffy at tcenter2
    show cosmos at rtr
    return

label s_lizalste:
    show lizzie flip at ltl_3
    show alice at tcenter2
    show steffy at rtr
    return

label s_ayalco:
    show ayu at ltl_2
    show alice at tcenter2
    show cosmos at rtr
    return

label s_maalco:
    show marina at ltl_2
    show alice at tcenter2
    show cosmos at rtr
    return

label s_yusteli:
    show yue at ltl_2
    show steffy at tcenter2
    show lizzie at rtr
    return

label s_yuayuco:
    show yue at ltl_2
    show ayu at tcenter
    show cosmos at rtr
    return

label s_stefayuco:
    show ayu at ltl_2
    show steffy at tcenter2
    show cosmos at rtr
    return

label s_lizayuco:
    show ayu at ltl_2
    show lizzie at tcenter2
    show cosmos at rtr
    return

label s_lizfayuco:
    show lizzie at ltl_2
    show ayu at tcenter2
    show cosmos flip at rtr_hazel2
    return

label s_stefelicos:
    show steffy at ltl_2
    show lizzie at tcenter2
    show cosmos at rtr
    return

label s_stemazel:
    show steffy at ltl_2
    show marina flip at rtr
    show hazel flip at rtr_hazel2
    return

label s_stelizel:
    show steffy at ltl_2
    show lizzie at tcenter2
    show hazel flip at rtr_hazel2
    return

label s_ahic:
    show ayu at ltl_2
    show hifumi at tcenter2
    show cosmos at rtr
    return

label s_hacoma:
    show hazel at ltl_2
    show cosmos at tcenter2
    show marina flip at rtr_hazel3
    return

label s_amhi:
    show marina at ltl_2
    show hifumi at tcenter2
    show ayu at rtr
    return

label s_acohi:
    show ayu at ltl_2
    show cosmos at tcenter2
    show hifumi at rtr_ayu
    return

label s_ahaco:
    show ayu at ltl_2
    show hazel at tcenter2
    show cosmos at rtr
    return

label s_ahiha:
    show ayu at ltl_2
    show hifumi at tcenter2
    show hazel flip at rtr_hazel2
    return

label s_ayhaz:
    show ayu at ltl_marina2
    show yue at tcenter
    show hazel flip at rtr_hazel
    return

label s_hiyha:
    show hifumi at ltl_marina2
    show yue at tcenter
    show hazel flip at rtr_hazel
    return

label s_yhahi:
    show yue at ltl_marina2
    show hazel flip at tcenter2
    show hifumi at rtr_ayu
    return

label s_mayhi:
    show marina at ltl_marina2
    show yue at tcenter
    show hifumi at rtr_2
    return

label s_aycohi:
    show ayu at ltl_2
    show cosmos at tcenter
    show hifumi at rtr_2
    return


label s_hayc:
    show hazel at ltl_2
    show ayu at tcenter2
    show cosmos at rtr_2
    return

label s_ach:
    show ayu at ltl_2
    show cosmos at tcenter
    show hifumi at rtr_ayu
    return

label s_hach:
    show hazel at ltl_2
    show cosmos at tcenter2
    show hifumi at rtr_2
    return

label s_all:
    show marina at ltl_marina2
    show ayu at tcenter2
    show cosmos at rtr
    return

label s_mah:
    show marina at ltl_marina2
    show ayu at tcenter2
    show hifumi at rtr
    return

label s_myha:
    show marina at ltl_marina2
    show yue at tcenter2
    show hazel flip at rtr_hazel
    return

label s_mcha:
    show marina at ltl_marina2
    show cosmos at tcenter2
    show hazel flip at rtr_hazel
    return

label s_myc:
    show marina at ltl_marina2
    show yue at tcenter2
    show cosmos at rtr
    return

label s_mac:
    show marina at ltl_marina2
    show ayu at tcenter2
    show cosmos at rtr
    return

label s_mhc:
    show marina at ltl_marina2
    show hifumi at tcenter2
    show cosmos at rtr
    return

label s_ham:
    show marina at ltl_marina2
    show hifumi at tcenter2
    show ayu at rtr
    return

label s_aycoma:
    show ayu at rtr_2
    show cosmos at tcenter2
    show marina at ltl_marina2
    return

label s_ayhama:
    show ayu at rtr_2
    show hazel at tcenter2
    show marina at ltl_marina2
    return

label s_hiama:
    show hifumi at rtr_2
    show ayu at tcenter2
    show marina at ltl_marina2
    return

label s_hicoma:
    show hifumi at rtr_2
    show cosmos at tcenter2
    show marina at ltl_marina2
    return

label s_all2:
    show marina at ltl_marina2
    show ayu at tcenter2
    show cosmos at rtr_2
    return

label s_hihama:
    show hifumi at rtr_2
    show hazel at tcenter2
    show marina at ltl_marina2
    return

label s_stefhama:
    show steffy at rtr_2
    show hazel at tcenter2
    show marina at ltl_marina2
    return

label s_hca:
    show hifumi at rtr_2
    show cosmos at tcenter2
    show ayu at ltl_2
    return

label s_hya:
    show hifumi at rtr_2
    show yue at tcenter2
    show ayu at ltl_2
    return

label s_cya:
    show cosmos at rtr_2
    show yue at tcenter2
    show ayu at ltl_2
    return

label s_cyh:
    show cosmos at rtr_2
    show yue at tcenter2
    show hifumi at ltl_2
    return




###

#label s_om:
#    show ohana at ltl
#    show mikoto at rtl
#    return

#label h_om:
#    hide ohana at ltl
#    hide mikoto at rtl
#    return

#label s_ohana:
#    show ohana at tcenter
#    return

#label h_ohana:
#    hide ohana at tcenter
#    return
