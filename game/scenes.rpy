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
