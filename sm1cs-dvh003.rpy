label sm1cs_dvh003:

    ## "Talk to Denise in her office around Noon."

    #denise sitting in her chair
    scene sm1cs-dvh003-01 mc-dvh-office_c1 with dissolve
    #dvh looks up, frowns at mc
    play voice3 girl34_angry_nergh noloop
    dvh "Ugh. The pannekoek. Yes, little Bram? What are you here for?"
    #mc scowls, then crosses his arms
    scene sm1cs-dvh003-01 mc-dvh-office_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "That's a bit much, don't you think? Also, I looked that up. Why are you calling me a \"pancake\"?"
    #dvh laughs, leaning back in her chair
    scene sm1cs-dvh003-02 mc-dvh-office2_c1 with dissolve
    play voice3 girl34_no_nah2 noloop
    dvh "It's a Dutch thing. Don't worry about it too much, little Bram."
    #mc steps forward, sticking his chin up
    scene sm1cs-dvh003-02 mc-dvh-office2_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I've been studying, and I wanted to show you that I am serious about my acting skills. Do you have a minute, so I can show you my form?"
    #dvh purses her lips, then puts a finger on her chin
    scene sm1cs-dvh003-03 mc-dvh-office3_c1 with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    dvh "Fine. I have a minute, but you'd better bring your best to this, or Little Bram, you will stay."
    mct "Well, I was going to do that soliloquy from Orpheus Descending... but I think I have something better, now."
    #mc steps back a little
    scene sm1cs-dvh003-03 mc-dvh-office3_c2 with dissolve
    play voice2 mc_angry_oof noloop
    mc "I'll be doing Dracula. In this scene, he's berating a subordinate who calls him out for the suicidal nature of his plan to eradicate human life."
    #dvh raises an eyebrow, but waves a hand at mc to continue
    scene sm1cs-dvh003-04 mc-dvh-office4_c1 with dissolve
    play voice3 girl34_yes_ugu1 noloop
    pause
    #mc makes an angry face, lifting one hand up like a claw, palm up
    scene sm1cs-dvh003-04 mc-dvh-office4_c2 with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "I will not be questioned by you. I have told you how it will be."
    #mc takes a step forward, "claw" hand still raised
    scene sm1cs-dvh003-04-2 mc-dvh-office5_c2 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "The humans will die. You will be taken care of. Little Godbrand. Little vampire."
    #me bares his teeth, as if showing fangs, still angry
    scene sm1cs-dvh003-05 mc-dvh-talk_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Little parasite. Little boat weevil who delights in making noise and pretending he is important and dangerous."
    mc "Are you going to continue questioning me? Are you going to {b}fight{/b} me, little Godbrand?"
    #mc face returns to a neutral expression, his hand drops, and he steps back to where he was when his monologue started
    scene sm1cs-dvh003-05 mc-dvh-talk_c2 with dissolve
    mc "Annnd scene..."
    #dvh looks interested, leaning forward onto her desk
    scene sm1cs-dvh003-06 mc-dvh-stand_c1 with dissolve
    play voice3 girl34_surprised_wow4 noloop
    dvh "Interesting... I approve. The parallels between Dracula's relationship to an upstart Godbrand and our own are not lost on me."
    scene sm1cs-dvh003-06 mc-dvh-stand_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I was originally planning on Orpheus Descends, but your \"Little Bram\" remark inspired me, and I really like that show."
    #dvh frowns, then stands up from behind her desk, walking around to join mc
    scene sm1cs-dvh003-07 mc-dvh-walk_c1 with dissolve
    play voice3 girl34_thinking_emm1 noloop
    dvh "Alright, I admit I was not in the best of moods. You know how I feel about paperwork."
    dvh "Say I give you this chance. Say I take you under my wing, and teach you. Will you keep showing me such improvement?"
    #mc nods, looking right into dvh's eyes
    scene sm1cs-dvh003-07 mc-dvh-walk_c2 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "I will. I'm serious about my acting, like I said."
    #3 renders of dvh nods
    play voice3 girl34_arrogant_huh1 noloop
    dvh "And you will accept all of my instructions?{w} You will not run away when I challenge you?"
    scene sm1cs-dvh003-08 mc-dvh-talk_c1 with dissolve
    play voice2 mc_no_no8 noloop
    mc "No, I won't run. I want to do better and improve the troupe's performances."
    #mc kind of saying he expects some respect in return
    mc "But I also need you to both understand and respect my work."
    #dvh looks a bit mischevious
    scene sm1cs-dvh003-08 mc-dvh-talk_c2 with dissolve
    play voice3 girl34_arrogant_ha4 noloop
    dvh "Lekker. Then you will strip."
    mc "Strip? Who?"
    mc "Me stripping?"
    # then starts to strip, taking off her shirt
    scene sm1cs-dvh003-08-2 mc-dvh-talk2_c2 with dissolve
    dvh "Yes."
    play voice3 girl34_yes_yeah3 noloop
    dvh "To act is to reveal your entire self to the audience.{w} Unguarded. Uncovered."
    #mc hesitates, unable to take his eyes off of dvh's breasts for just a moment
    scene sm1cs-dvh003-09 mc-dvh-undress_c1 with dissolve
    #mc then he takes his own shirt off
    menu:
        "Flirt with her" (hint = "sm1cs_dvh003_m01_h01"):
            $ player.set_choice("sm1cs_dvh003_flirt_dvh")
            $ CharacterController.get_character("dvh").add_point()
            play voice2 mc_happy_hah2 noloop
            mc "I keep forgetting that nudity isn't strange at all for you. It's quite a culture shock, even if you have amazing breasts."
            #dvh pauses as she's about to take her shorts off. She looks back at mc, with her eyebrow raised like she's not sure how to take that
            scene sm1cs-dvh003-08-3 mc-dvh-talk3_c2 with dissolve
            play voice3 girl34_arrogant_ha2 noloop
            dvh "I am aware of the effect I have on men."

        "Keep your mouth shut" (hint = "sm1cs_dvh003_m01_h02"):
            $ player.set_choice("sm1cs_dvh003_mouth_shut")
            scene sm1cs-dvh003-08-3 mc-dvh-talk3_c2 with dissolve
            play voice3 girl34_thinking_hmm4 noloop

    #mc takes his pants off, not seeing the look, and dvh gets a good look at his cock
    dvh "{i}Hmph{/i}. At least you are not actually a \"little\" Godbrand..."
    #mc looks up, dvh waves her hands at him and continues stripping
    scene sm1cs-dvh003-10 mc-dvh-undress2_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "Denise checking me out wasn't on my bingo card. Better play this as cool as possible."
    #once both are naked, dvh stands an arm's length away from mc
    scene sm1cs-dvh003-10 mc-dvh-undress2_c2 with dissolve
    play voice3 girl34_disappointed_eem3 noloop
    dvh "We stand close, for this. I like the angry, powerful man role."
    dvh "You handled that quite well."
    dvh "This time, I want you to bring that same energy to a young woman who has refused you often, but who you love."
    #mc looks at dvh's naked body, quickly getting a hard-on and stepping just a little closer.
    scene sm1cs-dvh003-12 mc-dvh-look_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Anything else?"
    #dvh puts up a hand, putting it on mc's chest and gently pushing him back.
    scene sm1cs-dvh003-14 mc-dvh-stop_c2 with dissolve
    play voice3 girl34_arrogant_pff noloop
    dvh "Down boy. You respect this young woman, you want her to be yours, need her to be yours, but she won't play ball."
    dvh "Show me your {b}frustration{/b}..."
    dvh "{b}Tease{/b} me with your lust. Without touching me of course."
    dvh "Then you will pass."
    #mc closes his eyes and takes a deep breath, then gives a thumbs up.
    scene sm1cs-dvh003-14 mc-dvh-stop_c3 with dissolve
    mct "I am the master of my domain. I am the master of my domain."
    #dvh steps closer, looking hurt and innocent
    scene sm1cs-dvh003-15 mc-dvh-talk_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mct "But fuck me, Denise is hot."
    scene sm1cs-dvh003-15 mc-dvh-talk_c2 with dissolve
    play voice3 girl34_surprised_ohmy1 noloop
    dvh "My Lord, you must stop this foolishness! You have seen me bare, is that not enough? Can that not be satisfactory?"
    #mc face twists in anger and he steps forward as well, leaving barely half a meter between them
    scene sm1cs-dvh003-16 mc-dvh-close_c1 with dissolve
    play voice2 mc_no_no4 noloop
    mc "No, no, and thrice damn it more, no! I cannot be satisfied with only your memory, with only your scent and the image of your hair of flame!"
    #dvh reaches up, putting a hand on mc's chest
    scene sm1cs-dvh003-16 mc-dvh-close_c2 with dissolve
    play voice3 girl34_angry_ahem1 noloop
    dvh "You must! You must satisfy yourself with this paltry gift, for I am sworn to marry another."
    #mc reaches up, putting his hand on the back of dvh's head, like the claw he made during his Dracula monologue
    scene sm1cs-dvh003-17 mc-dvh-close2_c1 with dissolve
    mct "Denise is touching me."
    play voice2 mc_angry_errr4 noloop
    mc "A paltry gift for your earnest love, and an earnest marriage for your paltry suitor. These seem mismatched, pretty maid."
    scene sm1cs-dvh003-17 mc-dvh-close2_c2 with dissolve
    play voice3 girl34_happy_relief3 noloop
    dvh "Mismatched only in spirit, my Lord. For wicked hearts such as ours, this needs must."
    #mc's cock brushes on dvh
    scene sm1cs-dvh003-18 mc-dvh-close3_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "So close. Must resist!"
    mc "What fools we mortals be, if love such as this is wicked. No, let me be a villain and trample the hearts of those who would turn us out."
    #dvh looks down at mc's cock, reaching down to grip it
    scene sm1cs-dvh003-19 mc-dvh-close4_c1 with dissolve
    mct "Oh fuck!"
    #mc gasps,
    scene sm1cs-dvh003-19 mc-dvh-close4_c2 with dissolve
    play voice3 girl34_sex_closedmoan1 noloop
    pause
    #moment of them looking at each other - simplest of smiles on dvh's lips
    scene sm1cs-dvh003-19-2 mc-dvh-close5_c1 with dissolve
    pause
    #then the smile is gone
    scene sm1cs-dvh003-19-3 mc-dvh-close6_c1 with dissolve
    pause
    #dvh pushes mc back
    scene sm1cs-dvh003-20 mc-dvh-push_c2 with dissolve
    play voice3 girl34_thinking_emm5 noloop
    dvh "Enough.{w} You have convinced me, [mcname]."
    mct "Oh thank god!"
    #dvh and mc get dressed again. dvh stays facing away from mc, refusing to look at him
    scene sm1cs-dvh003-21 mc-dvh-end_c2 with fade
    #sound sfx - zipping up sfx
    play voice3 girl34_happy_relief1 noloop
    dvh "You did well, but don't think I didn't notice your hand on the back of my head. You need better control, but it was adequate for the scene."
    dvh "Adequate is not enough, for my understudy, but it will do for now."
    #mc smiles, then clears his throat
    scene sm1cs-dvh003-22 mc-dvh-end2_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "So, are you satisfied, or not?"
    scene sm1cs-dvh003-23 mc-dvh-out_c1 with dissolve
    play voice3 girl34_angry_ahem4 noloop
    dvh "Get out."
    #mc pauses for a moment. Then he turns to leave. When he turns the handle, dvh scowls and crosses her arms, still facing away.
    scene sm1cs-dvh003-23 mc-dvh-out_c2 with dissolve
    pause
    scene sm1cs-dvh003-24 mc-dvh-pause_c1 with dissolve
    pause
    scene sm1cs-dvh003-25 mc-dvh-pause2_c2 with dissolve
    play voice3 girl34_hey_angry7 noloop
    dvh "[mcname]?"
    #mc pauses, looking back
    scene sm1cs-dvh003-26 mc-dvh-pause3_c2 with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    dvh "I have decided to give you another audition."
    #mc is elated - talking
    scene sm1cs-dvh003-27 mc-dvh-leave_c2 with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "Really? That's great, Denise. When?"
    #dvh talking again
    scene sm1cs-dvh003-27 mc-dvh-leave_c1 with dissolve
    play voice3 girl34_arrogant_hm3 noloop
    dvh "At a time of my choosing, naturally."
    dvh "Now go. Pester me no longer, my paltry understudy."
    #mc looks grateful
    scene sm1cs-dvh003-28 mc-dvh-leave2_c1 with dissolve
    mct "Yes!"
    play voice2 mc_happy_yay2 noloop
    mc "Thank you, Denise!"
    #dvh flaps a hand back at him and goes back to her desk
    scene sm1cs-dvh003-28 mc-dvh-leave2_c2 with dissolve
    play voice3 girl34_angry_ahem2 noloop
    dvh "{i}Oprotten{/i}. I have work to do."
    #mc walking out of the office
    scene sm1cs-dvh003-29 mc-dvh-leave3_c1 with dissolve
    pause

    $ StoryController.end_scene(DVH_STORY)
    return
