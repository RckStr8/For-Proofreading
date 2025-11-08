label sm1cs_arj002i:

    ##quest log - "Talk to Stacy about AmRose in the Afternoon"

    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_yes_okay2 noloop
    mc "Alright, Stacy. I think it's time."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_happy_wooh1 noloop
    sy "Time for ice cream? Yes!"
    play voice2 mc_arrogant_heh1 noloop
    mc "Hah. No, I mean, time for us to get back at AmRose for her little fake customer scheme."
    play voice3 stacy_thinking_oh2 noloop
    sy "Ooooh. That is going to be even better than ice cream."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_hmm1 noloop
    sy "So what is the plan?"
    play voice2 mc_thinking_hmm2 noloop
    mc "I'll keep it simple. I'll text her and ask her to help with a hardware problem."
    mc "Amrose will come because she is still a good person."
    mc "And if that is not enough, she probably can't resist the chance to try to spy on our systems again."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_happy_laugh1 noloop
    sy "Diabolical. Good luck."

    $ StoryController.end_scene(ARJ_STORY)
    return
