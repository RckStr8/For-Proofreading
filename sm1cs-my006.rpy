label sm1cs_my006_replay:
label sm1cs_my006:

    ## Text melony after 3 DAYS HAVE PASSED

    scene sm1cs-my006-01 mc-enters-my-room-start-scene_c1 with Fade(0.5, 0.5, 0.5)
    play voice2 mc_angry_huh2 noloop
    mct "Wow... this is way fancier than I was expecting..."
    scene sm1cs-my006-02 mct-wow-fancy-didnt-realize-melony-money_c1 with dissolve
    if persistent.is_special:
        mct "I didn't realize Mom had so much money..."
    else:
        mct "I didn't realize Melony had so much money..."
    scene sm1cs-my006-03 my-that-you-mc-yeah-just-me_c1 with dissolve
    play voice3 girl34_hey_scandalized1_muffled noloop
    my "[mcname]? Is that you?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yep! Just me!"
    scene sm1cs-my006-04 my-sorry-be-out-mc-dont-worry_c1 with dissolve
    play voice3 girl34_thinking_eeh2_muffled noloop
    my "Sorry, I'll be right out!"
    play voice2 mc_yes_aga1 noloop
    mc "Don't worry! Take your time!"
    scene sm1cs-my006-05 mc-looking-around-mct-wonder-how-money-doing-well_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    if persistent.is_special:
        mct "Damn, I wonder how much money Mom has..."
    else:
        mct "Damn, I wonder how much money Melony has..."
    mct "She has to be doing pretty well to afford a spot like this-"
    scene sm1cs-my006-06 mc-waiting-offcam-my-calls-him_c1 with dissolve
    play voice3 girl34_thinking_emm1 noloop
    my "[mcname]?"
    scene sm1cs-my006-07 mc-happy-surprised-sees-my_c1 with dissolve
    play voice2 mc_scared_huuuh1 noloop
    pause
    scene sm1cs-my006-08 my-appears-in-room_c1 with dissolve
    pause
    scene sm1cs-my006-09 my-reveal-new-dress_c1 with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    my "[mcname]? You okay?"
    scene sm1cs-my006-10 mc-mouth-gaping-no-words_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Oh, uhh..."
    scene sm1cs-my006-11 my-cat-got-tongue-mc-sorry_c1 with dissolve
    play voice3 girl34_arrogant_huh2 noloop
    my "What, cat got your tongue?"
    play voice2 mc_disappointed_ah2 noloop
    mc "Sorry..."
    scene sm1cs-my006-12 mc-look-great-my-always-charmer_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    if persistent.is_special:
        mc "You look great, Mom."
    else:
        mc "You look amazing, Melony."
    play voice3 girl34_happy_laugh1 noloop
    my "Always the charmer."
    scene sm1cs-my006-13 my-sorry-took-so-long-made-sure-look-best_c1 with dissolve
    play voice3 girl34_thinking_emm2 noloop
    my "I'm sorry it took me so long. I just needed to make sure I looked my best for you."
    scene sm1cs-my006-14 my-should-get-going-not-late-mc-oh-oh-yeah_c1 with dissolve
    play voice3 girl34_hey_simple1 noloop
    my "But we should get going! We don't want to be late for your reservation!"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, oh yeah!"
    scene sm1cs-my006-15 mc-before-we-go_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "But, before we go..."
    scene sm1cs-my006-16 mc-offers-hand-what-gentleman-my-hehe_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What kind of a gentleman would I be, if I didn't offer you my arm."
    play voice3 girl34_happy_laugh2 noloop
    my "Hehehehehehe."
    scene sm1cs-my006-17 my-takes-mc-hand-how-such-gentleman_c1 with dissolve
    play voice3 girl34_surprised_ohmy2 noloop
    if persistent.is_special:
        my "How did I raise such a fine young gentleman?"
    else:
        my "How did you turn into such a fine, young gentleman?"
    scene sm1cs-my006-18 mc-smirking-no-idea_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "No idea."
    scene sm1cs-my006-19 my-heheh-after-you_c1 with dissolve
    play voice3 girl34_happy_laugh3 noloop
    my "Hehehehehe. Well, after you, sir."

    jump sm1cs_my006_restuarant

label sm1cs_my006_restuarant:

    scene sm1cs-my006-20 mc-my-arrive-restaurant_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-my006-21 mc-my-sit-talk-in-booth_c1 with dissolve
    pause
    scene sm1cs-my006-22 mc-ordering-waiter_c1 with dissolve
    pause
    scene sm1cs-my006-23 mc-my-cheering-each-other_c1 with dissolve
    pause
    scene sm1cs-my006-24 my-eating-food_c1 with dissolve
    pause
    scene sm1cs-my006-25 my-mc-staring-loving-mc_c1 with dissolve
    pause
    scene sm1cs-my006-26 mc-my-talking-after-meal_c1 with dissolve
    pause
    scene sm1cs-my006-27 mc-my-leaving-restaurant_c1 with dissolve
    pause

    jump sm1cs_my006_hotel_room

