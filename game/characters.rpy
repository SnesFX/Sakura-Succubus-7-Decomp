
init:

    $ huer = 1.0
    $ hueb = 1.0
    $ hueg = 1.0

##################

    image ayu:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Ayu/bases/%s.png"%(abody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Ayu/faces/%s.png"%(aface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image ayu flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Ayu/bases/%s.png"%(abody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Ayu/faces/%s.png"%(aface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

###################

    image cosmos:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Cosmos/bases/%s.png"%(cbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Cosmos/faces/%s.png"%(cface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image cosmos flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Cosmos/bases/%s.png"%(cbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Cosmos/faces/%s.png"%(cface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

###################

    image marina:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Marina/bases/%s.png"%(mbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Marina/faces/%s.png"%(mface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image marina flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Marina/bases/%s.png"%(mbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Marina/faces/%s.png"%(mface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

###################

    image hifumi:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Hifumi/bases/%s.png"%(hbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Hifumi/faces/%s.png"%(hface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image hifumi flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Hifumi/bases/%s.png"%(hbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Hifumi/faces/%s.png"%(hface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

###################

    image hazel:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Hazel/bases/%s.png"%(habody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Hazel/faces/%s.png"%(haface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image hazel flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Hazel/bases/%s.png"%(habody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Hazel/faces/%s.png"%(haface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

#########################

    image yue:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Yue/bases/%s.png"%(ybody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Yue/faces/%s.png"%(yface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image yue flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Yue/bases/%s.png"%(ybody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Yue/faces/%s.png"%(yface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

#########################

    image steffy:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Steffy/bases/%s.png"%(sbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Steffy/faces/%s.png"%(sface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image ayu flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Steffy/bases/%s.png"%(sbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Steffy/faces/%s.png"%(sface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

#########################

    image lizzie:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Lizzie/bases/%s.png"%(lbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Lizzie/faces/%s.png"%(lface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image lizzie flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Lizzie/bases/%s.png"%(lbody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Lizzie/faces/%s.png"%(lface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

#########################

    image alice:
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Alice/bases/%s.png"%(albody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Alice/faces/%s.png"%(alface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )

    image alice flip:
        xzoom -1
        LiveComposite(
            (606,720),
            (0,0), im.MatrixColor("sprites/Alice/bases/%s.png"%(albody),im.matrix.tint(huer, hueg, hueb)), #clothes
            (0,0), im.MatrixColor("sprites/Alice/faces/%s.png"%(alface),im.matrix.tint(huer, hueg, hueb)), #expressions
            )
