screen roomscreen:
    imagemap:
        idle "room.png"
        hover "roomhover.png"
        ground "room.png"
        hotspot(360, 24, 1170, 651) action Jump ("apartments")

screen apartmentsscreen:
    imagemap:
        idle "apartments.png"
        hover "apartmentshover.png"
        ground "apartments.png"
        hotspot(39, 9, 744, 485) action Jump ("apartment3")
        hotspot(969, 61, 902, 473) action Jump ("apartment1")
        hotspot(40, 560, 749, 435) action Jump ("apartment2")
        hotspot(1008, 553, 900, 493) action Jump("apartment4")

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
        hotspot(809, 608, 295, 289) action Jump ("tv")
        hotspot(0, 540, 793, 537) action Jump ("bed")
        hotspot(0, 179, 256, 316) action Jump ("windowsol")
        hotspot(669, 206, 161, 271) action Jump ("cig")
        hotspot(1159, 196, 341, 572) action Jump ("mirror")
        hotspot(274, 257, 155, 154) action Jump ("books")
        hotspot(1523, 684, 279, 203) action Jump ("phone")

screen apartment3screen:
    imagemap:
        idle ""
        hover ""
        ground ""
        ##hotspot