label sm1cs_my006_hotel_room:

    scene sm1cs-my006-28 mc-my-arive-back-hotel-room-night-time_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-my006-29 my-hehe-not-know-hate-prequels-mc-how-not_c1 with dissolve
    play voice3 girl34_happy_laugh4 noloop
    my "Hehehehehe! I never knew you had such strong opinions on the prequels, [mcname]!"
    play voice2 mc_yes_yeah7 noloop
    mc "How can you not! They're terrible!"
    scene sm1cs-my006-30 my-hehehe_c1 with dissolve
    play voice3 girl34_happy_laugh5 noloop
    my "Hehehehehehe!"
    scene sm1cs-my006-30 my-say-thought-numbers-mc-correct-numbers_c1 with dissolve
    play voice3 girl34_disappointed_eeh3 noloop
    my "I will say though, my ranking from best to worse is Episode 5-4-6-3-1-2."
    play voice2 mc_arrogant_heh1 noloop
    mc "Isn't that the only right way to rank them?"
    scene sm1cs-my006-31 my-laughs-again_c1 with dissolve
    play voice3 girl34_happy_laugh6 noloop
    my "Hehehehehe!"
    scene sm1cs-my006-32 my-looks-horny-this-been-wonderful-night_c1 with dissolve
    play voice3 girl34_hey_simple4 noloop
    my "This has been a wonderful night, [mcname]."
    scene sm1cs-my006-33 mc-really-enjoyed-date-my-so-was-date_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "It has!"
    if persistent.is_special:
        mc "I really enjoyed our date tonight, Mom."
    else:
        mc "I really enjoyed our date tonight, Melony."
    play voice3 girl34_disappointed_oof1 noloop
    my "Oh, so it was a date!"
    scene sm1cs-my006-34 mc-nervous-not-sure-what-say_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "I-"
    scene sm1cs-my006-35 my-just-jerking-you-mc-still-no-words_c1 with dissolve
    play voice3 girl34_happy_relief4 noloop
    my "I'm just jerking your chain, [mcname]. I had a lovely time too."
    my "I..."
    scene sm1cs-my006-36 mc-eyebrows-raised-yeah_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1cs-my006-37 my-looks-through-window-want-say-thanks-taking-out-dates_c1 with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    my "I want to say 'thank you'. Thank you for talking to treating me so well after how I acted when I first came to Crowning."
    my "Spending time with you... well it's been a joy. And each time you make me laugh. {w}I..."
    scene sm1cs-my006-38 my-silent-mc-you_c1 with dissolve
    my "..."
    play voice2 mc_thinking_hm noloop
    mc "You?"
    scene sm1cs-my006-39 my-i-oh-fuck-it_c1 with dissolve
    play voice3 girl34_happy_relief1 noloop
    my "I..."
    my "Oh, fuck it."
    scene sm1cs-my006-40 my-lunges-in-mc-arms_c1 with dissolve
    play voice3 girl13_sex_closedmoan1 noloop
    play voice2 mc_pain_mff2 noloop
    play sound mc_kiss1
    pause
    scene sm1cs-my006-41 my-mc-kiss_c1 with dissolve
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-my006-42 mc-my-keep-making-out_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    play sound mc_kiss2
    play voice3 girl13_sex_closedmoan2 noloop
    pause
    scene sm1cs-my006-43 mc-my-break-mc-starts-speaking-my-shush_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.8
    mc "M-"
    play voice3 stacy_shhh noloop
    my "Shhh, don't say anything [mcname]. Don't let me think about what I'm doing too hard."
    scene sm1cs-my006-44 my-been-so-good-me-treated-me-good_c1 with dissolve
    play voice3 girl34_angry_breath1 noloop
    my "You have been incredible to me. You've ignited something inside me that I feared I had lost."
    scene sm1cs-my006-45 my-want-this-please-shut-up_c1 with dissolve
    play voice3 girl34_disappointed_mmf4 noloop
    my "And I want this. Right now, I want {i}this{/i}. I want {i}you{/i}."
    my "Unless...{w} You don't feel the same way."
    scene sm1cs-my006-46 mc-smiles-agrees-okay_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I do. I want you too."
    scene sm1cs-my006-47 mc-my-keep-making-out_c1 with dissolve
    play voice3 girl13_sex_closedmoan3 noloop
    play voice2 mc_pain_mff1 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-my006-48 my-puts-hands-pants-mc-wait-what-my-what-said-shut-up_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, what are you-"
    if persistent.is_special:
        my "Shhh. Leave everything to Mommy, my dear."
    else:
        my "Leave it to me, [mcname]"
    scene sm1cs-my006-49 mc-yep-sorry-my-good-boy_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.0
    mc "Yep. Sorry."
    play voice3 girl34_yes_ugu2 noloop
    my "Good boy."
    scene sm1cs-my006-50 my-takes-mc-pants-off_c1 with dissolve
    pause
    scene sm1cs-my006-51 mc-naked-my-what-good-boy-gets-mc-what_c1 with dissolve
    play voice3 girl34_arrogant_ha1 noloop
    my "And do you know what good boys get?"
    play voice2 mc_surprised_what7 noloop
    mc "What?"
    scene sm1cs-my006-52 my-takes-off-clothes-a-treat_c1 with dissolve
    play voice3 girl13_sex_closedmoan4 noloop
    my "A treat."
    scene sm1cs-my006-53 my-kneels-front-mc_c1 with dissolve
    pause
    scene sm1cs-my006-54 my-mm-looks-amazing_c1 with dissolve
    play voice3 girl34_happy_mmm3 noloop
    my "Mmmm... it looks... amazing."
    scene sm1cs-my006-55 my-cant-remember-last-time-feels-warm_c1 with dissolve
    play voice3 girl34_disappointed_mmf2 noloop
    my "I can't even remember the last time I had a cock in my hands..."
    my "It feels so warm... {i}so good...{/i}"
    scene sm1cs-my006-56 my-such-wonderful-cock-no-words_c1 with dissolve
    play voisex3 girl34_sex_sucking_soft
    play voisex4 girl34_sex_closedmoan2 noloop
    play voisex2 mc_sex_openmoans2
    my "Such a wonderful, hard cock..."
    my "I... I..."
    scene sm1cs-my006-57 my-takes-mc-cock_c1 with dissolve
    pause
    scene sm1cs-my006-58 my-gives-mc-blowjob-anim_c1 with dissolve
    pause
    scene sm1cs-my006-59 bj-alt-angle-mc-holyshit-my-glick_c2 with dissolve
    play voisex3 girl34_sex_sucking_deep
    play voisex2 mc_sex_openmoans1
    mc "Holy shit!"
    my "Gllck, gllck, gllllck!"
    mc "Fuuuuck!"
    scene sm1cs-my006-60 bj-alt-angle-mc-that-incredible-melony-sucking-cock_c3 with dissolve
    mc "That's - ngggg - you're incredible!"
    if persistent.is_special:
        mc "Holy shit, Mom is sucking my cock!"
    else:
        mc "Holy shit, Melony is sucking my cock!"
    mct "She's really going for it!"
    scene sm1cs-my006-61 bj-alt-angle-mct-stacy-never-believe-this_c4 with dissolve
    mct "I don't believe it!"
    scene sm1cs-my006-62 bj-alt-angle-my-glick-glick-mc-cock-in-heaven_c5 with dissolve
    my "Gllck, gglllck, glllck, glllck, gllck!"
    mct "Fuck... my cock is in heaven. Oh my Goooood!"
    mc "Oh, this feels so goooood!"
    scene sm1cs-my006-63 bj-alt-angle-my-sucking-sound-mc-oh-shit-tongue_c6 with dissolve
    my "Glck, glck, gllllck!"
    if persistent.is_epcial:
        mc "Holy shit, Mom. I-I– ngggghhhh!"
    else:
        mc "Holy shit, Melony. I-I- nggggghhhhhh!"
    mc "Oh, what the - your tongue - shiiiiiit!"
    mc "Ngggghhhh - oh yeah, shit - that feels sooooooo good!"
    scene sm1cs-my006-64 bj-alt-angle-mc-fuck-shit-fuck-my-intense-sucking_c7 with dissolve
    mc "Oh fuck, oh fuuuuuck-!"
    my "Gllllck, gllck, glllcccccckkkk!"
    mc "Shit, shit!"
    play voisex3 girl34_arrogant_hm1 noloop
    stop voisex2 fadeout 1.0
    scene sm1cs-my006-65 my-stops-sucking-mc-cock_c1 with dissolve
    pause
    scene sm1cs-my006-66 my-cant-let-finish-mc-oh-yeah_c1 with dissolve
    play voisex3 girl34_arrogant_ha3 noloop
    my "I can't let you finish yet, [mcname]."
    play voisex2 mc_surprised_oh1 noloop
    mc "Oh yeah?"
    my "Mmhmmm..."
    scene sm1cs-my006-67 my-mmmhm-mc-why-that_c1 with dissolve
    play voisex2 mc_surprised_why3 noloop
    mc "And why's that?"
    play voisex3 girl34_thinking_emm3 noloop
    my "Because..."
    scene sm1cs-my006-68 my-takes-panties-off-because_c1 with dissolve
    play voisex3 girl34_happy_mmm1 noloop
    my "Because I want you - hell, I {i}need{/i} you."
    scene sm1cs-my006-69 mc-happy-shock-starring-my_c1 with dissolve
    pause
    scene sm1cs-my006-70 my-naked-because-want-need-_c1 with dissolve
    play voisex3 girl34_happy_relief2 noloop
    my "I need you to fuck me...{w} I need to feel your cock inside of me..."
    scene sm1cs-my006-71 my-need-fuck-me-please-need-you_c1 with dissolve
    play voisex3 girl34_pain_ergh noloop
    if persistent.is_special:
        my "Please, baby. I need it - I need {i}you{/i}."
    else:
        my "Please, [mcname]. I need it - I need {i}you{/i}."
    scene sm1cs-my006-72 mc-how-say-no-you-my-always-wild-child_c1 with dissolve
    play voisex2 mc_disappointed_off2 noloop
    if persistent.is_special:
        mc "How can I say no to you, Mom?"
    else:
        mc "How can I say no to you, Melony?"
    play voisex3 girl34_arrogant_pff noloop
    my "I don't know, you were always a wild child, [mcname]."
    scene sm1cs-my006-73 mc-smirking-not-that-wild_c1 with dissolve
    play voisex2 mc_thinking_hmm1 noloop
    mc "You think I will ignore you? Looking like this?"
    scene sm1cs-my006-74 my-god-hope-not-thinking-this-since-bikini_c1 with dissolve
    play voisex3 girl34_sex_closedmoan4 noloop
    my "God, I hope not.{w} I've been thinking about this since the bikini competition..."
    scene sm1cs-my006-75 my-everynight-picture-right-after-date_c1 with dissolve
    play voisex3 girl34_sex_closedmoan5 noloop
    my "But that date night...{w} I knew I couldn't hold back any longer."
    scene sm1cs-my006-76 my-you-your-hard-cock_c1 with dissolve
    play voisex3 girl34_angry_breath2 noloop
    my "You and your hard cock..."
    scene sm1cs-my006-77 mc-cock-top-my-pussy_c1 with dissolve
    my "About to enter me..."
    my "Am I dreaming? Pinch me."
    scene sm1cs-my006-78 mc-pinches-nipple-like-that-my-moans-mm_c1 with dissolve
    play voisex2 mc_arrogant_heh2 noloop
    play voisex3 girl34_disappointed_mmf2 noloop
    mc "Like this?"
    my "Mmmmmmm!"
    my "Bad boy..."
    scene sm1cs-my006-79 mc-think-exactly-supposed-do-it_c1 with dissolve
    play voisex2 mc_happy_hah2 noloop
    mc "I think that's exactly how I was supposed to do it."
    scene sm1cs-my006-80 mc-you-sure-my-does-this-answer-question_c1 with dissolve
    play voisex2 mc_hey_hey2 noloop
    if persistent.is_special:
        mc "Mom... are you sure?"
    else:
        mc "Melony... are you sure?"
    play voisex3 girl13_sex_openmoans_short1 noloop
    scene sm1cs-my006-81-pushes-herself-onto-mc-cock_c1 with hpunch
    my "Does this answer your question?"
    scene sm1cs-my006-82 mc-shit-my-oh-fuck_c1 with dissolve
    play voisex3 girl13_sex_openmoans1
    play voisex2 mc_sex_openmoans3
    mc "Shit-!"
    my "Ohhh - ohhh, fuck!"
    stop voisex3 fadeout 1.0
    scene sm1cs-my006-83 mc-okay-my-yeah-need-minute_c1 with dissolve
    play voisex2 d1s5b_emmm noloop
    if persistent.is_special:
        mc "Mom, are you okay?"
    else:
        mc "Melony, are you okay?"
    play voisex3 girl34_happy_relief3 noloop
    my "Y-yes. I just - nngggghhh - need a minute."
    scene sm1cs-my006-84 my-been-long-mct-can-tell-tight_c1 with dissolve
    play voisex3 girl34_disappointed_eeh4 noloop
    my "It's been - well, a very {i}long{/i} time since I've done this."
    mct "I can tell, Jesus she's so tight..."
    scene sm1cs-my006-85 my-just-moment-adjust-god-cock-feels-great_c1 with dissolve
    play voisex3 girl34_angry_breath1 noloop
    my "I just n-need a moment to adjust..."
    my "God...{w} but your cock feels heavenly, [mcname]..."
    scene sm1cs-my006-86 my-go-slow-mc-hesitant_c1 with dissolve
    play voisex3 girl13_sex_closedmoan6 noloop
    my "O-okay. Go slow. But whatever else happens, I don't want you to stop."
    play voisex2 d1s5_mcthinks noloop volume 1.6
    mc "Are you-"
    scene sm1cs-my006-87 my-just-fuck-me-mc-okay_c1 with dissolve
    play voisex3 girl34_sex_closedmoan1 noloop
    my "Yes. I need you to fuck me. Please."
    play voisex2 mc_angry_huh2 noloop
    if persistent.is_special:
        mc "Okay, Mom."
    else:
        mc "Okay, Melony."
    scene sm1cs-my006-88 mc-fucks-my-slowly-missionary-anim_c1 with dissolve
    play voisex3 girl13_sex_openmoans2 volume 0.8
    play voisex2 mc_sex_openmoans3
    my "Oh fuck!"
    mc "*grunting*"
    my "Nggggh - yes! I just - nggggggh, fuck!"
    scene sm1cs-my006-89 missionary-alt-angle-my-oh-fuck-mc-you_c2 with dissolve
    my "Oh Goooood..."
    my "Goooddddd! Mmmmmppphhh!"
    mc "Shit-"
    scene sm1cs-my006-90 missionary-alt-angle-my-oh-god_c3 with dissolve
    my "Mmmmmmm, [mcname]! Yessss!"
    if persistent.is_special:
        mc "Mom!"
    else:
        mc "Melony!"
    my "This is incredible!"
    my "Mmmmm! Yesssssss!"
    scene sm1cs-my006-91 missionary-alt-angle-my-yes-mc-calls-her_c4 with dissolve
    my "Oh yeah, right there!!!"
    if persistent.is_special:
        mc "Oh, Mom. Your pussy is clamping down on my cock!"
    else:
        mc "God, your pussy is clamped around my cock!"
    mc "This is so good, and you're so wet!"
    scene sm1cs-my006-92 missionary-alt-angle-my-right-there-mc-god-pussy_c5 with dissolve
    my "Oh, I've needed this for so long! Oh, ohhhh!!!"
    my "Mmmmm, just like that, [mcname], oh yes!"
    scene sm1cs-my006-93 missionary-alt-angle-my-needed-this-just-like-that_c6 with dissolve
    my "Oh, your cock feels soooo good inside me - mmmmmm!"
    my "The perfect - mmmmnnnnggg - fit!"
    scene sm1cs-my006-94 missionary-alt-angle-my-cock-so-good-inside_c7 with dissolve
    mc "Fuck - ngggh, it's so tight!"
    mc "Damn - oh, it feels so good! Shit!"
    scene sm1cs-my006-95 missionary-alt-angle-my-please-no-cum-yet_c8 with dissolve
    my "Oh, please don't cum yet, [mcname]. There's - mmmmpphhh - more I want to do!"
    mc "I - nggghhhh - I can try and hold out-!"
    stop voisex2 fadeout 1.0
    scene sm1cs-my006-96 my-need-wait-allow-cum-been-long-since-done-like-this_c1 with dissolve
    play voisex3 girl34_angry_argh3 noloop
    my "[mcname], I need you to wait until I can say you can cum, okay?"
    my "It's been a long time since I've done anything like this, and I..."
    scene sm1cs-my006-97 my-need-more-till-cant-take-can-do_c1 with dissolve
    my "And I need more. I need more of you. I need you to fuck me until I can't take it anymore, okay?"
    my "Can you do that for me?"
    scene sm1cs-my006-98 mc-yes-i-can_c1 with dissolve
    play voisex2 mc_yes_yes1 noloop
    if persistent.is_special:
        mc "I can do that, Mom."
    else:
        mc "I can do that, Melony."
    scene sm1cs-my006-99 my-good-boy-now-up_c1 with dissolve
    play voisex3 girl34_happy_nice1 noloop
    my "Good boy."
    my "Now, up!"
    scene sm1cs-my006-100 mc-wha-my-switching-up_c1 with dissolve
    play voisex2 mc_surprised_what2 noloop
    mc "Wha..."
    play voisex3 girl34_arrogant_ha2 noloop
    my "We're switching it up!"
    scene sm1cs-my006-101 my-mct-goddamn-my-always-loved-doggy_c1 with dissolve
    play voisex2 mc_angry_errr8 noloop
    mct "Goddamn..."
    scene sm1cs-my006-102 my-personally-think-best-way-fucked-mc-i_c1 with dissolve
    play voisex3 girl34_thinking_hmm2 noloop
    my "Because I've always been a fan of doggy style."
    my "I personally think it's the best way to be fucked."
    play voisex2 d3s7_mcemm noloop
    mc "I..."
    scene sm1cs-my006-103 my-cat-got-tongue-pussy-mind-mc-no-words_c1 with dissolve
    play voisex3 girl34_thinking_hmm1 noloop
    my "Hmmm? Cat got your tongue? A little pussy on your mind, [mcname]?"
    play voisex2 d1s5_orgasm noloop
    mc "I... I..."
    scene sm1cs-my006-104 my-wiggle-ass-come-over-mc-alright_c1 with dissolve
    play voisex3 girl34_arrogant_ha4 noloop
    my "Well come over here and get it off your mind, and onto your dick!"
    play voisex2 mc_yes_yeah1 noloop
    mc "All right."
    scene sm1cs-my006-105 my-mm-taking-sweet-time-mc-memory-serves_c1 with dissolve
    play voisex3 girl34_sex_closedmoan3 noloop
    my "Mmmm, taking your sweet time, are you?"
    scene sm1cs-my006-106 mc-maybe-want-tease-bit_c1 with dissolve
    play voisex2 d1s5_mchappy noloop volume 1.6
    mc "If memory serves, wasn't it just you who was begging me to go until you came?"
    mc "Maybe, I want to tease you a little bit?"
    scene sm1cs-my006-107 mc-what-think-about-that-my-think-rather_c1 with dissolve
    play voisex3 girl34_sex_closedmoan6 noloop
    my "Mmmmmm..."
    play voisex2 mc_angry_hm1 noloop
    if persistent.is_special:
        mc "What do you think about that, Mom?"
    else:
        mc "What do you think about that, Melony?"
    my "I think I'd rather-"
    scene sm1cs-my006-108 mc-teases-pussy-what-that-my-mmmrgh_c1 with dissolve
    play voisex2 mc_arrogant_huh2 noloop
    mc "What was that?"
    play voisex3 girl34_angry_breath1 noloop
    my "Mmmrrrgghhhh..."
    scene sm1cs-my006-109 mc-like-feeling-cock-pussy-my-silent_c1 with dissolve
    play voisex2 mc_thinking_mmm7 noloop
    mc "You like the feeling of my cock on your pussy, don't you?"
    my "..."
    scene sm1cs-my006-110 mc-makes-dirty-girl-my-maybe_c1 with dissolve
    play voisex2 mc_thinking_mmm4 noloop
    mc "That makes you a dirty, dirty girl, doesn't it?"
    play voisex3 girl34_yes_questioning7 noloop
    my "Mmmmm... maybe..."
    scene sm1cs-my006-111 mc-smirks-lucky-likes-dirty-girls_c1 with dissolve
    play voisex2 mc_thinking_hmm9 noloop
    mc "Well, fortunately for you..."
    mc "I like dirty, dirty girls."
    play voisex3 girl34_scared_ah7 noloop
    scene sm1cs-my006-112 my-takes-mc-cock_c1 with vpunch
    my "[mcname]-"
    scene sm1cs-my006-113 mc-fucks-my-doggystyle-anim_c1 with dissolve
    play voisex3 girl13_sex_openmoans2 volume 0.8
    play voisex2 mc_sex_openmoans3
    my "Oh, FUCK, [mcname]!"
    if persistent.is_special:
        mc "Shit - your lips are pulling me in, Mom!"
    else:
        mc "Shit - your lips are pulling me in!"

    my "Oh, GOD, fuck!"
    scene sm1cs-my006-114 doggystyle-alt-angle-my-oh-fuck-mc-pussy-clamped_c2 with dissolve
    mc "Shhhii - ngggh - how - fuhh, how do you like that?"
    my "Fuck, FUCK!"
    my "Fuuuuccckkk! Oh, it feels soooo - ngggh - soooo gooooood!"
    scene sm1cs-my006-115 doggystyle-alt-angle-mc-shiit-how-do-that-my-fuck-fuck_c3 with dissolve
    mc "Y-yeah? Tell me how good!"
    my "Ngggh - I love feeling your throbbing cock pound my pussy!"
    my "I l-love - mmmm - the way it slides out of me!"
    scene sm1cs-my006-116 doggystyle-alt-angle-mc-tell-how-good-my-love-cock_c4 with dissolve
    my "I love feeling how it - oh GOD - it twitches every time I moan!"
    my "And I love, {i}love{/i}-"
    my "Fuck, [mcname], you're going to make me cum!"
    scene sm1cs-my006-117 doggystyle-alt-angle-my-love-how-feels_c5 with dissolve
    if persistent.is_special:
        mc "Nggh - w-what do you love, Mom!?"
    else:
        mc "Ngggh - w-what do you love, Melony?"
    my "Oh, I'm so close-"
    mc "That's not an answer!"
    scene sm1cs-my006-118 doggystyle-alt-angle-mc-what-do-love-melony-my-so-close_c6 with dissolve
    my "I - ohhh fuuuuhhhhccckk - I-I-"
    my "I love that it's {i}your{/i} cock, [mcname]!"
    my "Oh, I've wanted you so badly!"
    scene sm1cs-my006-119 doggystyle-alt-angle-my-oh-fuck-love-its-your-cock-wanted-badly_c7 with dissolve
    my "I knew it when you were fondling my tits in my swimsuit!"
    my "And the other night, I could feel your hard, throbbing dick touching my feet!"
    my "I-it made me so wet - fuuuuck - I'm almost there, [mcname]!"
    scene sm1cs-my006-120 doggystyle-alt-angle-my-knew-when-fondling-tits_c8 with dissolve
    mc "Shiiiit - nggggh!"
    my "I felt so dirty rubbing your dick through your pants, but God it felt so goooood!"
    my "And I could feel your eyes devouring me - fuuuuck!"
    scene sm1cs-my006-121 doggystyle-alt-angle-my-about-cum-mc-do-all-over-cock_c9 with dissolve
    my "Oh, God, [mcname]! [mcname]! I'm - I'm-!"
    mc "Do it, cum! Cum all over my cock!"
    my "FuuuUUUUUCCCCK!"
    play voisex3 girl13_sex_orgasming2
    scene sm1cs-my006-122 my-orgasm-face-oh-fuck-fuck-fuck_c1 with vpunch
    my "Oh fuck, oh fuck, ohfuckohfuckohfuck! Fuckity fuuuuuck!"
    stop voisex2 fadeout 1.0
    scene sm1cs-my006-123 my-drops-bed-destroyed-mct-jesus-ass-amazing_c1 with dissolve
    play voisex3 girl13_sex_closedmoan2 noloop
    mct "Jesus..."
    if persistent.is_special:
        mct "Mom's ass is amazing... and her pussy, fucking wow."
    else:
        mct "Melon'y ass is amazing... and her pussy, fucking wow."
    scene sm1cs-my006-124 mct-whole-time-no-idea-lucky-man_c1 with dissolve
    play voisex2 mc_thinking_mmm3 noloop
    mct "This whole time... I had no idea."
    mct "But God am I a lucky man..."
    scene sm1cs-my006-125 my-calls-mc-doesnt-feel-you-came_c1 with dissolve
    play voisex3 girl34_thinking_emm5 noloop
    my "Mmmm... [mcname]?"
    my "Mmmm, it doesn't feel like you came?"
    scene sm1cs-my006-126 mc-instructed-no-cum-my-did-well_c1 with dissolve
    play voisex2 mc_no_nope1 noloop
    mc "Nope, not yet. I was given very clear instructions."
    play voisex3 girl34_yes_ugu1 noloop
    my "Mmmhmmm, and you have followed them very well."
    scene sm1cs-my006-127 my-lay-down-bed_c1 with dissolve
    play voisex3 girl34_arrogant_huh1 noloop
    my "Why don't you lay down on the bed?"
    scene sm1cs-my006-128 mc-laying-like-idea-my-thought-might_c1 with dissolve
    play voisex2 mc_yes_yes4 noloop
    mc "I like the sound of that."
    play voisex3 girl34_arrogant_aga noloop
    my "I thought you might!"
    scene sm1cs-my006-129 mc-lays-position-my-touches-cock_c1 with dissolve
    pause
    scene sm1cs-my006-130 my-why-not-let-help-mc-yes-maam_c1 with dissolve
    play voisex3 girl34_sex_closedmoan5 noloop
    if persistent.is_special:
        my "Mmmm, why don't you let Mom help you cum, hmmm?"
    else:
        my "Why don't you let me help you cum, hmmm?"
    play voisex2 mc_thinking_mmm6 noloop
    mc "Mmmm, yes ma'am!"
    scene sm1cs-my006-131 my-reaches-mc-cock-feel-good-hand_c1 with dissolve
    play voisex3 girl34_sex_closedmoan4 noloop
    my "Mmmm... it just feels so good in my hand..."
    scene sm1cs-my006-132 my-guides-dick-pussy-but-feel-better_c1 with dissolve
    my "But this will feel even better-"
    scene sm1cs-my006-133 my-sits-mc-cock_c1 with dissolve
    play voisex3 girl34_pain_ah1 noloop
    my "Oh, fuck!"
    scene sm1cs-my006-134 my-lowers-on-dick-mc-you-okay-my-mm-better_c1 with dissolve
    play voisex2 mc_angry_huh1 noloop
    mc "Are you okay!?"
    scene sm1cs-my006-135 my-just-sensitive-all-my-made-cum-hard_c1 with dissolve
    play voisex3 girl13_sex_closedmoan1 noloop
    my "Mmmhmmm! B-better than, okay!"
    my "Just... a little sensitive is all."
    my "You made me cum so hard... my pussy is still tingling."
    scene sm1cs-my006-136 mc-not-gonna-lie-my-thought-might-be_c1 with dissolve
    play voisex2 mc_arrogant_heh3 noloop
    mc "Not going to lie, I'm a little happy to hear that."
    scene sm1cs-my006-137 my-but-told-help-not-finished_c1 with dissolve
    play voisex3 girl34_happy_mmm2 noloop
    my "Mmm, thought you might be."
    my "But, I told you I'd help you, so I'm not quite finished yet..."
    scene sm1cs-my006-138 my-rides-mc-squatting-anim_c1 with dissolve
    play voisex3 girl13_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    my "Ohhh fuuuuuuuck!"
    mc "Shit-!"
    mc "Fuck this feels sooo gooood!"
    my "Fuuhhh - it does! Nggghhh! Mmmm - so goood!"
    my "G-god, I already - mmmmnnnggg - already feel like cumming again!"
    scene sm1cs-my006-139 cowgirl-alt-angle-my-oh-fuck-mc-shit_c2 with dissolve
    mc "Oh I definitely - nggghhh - won't last much longer!"
    my "Oooo, ooooooo, ooouuuahhhh! I - mmmrrrggghhh - hope so!"
    my "I'm not sure - nngghhhh, mmmmmm - how much I have left in me-!"
    scene sm1cs-my006-140 cowgirl-alt-angle-mc-fuck-so-good-my-already-like-cumming_c3 with dissolve
    my "Fuck! Oh, shit!"
    if persistent.is_special:
        mc "Mom!"
    else:
        mc "Melony!"
    my "Just a little - mmmmmm - little orgasm, but another b-big one-!"
    scene sm1cs-my006-141 cowgirl-alt-angle-mc-oh-deff-my-moaning_c4 with dissolve
    my "Oh God, mmmmm-!"
    mc "Shit- ngggh!"
    if persistent.is_special:
        mc "Mom, I'm getting close!"
    else:
        mc "Melony, I'm getting close!"
    my "M-me too!"
    my "Let's see if I can't help us both out..."
    scene sm1cs-my006-142 cowgirl-alt-angle-my-oh-shit-mc-melony-my-just-little-orgasm_c5 with dissolve
    play voisex3 girl13_sex_openmoans2 volume 0.8
    play voisex2 mc_sex_openmoans3
    my "Fuck, fuck, quick it, fuck, faster! Mmmmmm!"
    mc "Shhhiiiitttt!!! Ngghhhh, ouuuahhhh!"
    scene sm1cs-my006-143 cowgirl-alt-angle-my-oh-god-mm-mc-getting-close_c6 with dissolve
    my "Oh, oh, fuuck, fuck, I can feel, fuck, your cock starting to twitch!"
    mc "I'm sooo - fuuuck! I'm going to-!"
    my "Yes, [mcname], yes!"
    scene sm1cs-my006-144 cowgirl-alt-angle-my-fuck-fuck-faster_c7 with dissolve
    my "I want you to fill my pussy up! I want you to cum inside me!"
    my "I want your sperm to be dripping out of my pussy! Yes, YES!"
    scene sm1cs-my006-145 cowgirl-alt-angle-my-want-fill-pussy_c8 with dissolve
    if persistent.is_special:
        mc "Fuuuhhh - Mom, I'm going to cum!"
        my "Me too, son, me too! Cum, cum inside meeee!"
    else:
        mc "Fuuhhhh - Melony, I'm going to cum!"
        my "Yes, yes, fuck, fuck! Fill me uuppppp!"
    play voisex3 girl13_sex_orgasming1
    play voisex2 mc_sex_orgasm4 noloop
    scene sm1cs-my006-146 my-orgasm-again-fuckfuckfuck-mc-will-cum_c1 with hpunch
    my "Fuckfuckfuckfuckfuckfuckfuck!"
    mc "I'm cumming!"
    play voisex3 girl13_sex_orgasm1 noloop
    scene sm1cs-my006-147 my-drops-ballsdeep_c1 with vpunch
    my "Ohfuuuuuuuuuccccckkkkkkkkkkk!!!"
    scene sm1cs-my006-148 my-ahegao-can-feel-coc-spurting-inside_c1 with dissolve
    my "Oh, I can feel - oh I can feel your cock spurting inside me - ohfuck!"
    scene sm1cs-my006-149 my-collapse-top-mc-my-oh-shit-oh-shit_c1 with dissolve
    play voisex3 girl13_angry_breath noloop
    my "Oh shit... oh shit..."
    scene sm1cs-my006-150 mc-cock-still-inside-creampie_c1 with dissolve
    my "Fuck... fuck... fuck..."
    play voisex2 mc_yes_yeah7 noloop
    mc "Yeah?"
    play voisex3 girl34_happy_relief5 noloop
    my "Mmhmmm... that was... good..."
    scene sm1cs-my006-151 my-best-sex-ever-mc-really_c1 with dissolve
    play voice3 girl34_thinking_emm4 noloop
    my "Best sex I've ever had..."
    play voice2 mc_angry_really noloop
    mc "Really?"
    scene sm1cs-my006-152 my-why-lie-mc-happy-hear-good_c1 with dissolve
    play voice3 girl34_yes_happy2 noloop
    if persistent.is_special:
        my "Why would I lie to you, son?"
    else:
        my "Why would I lie to you?"
    play voice2 mc_surprised_wow4 noloop
    mc "I'm just happy to hear it was good."
    scene sm1cs-my006-153 my-oh-better-good-mc-well_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, so much better than good..."
    play voice2 d2s9_confused noloop volume 1.6
    mc "Well-"
    scene sm1cs-my006-154 my-no-move-yet-mc-confused-okay_c1 with dissolve
    play voice3 girl34_no_nouh1 noloop
    my "Don't move, yet."
    play voice2 mc_yes_okay1 noloop
    mc "Okay?"
    scene sm1cs-my006-155 my-sorry-uuhm-mc-what_c1 with dissolve
    play voice3 girl34_happy_relief1 noloop
    my "Sorry... I, uhm..."
    play voice2 mc_thinking_hmm6 noloop
    mc "What?"
    scene sm1cs-my006-156 my-oh-nothing-mc-no-reason-bashful-now_c1 with dissolve
    play voice3 girl34_disappointed_mmf1 noloop
    my "Oh, it's... nothing..."
    play voice2 mc_no_nah1 noloop
    if persistent.is_special:
        mc "There's no reason to be bashful now, Mom. I already fucked your brains out."
    else:
        mc "There's no reason to be bashful now, Melony. I already fucked your brains out."
    scene sm1cs-my006-157 my-good-point-no-move-yet-love-cock-inside_c1 with dissolve
    play voice3 girl34_happy_relief3 noloop
    my "You've got a good point..."
    my "I don't want you to move yet, because I love feeling your cock still twitching in my pussy."
    scene sm1cs-my006-158 mct-jesus-melony-perv-my-cant-fault-girl_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    if persistent.is_special:
        mct "Damn! Mom's kind of a perv! Jesus..."
    else:
        mct "Damn, Melony's kind of a perv! Wow..."
    play voice3 girl34_hey_happy noloop
    my "Can't fault a girl for wanting to enjoy this a little longer."
    scene sm1cs-my006-159 mc-no-guess-not-my-mmm_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "No, I guess I can't."
    play voice3 girl34_sex_closedmoan4 noloop
    my "Mmmmm..."
    scene sm1cs-my006-160 my-all-good-thing-end_c1 with dissolve
    play voice3 girl34_disappointed_eeh4 noloop
    my "But... all good things must come to an end."
    scene sm1cs-my006-161 my-gets-off-mc-cock-moans_c1 with dissolve
    play voice3 girl34_disappointed_mmf3 noloop
    my "Nnnnnnnngggghhhh..."
    scene sm1cs-my006-162 mc-my-laying-in-bed_c1 with dissolve
    pause
    scene sm1cs-my006-163 my-well-mc-now-what_c1 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Well..."
    play voice3 girl34_thinking_mmm noloop
    my "Well?"
    mc "Now what?"
    scene sm1cs-my006-164 my-what-mean-mc-just-had-sex_c1 with dissolve
    play voice3 girl34_thinking_hmm5 noloop
    my "What do you mean?"
    play voice2 mc_thinking_emm1 noloop
    mc "Well... we just had sex, and-"
    scene sm1cs-my006-165 my-anyone-said-rude-talk-about-mc-uhh_c1 with dissolve
    play voice3 girl34_angry_ahem2 noloop
    my "[mcname], has anyone ever said it's rude to talk about this kind of stuff, right after you've had some of the best sex of your life?"
    play voice2 mc_disappointed_ehh3 noloop
    mc "Uhhhh..."
    scene sm1cs-my006-166 my-cause-it-is-why-not-cuddle_c1 with dissolve
    play voice3 girl34_hey_simple3 noloop
    my "Because it is. Instead of thinking about all of that, and whatever weird lines and boundaries we've just crossed."
    my "Why don't we cuddle, and enjoy this moment together?"
    scene sm1cs-my006-167 mc-sounds-good-me_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "That sounds good to me."
    scene sm1cs-my006-168 my-god-really-go-cigarette-mc-you-smoke_c1 with dissolve
    play voice3 girl34_happy_phew2 noloop
    my "God... I could really go for a cigarette right now."
    play voice2 mc_surprised_uh3 noloop
    mc "You smoke!?"
    scene sm1cs-my006-169 my-not-anymore_c1 with dissolve
    play voice3 girl34_no_nonono3 noloop
    my "Not anymore."
    scene sm1cs-my006-170 mct-still-lot-know-about-melony-smoking-freak-sheets_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    if persistent.is_special:
        mct "Wow... there's still a lot about Mom I don't know..."
    else:
        mct "Wow... there's still a lot about Melony I don't know..."
    mct "She smokes. And she's a freak in the sheets..."
    scene sm1cs-my006-171 mc-closes-eyes-mct-least-got-plenty-time-now_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "At least I've got plenty of time to get to know her, now..."
    scene sm1cs-my006-172 mc-my-fall-asleep_c1 with dissolve
    pause

    jump sm1cs_my006_next_morning

