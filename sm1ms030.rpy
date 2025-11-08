
define image_dissolve_ms030_66 = ImageDissolve("images/MS/s030/transitions/sm1ms030-66 post_credit_scene_sb_talk_samiyaappears_transition.png", 2.0, ramplen=8, reverse=False, alpha=True, time_warp=None)

label sm1ms030:

    scene sm1ms030-00 post_credit_scene with dissolve
    pause
    scene sm1ms030-01 post_credit_scene_eyesopen with dissolve
    pause
    scene sm1ms030-02 post_credit_scene_pullback_darkness with dissolve
    pause
    scene sm1ms030-03 post_credit_scene_pirateship with dissolve
    pause
    scene sm1ms030-03-1 post_credit_scene_pirateship with dissolve
    pause
    scene sm1ms030-04 post_credit_scene_sytalk_pirateship with dissolve
    sy "Pirate ship?"
    scene sm1ms030-05 post_credit_scene_sytalk_pirateship_alien with dissolve
    sy "Alien planet? Are we filming?"
    scene sm1ms030-05-3 post_credit_scene_sytalk_pirateship_alien with dissolve
    sy "Or am I dreaming we're filming?"
    scene sm1ms030-05-2 post_credit_scene_sytalk_pirateship_alien with dissolve
    pause
    scene sm1ms030-06 post_credit_scene_zp_talk_zemfira_appears with dissolve
    zp "Nope!"
    scene sm1ms030-07 post_credit_scene_sy_talk_zemfira_appears with dissolve
    sy "Ah! Zemfira!"
    scene sm1ms030-08 post_credit_scene_sy_talk_zemfira_appears with dissolve
    sy "How is Taboo University going?"
    scene sm1ms030-09 post_credit_scene_zp_talk with dissolve
    zp "Really good. Things are really heating up with the investigation."
    scene sm1ms030-10 post_credit_scene_zp_talk_kinkysmile with dissolve
    zp "My last scene was incredible!"
    scene sm1ms030-11 post_credit_scene_sy_talk_ with dissolve
    sy "Yeah, it was."
    scene sm1ms030-12 post_credit_scene_sy_talk_clap with dissolve
    sy "Ready for a new post-credits scene?"
    scene sm1ms030-13 post_credit_scene_zp_talk_excited with dissolve
    zp "Hell yes!"
    scene sm1ms030-15 post_credit_scene_sy_talk_fingerhead with dissolve
    sy "Nice. First things first. I need a different outfit!"
    scene sm1ms030-16 post_credit_scene_sy_talk_closeeyes with dissolve
    sy "My sexy swimwear!"
    scene sm1ms030-17 post_credit_scene_sy_talk_closeeyes_naked with dissolve
    pause
    scene sm1ms030-18 post_credit_scene_sy_talk_closeeyes_swimsuit1 with dissolve
    pause
    scene sm1ms030-17 post_credit_scene_sy_talk_closeeyes_naked with dissolve
    pause
    scene sm1ms030-19 post_credit_scene_sy_talk_closeeyes_swimsuit2 with dissolve
    pause
    scene sm1ms030-17 post_credit_scene_sy_talk_closeeyes_naked with dissolve
    pause
    scene sm1ms030-20 post_credit_scene_sy_talk_closeeyes_swimsuit3 with dissolve
    pause
    scene sm1ms030-21 post_credit_scene_sy_talk with dissolve
    sy "That's better!"
    scene sm1ms030-22 post_credit_scene_zp_talk with dissolve
    zp "Should I change?"
    scene sm1ms030-23 post_credit_scene_sy_talk with dissolve
    sy "I got you!"
    scene sm1ms030-24 post_credit_scene_sy_talk_thinking with dissolve
    pause
    scene sm1ms030-25 post_credit_scene_zp_talk_naked with dissolve
    pause
    scene sm1ms030-26 post_credit_scene_zp_talk_naked with dissolve
    pause
    scene sm1ms030-27 post_credit_scene_zp_talk_bdsm with dissolve
    pause
    scene sm1ms030-28 post_credit_scene_zp_talk_lookself with dissolve
    pause
    scene sm1ms030-29 post_credit_scene_zp_talk with dissolve
    zp "This is not one of my outfits, Stacy."
    scene sm1ms030-30 post_credit_scene_sy_talk with dissolve
    sy "Yeah, but it suits you."
    sy "Plus, this is the S&M Studio ending after all."
    scene sm1ms030-31 post_credit_scene_zp_talk_accepts with dissolve
    zp "Okay, since you just finished a game, I'll let you have this one."
    scene sm1ms030-32 post_credit_scene_sy_talk_heart with dissolve
    sy "Thanks!"
    scene sm1ms030-33 post_credit_scene_zp_talk with dissolve
    zp "Do we wait for someone?"
    scene sm1ms030-34 post_credit_scene_sy_talk with dissolve
    sy "Yes, Daisy should be here!"
    scene sm1ms030-35 post_credit_scene_zp_talk with dissolve
    zp "Why?"
    scene sm1ms030-36 post_credit_scene_sy_talk with dissolve
    sy "She always joins my post-credits scenes!"
    scene sm1ms030-37 post_credit_scene_sy_talk_daisy with dissolve
    dd "Wouldn't miss it for the world!"
    scene sm1ms030-38 post_credit_scene_sy_talk with dissolve
    sy "AAAA! Daisy!"
    scene sm1ms030-39 post_credit_scene_sy_talk_holdinghands with dissolve
    sy "I'm so happy to see you!"
    scene sm1ms030-40 post_credit_scene_dd_talk_holdinghands with dissolve
    dd "Me too! Love you, babe!"
    scene sm1ms030-41 post_credit_scene_dd_talk_looks with dissolve
    dd "Are we doing another post-credits scene?"
    scene sm1ms030-42 post_credit_scene_sy_talk with dissolve
    sy "Yes. We just finished Fetish Locator S&M Studio Season One."
    scene sm1ms030-43 post_credit_scene_zp_talk with dissolve
    zp "What a mouthful."
    scene sm1ms030-44 post_credit_scene_sy_talk_laugh with dissolve
    sy "Oh, I got plenty of those this season."
    scene sm1ms030-45 post_credit_scene_dd_talk with dissolve
    dd "So?{w} How was it? Is S&M just another Fetish Locator game?"
    scene sm1ms030-46 post_credit_scene_sy_talk with dissolve
    sy "Oh no! It's so much more!"
    sy "We have a whole city full of characters! Jobs to do, girls to date, movies to film!"
    if player.get_choice("pirates_movie_done"):
        scene sm1ms030-47 post_credit_scene_zp_talk with dissolve
        zp "Right. I saw the first movie. Taisia looks hot as a pirate."
        scene sm1ms030-48 post_credit_scene_sy_talk with dissolve
        sy "Yeah, she does."
    if player.get_choice("scifi_movie_done"):
        scene sm1ms030-47 post_credit_scene_zp_talk with dissolve
        zp "Nari was amazing as the alien in your sci-fi movie."
        scene sm1ms030-48 post_credit_scene_sy_talk with dissolve
        sy "Yeah, she was."
    scene sm1ms030-49 post_credit_scene_zp_talk with dissolve
    zp "You've made two movies so far. Is that it?"
    scene sm1ms030-50 post_credit_scene_sy_talk_ddexcited with dissolve
    sy "Of course not.{w} We're going to make a bunch more in Season Two!"
    scene sm1ms030-51 post_credit_scene_dd_talk with dissolve
    dd "That sounds great!"
    scene sm1ms030-52 post_credit_scene_sy_talk with dissolve
    sy "It is! We had so much fun making this game!"
    scene sm1ms030-53 post_credit_scene_dd_talk with dissolve
    dd "Okay, can I join?"
    scene sm1ms030-54 post_credit_scene_sy_talk_thinking with dissolve
    sy "Maybe."
    scene sm1ms030-55 post_credit_scene_dd_talk with dissolve
    dd "Maybe?"
    scene sm1ms030-56 post_credit_scene_sy_talk_explaining with dissolve
    sy "Well, the cast is already pretty big. We only had one spot in Season One for a returning character, and Min won the popular vote."
    scene sm1ms030-57 post_credit_scene_dd_talk_remembering with dissolve
    dd "Oh, yeah."
    dd "She beat me."
    scene sm1ms030-58 post_credit_scene_dd_talk_playfulmad with dissolve
    dd "I'll get you for that, Min. Somehow."
    scene sm1ms030-59 post_credit_scene_sy_talk_laughing with dissolve
    sy "Haha."
    scene sm1ms030-60 post_credit_scene_zp_talk with dissolve
    zp "Can I also join the vote?"
    scene sm1ms030-61 post_credit_scene_sy_talk_sorryface with dissolve
    sy "I think it's only for characters from the original Fetish Locator trilogy. Sorry!"
    scene sm1ms030-62 post_credit_scene_zp_talk_toocool with dissolve
    zp "Heh, whatever. I have enough fun in TU anyway."
    scene sm1ms030-63 post_credit_scene_dd_talk_checkin with dissolve
    dd "So there will be a vote for a character from the original Fetish Locator to join the cast for Season Two?"
    scene sm1ms030-64 post_credit_scene_sy_talk with dissolve
    sy "Exactly!"
    scene sm1ms030-65 post_credit_scene_dd_talk_thumbsup with dissolve
    dd "Okay, I'm in!"
    #sm1ms030-66 post_credit_scene_sb_talk_samiyaappears_transition
    scene sm1ms030-66 post_credit_scene_sb_talk_samiyaappears with image_dissolve_ms030_66
    pause
    scene sm1ms030-67 post_credit_scene_sb_talk with dissolve
    sb "Hold your horses, Diamond girl!"
    scene sm1ms030-68 post_credit_scene_sb_talk_fontstacy with dissolve
    sb "You're not the only one who wants to join!"
    scene sm1ms030-69 post_credit_scene_sy_talk_surprised with dissolve
    sy "Oh! Samiya! You want in, too?"
    scene sm1ms030-70 post_credit_scene_sb_talk with dissolve
    sb "Damn straight. This is where the party's at, after all."
    scene sm1ms030-71 post_credit_scene_sb_talk_smiledd with dissolve
    sb "So you may as well toss in the towel now, Daisy."
    scene sm1ms030-72 post_credit_scene_dd_talk_battke with dissolve
    dd "I never quit."
    sb "We'll see about that."
    scene sm1ms030-73 post_credit_scene_dd_talk_super with dissolve
    pause
    scene sm1ms030-76 post_credit_scene_sb_talk_charge with dissolve
    pause
    scene sm1ms030-77 post_credit_scene_zp_talk_breakup_turnofffire with dissolve
    zp "Okay, okay! Girls don't fight!"
    scene sm1ms030-78 post_credit_scene_zp_talk_turnstacy with dissolve
    zp "So where will this vote be? I wanna vote."
    scene sm1ms030-79 post_credit_scene_sy_talk_patreon with dissolve
    sy "It depends on our Supporters of course!"
    scene sm1ms030-80 post_credit_scene_zp_talk_thinking with dissolve
    zp "I guess I can make some time to vote."
    scene sm1ms030-81 post_credit_scene_sy_talk_close with dissolve
    sy "Excellent...{w} You know..."
    scene sm1ms030-82 post_credit_scene_sy_talk_seductive with dissolve
    sy "Nothing turns me on more than people voting in our polls."
    scene sm1ms030-83 post_credit_scene_sy_talk_touchback with dissolve
    sy "You'll get to make your mark on S&M's development. That's hot, isn't it?"
    scene sm1ms030-84 post_credit_scene_zp_talk_lips with dissolve
    zp "So hot..."
    scene sm1ms030-85 post_credit_scene_zp_talk with dissolve
    zp "Mmm."
    scene sm1ms030-86 post_credit_scene_zp_talk_kiss with dissolve
    pause
    scene sm1ms030-87 post_credit_scene_zp_talk_kiss with dissolve
    pause
    scene sm1ms030-89 post_credit_scene_sb_talk_syattention with dissolve
    sb "Yo, Stacy. What can we expect for Season Two of S&M Studio?"
    scene sm1ms030-90 post_credit_scene_sy_talk_distracted with dissolve
    sy "Huh?"
    scene sm1ms030-91 post_credit_scene_sy_talk_smiling with dissolve
    sy "Oh, yeah."
    scene sm1ms030-92 post_credit_scene_zp_talk_waving with dissolve
    zp "I should get back to TU."
    zp "The story is not going to finish itself."
    scene sm1ms030-93 post_credit_scene_sb_talk_girlswave with dissolve
    sb "Bye Zemfira. Love your whole vibe by the way."
    scene sm1ms030-94 post_credit_scene_zp_talk with dissolve
    zp "Thanks, Samiya."
    scene sm1ms030-95 post_credit_scene_zp_talk_disappears with dissolve
    pause
    scene sm1ms030-96 post_credit_scene_sy_talk_snap with dissolve
    sy "Alright, let me get some help to talk up what is coming for Season Two."
    sy "Nari. April. If you please."
    scene sm1ms030-97 post_credit_scene_sy_talk_nari_am_appear with dissolve
    pause
    scene sm1ms030-98 post_credit_scene_ns_talk_excited with dissolve
    ns "Oh, whoa!"
    scene sm1ms030-99 post_credit_scene_am_talk with dissolve
    am "What is this?"
    scene sm1ms030-100 post_credit_scene_ns_talk_explaining with dissolve
    ns "It's a post-credits scene."
    scene sm1ms030-101 post_credit_scene_ns_talk_wavesy with dissolve
    ns "Hi, Stacy!"
    scene sm1ms030-102 post_credit_scene_sy_talk_wave with dissolve
    sy "Hi, Nari. Can you two talk about our plans for Season Two?"
    scene sm1ms030-103 post_credit_scene_ns_talk_excited with dissolve
    ns "Sure!"
    scene sm1ms030-104 post_credit_scene_ns_talk_thinking with dissolve
    ns "So, in Season Two, we're going to see if the Orbix workers can overcome their differences and put the product out on time."
    scene sm1ms030-105 post_credit_scene_am_talk with dissolve
    am "Yawn."
    scene sm1ms030-106 post_credit_scene_am_talk_fist with dissolve
    am "I want to talk about my content in Season Two!"
    scene sm1ms030-107 post_credit_scene_am_talk_point with dissolve
    am "I'd better get to be in the movies!"
    scene sm1ms030-108 post_credit_scene_ns_talk_looks with dissolve
    ns "Who are you talking to?"
    scene sm1ms030-109 post_credit_scene_am_talk_smiling with dissolve
    am "The powers in the dark."
    scene sm1ms030-110 post_credit_scene_ns_talk_looks with dissolve
    ns "Oh, you're mad that you didn't get to be in the movies yet."
    scene sm1ms030-111 post_credit_scene_am_talk_bummed with dissolve
    am "Yeah! Taisia got to be in two. You got to be in one."
    am "I got squat."
    scene sm1ms030-112 post_credit_scene_ns_talk_hug with dissolve
    ns "Don't worry, April. I'm sure the team will have you in one."
    scene sm1ms030-113 post_credit_scene_am_talk with dissolve
    am "Thanks, Nari. You're really all right, aren't you?"
    scene sm1ms030-114 post_credit_scene_ns_talk_smiling with dissolve
    ns "I try."
    scene sm1ms030-115 post_credit_scene_dvh_talk_ns_am_lookaround with dissolve
    dvh "April and Nari exit stage left."
    scene sm1ms030-116 post_credit_scene_am_talk with dissolve
    am "What the hell?"
    scene sm1ms030-117 post_credit_scene_ns_talk_ns_am_vanish with dissolve
    pause
    scene sm1ms030-118 post_credit_scene_ns_talk_ns_am_vanish with dissolve
    pause
    scene sm1ms030-119 post_credit_scene_dvh_talk_appear_dress with dissolve
    dvh "..."
    scene sm1ms030-120 post_credit_scene_sy_talk_questioning with dissolve
    sy "Denise? How did you get here?"
    scene sm1ms030-121 post_credit_scene_dvh_talk_smile with dissolve
    dvh "The Mistress of the Theater always has a few tricks up her sleeve."
    scene sm1ms030-122 post_credit_scene_dvh_talk_pose with dissolve
    dvh "And I will not be denied my time in the spotlight."
    scene sm1ms030-123 post_credit_scene_dvh_talk_lookcamera with dissolve
    dvh "For Season Two, we will finally see if our leading man has the chops for the stage."
    scene sm1ms030-124 post_credit_scene_dvh_talk_smile with dissolve
    dvh "But of course, the main event will be my first sex scene!"
    dvh "Rest assured, the audience will give me a standing ovation."
    scene sm1ms030-125 post_credit_scene_dvh_talk_bow with dissolve
    dvh "It will be a tour de force, hitherto unseen in the Fetish Locator universe."
    pause
    scene sm1ms030-126 post_credit_scene_sy_talk_rolleyes with dissolve
    sy "And people call me dramatic."
    scene sm1ms030-127 post_credit_scene_sy_talk_snap with dissolve
    sy "Thanks, Denise."
    scene sm1ms030-128 post_credit_scene_sy_talk_snap with dissolve
    "*snap*"
    scene sm1ms030-129 post_credit_scene_sy_talk_staff_focus with dissolve
    sy "Alright. That's enough of that."
    scene sm1ms030-130 post_credit_scene_sy_talk_staff_focus with dissolve
    sy "Here is a quick recap of everything to expect from Fetish Locator S&M Studio..."
    scene sm1ms030-131 post_credit_scene_sy_talk_twofingers with dissolve
    sy "Season Two!"
    pause
    scene sm1ms030-132 post_credit_scene_sy_talk_slam with dissolve
    pause
    scene sm1ms030-133 post_credit_scene_sy_talk_slamground with vpunch
    pause
    scene sm1ms030-134 post_credit_scene_sy_talk_portal with dissolve
    dd "Oooh."
    scene sm1ms030-135 post_credit_scene_my_talk_emerges with dissolve
    pause
    scene sm1ms030-136 post_credit_scene_my_talk_pose with dissolve
    my "More movies. Pirates and Sci-Fi were just the beginning!"
    my "The team is hard at work coming up with more scintillating stories to explore on the silver porn screen."
    scene sm1ms030-137 post_credit_scene_ef_talk_elina with dissolve
    pause
    scene sm1ms030-138 post_credit_scene_ef_talk_elina_sexypose with dissolve
    ef "There are two new factions planned for Season Two."
    scene sm1ms030-139 post_credit_scene_ef_talk_wink with dissolve
    ef "One has a lot of black leather and lace."
    ef "The other is where fortunes are made and lost."
    scene sm1ms030-140 post_credit_scene_sy_talk_camera_staffgone with dissolve
    sy "And, of course,"
    sy "There will be tons of sex scenes in the new season!"
    scene sm1ms030-141 post_credit_scene_dd_talk_excited with dissolve
    dd "Excellent. I can't wait for it."
    scene sm1ms030-142 post_credit_scene_sb_talk_chimingin with dissolve
    sb "And the Patreon poll!"
    scene sm1ms030-143 post_credit_scene_my_talk_wave with dissolve
    my "Until then, thank you all so much for playing our game."
    scene sm1ms030-144 post_credit_scene_my_talk_blowkiss with dissolve
    pause
    scene sm1ms030-145 post_credit_scene_my_talk_blowkiss with dissolve
    my "Mwah!"
    scene sm1ms030-146 post_credit_scene_all_talk_cameraaway with dissolve
    "Everyone" "Thank you!"
    scene sm1ms030-147 post_credit_scene_all_talk_cameraaway with dissolve
    "Everyone" "See you in Season Two!"

    $ StoryController.end_scene(MS)
    return
