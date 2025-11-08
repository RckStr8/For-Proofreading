label sm1fs_t008:

    scene sm1fs_t008-01 dvh-mc-office with dissolve
    pause
    scene sm1fs_t008-02 dvh-talk-mc with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    dvh "I talked it over with Bruce. We both agree that you pulled your weight during the show."
    dvh "Without complaint. And even better, without issue."
    scene sm1fs_t008-03 dvh-talk-mc with dissolve
    play voice3 girl34_yes_aga3 noloop
    dvh "The show went forward, no one forgot their lines, the audience laughed and cheered."
    dvh "It all amounts to a win for us, and you played a part in it."
    scene sm1fs_t008-04 mc-talk-dvh with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Happy to be a part of the team, Denise."
    scene sm1fs_t008-05 dvh-talk-mc with dissolve
    play voice3 girl34_arrogant_hm2 noloop
    dvh "Now, you will have a spot as a stage hand as long as you wish, but I know that you want to take on a larger role."
    menu:
        "I did once" (hint="sm1fs_t008_m01_h01"):
            $ player.set_choice("sm1fs_t008_did_once")
            scene sm1fs_t008-06 mc-talk-dvh with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "I did once."
            scene sm1fs_t008-07 dvh-talk-mc with dissolve
            play voice3 girl34_disappointed_oh2 noloop
            dvh "Oh, have you changed your mind?"
            scene sm1fs_t008-08 mc-talk-dvh with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "I mean, what are we talking about here?"
            scene sm1fs_t008-09 dvh-talk-mc with dissolve
            play voice3 girl34_thinking_emm1 noloop
            dvh "I'm talking about letting you audition for a spot in the theater troupe."

        "You mean, I'm going to get to act on stage?" (hint="sm1fs_t008_m01_h02"):
            $ player.set_choice("sm1fs_t008_get_to_act")
            scene sm1fs_t008-10 mc-talk-dvh with dissolve
            play voice2 d1s2_hmm noloop volume 1.7
            mc "You mean, I finally get to act on stage with the troupe?"
            scene sm1fs_t008-11 dvh-talk-mc with dissolve
            play voice3 girl34_no_nope4 noloop
            dvh "Not quite."
            scene sm1fs_t008-12 dvh-talk-mc with dissolve
            play voice3 girl34_thinking_emm1 noloop
            dvh "I have seen your commitment to the theater group as a whole."
            dvh "And witnessed your willingness to hone your skills."
            dvh "For that reason, I will allow you to audition again."

    scene sm1fs_t008-13 dvh-talk-mc with dissolve
    play voice3 girl34_hey_simple5 noloop
    dvh "Follow me. She should be on stage."
    scene sm1fs_t008-14 mc-talk-dvh with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Who?"
    scene sm1fs_t008-15 dvh-mc with dissolve
    dvh "..."
    scene sm1fs_t008-16 dvh-mc-theater with fade
    pause
    scene sm1fs_t008-17 tl-talk with dissolve
    play voice4 girl24_arrogant_huh1 noloop
    tl "Yo."
    scene sm1fs_t008-18 mc-talk-tl with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey Taisia."
    scene sm1fs_t008-19 dvh-talk-mc with dissolve
    play voice3 girl34_disappointed_eem1 noloop
    dvh "On the tablet is several short monologues and scenes. You will select one from the list."
    dvh "Once you make your selection, you'll have exactly thirty minutes to prep yourself."
    scene sm1fs_t008-20 dvh-talk-tl with dissolve
    play voice3 girl34_arrogant_hm1 noloop
    dvh "Then you will run the scene. Taisia will fill in for any additional characters needed."
    scene sm1fs_t008-21 dvh-talk-mc with dissolve
    play voice3 girl34_yes_ugu1 noloop
    dvh "Taisia will have a script, but I must require you to do the scene without assistance."
    dvh "No script. No second takes."
    scene sm1fs_t008-22 dvh-talk-mc with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    dvh "Just one chance to make me feel something that isn't the urge for another cigarette."
    scene sm1fs_t008-23 dvh-lighter with dissolve
    pause
    scene sm1fs_t008-24 dvh-talk with dissolve
    dvh "..."
    scene sm1fs_t008-25 dvh-talk-mc with dissolve
    play voice3 girl34_arrogant_laugh2 noloop
    dvh "As you can imagine, this is a tall order."
    menu:
        "Secondhand smoke kills, Denise" (hint="sm1fs_t008_m02_h01"):
            $ player.set_choice("sm1fs_t008_secondhand_smoke")
            scene sm1fs_t008-26 c1-mc-talk-dvh with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "Secondhand smoke kills, Denise."
            scene sm1fs_t008-27 c1-dvh-talk-mc with dissolve
            play voice3 girl34_disgust_woeagh1 noloop
            dvh "And second-tier actors kill a play faster than a shot in the head."
            scene sm1fs_t008-28 c1-tl-talk with dissolve
            play voice4 girl24_happy_mmm noloop
            tl "R.I.P, Mr. Lincoln.{w} He was a real one."
            scene sm1fs_t008-29 c1-dvh-talk with dissolve
            play voice3 girl34_arrogant_ha4 noloop
            dvh "Make your selection. Some of us have a schedule to keep."
            scene sm1fs_t008-30 c1-mc-talk-dvh with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "Okay, okay."

        "I know I can deliver the goods" (hint="sm1fs_t008_m02_h02"):
            $ player.set_choice("sm1fs_t008_deliver_goods")
            scene sm1fs_t008-31 c2-mc-talk-dvh with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "You can count on me, Denise."
            scene sm1fs_t008-32 c2-dvh-talk-mc with dissolve
            play voice3 girl34_arrogant_ha4 noloop
            dvh "Realists know they can only count on themselves."
            dvh "And even then, we can only count on ourselves half the time."
            scene sm1fs_t008-33 c2-dvh-talk with dissolve
            play voice3 girl34_arrogant_ugu1 noloop
            dvh "You will either succeed, or you will fail, [mcname]."
            dvh "Be content with that."
            scene sm1fs_t008-34 c2-tl-talk with dissolve
            play voice4 girl24_arrogant_kgh1 noloop
            tl "And people say I'm a bitch."
            scene sm1fs_t008-35 c2-dvh-talk-tl with dissolve
            play voice3 girl34_hey_angry7 noloop
            dvh "I heard that."
            scene sm1fs_t008-36 c2-tl-talk-mc with dissolve
            play voice4 girl24_thinking_emm2 noloop
            tl "You better figure out a piece, [mcname]."

        "Why the time limit?" (hint="sm1fs_t008_m02_h03"):
            $ player.set_choice("sm1fs_t008_time_limit")
            scene sm1fs_t008-37 c3-mc-talk-dvh with dissolve
            play voice2 mc_surprised_why2 noloop
            mc "Why the time limit?"
            scene sm1fs_t008-38 c3-dvh-talk-mc with dissolve
            play voice3 girl34_disappointed_huh noloop
            dvh "There is only so much time before your candle is snuffed out."
            scene sm1fs_t008-39 c3-mc-talk-dvh with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "Sure, but like, usually people have more than thirty minutes to prepare to know a script completely."
            scene sm1fs_t008-40 c3-dvh-talk-mc with dissolve
            play voice3 girl34_arrogant_huh3 noloop
            dvh "Are you giving up already, [mcname]?"
            scene sm1fs_t008-37 c3-mc-talk-dvh with dissolve
            play voice2 mc_no_no2 noloop
            mc "No. I can do this. I'm just..."
            scene sm1fs_t008-38 c3-dvh-talk-mc with dissolve
            play voice3 girl34_arrogant_pff noloop
            dvh "Just...{w} wasting my time?"
            scene sm1fs_t008-41 c3-tl-talk-mc with dissolve
            play voice4 girl24_thinking_huh1 noloop
            tl "Come on, [mcname]. Forget about her."
            tl "She must be having her time of the month or some shit."
            scene sm1fs_t008-42 c3-dvh-talk-tl with dissolve
            play voice3 girl34_angry_argh4 noloop
            dvh "Taisia!"
            scene sm1fs_t008-43 c3-tl-talk-dvh with dissolve
            play voice4 girl24_arrogant_huh2 noloop
            tl "What? You sound ready to bite his head off."
            scene sm1fs_t008-44 c3-dvh-talk-tl with dissolve
            play voice3 girl34_angry_nergh noloop
            dvh "This is serious work."
            scene sm1fs_t008-45 c3-tl-talk-dvh with dissolve
            play voice4 girl24_arrogant_yeah1 noloop
            tl "It's community theater."
            scene sm1fs_t008-46 c3-dvh-talk with dissolve
            dvh "..."
            scene sm1fs_t008-47 c3-mc-talk-tl with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "I think my chances of passing this audition just got fucked."
            scene sm1fs_t008-48 c3-tl-talk-mc with dissolve
            play voice4 girl24_no_simple1 noloop
            tl "No way. She is too 'professional' to do that."
            tl "Denise will pass you if you deserve it, and fail you if you deserve that."
            scene sm1fs_t008-49 c3-mc-talk-tl with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Gee, thanks."
            scene sm1fs_t008-50 c3-tl-talk-mc with dissolve
            play voice4 girl24_yes_aga noloop
            tl "You got it."
            scene sm1fs_t008-51 c3-mc-talk-tl with dissolve
            play voice2 mc_angry_off noloop
            mc "I guess I should figure out which set to use."

    scene sm1fs_t008-52 mc-tl with dissolve
    pause
    scene sm1fs_t008-53 mc-talk-tl with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "I've got it."
    scene sm1fs_t008-54 tl-talk-mc with dissolve
    play voice4 girl24_disappointed_eeh2 noloop
    tl "Finally."
    scene sm1fs_t008-55 mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Number Sixteen."
    scene sm1fs_t008-56 tl-talk-mc with dissolve
    play voice4 girl24_surprised_what2 noloop
    tl "Really?"
    scene sm1fs_t008-55 mc-talk-tl with dissolve
    mc "Come on. It's a classic."
    scene sm1fs_t008-56 tl-talk-mc with dissolve
    play voice4 girl24_arrogant_hah noloop
    tl "Alright."

    jump sm1fs_t008_later

