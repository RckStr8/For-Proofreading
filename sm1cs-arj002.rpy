label sm1cs_arj002:

    ###quest log - "Text AmRose in the afternoon"
    ###the end of the text conversation leads right into the scene

    default arj_mcname = _("Master")

    # AmRose walks into the studio apartment. arj is inside - near the door, mc waves to greet her. mc takling - fade in
    scene sm1cs-arj002-01 mc-arj-enter-wave with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Hey there, long time no see! Come in, make yourself at home."
    play voice4 amrose_hey_active1 noloop
    arj "Hi, [mcname]."
    #arj looking at sy - stacy is not being the best at being subtle
    scene sm1cs-arj002-02 mc-arj-notices-stacy with dissolve
    play voice4 amrose_thinking_oh2 noloop
    arj "And Stacy. [mcname] didn't mention you'd be here too."
    scene sm1cs-arj002-03 mc-arj-stacy-responds with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "I do live here, you know."
    play voice4 amrose_yes_yeah2 noloop
    arj "Right..."
    #sy giggling
    scene sm1cs-arj002-04 mc-arj-sy-go-in-for-hug with dissolve
    play voice3 stacy_laugh noloop
    sy "Sorry, AmRose. We've been so busy with work, I forgot my manners."
    #sy comes in for a hug - arj is not sure about this
    scene sm1cs-arj002-05 mc-arj-sy-talk-hug with dissolve
    #arj accepts the hug - she's got to play her own role
    play voice4 amrose_happy_mmm noloop
    arj "Mmmm."
    play voice3 stacy_hmm noloop
    sy "What's new with you?"
    #sy and arj are done hugging - arj responding - playing with her fingers a bit
    scene sm1cs-arj002-06 mc-arj-sy-talk-end-hug with dissolve
    play voice4 amrose_no_nah noloop
    arj "Just staying busy with classes."
    #arj smiles
    scene sm1cs-arj002-07 mc-arj-sy-talk-look-to-mc with dissolve
    play voice4 amrose_happy_laugh2 noloop
    arj "Then I get a text from [mcname]. Needing my magic fingers."
    #mc talking
    scene sm1cs-arj002-08 mc-arj-sy-talk-mc-respond with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "We're glad you had the time. AmRose. It's a shame you're not living here; the thing could have already been fixed by now."
    #arj smiling
    scene sm1cs-arj002-09 mc-arj-sy-talk-three-in-shot with dissolve
    play voice4 amrose_yes_okay1 noloop
    arj "Well, I'm here now."
    ###part 2 - leading to the scene
    #mc gesturing toward the couch
    scene sm1cs-arj002-10 mc-arj-sy-talk-invite-to-couch with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I do have a little confession to make, AmRose."
    scene sm1cs-arj002-11 mc-arj-sy-talk-standing-near-couch with dissolve
    play voice4 amrose_disappointed_oh3 noloop
    arj "Oh?"
    play voice2 mc_yes_ugu1 noloop
    mc "This issue we're having. It actually has to do with a new porno we are trying to make."
    #arj is standing near the couch - looking back at him - smirking at him
    play voice4 amrose_arrogant_pff noloop
    arj "Hmmph. It's no wonder you didn't lead with that."
    mc "Sorry. But we really need your help."
    #sy stepping in to help with the sale
    scene sm1cs-arj002-12 mc-arj-sy-talk-stacy-join with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Please, AmRose. This client, well, we really need to keep them happy."
    sy "If we lose them, we might have to close up shop."
    scene sm1cs-arj002-13 mc-arj-sy-talk-face-away with dissolve
    play voice4 amrose_no_long noloop
    arj "Oh no..."
    #arj turning away from both so they can't see her face - arj is smiling
    arj "Well, I will do whatever I can to make sure that doesn't happen."
    #arj turns back towards them
    scene sm1cs-arj002-14 mc-arj-sy-talk-turn-back with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "How exactly can I help you two anyhow?"
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "The client wants to do a scene with a redhead."
    mc "We have used wigs on Stacy in the past, but I think to really make it pop, we need the genuine article."
    #arj is surprised by that
    scene sm1cs-arj002-15 mc-arj-sy-talk-close-up with dissolve
    play voice4 amrose_disappointed_oh1 noloop
    arj "Oh. Uh... but the client didn't bring it up, right?"
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah."
    #arj trying to be all casual
    scene sm1cs-arj002-16 mc-arj-sy-talk-focus-sy with dissolve
    play voice4 amrose_angry_cough1 noloop
    arj "Don't you think if they cared about that, they would have mentioned it."
    #sy smilng and talking - arj is like - shit, I can't really push back without revealing what I know
    scene sm1cs-arj002-17 mc-arj-sy-talk-sy-respond with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Part of our service is deciphering the unspoken wants of the customer, AmRose."
    sy "[mcname] taught me that from his business lessons."
    play voice4 amrose_yes_yap noloop
    arj "Of course."
    #mc putting his hand on arj's shoulder
    scene sm1cs-arj002-18 mc-arj-sy-talk-touch-shoulder-menu-choice with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "So will you still help us, AmRose?"
    mc "I wouldn't ask if we had another choice."
    menu:
        "I really enjoyed how it felt being with you when we got together" (hint="sm1cs_arj002_m01_h01"):
            $ player.set_choice("sm1cs_arj002_enjoyed_together")
            #mc talking to arj about how good it felt when they were together
            scene sm1cs-arj002-19 mc-arj-sy-option-one-talk-happy with dissolve
            play voice2 mc_happy_a1 noloop
            mc "I really enjoyed being together with you last time, AmRose."
            mc "You can't fault me for wanting another afternoon with my favorite ginger snap."
            #arj letting it get to her head a little - she is only human
            scene sm1cs-arj002-20 mc-arj-sy-option-one-talk-shy-reaction with dissolve
            play voice4 amrose_thinking_hmm1 noloop
            arj "Hmmm. Not when you put it like that."
            #arj touching mc's arm - sexy - flirting looking
            scene sm1cs-arj002-21 mc-arj-sy-option-one-talk-flirty with dissolve
            play voice4 amrose_disappointed_ehh1 noloop
            arj "It's been a hard week. I could use a little reward..."

        "I know I couldn't make time for you earlier, but now I can" (hint="sm1cs_arj002_m01_h02"):
            $ player.set_choice("sm1cs_arj002_couldnt_make_time")
            #mc looks regretful about his past time with arj
            scene sm1cs-arj002-22 mc-arj-sy-option-two-talk-regret with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mc "I know I couldn't make time for you earlier, but now I can."
            #arj is a little offended - arj and mc talking - mc is apologetic
            scene sm1cs-arj002-23 mc-arj-sy-option-two-talk-offended with dissolve
            play voice4 amrose_arrogant_huh3 noloop
            arj "Haha. So this is a consolation bang too?"
            scene sm1cs-arj002-24 mc-arj-sy-option-two-talk-mischevious with dissolve
            play voice2 mc_no_no6 noloop
            mc "No way! I'm sorry, I didn't mean for it to sound like {i}that{/i}."
            #mc has his mischievous grin on
            mc "Still...{w} even if it was."
            mc "I promise that I'll more than make up for being busy earlier."
            #arj likes the sound of that
            scene sm1cs-arj002-25 mc-arj-sy-option-two-talk-likes-the-idea with dissolve
            play voice4 amrose_thinking_hmm1 noloop
            arj "Mmm. Well, that does sound promising."

    #arj stands near the photoshoot whitescreen - she is playing with them - the chair is on the set
    scene sm1cs-arj002-26 mc-arj-sy-talk-standby-photo-area with dissolve
    play voice4 amrose_angry_ergh noloop
    arj "But... maybe that is just my weakness for you talking."
    arj "I don't know...{w} I'm not sure I can get involved in this business."
    #arj looks at stacy
    arj "It has rotten roots."
    scene sm1cs-arj002-27 mc-arj-sy-talk-rotten with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "They're not rotten!"
    #mc looks at sy - come on-  play nice
    scene sm1cs-arj002-28 mc-arj-sy-talk-play-nice with dissolve
    play voice2 mc_angry_cough1 noloop
    #sy sighs
    pause
    scene sm1cs-arj002-29 mc-arj-sy-talk-sigh with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "I mean, maybe their origin comic was a little sketchy, but can't we just focus on the big shiny blockbuster that a lot of people are going to love."
    scene sm1cs-arj002-30 mc-arj-sy-talk-not-a-good-fit with dissolve
    play voice4 amrose_thinking_hmm4 noloop
    arj "I could. Maybe..."
    arj "But I guess, I just don't think it's a good fit."
    scene sm1cs-arj002-31 mc-arj-sy-talk-stepping-closer with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What's not a good fit?"
    play voice4 amrose_disappointed_oh5 noloop
    arj "Me doing a porno, [mcname]."
    arj "I mean, it just sounds like I was the easy choice and you don't want to do the hard work to find a natural redhead."
    #mc is confused
    scene sm1cs-arj002-32 mc-arj-sy-thinking-confused with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Where is this coming from?"
    mct "Does she know we know? Or is she just toying with me?"
    #arj just has her nice mask on - revealing nothing
    scene sm1cs-arj002-33 mc-arj-sy-smile-waiting with dissolve
    arj "..."
    mct "What do you want from me, AmRose?"
    #mct recognizes it
    scene sm1cs-arj002-34 mc-arj-sy-think-brow-raise-realization with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Ah... I think... after all the time she was my playful pet, she wants to switch roles a bit."
    #shot from the side showing mc and arj - gap in between them
    scene sm1cs-arj002-35 mc-arj-sy-think-side-shot with dissolve
    mct "She wants me to beg for her help."
    mct "Maybe she'll see how far I'll go. Maybe she knows and is offering me a way out."
    #shot of mc's eyes
    scene sm1cs-arj002-36 mc-arj-sy-think-eye-close-up with dissolve
    play voice2 d14s16_smell noloop
    mct "Fuck me."
    menu:
        "I'll beg her" (hint="sm1cs_arj002_m02_h01"):
            $ player.set_choice("sm1cs_arj002_beg_arj")
            #mc accepting that he will beg for her help
            scene sm1cs-arj002-37 mc-arj-sy-option-one-think-have-to-beg with dissolve
            play voice2 mc_angry_hm1 noloop
            mct "I'll beg her. It's not the worst thing I've had to do for the company."
            #mc pleading with arj - coming a bit closer
            scene sm1cs-arj002-38 mc-arj-sy-option-one-talk-step-closer-plead with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "AmRose, please help us with the scene."
            mc "You're right, there are probably other people we could hire for it."
            mc "But we need this done now."
            #mc being soft and vulnerable
            scene sm1cs-arj002-39 mc-arj-sy-option-one-talk-i-need-you with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "{b}I{/b} need you..."
            #arj - little break in her defenses
            scene sm1cs-arj002-40 mc-arj-sy-option-one-silent-defense-break with dissolve
            play voice4 amrose_disappointed_ehh2 noloop
            arj "..."

        "I'm not begging her" (hint="sm1cs_arj002_m02_h02"):
            $ player.set_choice("sm1cs_arj002_dont_beg_arj")
            #mc kind of shrugs - lifts his arms a bit- mc talking
            scene sm1cs-arj002-41 mc-arj-sy-option-two-not-begging with dissolve
            play voice2 mc_yes_okay3 noloop
            mc "Alright, if you're not in, you're not in."
            mc "That's okay with me."
            #sy is confused
            scene sm1cs-arj002-42 mc-arj-sy-option-two-talk-questioning with dissolve
            play voice3 stacy_surprised_huh3 noloop
            sy "It is?"
            #mc talking to stacy
            scene sm1cs-arj002-43 mc-arj-sy-option-two-talk-turn-to-stacy with dissolve
            play voice2 d9s2_yeah noloop volume 1.8
            mc "Sure. We're not going to make AmRose do something she doesn't want."
            #mc talking to arj
            scene sm1cs-arj002-44 mc-arj-sy-option-two-talk-does-not-have-to-help with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "She doesn't have to help us..."

    #arj explaining that she was just playing a bit hardball
    scene sm1cs-arj002-45 mc-arj-sy-talk-call-out-name with dissolve
    play voice4 amrose_angry_breath2 noloop
    arj "[mcname]..."
    if player.get_choice("sm1cs_arj002_beg_arj"):
        #arj feels a bit bad she made him beg
        scene sm1cs-arj002-46 mc-arj-sy-talk-zoom-just-a-bit-of-fun with dissolve
        play voice4 amrose_arrogant_huh1 noloop
        arj "I didn't mean you had to beg me."
        arj "I was just having a little fun."
    else:
        #arj smiling at him
        scene sm1cs-arj002-47 mc-arj-sy-else-option-talk-smile with dissolve
        play voice4 amrose_arrogant_huh1 noloop
        arj "Of course I will help you, [mcname]."
        arj "I'm not turning you down, I just wanted to make you sweat a bit."
    #mc chuckling
    scene sm1cs-arj002-48 mc-arj-sy-else-option-talk-chuckle with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "Haha."
    mc "Well, mission accomplished."
    #sy lost track - she wants to double check
    scene sm1cs-arj002-49 mc-arj-sy-talk-double-checking with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Wait, so you'll do the scene?"
    #arj nods
    scene sm1cs-arj002-50 mc-arj-sy-talk-confirming with dissolve
    #arj talking to sy
    play voice4 amrose_yes_confident2 noloop
    arj "Of course I will, Stacy."
    #sy cheering
    scene sm1cs-arj002-51 mc-arj-sy-talk-cheer-yay with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Yay."
    #sy clapping her hands and standing near amrose
    scene sm1cs-arj002-52 mc-arj-sy-talk-get-into-wardrobe with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Let's get you both into wardrobe."
    ###part 3 - start of the filming
    #fade in on arj standing near stacy and mc - they are near the set, there is a chair on the set. AmRose is dressed in her bondage outfit. mc is in his leather pants and mask.
    scene sm1cs-arj002-53 mc-arj-sy-time-pass-standing-near-photoshoot with fade
    sy "You look amazing."
    arj "*sheepishly* Thanks."
    #mc gestures towards the set
    scene sm1cs-arj002-54 mc-arj-sy-talk-usher-to-chair with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so for this scene, we need you to sit down and relax. Just be yourself."
    # AmRose looks at the chair warily
    scene sm1cs-arj002-55 mc-arj-sy-pause-wary-at-chair with dissolve
    pause
    #arj sits down
    scene sm1cs-arj002-56 mc-arj-sy-walk-up-to-chair with dissolve
    play voice4 amrose_thinking_hmm3 noloop
    arj "Alright... sounds easy enough."
    #arj looks at stacy and mc - mc is getting the camera and tripod in place -arj and sy talking
    scene sm1cs-arj002-57 mc-arj-sy-talk-sit-down with dissolve
    play voice4 amrose_arrogant_huh2 noloop
    arj "And now what? I just realized I haven't seen a script."
    scene sm1cs-arj002-58 mc-arj-sy-talk-camera-setup with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh, you don't need one. In this scene, you're just the sexy plaything."
    sy "The arm-candy."
    #arj looks down at the chair
    scene sm1cs-arj002-59 mc-arj-sy-talk-look-down-at-chair with dissolve
    play voice4 amrose_happy_laugh3 noloop
    arj "Or perhaps the chair-candy."
    #sy laughing
    scene sm1cs-arj002-60 mc-arj-sy-talk-laugh with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Exactly. That is your motivation."
    sy "The Master is coming home to play with you. You've been a naughty girl."
    #alt shot of sy  - include arj in the foreground
    scene sm1cs-arj002-61 mc-arj-sy-talk-alt with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "You know that you have to be punished, and you're getting a little wet thinking about it."
    #arj biting her bottom lip
    scene sm1cs-arj002-62 mc-arj-sy-talk-shy-horny with dissolve
    play voice4 amrose_angry_breath1 noloop
    arj "*breathing shallow*"
    arj "And what do I call, [mcname]?"
    #sy thinking that is a good question - sy talking
    scene sm1cs-arj002-63 mc-arj-sy-talk-thinking with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Very good question."
    menu:
        "What do you want AmRose to call you during sex scenes?"
        "Master" (hint="sm1cs_arj002_m04_h01"):
            $ arj_mcname = _("Master")

        "Daddy" (hint="sm1cs_arj002_m04_h02"):
            $ arj_mcname = _("Daddy")

        "Sir" (hint="sm1cs_arj002_m04_h03"):
            $ arj_mcname = _("Sir")

        "My name" (hint="sm1cs_arj002_m04_h04"):
            $ arj_mcname = mcname

    #mc thinking
    scene sm1cs-arj002-64 mc-arj-sy-think-menu-name-choice with dissolve
    mc "Call me, [arj_mcname!t]."
    #sy talking to arj
    scene sm1cs-arj002-65 mc-arj-sy-talk-confirm-name with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "*excited moaning*"
    #arj likes the sound of that
    scene sm1cs-arj002-66 mc-arj-sy-talk-agree-happy with dissolve
    play voice4 amrose_yes_okay2 noloop
    arj "[arj_mcname!t]. Alright."
    #sy looks at mc - sy and mc talking
    scene sm1cs-arj002-67 mc-arj-sy-talk-thumbs-up-ready with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "We good, [mcname]?"
    play voice2 mc_yes_yeah4 noloop
    mc "We're good."
    #sy signals for them to start action.
    scene sm1cs-arj002-68 mc-arj-sy-talk-ready-to-go-full-shot with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay, rolling... Action!"
    #arj is looking a little awkward on the chair
    scene sm1cs-arj002-69 mc-arj-sy-talk-shy with dissolve
    play voice4 amrose_disappointed_oh2 noloop
    arj "Oh... I'm worried."
    arj "Who knows what [arj_mcname!t] has planned for me."
    #mc giving her instructions
    scene sm1cs-arj002-70 mc-arj-sy-talk-doing-good with dissolve
    play voice2 d2s9_confused noloop
    mc "Good start, AmRose."
    mc "Maybe grind on the chair a bit, like a cat with a scratching post."
    #arj nods
    scene sm1cs-arj002-71-01 mc-arj-sy-nod with dissolve
    pause
    #arj turns around on the chair - boobs facing the back of the chair
    scene sm1cs-arj002-72 mc-arj-sy-talk-turn-around-in-chair with dissolve
    play voisex4 amrose_old_moaning
    arj "*shaky breath* Oh... I'm getting so worried."
    #arj rubbing her tits against the chair
    scene sm1cs-arj002-73 mc-arj-sy-talk-stretch-over-chair with dissolve
    arj "What will [arj_mcname!t] do to me when he finds out I've been..."
    #arj kind of turning around on the chair - one hand touching her lips
    scene sm1cs-arj002-74 mc-arj-sy-talk-turn-around with dissolve
    play voisex4 amrose_angry_ergh noloop
    arj "So bad..."
    #sy is excited by that - stacy is filming now
    scene sm1cs-arj002-75 mc-arj-sy-talk-likes-what-she-sees with dissolve
    play voice3 stacy_suckmoan3 noloop
    sy "*whispers* That's the good shit."
    #sy signals to mc
    scene sm1cs-arj002-76 mc-arj-sy-talk-tell-to-get-in with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "You're up, slugger."
    #mc walking onto the stage with rope
    scene sm1cs-arj002-77 mc-arj-sy-enter-mc with dissolve
    arj "[arj_mcname!t]. You're here."
    scene sm1cs-arj002-78-01 mc-arj-sy-tie-amrose-feet with dissolve
    mc "Yes. Have you been a good girl?"
    scene sm1cs-arj002-78-02 mc-arj-sy-tie-amrose-hand with dissolve
    arj "I try, [arj_mcname!t]. But it's so hard to behave when you're not around."
    scene sm1cs-arj002-79 mc-arj-sy-talk-touch-boob with dissolve
    play voisex4 dahlia_sex_closedmoan1 noloop
    arj "Mmmm."
    #3 render montage - mc tying up arj - arj is nervous at first but quickly gets into it. mc doesn't tie her to the chair. he just ties her body up. We need to be able to move her as needed later on
    #mc finishes tying her up and makes sure the rope is tight
    scene sm1cs-arj002-80 mc-arj-sy-talk-close-grin with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "*grunts*"
    #mc groping her tit and arj softly moaning
    scene sm1cs-arj002-81 mc-arj-sy-talk-play-innocent with dissolve
    play voisex4 amrose_old_moaning noloop
    arj "Ooouha... You know I love it when you tie me up."
    #mc is in close to her grinning - talking
    scene sm1cs-arj002-82 mc-arj-sy-talk-play-with-nipple with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Is that why you keep causing me trouble."
    #arj plays at being innocent
    play voisex4 amrose_no_simple1 noloop
    arj "I don't mean to."
    mc "I'm not so sure."
    #mc plays with her nipple
    scene sm1cs-arj002-83 mc-arj-sy-talk-lift-chin with dissolve
    play voice4 amrose_arrogant_huh4 noloop
    arj "Well... you know what I like. And you know I'm your perfect toy."
    arj "Whatever punishment you think I deserve..."
    arj "I'm ready for it."
    #mc holding her chin - arj loves in
    play voice2 mc_happy_oof3 noloop
    mc "Eager aren't we?"
    ###part 4 - The Reveal
    #shot focused on arj's face - looking quite horny
    scene sm1cs-arj002-84 mc-arj-sy-talk-shy with dissolve
    play voice4 amrose_yes_confident1 noloop
    arj "For you? Always..."
    #sy is smiling - the trap is about to be sprung
    scene sm1cs-arj002-85 mc-arj-sy-talk-smile-spring-trap with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Okay..."
    #sy walking in to join mc
    scene sm1cs-arj002-86 mc-arj-sy-talk-step-into-scene with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "And now we get to do some watersports with you, AmRose."
    #arj is unsure about that
    scene sm1cs-arj002-87 mc-arj-sy-talk-questioning-watersports with dissolve
    play voice4 amrose_surprised_what noloop
    arj "Watersports... Really?"
    #sy licks her lips - she was turned on watching mc play with amrose
    scene sm1cs-arj002-88 mc-arj-sy-talk-tongue-turned-on with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Yes. It was one of the main requests for the client."
    sy "So we got to make sure that we tick off that box."
    #arj speaks without really even thinking - she is a bit horny from being played with by mc.
    scene sm1cs-arj002-89 mc-arj-sy-talk-speak-quickly with dissolve
    play voice4 amrose_surprised_huh2 noloop
    arj "I don't remember putting watersports on the request."
    #mc replies quickly
    scene sm1cs-arj002-90 mc-arj-sy-talk-respond with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, that's right. You wanted boofing."
    mc "{b}You{/b} asked for any boofing videos we had made'"
    #arj is like shit
    scene sm1cs-arj002-91 mc-arj-sy-pause-look-away-shit with dissolve
    arj "Mmm."
    mct "Haha. Now it's her turn to sweat."
    #arj trying to recover
    scene sm1cs-arj002-92 mc-arj-sy-talk-recover with dissolve
    play voice4 amrose_surprised_oh1 noloop
    arj "Oh! You're confusing me. I'm not the client. I didn't ask for anything."
    arj "But if the client asked for watersports, we can try that."
    menu:
        "Tease her" (hint="sm1cs_arj002_m03_h01"):
            $ player.set_choice("sm1cs_arj002_tease_arj")
            scene sm1cs-arj002-93 mc-arj-sy-tease-talk-lean-in-close with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "Come on, AmRose."
            mc "You can do better than that."
            #arj looks away - nervous
            scene sm1cs-arj002-94 mc-arj-sy-tease-talk-look-away-kiss-neck with dissolve
            play voice4 amrose_surprised_uh2 noloop
            arj "I... How... I mean... I don't know what the client wanted."
            #mc looking at her - bit of intense eyes - II figured you out
            scene sm1cs-arj002-95 mc-arj-sy-tease-talk-figured-out with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Oh I think you do."
            arj "*nervous breathing*"

        "The jig is up, my sweet red flower" (hint="sm1cs_arj002_m03_h02"):
            $ player.set_choice("sm1cs_arj002_jig_is_up")
            #mc stroking her cheek
            scene sm1cs-arj002-96 mc-arj-sy-talk-stroke-cheek with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "I'm afraid the jig is up, my sweet red flower."

    #arj pretending a bit more
    scene sm1cs-arj002-97 mc-arj-sy-talk-stacy-walk-by with dissolve
    play voice4 amrose_angry_ehh noloop
    arj "I don't know what you're talking about."
    scene sm1cs-arj002-98 mc-arj-sy-talk--stand-behind-hand-on-shoulder with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Then how did you know watersports wasn't in the order?"
    #sy touching amrose's hips
    sy "Unless you wrote it."
    #mc and sy circling around armrose - not menacing - they are having fun
    scene sm1cs-arj002-99 mc-arj-sy-talk-circle-around with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "I think...{w} [mcname] must have talked about it earlier."
    scene sm1cs-arj002-100 mc-arj-sy-talk-pause-stand-infront with dissolve
    play voice2 amrose_no_uhuh noloop
    mc "I did no such thing."
    #mc and sy standing in front of arj
    scene sm1cs-arj002-101 mc-arj-sy-struggle-with-tied-hands with dissolve
    #arj tries in vain to escape the ropes
    play voice4 amrose_angry_errr noloop
    arj "Hrrrrn."
    #arj looks down at the ropes - defeated
    scene sm1cs-arj002-102 mc-arj-sy-talk-look-down with dissolve
    play voice4 amrose_disgust_argh noloop
    arj "Ah... the ropes."
    arj "Clever girl..."
    #arj looking at mc
    arj "And boy."
    #sy and mc laughing
    scene sm1cs-arj002-103 mc-arj-sy-talk-laughing with dissolve
    play voice2 mc_happy_laugh3 noloop
    play voice3 stacy_happy_laugh3 noloop
    "Stacy and [mcname]" "*laughing*"
    #arj asks what he charges are - stacy chuckles
    scene sm1cs-arj002-104 mc-arj-sy-talk-accusation with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "So... What's the accusation exactly?"
    play voice3 stacy_mmm1 noloop
    sy "Accusation?"
    #mc gives arj a knowing look - mc talking
    scene sm1cs-arj002-105 mc-arj-sy-talk-jig-is-up with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "AmRose, stop playing dumb. We know what's going on here."
    mc "You've been pretending to be our client so you could figure out if we had your data from Fetish Locator."
    #arj is playing touch
    scene sm1cs-arj002-106 mc-arj-sy-talk-playful-smile with dissolve
    play voice4 amrose_arrogant_hmm1 noloop
    arj "Hmmph. Even if I admitted to that, and I don't. You have no proof."
    scene sm1cs-arj002-107 mc-arj-sy-talk-question with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "Girl please. It got a little obvious at the end."
    scene sm1cs-arj002-108 mc-arj-sy-talk-look-away-embarrassed with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "Mmm. Maybe I slipped up. But I stand by what I did."
    #arj playful smile
    scene sm1cs-arj002-109 mc-arj-sy-talk-wide-shot with dissolve
    play voice4 amrose_happy_phew3 noloop
    arj "Or I would if not for the rope."
    #sy looking at her
    play voice3 stacy_thinking_hmm4 noloop
    sy "You were trying to see if we still had your sensitive data from the Fetish Locator App."
    sy "Weren't you?"
    # AmRose looks away guiltily, her face reddening.
    scene sm1cs-arj002-110 mc-arj-sy-talk-touch-shoulder with dissolve
    #arj breaks - sniffing a bit, eyes a little watery
    play voice4 amrose_pain_sobs1 noloop
    arj "*sniffs*"
    #arj apologizing to mc
    arj "I... I'm sorry.{w} I'm so sorry, [mcname]."
    arj "I was just so worried and angry."
    #shot from above - showing the three of them - intimate moment - the secret is finally coming out.
    #mc touching her shoulder
    scene sm1cs-arj002-111 mc-arj-sy-talk-kneel with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "When you chose not to delete the data, all I could think of was my secret getting leaked."
    play voice2 mc_yes_aga2 noloop
    mc "I know, AmRose."
    #mc going like - come on
    mc "But come on."
    #mc kneels to be at her eye level
    mc "You {i}know{/i} me..."
    mc "I would never hurt you. Your secret has been safe with me since I learned it."
    #arj sniffling a bit
    scene sm1cs-arj002-112 mc-arj-sy-talk-sad with dissolve
    play voice4 amrose_pain_sobs2 noloop
    arj "*sniffing* [mcname]."
    #mc looks back at stacy
    scene sm1cs-arj002-113 mc-arj-sy-talk-gesture-at-stacy with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "And to get into specifics, Stacy deleted the stuff with you on it."
    #mc talking to arj - just focused on the two of them
    scene sm1cs-arj002-114 mc-arj-sy-pause-on-stacy with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "And I've looked through it myself to make sure it's gone for good."
    #arj smiling through some tears
    scene sm1cs-arj002-116 mc-arj-sy-talk-emotional-calls-out-name with dissolve
    play voice4 amrose_pain_sobs3 noloop
    arj "Oh, [mcname]."
    #mc leans in to kiss her
    scene sm1cs-arj002-117 mc-arj-sy-pause-kiss with dissolve
    play voice2 d1s1_mmm noloop
    play sound dahlia_kiss_french1
    pause
    #mc pulls back
    scene sm1cs-arj002-116 mc-arj-sy-talk-emotional-calls-out-name with dissolve
    play voice4 amrose_pain_sobs5 noloop
    arj "*sniff* This has just been an awful mistake. I thought about the plan late one night."
    arj "I think... it was after seeing your place the first time."
    #mc laughing - arj smiling bittersweet
    scene sm1cs-arj002-118 mc-arj-sy-talk-pull-back with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "You mean before the remodel? It really was shitty, haha."
    scene sm1cs-arj002-120 mc-arj-sy-talk-wide-shot-alt-shot with dissolve
    play voice4 amrose_angry_breath1 noloop
    arj "It was, but it had potential."
    #shot from a bit of distance showing off the studio and how improved it is
    arj "But just look at it now. I was stubborn, and I thought, well, I'll use the studio to get at Stacy from another angle."
    arj "I let my fear make decisions. And I started thinking..."
    scene sm1cs-arj002-119 mc-arj-sy-talk-wide-shot-about-studio with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "You didn't want me anymore..."
    play voice2 mc_no_uhuh1 noloop
    mc "That's not true."
    play voice4 amrose_happy_phew1 noloop
    arj "*relieved sigh*"
    arj "Being away from you all this time made each day worse for me."
    arj "But being here with you now..."
    scene sm1cs-arj002-121 mc-arj-sy-talk-hold-face with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "You can see it in my eyes..."
    play voice4 amrose_pain_ahh2 noloop
    arj "Oh god, it's so lame. I'm such a mess."
    play voice2 mc_no_no5 noloop
    mc "No, AmRose. Well I mean kind of."
    play voice4 amrose_old_haha2 noloop
    arj "*sad laughing*"
    #mc wipes away her tears
    mc "But I would make out with you in a shitstorm if it meant tasting your lips."
    mc "And that's the fluffy lord's truth."
    scene sm1cs-arj002-119 mc-arj-sy-talk-wide-shot-about-studio with dissolve
    play voice4 amrose_old_upset noloop volume 1.7
    arj "I've been such a fool.{w} Stacy..."
    arj "I owe you an apology too. While everything was ending last year, well..."
    arj "Sometimes inner demons speak louder than angels."
    scene sm1cs-arj002-122 mc-arj-sy-talk-apologize-stacy with dissolve
    play voice3 stacy_no_nonono1 noloop
    sy "There is nothing to apologize for, AmRose."
    sy "Well... *coughs lightly* Nothing that you can't make up for."
    scene sm1cs-arj002-123 mc-arj-sy-talk-stand with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "Mmmm. I did do a bad thing. And penance... sounds appropriate."
    play voice2 mc_no_nope1 noloop
    mc "Not at all, my little plaything."
    mc "Are you ready to continue filming?"
    scene sm1cs-arj002-124 mc-arj-sy-talk-horny-notice-boner with dissolve
    play voice4 amrose_yes_confident2 noloop
    arj "Yes... [mcname]."
    #arj looks a bit sluttier
    arj "I mean...{w}Yes, [arj_mcname!t]."
    ###part 5 - Sex Scene
    #mc pulls arj's body forward a bit so she is bent forward and able to suck on his cock
    scene sm1cs-arj002-125 mc-arj-sy-talk-pull-forward with dissolve
    play voice4 amrose_old_wow noloop
    arj "Oh!"
    play voice2 mc_scared_oh1 noloop
    mc "Your punishment begins now my pet."
    scene sm1cs-arj002-126 mc-arj-sy-open-mouth-lean-forward with dissolve
    play voice4 amrose_happy_yeah2 noloop
    arj "Yes, [arj_mcname!t]..."
    #arj opening up her mouth
    # animation 1- blowjob - intro - arj still tied up - arj in chair - mc pulls her body forward and is making her give him a blowjob - he has his hand on her head
    scene sm1cs-arj002-130 mc-arj-sy-animation-one-blowjob- with dissolve
    play voisex4 amrose_old_fsucking2
    play voisex2 mc_sex_openmoans2
    mc "Good girl. You still remember your old tricks."
    arj "Mlrph... flurrphah..."
    #alt angle anim 1
    play voisex3 stacy_disappointed_oh7 noloop
    sy "Oh that is so hot."
    mc "Fuck me, her lips feel so good."
    #alt angle anim 1
    arj "*wet, sloppy sucking*"
    ###pause animation 1
    #mc pulls his cock out of arj's throat
    scene sm1cs-arj002-131 mc-arj-sy-talk-pull-cock-out with dissolve
    play voisex4 amrose_angry_breath2 noloop
    stop voisex2 fadeout 1.0
    arj "Fuaah-huaaah..."
    arj "But [arj_mcname!t] I haven't made you cum yet."
    #mc smiles at her - talking
    scene sm1cs-arj002-132 mc-arj-sy-talk-smile with dissolve
    play voisex2 mc_angry_fuck3 noloop
    mc "Fuck I've missed this so much!"
    #mc taps his cock against her lips
    scene sm1cs-arj002-133 mc-arj-sy-talk-push-cock-to-lips with dissolve
    play voisex4 dahlia_sex_closedmoan2 noloop
    arj "Mrraha-haah..."
    play voisex2 mc_arrogant_heh2 noloop
    mc "You're going to be my little cocksleeve whenever I need one."
    mc "Aren't you?"
    #arj is just overcome with horniness - drooling from her lips - sticky
    scene sm1cs-arj002-134 mc-arj-sy-talk-desparate with dissolve
    play voisex4 amrose_happy_yes2 noloop
    arj "Yes! Whenever you want me."
    arj "Hhuaaah."
    #mc pushes his cock back inside her mouth to start the animation again
    scene sm1cs-arj002-135 mc-arj-sy-push-cock-back-in with dissolve
    play voisex4 amrose_old_fsucking
    play voisex2 mc_sex_openmoans2
    play sound mc_sex_sucking_fast2 loop
    arj "Plupfff."
    #resume animation 1
    #alt angle anim 1
    #end of anim 1
    #mc releases arj - she is lying back in the seat
    #mc unties her hands - just her hands
    scene sm1cs-arj002-136 mc-arj-sy-pause-release-her with dissolve
    play voisex4 amrose_angry_breath2 noloop
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    arj "Murah-hhuaah...{w} Is my punishent over already, [arj_mcname!t]."
    scene sm1cs-arj002-137 mc-arj-sy-talk-untie with dissolve
    play voisex2 mc_no_no2 noloop
    mc "Not by a long shot."
    scene sm1cs-arj002-138 mc-arj-sy-talk-raise-hand with dissolve
    #mc holds her hand
    mc "*rope rustling*"
    play voisex2 mc_thinking_hmm5 noloop
    mc "But do deserve a little treat."
    #mc kisses it
    scene sm1cs-arj002-139 mc-arj-sy-talk-kiss-hand with dissolve
    play voisex2 d1s1_mmm noloop
    play sound mc_kiss3
    mc "Mwaaah."
    #arj loves it
    scene sm1cs-arj002-140 mc-arj-sy-talk-happy with dissolve
    play voisex2 mc_thinking_mmm1 noloop
    mc "I missed you like a sailor misses their port."
    #mc ordering her to turn around
    scene sm1cs-arj002-141 mc-arj-sy-talk-tell-to-turn-around with dissolve
    play voisex2 mc_arrogant_heh1 noloop
    mc "Now turn you body around, my slut."
    scene sm1cs-arj002-142 mc-arj-sy-talk-turn-around-giggle with dissolve
    play voisex4 amrose_yes_happy2 noloop
    arj "*shivering moan* Yes, [arj_mcname!t]."
    #arj turns her body around on the chair
    play voisex4 amrose_happy_laugh6 noloop
    arj "*giggles*"
    #arj is in position on the seat - mc has his hand on her asscheek - lining up
    scene sm1cs-arj002-143 mc-arj-sy-pause-line-up-behind with dissolve
    pause
    scene sm1cs-arj002-144 mc-arj-sy-talk-push-inside with hpunch
    #mc pushes his cock inside her - halfway in
    play voisex4 amrose_sex_orgasm1 noloop
    play voisex2 mc_angry_errr4 noloop
    arj "Ahuaaah... I love it when [arj_mcname!t] shoves his cock in my pussy!"
    #mc is all the way inside and pulls her arms back
    scene sm1cs-arj002-145 mc-arj-sy-push-all-the-way-in with dissolve
    play voisex4 dahlia_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    arj "*moaning passionately*"
    scene sm1cs-arj002-146 mc-arj-sy-animation-two-chair-doggy with dissolve
    # Animtion 2- mc fucking amrose - she is facing the back of the chair - legs folded - she is still tied up - mc is pulling her hands back - arj moaning passionately
    arj "Fuck yes-huaaah!"
    #alt angle anim 2
    sy "Now she's really getting into it!"
    mc "Did you miss this cock, my little redhead minx?"
    #alt angle anim 2
    arj "Moo-huaah!"
    arj "Everyday and twice on sundays!"
    arj "Oh god. Yes! YES!"
    #alt angle anim 2
    arj "I've missed your big cock pounding into my pussy so much!"
    #alt angle anim 2
    ###end of anim 2
    #sy puts a hand on mc's shoulder - sy talking - mc looking back at her
    stop voisex2 fadeout 1.0
    stop voisex4 fadeout 1.0
    scene sm1cs-arj002-147 mc-arj-sy-talk-stacy-interrupt with dissolve
    play voisex3 stacy_hey noloop
    sy "Mind if I cut in."
    #arj looks back toward stacy - moaning softly
    scene sm1cs-arj002-148 mc-arj-sy-pause-turn-to-look with dissolve
    pause
    #arj notices stacy has a strapon on
    scene sm1cs-arj002-149 mc-arj-sy-talk-shock with dissolve
    play voisex4 amrose_surprised_oh2 noloop
    arj "Oh... I didn't realize you wanted to punish me too, Stacy."
    #mc pulls back - stacy wagging her finger towards arj - using her finger to beckon arj
    scene sm1cs-arj002-150 mc-arj-sy-reveal-strap-on with dissolve
    play voisex3 stacy_yes_yeah2 noloop
    sy "I very much want to. Don't worry."
    scene sm1cs-arj002-151 mc-arj-sy-talk-mc-let-stacy-pass with dissolve
    play voisex3 stacy_happy_laugh2 noloop
    sy "I'll go easy on you."
    #fade in - stacy is on the chair - arj is arms are ied up again - but that's really only part of her tied up. Arj is settled above the strapon-dildo
    scene sm1cs-arj002-152 mc-arj-sy-pause-sit-on-tip with fade
    #stacy guides her down to the shaft
    play voisex4 amrose_sex_orgasm2 noloop
    arj "Ha-houahah..."
    arj "This is easy?"
    play voisex3 stacy_arrogant_huh5 noloop
    sy "Haha. You know you love it."
    #stacy kisses arj
    scene sm1cs-arj002-154-02 mc-arj-sy-kiss with dissolve
    play voisex4 dahlia_sex_closedmoan4 noloop
    play voisex3 stacy_suckmoan1 noloop
    play sound dahlia_kiss_french1
    sy "Mrrmmm."
    #arj kissing her back
    arj "Ymmmm."
    # animation 3- stacy fucking amrose with strapon - stacy is sitting on the chair holding arj - they're kissing and moaning intermitently
    scene sm1cs-arj002-155 mc-arj-sy-animation-three-chair-strapon with dissolve
    play voisex3 stacy_fmoans5
    play voisex4 amrose_old_moaning2
    sy "I know we may not always agree on everything across the line, AmRose."
    sy "But I really hope, from here on out, we don't keep secrets from each other."
    #alt angle anim 3
    arj "Ah-huaha... Stacy..."
    arj "I'd like that very much."
    #alt angle anim 3
    #alt angle anim 3
    sy "I'll still be a troublemaker, and a brat sometimes, but you'll never feel like you have to keep things from me."
    sy "Ohouaah...{w} Deal?"
    #alt angle anim 3 - focus on arj's body
    play voisex4 amrose_old_orgasming
    arj "Fuaaah... Deal!"
    arj "No-ah... I'm getting so close. Oh god..."
    arj "It feels so good."
    sy "[mcname] and I are always going to be there to make you feel great, AmRose."
    scene sm1cs-arj002-156 mc-arj-sy-talk-my-turn with vpunch
    arj "Yes-oohuaah-ha-aha!"
    #end of anim 3
    #mc standing in front of the two girls - they've both got that cum glaze look in their eyes
    play voisex2 mc_thinking_hmm1 noloop
    mc "My turn..."
    # animation 4- mc fucking amrose - mc sitting on chair - arj is on his lap - arj's hands are tied up. Arj's legs are spread wide and they hook over mc's legs. Mc is squeezing her right tit and holding her shoulder  - fade in
    stop voisex3 fadeout 1.0
    scene sm1cs-arj002-157 mc-arj-sy-animation-four-chair-sex with dissolve
    play voisex4 dahlia_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    mc "Damn. You feel even tighter now."
    #alt angle anim 4
    arj "It's this pose, [arj_mcname!t]."
    arj "It makes me extra tight."
    #alt angle anim 4
    arj "Bhuaah... buarh... fuahk-ahah..."
    arj "Thank you for forgiving me, [mcname]."
    arj "I'm glad you found me out..."
    arj "Before something bad happened."
    #alt angle anim 4
    mc "It was never going to get that far, AmRose."
    mc "I'm just mad at myself that I didn't see it."
    #alt angle anim 4
    arj "Ohuaa-huaah... it's been... too long since you had a good mystery."
    mc "Or my favorite redhead bouncing on my cock."
    #alt angle anim 4
    arj "*laughing and then moaning*"
    #alt angle anim 4
    arj "Oh Fuck... hurha... {w}[mcname]! I'm cumming...."
    arj "You're making me cum all over your amazing dick-hhuaa-rufaaah!"
    #end of anim 4
    #arj cumming her brains out - some cum leaking out from between her legs
    play voisex4 amrose_old_orgasming
    play voisex2 mc_sex_openmoans3
    scene sm1cs-arj002-158 mc-arj-sy-cumming with vpunch
    arj "Fuccc-kahaa-hraaaiieee!"
    scene sm1cs-arj002-159 mc-arj-sy-cumming-02 with vpunch
    pause
    #mc is grunting - arj got super tight on his cock
    scene sm1cs-arj002-160 mc-arj-sy-talk-tighten with dissolve
    mc "Shit... AmRose."
    #arj is nearly delirious
    arj "*panting* Just cum in me."
    #mc siling but also asking her
    scene sm1cs-arj002-161 mc-arj-sy-talk-smiling with dissolve
    mc "Yeah?"
    #arj wants the creampie
    arj "Yeah! I want-uhaa... {w}I want to feel you throbbing as you fill up my naughty cunt."
    #mc cums inside of arj - arj has her tongue out - eyes crossed
    #mc lifts her up - more cum spiling out of her pussy
    play voisex2 mc_sex_orgasm4 noloop
    play voisex4 [amrose_sex_orgasm4, amrose_sex_orgasm3] noloop
    scene sm1cs-arj002-162 mc-arj-sy-cum-inside with vpunch
    pause
    scene sm1cs-arj002-163 mc-arj-sy-cum-spilling-out with dissolve
    pause
    scene sm1cs-arj002-164 mc-arj-sy-talk-alot-of-cum with dissolve
    #sy is impressed
    play voice3 stacy_surprised_ohmy1 noloop
    sy "What a big load."
    play voisex2 mc_happy_oof3 noloop
    mc "I think my balls knew it was a chance to make up for lost time."
    scene sm1cs-arj002-165 mc-arj-sy-talk-can-i-eat with dissolve
    play voisex3 stacy_laugh4 noloop
    sy "Haaha."
    #sy asking amrose if she can eat her out
    sy "Mind if I have a taste, AmRose?"
    #arj likes the idea a lot
    scene sm1cs-arj002-166 mc-arj-sy-talk-likes idea with dissolve
    play voisex4 amrose_thinking_oh2 noloop
    arj "I would love that."
    arj "I haven't felt your tongue in months."
    #everyone getting into position for animation 5
    scene sm1cs-arj002-168 mc-arj-sy-licks-pussy with dissolve
    #stacy licks cum out of arj's pussy
    play voisex3 stacy_sucks1
    play voisex4 amrose_old_moaning2
    sy "Yum yum."
    arj "Ahu-ahuah..."
    #mc puts his cock inside stacy's pussy
    play voisex3 stacy_pain_mmm1 noloop
    scene sm1cs-arj002-169 mc-arj-sy-talk-pushes-into-stacy with dissolve
    queue voisex3 stacy_sucks1
    play voisex2 mc_sex_openmoans2
    sy "Yeouch-gaaah!"
    sy "[mcname]! Don't just plow into someone when she's eating a creampie taco."
    #arj is embararssed but can't keep herself from laughing
    play voisex4 amrose_happy_laugh7 noloop
    scene sm1cs-arj002-170 mc-arj-sy-talk-laughing with dissolve
    queue voisex4 amrose_old_moaning2
    arj "Haha-haha."
    #mc thrussting into stacy
    scene sm1cs-arj002-171 mc-arj-sy-talk-mc-focus with dissolve
    mc "I got hard the moment you said you wanted to lick my cum out of AmRose's pussy."
    sy "Ah-ahuaah... Well... I can't blame you for that."
    sy "Ohua-huaaha..."
    # Animation 5 - mc fucking stacy - amrose on stacy's face. stacy eating out creampie.
    sy "This is the fucking life!"
    mct "This is magnificent."
    #alt angle anim 5
    mct "Me and {b}my{/b} girls."
    #alt angle anim 5
    mct "{font=DejaVuSans.ttf}𝅘𝅥𝅮{/font} Reunited and it feels so good. 𝅘𝅥𝅮"
    #alt angle anim 5
    #alt angle anim 5 - focus on arj
    arj "Muf-ahauah... Oh Stacy."
    arj "You're going to make me cum all over again!"
    sy "*excited slurping sounds*"
    #alt angle anim 5
    #end of anim 5
    #mc pulls out - stroking his cock
    stop voisex4 fadeout 1.0
    stop voisex3 fadeout 1.0
    scene sm1cs-arj002-174 mc-arj-sy-talk-line-up with dissolve
    play voisex2 mc_happy_yay2 noloop
    mc "Line up you two."
    scene sm1cs-arj002-175 mc-arj-sy-both-line-up with dissolve
    play voisex2 d7s4_mcbreathing
    pause
    scene sm1cs-arj002-176-01 mc-arj-sy-cumming with dissolve
    pause
    play voisex2 mc_sex_orgasm2 noloop
    play voisex3 stacy_moan6 noloop
    play voisex4 dahlia_sex_closedmoan1 noloop
    scene sm1cs-arj002-176-02 mc-arj-sy-cumming with hpunch
    pause
    scene sm1cs-arj002-176-03 mc-arj-sy-cumming with dissolve
    play voisex3 stacy_moan4 noloop
    sy "Oooh-huaah..."
    play voisex4 amrose_yes_ugu noloop
    arj "*panting* Yes."
    #both girls face their bodies towards each other - smooshing their boobs together- but their heads face mc. They're both looking super horny / cum drunk
    #cum on stacy and arj's faces and upper tits
    scene sm1cs-arj002-177 mc-arj-sy-talk-thinking-what-im-thinking with dissolve
    #both girls turn in to face each other
    play voisex3 stacy_disappointed_mmm1 noloop
    sy "Mmm. You thinking what I'm thinking?"
    play voisex4 amrose_yes_yeah1 noloop
    arj "Let's."
    #cute kiss between the two
    scene sm1cs-arj002-178-01 mc-arj-sy-hug-kneel with dissolve
    play voisex4 dahlia_sex_closedmoan4 noloop
    play voisex3 stacy_suckmoan1 noloop
    play sound dahlia_kiss_french1
    arj "Mrmm..."
    sy "Ahhuammm..."
    #mc faces the two and hugs them both
    scene sm1cs-arj002-178-02 mc-arj-sy-hug-rest-shoulder with dissolve
    #both girls lay their chins on either of his shoulders - loving the hug
    play voisex3 stacy_suckmoan2 noloop
    sy "Mrmmm."
    play voisex4 amrose_happy_mmm noloop
    arj "Hnnmmm."
    ###part 6 - Ending
    # The scene transitions to them cuddling in bed, naked bodies intertwined as they bask in the afterglow of their lovemaking. Mc is in middle, arj and sy are on either side. Everyone is naked and cleaned up - fade in
    scene sm1cs-arj002-179 mc-arj-sy-on-bed-cuddle with fade
    pause
    scene sm1cs-arj002-180 mc-arj-sy-talk-lift-head with dissolve
    #arj talking
    play voice3 amrose_happy_phew2 noloop
    arj "You know... I think this is exactly what we all needed. A new chapter."
    #arj smiles at mc
    arj "For all of us."
    #mc talking - sy agreeing with him
    scene sm1cs-arj002-181 mc-arj-sy-talk-smile with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Definitely. We got everything in the open, and we fucked each other senseless."
    mc "I don't think I've ever felt closer to you two than ever before."
    scene sm1cs-arj002-182 mc-arj-sy-talk-stacy-focus with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Seconded. Now that we're back together, we'll be fucking unstoppable."
    # AmRose snuggles closer to [mcname] as Stacy wraps an arm around her shoulders from behind.
    play voice4 amrose_thinking_hmm5 noloop
    arj "So... what do we do now? What comes next?"
    scene sm1cs-arj002-183 mc-arj-sy-talk-snuggle with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Well, it's actually nearly time to start planning our next movies."
    mc "This studio isn't going to get famous all on its own."
    play voice4 amrose_yes_yeah4 noloop
    arj "Of course not."
    arj "Well, whatever I can do to help, I'll be here from now on."
    arj "Unless I'm in class."
    play voice2 mc_happy_oof1 noloop
    mc "Ooooh. Someone thinking of moving in?"
    #arj kisses him
    scene sm1cs-arj002-184 mc-arj-sy-pause-kiss with dissolve
    play voice4 amrose_thinking_hmm4 noloop
    play voice2 d1s1_mmm noloop
    play sound mc_kiss1
    pause
    #arj smiling at mc
    scene sm1cs-arj002-185 mc-arj-sy-talk-amrose-smiling with dissolve
    play voice4 amrose_no_uhuh noloop
    arj "Not just yet."
    play voice2 mc_surprised_why3 noloop
    mc "Why not?"
    arj "Cause you know exactly what would be happening if the two of us were under the same roof all day."
    scene sm1cs-arj002-186 mc-arj-sy-talk-smiling-response with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "We'd be getting noise complaints every night."
    play voice4 amrose_happy_laugh1 noloop
    arj "Exactly."
    #mc smiles at her
    scene sm1cs-arj002-187 mc-arj-sy-talk-close-eyes with dissolve
    play voice2 d7s6_moan1 noloop
    mc "Well, our door is always open to you, AmRose."
    #mc closes his eyes
    mc "Now, if you two don't mind. I think it's time for my beauty sleep."
    mc "I'm going to need every wink of sleep now that I've got the emerald babe and the fiery ruby back in my life."
    #sy snuggles up
    scene sm1cs-arj002-188 mc-arj-sy-talk-goodnight with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "Sounds like you should join a gym."
    sy "Good night, [mcname]. Good night, AmRose."
    scene sm1cs-arj002-189 mc-arj-sy-talk-kiss-chest with dissolve
    play sound mc_kiss2
    play voice4 amrose_thinking_hmm3 noloop
    arj "Good night, Stacy."
    #arj kisses mc's neck
    play voice4 amrose_old_amha noloop
    arj "I've been dreaming about cuddling up and going to sleep with you."
    #mc smiles at her
    scene sm1cs-arj002-190 mc-arj-sy-talk-stick-with-me with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Stick with me, gorgeous. I'll make all your dreams come true."
    #arj giggles softly
    play voice4 amrose_old_amha noloop
    arj "*giggles*"
    #everyone is cuddled up and asleep
    scene sm1cs-arj002-191 mc-arj-sy-end with dissolve
    pause
    #decent energy cost
    #return to timeslot - Evening

    $ StoryController.end_scene(ARJ_STORY)
    return
