label sm1cs_bg005i:

    # Starts with an interaction in the studio with BG
    # Scene starts with KV telling BG and MC she has to run out, and to watch over the photo dojo while she's gone

    $ LocationController.draw_current_location("bg")
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral
    bg "Oh, hey [mcname]."
    mc "Hey. Got a minute?"
    bg "I, uh... Yeah. Sure."
    hide lpd_bg_neutral
    show expression cc.get_expression_image("bg", "neutral02") as lpd_bg_neutral02
    mc "Good. Because I think we need to talk."
    bg "About...?"
    mc "About the other night."
    hide lpd_bg_neutral02
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral
    bg "Oh. That. Yeah, the photos are going to be great, I think Kanya will—"
    mc "What photos? Amore, we were alone."
    bg "..."
    mc "I'm talking about what happened after."
    bg "I..."

    $ StoryController.end_scene(BG_STORY)
    return
