label sm1cs_mes_r1i:

    # Starts with an interaction in the studio with BG
    # Scene starts with KV telling BG and MC she has to run out, and to watch over the photo dojo while she's gone

    $ LocationController.draw_current_location("mes")
    show expression cc.get_expression_image("mes", "neutral01") as lsd_mes_neutral
    mc "Hey Min ready for some fun?"
    hide lsd_mes_neutral
    show expression cc.get_expression_image("mes", "excited01") as lsd_mes_neutral
    mes "Hell yeah I am!"

    jump sm1cs_mes_r1
