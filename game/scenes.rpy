screen roomscreen:
    imagemap:
        idle "room.png"
        hover "roomhover.png"
        ground "room.png"
        hotspot(175, 1, 1514, 599) action Jump ("apartments")
        hotspot(104, 954, 156, 110) action Jump ("ink")
        hotspot(338, 806, 661, 264) action Jump ("notes")
        hotspot(858, 661, 433, 97) action Jump ("board")
        #hotspot(1048, 902, 148, 96)
        hotspot(1214, 801, 180, 222) action Jump ("mug")
        hotspot(1426, 621, 322, 417) action Jump ("lamp")

screen apartmentsscreen:
    imagemap:
        idle "apartments.png"
        hover "apartmentshover.png"
        ground "apartments.png"
        hotspot(53, 78, 821, 361) action Jump ("apartment3")
        hotspot(1251, 434, 229, 128) action Jump ("apartment1")
        hotspot(43, 478, 829, 333) action Jump ("apartment2")
        hotspot(1250, 695, 221, 130) action Jump("apartment4")

screen apartment1screen:
    imagemap:
        idle "arguebase.png"
        hover "arguehover.png"
        ground "arguebase.png"
        hotspot(485, 268, 409, 674) action Jump("herstart")
        hotspot(1062, 267, 413, 520) action Jump ("himstart")

screen apartment4screen:
    imagemap:
        idle "solitude.png"
        hover "solitudehover.png"
        ground "solitude.png"
        hotspot(815, 622, 279, 293) action Jump ("tv")
        hotspot(0, 540, 793, 537) action Jump ("bed")
        hotspot(0, 154, 244, 387) action Jump ("windowsol")
        hotspot(747, 311, 104, 152) action Jump ("cig")
        hotspot(1137, 191, 412, 745) action Jump ("mirror")
        hotspot(258, 178, 273, 223) action Jump ("books")
        hotspot(791, 0, 197, 253) action Jump ("light")
        hotspot(1501, 742, 238, 125) action Jump ("phone")

screen apartment3screen:
    imagemap:
        idle ""
        hover ""
        ground ""
        ##hotspot