label sm1cs_my006_next_morning:

    scene black
    show screen scene_transition(_("Next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs-my006-173 transition-next-day_c1
    play voice2 d7s6_snoring fadein 1.5
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-my006-174 mc-opens-eyes-slowly_c1 with dissolve
    play voice2 d7s6_awake noloop
    pause
    scene sm1cs-my006-175 mc-wide-awak-shit-fell-asleep-here_c1 with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mct "Shit... must have dozed off for a sec-"
    mct "Oh shit! I fell asleep here!"
    scene sm1cs-my006-176 mc-sits-up-shit-not-supposed-my-mmm_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Shit, I wasn't supposed to-"
    play voice3 girl34_disappointed_mmf4 noloop
    my "Mmmmm..."
    scene sm1cs-my006-177 my-good-morning-mc-oh-uhm-morning_c1 with dissolve
    play voice3 girl34_hey_laughing noloop
    my "Mmmm, good morning, [mcname]."
    play voice2 d2s12_emmm noloop
    if persistent.is_special:
        mc "Oh, uhm, morning, Mom."
    else:
        mc "Oh, uhm, morning, Melony."
    scene sm1cs-my006-178 my-what-tizzy-early-morning_c1 with dissolve
    play voice3 girl34_arrogant_huh3 noloop
    my "What's got you all in a tizzy so early in the morning?"
    scene sm1cs-my006-179 mc-not-mean-fall-asleep-here-my-it-fine-not-like-anyone-miss-you-bed_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I, uhh, just didn't mean to fall asleep here, is all."
    play voice3 girl34_happy_relief4 noloop
    my "It's fine, it's not like you have anyone whose going to miss you in bed."
    scene sm1cs-my006-180 mct-if-only-knew-mc-yeah-good-point_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mct "If only she knew..."
    mc "Uhm, yeah. Good point, but, uhm..."
    scene sm1cs-my006-181 mc-stands-up-have-important-business-my-call-sick_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I actually have a super important business, erm, meeting thing today, and I need to-"
    scene sm1cs-my006-182 my-crawl-back-bed-mc-gulp_c1 with dissolve
    play voice3 girl34_hey_scandalized2 noloop
    my "Just call in sick."
    my "Crawl back into bed. It'll be fuuuuun."
    scene sm1cs-my006-183 mct-jesus-ass-better-breakfast_c1 with dissolve
    "*GULP*"
    mct "Jesus... her ass looks better than breakfast..."
    scene sm1cs-my006-184 mc-akward-really-wish-could-if-could-believe-would_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I really wish I could, but this business meeting is super important."
    mc "If I could skip it, believe me, I would."
    scene sm1cs-my006-185 my-sits-up-nothing-can-do-convince-_c1 with dissolve
    play voice3 girl34_disappointed_eh noloop
    my "Are you sure there's nothing I can do to convince you?"
    scene sm1cs-my006-186 my-squishes-tits-let-slide-cock-fuck-tits-mc-again-gulps_c1 with dissolve
    play voice3 girl34_happy_relief3 noloop
    if persistent.is_special:
        my "Don't you want to slide your big, hard cock between Mommy's soft, warm tits and fuck them until you explode?"
    else:
        my "I'll let you slide your big, beautiful cock between my soft, warm tits and fuck them until you cover me in your cum."
    "*GULP*"
    scene sm1cs-my006-187 mc-not-know-how-badly-believe-would-get-meeting_c1 with dissolve
    play voice2 mc_angry_errr3 noloop
    mc "You have {i}no idea{/i} how badly I want to do that."
    if persistent.is_special:
        mc "Believe me, Mom. If I could get out of this meeting, I would."
    else:
        mc "Believe me, Melony, if there was any way I could get out of this business meeting I would."
    scene sm1cs-my006-188 mc-pants-on-but-have-go_c1 with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "There's nothing I'd rather do right now than pin you to the bed and ravage you."
    mc "But... I have to go."
    scene sm1cs-my006-189 my-pouty-okay-calls-mc_c1 with dissolve
    play voice3 girl34_yes_aga6 noloop
    my "Okay..."
    my "[mcname]?"
    scene sm1cs-my006-190 mc-yeah-my-not-ghosting-right_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    play voice3 girl34_thinking_emm1 noloop
    my "You're not... {w}regretting what we did, are you?"
    scene sm1cs-my006-191 mc-what-ofc-not_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What! No!"
    scene sm1cs-my006-192 mc-sits-next-my-edge-bed_c1 with dissolve
    pause
    scene sm1cs-my006-193 mc-last-night-incredible-still-much-not-know-about_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Last night was incredible. And I can't wait to do it again. I want to be even closer to you."
    mc "There's still so much I don't know about you, even though you've been around, my whole life."
    scene sm1cs-my006-194 mc-love-getting-know-woman-loved-making-love_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "And I mean... getting to fuck you, I mean that was like finally seeing the light for the first time."
    scene sm1cs-my006-195 my-oh-silver-tongue-devil_c1 with dissolve
    play voice3 girl34_arrogant_laugh1 noloop
    my "Mmmm. My little charmer."
    scene sm1cs-my006-196 mc-my-kiss_c1 with dissolve
    play voice3 girl34_sex_closedmoan3 noloop
    play voice2 d1s1_mmm noloop volume 1.4
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-my006-197 mc-but-gotta-go-my-fiine_c1 with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "But, I have to go."
    play voice3 girl34_angry_dough noloop
    my "Fiiiiine."
    scene sm1cs-my006-198 mc-love-you-my-love-you-too_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    if persistent.is_special:
        mc "I love you, Mom."
    else:
        mc "I love you, Melony."
    play voice3 girl34_happy_mmm2 noloop
    my "I love you, too."
    scene sm1cs-my006-199 mc-walks-out-room_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "We'll schedule another date soon, promise!"
    play voice3 girl34_happy_yay2 noloop
    my "We better!"
    $ renpy.end_replay()

    jump sm1cs_my006_at_studio

label sm1cs_my006_at_studio:

    scene black
    show screen scene_transition(_("Back at the studio"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs-my006-200 mc-back-at-studio_c1
    with Fade(0.5, 0.5, 0.5)
    $ SMGallery.unlock_gallery_slot("replay", "sm1cs_my006")
    pause
    scene sm1cs-my006-201 mct-okay-stacy-not-notice-mc-maybe-gaming_c1 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mct "Okay... maybe Stacy didn't notice I was gone all night."
    mct "Maybe she was working or gaming... maybe she assumed I got stuck at Orbix or the theater..."
    scene sm1cs-my006-202 mc-no-sign-her-sy-offcam-calls-mc_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "No sign of her, I think-"
    play voice4 stacy_hey_angry1 noloop
    sy "[mcname]!"
    scene sm1cs-my006-203 mc-flinch-realize-caught_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    pause
    scene sm1cs-my006-204 sy-top-stairs-where-been-mc-oh-uhm_c1 with dissolve
    play voice4 stacy_surprised_huh4 noloop
    sy "Where have you been!?"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, uhm, I was..."
    scene sm1cs-my006-205 sy-going-downstairs-still-wearing-same-clothes_c1 with dissolve
    play voice4 stacy_arrogant_huh4 noloop
    sy "Still wearing the same clothes from last night-"
    scene sm1cs-my006-206 sy-bedhead-diff-bed_c1 with dissolve
    play voice4 stacy_arrogant_hmm2 noloop
    sy "-with bed head, but you didn't sleep in our bed-"
    scene sm1cs-my006-207 sy-i-here-sick-all-morning-mc-stacy_c1 with dissolve
    play voice4 stacy_angry noloop
    sy "-and I have been worried sick all morning!"
    play voice2 mc_disappointed_ehh5 noloop
    mc "Stacy, I-"
    scene sm1cs-my006-208 sy-worried-sick-take-all-day-fucked-melony_c1 with dissolve
    play voice4 stacy_surprised_huh5 noloop
    if persistent.is_special:
        sy "Worried sick it was going to take all day for you to come home and tell what fucking Mom was like!"
    else:
        sy "Worried sick it was going to take all day for you to come home and tell what fucking Melony was like!"
    scene sm1cs-my006-209 mc-confused-what_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait..."
    scene sm1cs-my006-210 sy-smirk-did-think-mad-you_c1 with dissolve
    play voice4 stacy_happy_laugh4 noloop
    sy "What, did you think I was actually mad at you?"
    play voice2 mc_yes_yes8 noloop
    mc "I mean, maybe a little bit."
    play voice4 stacy_angry_argh1 noloop
    sy "I'm only mad that you haven't already starting telling me {b}everything{/b}!"
    scene sm1cs-my006-211 sy-gets-close-tell-she-freak-mc-aight-calm-down_c1 with dissolve
    play voice4 stacy_arrogant_ha2 noloop
    sy "So tell me! Is she a freak? What positions did you do? Are her tits super mesmerizing to watch bounce!? Tell, tell, tell!"
    play voice2 mc_happy_laugh3 noloop
    mc "All right, all right, just calm down!"
    scene sm1cs-my006-212 sy-will-calm-when-tell-mc-can-tell-later-exhausted_c1 with dissolve
    play voice4 stacy_no_angry1 noloop
    sy "I will once you tell me!"
    play voice2 mc_thinking_hmm5 noloop
    mc "Can I tell you about it later? I'm exhausted, Stacy."
    scene sm1cs-my006-213 sy-but-but-mc-promise-tell-everything_c1 with dissolve
    play voice4 stacy_pain_mmm1 noloop
    sy "But, but-!"
    play voice2 mc_thinking_hmm3 noloop
    mc "I pinky swear I'll tell you everything. But, as you can imagine, I had a long night-"
    scene sm1cs-my006-214 sy-hell-yeah-did-mc-just-want-shower_c1 with dissolve
    play voice4 stacy_angryhuh noloop
    sy "Hell yeah you did!"
    play voice2 mc_thinking_hm noloop
    mc "-and I just want to take shower and get a cup of coffee, okay?"
    mc "And maybe process last night a little bit."
    scene sm1cs-my006-215 sy-pouty-fiiine-mc-mothers-daughter_c1 with dissolve
    play voice4 stacy_yes_fine4 noloop
    sy "Fiiiiiiine."
    play voice2 mc_happy_hah1 noloop
    if persistent.is_special:
        mc "You really are your mother's daughter."
    else:
        mc "You and Melony sure do have a lot in common."
    sy "Oh yeah? And why's that?"
    scene sm1cs-my006-216 mc-she-did-same-thing-sy-wanted-more-mc-haha-later-sracy_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "She did literally that exact same thing to me when I was leaving this morning."
    play voice4 stacy_surprised_oh1 noloop
    sy "Oh, so she wanted {i}more?{/i}"
    play voice2 mc_happy_laugh2 noloop
    mc "Hahahaha - later, Stacy."
    scene sm1cs-my006-217 sy-pouting-fiine-mct-great-now-have-do-this-stereo_c1 with dissolve
    play voice4 stacy_pain_mmm2 noloop
    sy "Fiiiiiiiiine!"
    scene sm1cs-my006-218 mc-top-stairs-smirking-least-sex-fucking-awesome-end-scene_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Great, I should have known I'd have to tell Stacy every little thing that happened last night."
    mct "But, at least the sex is pretty fucking awesome!"

    jump sm1cs_my006_exit_to_studio

label sm1cs_my006_exit_to_studio:

    if vn_mode:
        $ StoryController.end_scene(MY_STORY)
        return

    $ gt.add((8 + (24 - gt.curr_hour)), 0, 0)
    $ player.sleep_common_function()
    $ player.progress_storyline(MY_STORY)
    return