label sm1fs_t008_later:

    scene black
    show screen scene_transition(_("Thirty minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1fs_t008-57 dvh-phone
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1fs_t008-58 mc-talk-dvh with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "We're ready, Denise."
    scene sm1fs_t008-59 dvh-talk-mc with dissolve
    play voice3 girl34_yes_yeap4 noloop
    dvh "Perfect."
    scene sm1fs_t008-60 dvh-talk-mc with dissolve
    play voice3 girl34_thinking_hmm5 noloop
    dvh "As the kids say. {w} Show me what you got."
    scene sm1fs_t008-61 mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "You got this."
    if player.get_choice("pirates_movie_done") or player.get_choice("scifi_movie_done"):
        mct "I've done a role in a film."
        scene sm1fs_t008-62 mc-inner-talk with dissolve
        mct "This should be a piece of cake."
    else:
        mct "Just... deep breaths... don't freeze up."
    scene sm1fs_t008-63 mc-talk with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Pah pah pah."
    scene sm1fs_t008-64 mc-talk-tl with dissolve
    play voice2 mc_angry_oof noloop
    mc "Kick us off, Taisia."
    scene sm1fs_t008-65 tl-talk-mc with dissolve
    play voice4 girl24_hey_active noloop
    tl "Hey, what's your problem, Shrek?"
    tl "What do you got against the whole world anyhow?"
    scene sm1fs_t008-66 mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Look, I'm not the one with the problem."
    scene sm1fs_t008-67 mc-talk-tl with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "It's the world who seems to have a problem with me!"
    scene sm1fs_t008-68 mc-talk-tl with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "People take one look at me and go 'Ah help! Run! A big stupid ugly ogre."
    scene sm1fs_t008-69 mc-talk-tl with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "*sighs* They judge me even before they know me."
    mc "That's why I'm better off alone."
    scene sm1fs_t008-70 tl-talk-mc with dissolve
    play voice4 girl24_thinking_ah noloop
    tl "You know what, when we met, I didn't you think you was just a big stupid ugly ogre."
    scene sm1fs_t008-71 mc-talk-tl with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I know."
    scene sm1fs_t008-72 mc-tl-look-dvh with dissolve
    pause
    scene sm1fs_t008-73 dvh with dissolve
    pause
    scene sm1fs_t008-74 dvh-talk with dissolve
    dvh "..."
    scene sm1fs_t008-75 mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Oh man. Did she hate it?"
    scene sm1fs_t008-76 dvh-clap with dissolve
    "*clap clap clap*"
    scene sm1fs_t008-77 dvh-walk with dissolve
    pause
    scene sm1fs_t008-78 dvh-stand with dissolve
    pause
    scene sm1fs_t008-79 mc-talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Uhh."
    scene sm1fs_t008-80 dvh-talk-el with dissolve
    play voice3 girl34_hey_angry6 noloop
    dvh "Eileen!"
    scene sm1fs_t008-81 el-talk-dvh with hpunch
    play voice5 girl32_yes_questioning noloop
    ec "Yes, Denise?"
    mct "Where did she pop out from?"
    scene sm1fs_t008-82 dvh-talk-el with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    dvh "Eileen, please add [mcname] to our official acting rolls."
    scene sm1fs_t008-83 el-talk-dvh with dissolve
    play voice5 girl32_yes_yep noloop
    ec "Right away, Denise."
    scene sm1fs_t008-84 dvh-talk-mc with dissolve
    play voice3 girl34_happy_phew1 noloop
    dvh "People doubted me. But there is the proof."
    dvh "I have taken a lump of wet clay, formless, witless."
    scene sm1fs_t008-85 mc-talk-dvh with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "Hey..."
    scene sm1fs_t008-86 dvh-talk-mc with dissolve
    play voice3 girl34_happy_nice4 noloop
    dvh "And turned this simpleton into an actor for the stage."
    scene sm1fs_t008-87 dvh-talk-mc with dissolve
    play voice3 girl34_happy_mmm1 noloop
    dvh "[mcname], it is my pleasure to welcome you to be an actor in our troupe."
    dvh "That piece was done flawlessly. You brought me right back to the moment I first heard them spoken."
    scene sm1fs_t008-86 dvh-talk-mc with dissolve
    play voice3 girl34_happy_relief2 noloop
    dvh "Kudos."
    dvh "You have the heat. I can see it clearly now."
    scene sm1fs_t008-88 mc-talk-dvh with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "So that means I pass?"
    scene sm1fs_t008-91 dvh-talk-mc with dissolve
    play voice3 girl34_yes_neutral5 noloop
    dvh "Yes. If you want it, I am prepared to add you to the acting roster."
    scene sm1fs_t008-92 mc-talk-dvh with dissolve
    play voice2 d9s2_ugu noloop volume 1.7
    mc "Nothing would make me-"
    scene sm1fs_t008-93 dvh-talk-mc with dissolve
    play voice3 girl34_angry_breath1 noloop
    dvh "Unless, of course, you have been ignoring my rules."
    scene sm1fs_t008-94 mc-talk-dvh with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    scene sm1fs_t008-95 dvh-talk-mc with dissolve
    play voice3 girl34_thinking_hmm4 noloop
    dvh "I did tell you when we first started out..."
    dvh "That the theater is not a place for debacherous sex, [mcname]."
    scene sm1fs_t008-96 dvh-talk-mc with dissolve
    play voice3 girl34_angry_ahem1 noloop
    dvh "Have you been sullying my actresses, [mcname]?"
    menu:
        "Lie" (hint="sm1fs_t008_m03_h01"):
            $ player.set_choice("sm1fs_t008_lie")

        "Truth" (hint="sm1fs_t008_m03_h02"):
            $ player.set_choice("sm1fs_t008_truth")
            scene sm1fs_t008-97 mc-talk-dvh with dissolve
            play voice2 d2s12_emmm noloop
            mc "Denise I-"

    scene sm1fs_t008-98 dvh-talk-mc with dissolve
    play voice3 girl34_angry_dough noloop
    dvh "Hold that thought."
    scene sm1fs_t008-99 dvh-talk with dissolve
    play voice3 girl34_disappointed_mmf4 noloop
    dvh "Hmm."
    scene sm1fs_t008-100 dvh-talk with dissolve
    play voice3 girl34_yes_yeah3 noloop
    dvh "Of course, Ms. Moretti."
    dvh "Yes, we are very happy to hear that."
    scene sm1fs_t008-101 dvh-talk with dissolve
    play voice3 girl34_disappointed_oh1 noloop
    dvh "Ah, you are very kind."
    scene sm1fs_t008-102 tl-talk-dvh with dissolve
    play voice4 girl24_hey_simple noloop
    tl "Hey so [mcname] is one of us, right?"
    scene sm1fs_t008-103 dvh-talk-tl with dissolve
    play voice3 girl34_yes_neutral3 noloop
    dvh "Yes. And during our next rehearsals, they'll be understudying for Kai."
    scene sm1fs_t008-104 mc-talk with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "Awesome."
    scene sm1fs_t008-105 dvh-talk with dissolve
    play voice3 girl34_thinking_emm5 noloop
    dvh "Sorry about that, Ms. Moretti."
    scene sm1fs_t008-106 tl-talk with dissolve
    play voice4 girl24_happy_laugh1 noloop
    tl "Haha!"
    scene sm1fs_t008-107 mc-inner-talk with dissolve
    play voice2 mc_pain_auh1 noloop
    mct "Bah!"
    scene sm1fs_t008-108 tl-talk-mc with dissolve
    play voice4 girl24_thinking_hmm4 noloop
    tl "Not bad, [mcname]."
    tl "Denise doesn't give too many second chances."
    scene sm1fs_t008-109 km-talk-tl with dissolve
    play voice5 girl31_yes_simple1 noloop
    km "Yes."
    if player.has_played_scene("sm1cs_km005"):
        scene sm1fs_t008-110 km-talk-mc with dissolve
        play voice5 girl31_thinking_mmm7 noloop
        km "Maybe she realized that there is more to you than meets the eye."
        km "I know I did."
        if player.has_played_scene("sm1cs_vs005"):
            scene sm1fs_t008-111 vs-talk-mc with dissolve
            play voice4 girl33_happy_laugh1 noloop
            vs "Just make sure all of our little adventures stay a secret."
            scene sm1fs_t008-112 km-talk-vs with dissolve
            play voice5 girl31_angry_cough4 noloop
            km "Then it might be good if you don't say them on stage, Veronica."
            scene sm1fs_t008-113 vs-talk-km with dissolve
            play voice4 girl33_surprised_oh noloop
            vs "Oh yeah."
            vs "Duh."
    if player.has_played_scene("sm1cs_vs003"):
        scene sm1fs_t008-111 vs-talk-mc with dissolve
        play voice4 girl33_happy_laugh2 noloop
        vs "Just be sure to keep your nose clean."
        vs "Remember, even if Denise asks, you've never had sex in the theater."
        scene sm1fs_t008-114 km-talk-vs with dissolve
        play voice5 girl31_surprised_what3 noloop
        km "What?"
        km "Of course, that would be his answer. He wouldn't have to lie."
        scene sm1fs_t008-115 km-talk-mc with dissolve
        play voice5 girl31_surprised_uh2 noloop
        km "Right, [mcname]?"
        scene sm1fs_t008-116 tl-talk-km with dissolve
        play voice3 girl24_thinking_hmm1 noloop
        tl "Come on, Kellie. We've all bent a rule now and then."
        scene sm1fs_t008-117 km-talk-tl with dissolve
        play voice5 girl31_no_uhuh noloop
        km "Not me."
        play voice3 girl24_arrogant_kgh2 noloop
        tl "Sure..."
    scene sm1fs_t008-118 km-talk-mc with dissolve
    play voice5 girl31_hey_excited noloop
    km "Well, either way, you should be congratulated for becoming part of the acting team, [mcname]."
    km "But just remember. An audition is one thing. When you're out on the stage with the audience out there in front of you..."
    scene sm1fs_t008-119 km-talk-mc with dissolve
    play voice5 girl31_happy_relief noloop
    km "It's like you've entered into a new world."
    km "A glorious."
    scene sm1fs_t008-120 km-talk-mc with dissolve
    play voice5 girl31_angry_ergh7 noloop
    km "And sometimes terrifying world."
    scene sm1fs_t008-121 mc-talk-km with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks, Kellie. I'll remember that."
    scene sm1fs_t008-122 vs-talk-hug-mc with dissolve
    play voice4 girl33_happy_woohoo noloop
    vs "Woohoo."
    scene sm1fs_t008-123 vs-talk-mc with dissolve
    play voice4 girl33_hey_involved noloop
    vs "And too think, just a little while ago you didn't even know what a script was."
    scene sm1fs_t008-124 mc-talk-vs with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I don't think that was me, Veronica."
    scene sm1fs_t008-125 vs-talk with dissolve
    play voice4 girl33_arrogant_huh1 noloop
    vs "Really? Hmmm. Maybe it was me."
    vs "Either way."
    scene sm1fs_t008-126 vs-talk-mc with dissolve
    play voice4 girl33_happy_yay noloop
    vs "Welcome to the acting roster, [mcname]."
    scene sm1fs_t008-127 mc-talk with dissolve
    $ SMGallery.unlock_gallery_slot("achievement", "04_CROWNING_IS_A_STAGE")
    play voice2 mc_disappointed_ah2 noloop
    mc "Thanks, everyone."
    mc "I should head on home."
    mc "This is exciting but I feel pretty drained."
    scene sm1fs_t008-128 km-talk-mc with dissolve
    play voice5 girl31_yes_aga noloop
    km "Of course. Just make sure to be ready for the next practice."
    scene sm1fs_t008-129 mc-talk-km with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "I will."

    $ StoryController.end_scene(THEATER_STORY_LINE, 1, 30, 1)
    return
