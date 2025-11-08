label sm1cs_mes_r1:

    if player.has_played_scene("sm1cs_mes_r1"):
        jump sm1cs_mes_r1_repeat
    else:
        jump sm1cs_mes_r1_initiator

label sm1cs_mes_r1_initiator:

    scene sm1cs-mes-r1-01 mc-enters-mes-room_c1 with dissolve
    pause
    scene sm1cs-mes-r1-02 mes-speaking-herself-korean-mc-you-okay_c1 with dissolve
    mes "{font=fonts/notosanskr-medium.ttf}...이게 무슨 개소리야...{/font}"
    mc "Min? You okay?"
    scene sm1cs-mes-r1-03 mes-snaps-back-fine-just_c1 with dissolve
    mes "I'm fine! Just—"
    scene sm1cs-mes-r1-04 mes-looks-down-regretful_c1 with dissolve
    pause
    scene sm1cs-mes-r1-05 mes-look-up-sigh-sorry-mc-what-going-on_c1 with dissolve
    mes "*sighs heavily* Sorry. I didn't mean to snap at you."
    mc "What's going on?"
    scene sm1cs-mes-r1-06 mes-just-everything-mes-brain-wont-shut-down_c1 with dissolve
    mes "It's just...everything. School, my parents constantly calling, second-guessing every decision I've made."
    mes "My brain won't shut up, [mcname]. It's like I'm drowning in my own thoughts."
    scene sm1cs-mes-r1-07 mc-when-last-break-mes-hah-what-break_c1 with dissolve
    mc "When's the last time you took a break?"
    mes "*laughs bitterly* What's a break? I don't remember."
    scene sm1cs-mes-r1-08 mes-looks-vulnerably-mc_c1 with dissolve
    pause
    scene sm1cs-mes-r1-09 mes-hungry-look-mes-need-stop-thinking-can-help-forget_c1 with dissolve
    mes "I just need to...stop thinking for a while."
    mes "Can you help me forget everything? Just for tonight?"
    scene sm1cs-mes-r1-10 mc-cmere_c1 with dissolve
    mc "C'mere."

    jump sm1cs_mes_r1_continue

label sm1cs_mes_r1_repeat:

    scene sm1cs-mes-r1-11 mc-enters-room-mes-pacing-nervous_c1 with dissolve
    pause
    scene sm1cs-mes-r1-12 mes-hey-mc-hey-yourself-look-tense_c1 with dissolve
    mes "Hey."
    mc "Hey yourself. You look tense."
    scene sm1cs-mes-r1-13 mes-long-day-mc-want-talk-about-it_c1 with dissolve
    mes "Long day."
    mc "Want to talk about it?"
    scene sm1cs-mes-r1-14 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Ask what happened" (hint="sm1cs_mes_r1_m00_h01"):
            $ player.set_choice("sm1cs_mes_r1_what_happened")
            scene sm1cs-mes-r1-18 choice-do-need-mc-do-need-me-to-mes-always-direct_c1 with dissolve
            mc "What happened?"
            scene sm1cs-mes-r1-15 choice-what-happened-mes-final-prep-mother-called-during-break_c1 with dissolve
            mes "Finals prep. My professor seems to think we're all superhuman."
            mes "And then my mother called during my lunch break."
            scene sm1cs-mes-r1-16 mes-wanted-know-what-done-wasting-mc-ouch_c1 with dissolve
            mes "She wanted to know if I was done \"wasting my potential\" yet."
            mc "Ouch."
            scene sm1cs-mes-r1-17 mes-yes-ouch_c1 with dissolve
            mes "Yeah. Ouch."

        "Ask if she needs you" (hint="sm1cs_mes_r1_m00_h02"):
            $ player.set_choice("sm1cs_mes_r1_needs_me")
            scene sm1cs-mes-r1-18 choice-do-need-mc-do-need-me-to-mes-always-direct_c1 with dissolve
            mc "Do you need me?"
            mes "Always so direct."
            scene sm1cs-mes-r1-19 mes-soft-yes-need-you-need-make-brain-shut-up_c1 with dissolve
            mes "*softer* Yes. I need you."
            mes "I need you to make my brain shut the fuck up for a while."

    scene sm1cs-mes-r1-20 mes-can-we-mc-say-no-more_c1 with dissolve
    mes "Can we...?"
    mc "Say no more."

    jump sm1cs_mes_r1_continue

label sm1cs_mes_r1_continue:

    scene sm1cs-mes-r1-21 mes-expression-relief-anticipation_c1 with dissolve
    pause
    scene sm1cs-mes-r1-22 mc-guides-mes-towards-bed_c1 with dissolve
    pause
    scene sm1cs-mes-r1-23 mes-sits-edge-looks-mc-desire_c1 with dissolve
    pause
    scene sm1cs-mes-r1-24 mc-puts-hand-mes-chin-what-need-from-me_c1 with dissolve
    mc "What do you need from me tonight, Min?"
    scene sm1cs-mes-r1-25 mes-melting-need-stop-being-perfect-daughter-need-stop-thinking-expectations_c1 with dissolve
    mes "I need to stop being the perfect daughter. The brilliant student."
    mes "I need to stop thinking about what everyone expects."
    scene sm1cs-mes-r1-26 mes-pulls-mc-by-shirt_c1 with dissolve
    pause
    scene sm1cs-mes-r1-27 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Tell me exactly what you need" (hint="sm1cs_mes_r1_m01_h01"):
            $ _sm1cs_mes_r1_gentle = True
            scene sm1cs-mes-r1-28 choice-gentle-mc-need-tell-what-need-words_c1 with dissolve
            mc "I need you to tell me exactly what you need. Use your words."
            scene sm1cs-mes-r1-29 mes-need-make-feel-good-forget-everything_c1 with dissolve
            mes "I need... I need you to make me feel good."
            mes "Make me forget everything except how you touch me."
            scene sm1cs-mes-r1-30 mes-make-yours-please_c1 with dissolve
            mes "Make me yours. Please?"
            scene sm1cs-mes-r1-31 mc-strokes-cheek-mc-that-good-girl_c1 with dissolve
            mc "That's my good girl. I'll take care of you."
            mc "But you have to keep talking. I want to hear every needy little sound."
            scene sm1cs-mes-r1-32 mes-closes-eyes-moans-can-do-that_c1 with dissolve
            mes "*soft moan* I can do that."

        "You don't need to think anymore tonight" (hint="sm1cs_mes_r1_m01_h02"):
            $ _sm1cs_mes_r1_gentle = False
            scene sm1cs-mes-r1-33 choice-domination-mc-dont-need-think-tonight_c1 with dissolve
            mc "You don't need to think anymore tonight."
            mc "I already know what you need."
            scene sm1cs-mes-r1-34 mes-flutter-yes-fuck-yes_c1 with dissolve
            mes "Yes...fuck, yes."
            scene sm1cs-mes-r1-35 mc-strip-get-on-bed-tonight-my-toy_c1 with dissolve
            mc "Strip. Get on the bed."
            mc "Tonight, you're just my toy. No thinking. No worrying."
            scene sm1cs-mes-r1-36 mes-starts-taking-off-clothes-yes-pls-use-however-want_c1 with dissolve
            mc "Just a pretty little fuckdoll for me to use."
            mes "God, yes. Please. Use me however you want."

    scene sm1cs-mes-r1-37 mes-takes-off-top_c1 with dissolve
    pause
    scene sm1cs-mes-r1-38 mes-takes-off-shorts_c1 with dissolve
    pause
    scene sm1cs-mes-r1-39 mes-takes-off-bra_c1 with dissolve
    pause
    scene sm1cs-mes-r1-40 mes-takes-off-panties_c1 with dissolve
    pause
    scene sm1cs-mes-r1-41 mes-naked-on-bed-please_c1 with dissolve
    mes "Please..."
    scene sm1cs-mes-r1-42 mc-undress-shirt_c1 with dissolve
    pause
    scene sm1cs-mes-r1-43 mc-takes-off-pants_c1 with dissolve
    pause
    scene sm1cs-mes-r1-44 mc-climbs-bed-mes-already-hard_c1 with dissolve
    mes "Fuck, you're already so hard for me."
    if _sm1cs_mes_r1_gentle is True:
        jump sm1cs_mes_r1_gentle
    else:
        jump sm1cs_mes_r1_rough

label sm1cs_mes_r1_gentle:

    scene sm1cs-mes-r1-45 gentle-path-mc-runs-fingers-tigh-mc-tell-how-feels_c1 with dissolve
    mc "Tell me how this feels."
    scene sm1cs-mes-r1-46 mc-reach-mes-pussy-mes-feels-amazing-mc-already-wet-me_c1 with dissolve
    mes "It feels... Oh God... It feels amazing."
    mc "You're already so wet for me. Were you thinking about this?"
    scene sm1cs-mes-r1-47 mes-nods-yes-all-day_c1 with dissolve
    mes "Yes... All day..."
    scene sm1cs-mes-r1-48 mc-slids-finger-in-mc-where-else-want-touch-mes-inside_c1 with dissolve
    mc "Where else do you want me to touch you?"
    mes "Inside... Please, I need you inside me..."
    scene sm1cs-mes-r1-49 mc-slits-second-finger-inside-mes-mc-like-this_c1 with dissolve
    mc "Like this?"
    mes "Yes! Just like that... Right there... Fuck..."
    scene sm1cs-mes-r1-50 mc-fingerbanging-mes-anim_c1 with dissolve
    pause
    scene sm1cs-mes-r1-56 mes-please-can-cum-mes-been-so-good-need-badly_c1 with dissolve
    mc "That's it. Use your words. Tell me how badly you need this."
    mes "I need it so badly. I need you so fucking badly, [mcname]."
    scene sm1cs-mes-r1-52 fingerbang-alt-angle-reverse-top-view_c3 with dissolve
    mes "Your fingers feel so good... Please don't stop..."
    mes "Fu— Fuck, I'm close..."
    scene sm1cs-mes-r1-53 fingerbang-alt-angle-low-side-view_c4 with dissolve
    mc "Not yet. You need to ask me nicely if you can cum."
    mes "*whimpering* No... Don't stop... Please..."
    scene sm1cs-mes-r1-54 fingerbang-alt-angle-closeup_c5 with dissolve
    mc "Ask. Nicely."
    mes "Please... Please can I cum for you?"
    scene sm1cs-mes-r1-55 fingerbang-alt-angle-cinematic-view_c6 with dissolve
    mes "I've been so good, I need it so badly..."
    scene sm1cs-mes-r1-57 mc-you-do-better_c1 with dissolve
    mc "You can do better than that."
    scene sm1cs-mes-r1-58 mes-desperate-begging-please-please-cum-fingers_c1 with dissolve
    mes "Please let me cum! I'll do anything, I just need to cum on your fingers!"
    mes "Please, [mcname], I'm begging you!"
    scene sm1cs-mes-r1-59 mc-good-girl-cum-for-me_c1 with dissolve
    mc "Good girl. Cum for me."
    scene sm1cs-mes-r1-60 mc-pushes-deeper-mes-thankyou-thankyou_c1 with hpunch
    mes "Oh fuck... Oh fuck yes... Thank you... Thank you..."
    scene sm1cs-mes-r1-61 mes-orgasming-fuuuck_c1 with vpunch
    mes "Fuuuuck..."

    jump sm1cs_mes_r1_continue_2

label sm1cs_mes_r1_rough:

    scene sm1cs-mes-r1-62 dom-path-mc-wraps-hand-around-mes-neck-mc-cum-when-say-got-it_c1 with dissolve
    mc "You cum when I say you can cum. Understand?"
    scene sm1cs-mes-r1-63 mes-yes-yes-understand_c1 with dissolve
    mes "Yes... Yes, Sir... I understand."
    scene sm1cs-mes-r1-64 mc-pushes-fingers-soaked-already-mes-only-your-slut_c1 with dissolve
    mc "You're fucking soaked already. Such a needy little slut."
    mes "Only for you... I'm only your slut..."
    scene sm1cs-mes-r1-65 mes-yes-yes-fuck-with-fingers_c1 with dissolve
    mc "That's right. My slut. My toy. My fuckmeat."
    scene sm1cs-mes-r1-50 mc-fingerbanging-mes-anim_c1 with dissolve
    mes "Oh God, oh God... I'm close... I'm so close..."
    scene sm1cs-mes-r1-52 fingerbang-alt-angle-reverse-top-view_c3 with dissolve
    mc "Not yet."
    scene sm1cs-mes-r1-53 fingerbang-alt-angle-low-side-view_c4 with dissolve
    mes "*frustrated whimper* Please! I was so close!"
    scene sm1cs-mes-r1-54 fingerbang-alt-angle-closeup_c5 with dissolve
    mc "And you'll get close again. And again. Until I decide you've earned it."
    scene sm1cs-mes-r1-55 fingerbang-alt-angle-cinematic-view_c6 with dissolve
    mes "Yes... Yes... Fuck me with your fingers..."
    mc "Beg for it."
    scene sm1cs-mes-r1-66 mc-beg-for-it-mes-please-let-cum_c1 with dissolve
    mes "Please! Please let me cum! I can't take it anymore!"
    scene sm1cs-mes-r1-67 mc-takes-fingers-out-not-good-enough_c1 with dissolve
    mc "Not good enough."
    scene sm1cs-mes-r1-68 mes-please-sir-do-anything-use-me-let-cum_c1 with dissolve
    mes "Please, Sir, please, I'll do anything! I need to cum so badly it hurts!"
    mes "Please use me, ruin me, just let me cum!"
    scene sm1cs-mes-r1-69 mc-evil-now-cum-now_c1 with dissolve
    mc "Now. Cum now."
    scene sm1cs-mes-r1-70 mc-pushes-again-fingers-inside-mes_c1 with dissolve
    pause
    scene sm1cs-mes-r1-71 mes-cums-finally-fuck-fuck-yes_c1 with vpunch
    mes "FUCK! FUCK YES!"
    scene sm1cs-mes-r1-72 mc-not-stopping-do-again-mes-cant-too-much_c1 with dissolve
    mc "One more. Give me one more right now."
    mes "I can't, I can't, it's too much—"
    scene sm1cs-mes-r1-73 mc-yes-you-can-cum-again_c1 with dissolve
    mc "Yes, you can. Cum again. Now."
    scene sm1cs-mes-r1-74 mes-cums-again-incoherent_c1 with vpunch
    mes "*incoherent crying out*"

    jump sm1cs_mes_r1_continue_2

label sm1cs_mes_r1_continue_2:

    scene sm1cs-mes-r1-75 mes-taking-breather-holy-shit_c1 with dissolve
    mes "Holy shit..."
    scene sm1cs-mes-r1-76 mc-gets-missionary-position-we-just-starting_c1 with dissolve
    mc "We're just getting started."
    scene sm1cs-mes-r1-77 mes-looks-mc-fucke-me-please-fuck-me_c1 with dissolve
    mes "Fuck me. Please drill my cunt, [mcname]."
    scene sm1cs-mes-r1-78 mc-opens-up_c1 with dissolve
    pause
    scene sm1cs-mes-r1-79 mc-pushes-in-pussy_c1 with dissolve
    mes "Oh fuck... You're so big... So fucking full..."
    if _sm1cs_mes_r1_gentle is True:
        scene sm1cs-mes-r1-80 mc-fucks-mes-missionary-anim_c1 with dissolve
        mc "You're so beautiful like this. So perfect for me."
        scene sm1cs-mes-r1-81 missionary-alt-angle-top-view_c2 with dissolve
        mes "Yes... Oh fuck yes..."
        mc "Tell me how it feels. I want to hear you."
        scene sm1cs-mes-r1-82 missionary-alt-angle-rear-view_c3 with dissolve
        mes "*moans* It feels amazing... You're so deep inside me..."
        mes "I can feel every inch of your cock..."
        scene sm1cs-mes-r1-83 missionary-alt-angle-over-shoulder-angle_c4 with dissolve
        mc "That's my good girl. Taking me so well."
        scene sm1cs-mes-r1-84 missionary-alt-angle-top-close-up-view_c5 with dissolve
        mes "Only for you... I'm only this good for you..."
        scene sm1cs-mes-r1-85 missionary-alt-angle-side-view_c6 with dissolve
        mc "Tell me when you're close. I want to feel you cum on my cock."
        scene sm1cs-mes-r1-86 gentle-path-mes-getting-close-fuck-hitting-deep_c1 with dissolve
        mes "*voice hitched* I'm getting close... Oh fuck, I'm getting so close..."
        mes "You're hitting me so deep...right there...keep going."
        scene sm1cs-mes-r1-87 mes-please-can-cum-for-you_c1 with dissolve
        mes "Please... Please can I cum for you?"
        scene sm1cs-mes-r1-88 mc-yes-cum-for-me-let-feel-it_c1 with dissolve
        mc "Yes. Cum for me. Let me feel it."
        scene sm1cs-mes-r1-89 mes-cums-again-yes-yes-yes-cumming-fuck_c1 with hpunch
        mes "Yes yes yes—! I'm cumming!"
        mes "Fuck!"
    else:
        scene sm1cs-mes-r1-80 mc-fucks-mes-missionary-anim_c1 with dissolve
        mc "This pussy belongs to me. You don't think, you don't worry."
        scene sm1cs-mes-r1-81 missionary-alt-angle-top-view_c2 with dissolve
        mc "You just lie there and take my cock like a good little fucktoy."
        scene sm1cs-mes-r1-82 missionary-alt-angle-rear-view_c3 with dissolve
        mes "*moans* Yes! It's yours! I'm yours! Use me!"
        scene sm1cs-mes-r1-83 missionary-alt-angle-over-shoulder-angle_c4 with dissolve
        mc "Such a desperate slut. You love being split open on my cock, don't you?"
        mes "Yes! I love it! I love being your slut!"
        scene sm1cs-mes-r1-84 missionary-alt-angle-top-close-up-view_c5 with dissolve
        mes "I'm going to cum... Fuck, I'm going to cum on your cock..."
        mc "Not yet."
        scene sm1cs-mes-r1-85 missionary-alt-angle-side-view_c6 with dissolve
        mes "*crying out* No! Please don't stop!"
        mc "You'll cum when your body can't take anymore. Not before."
        scene sm1cs-mes-r1-91 mc-fucks-her-again-mes-please-let-cum_c1 with dissolve
        mes "Please please please let me cum!"
        scene sm1cs-mes-r1-92 mc-edge-again-beg-convince-deserve-mes-i-do-anything_c1 with dissolve
        mc "Beg for me. Convince me you deserve it."
        mes "I'll do anything! I'm your toy, your fuckmeat, your personal cumdump!"
        scene sm1cs-mes-r1-93 mes-desperate-please-need-badly-cum_c1 with dissolve
        mes "Please let me cum, I need it so badly!"
        scene sm1cs-mes-r1-94 mc-chokes-mes-mc-cum-fucking-now_c1 with dissolve
        mc "Cum. Right fucking now."
        scene sm1cs-mes-r1-95 mes-has-another-orgasm-screams-fuck_c1 with vpunch
        mes "*nearly screaming* FUCK!"
        scene sm1cs-mes-r1-96 mc-not-stopping-again-mes-crying-cant-too-much-_c1 with dissolve
        mc "Again."
        mes "I can't... Too much... It's too much..."
        scene sm1cs-mes-r1-97 mc-merciless-again-of-keep-fucking-hours_c1 with dissolve
        mc "Yesm you can. Cum again or I'll keep fucking you like this for hours."
        scene sm1cs-mes-r1-98 mes-cums-final-time-barely-holding-together_c1 with vpunch
        mes "*sobbing with pleasure* I'm you're little sextoy."
    scene sm1cs-mes-r1-99 mes-trying-to-regain-composure_c1 with dissolve
    mes "*soft moaning*"
    scene sm1cs-mes-r1-100 mc-grabs-mes-drags-her-on-hands-knees_c1 with dissolve
    mc "On your hands and knees."
    scene sm1cs-mes-r1-101 mes-scrambles-obeys-orders_c1 with dissolve
    pause
    scene sm1cs-mes-r1-102 mes-presents-himself-please-need-more_c1 with dissolve
    mes "Please... I need more..."
    scene sm1cs-mes-r1-103 mc-positions-behind-mes_c1 with dissolve
    pause
    scene sm1cs-mes-r1-104 mc-slides-cock-inside-mes_c1 with dissolve
    mes "Oh fuck!"
    if _sm1cs_mes_r1_gentle is True:
        mc "Such a good girl for me. Taking everything I give you."
        scene sm1cs-mes-r1-105 mc-fucks-mes-doggystyle_c1 with dissolve
        pause
        scene sm1cs-mes-r1-106 doggystyle-alt-angle-pov-view_c2 with dissolve
        pause
        scene sm1cs-mes-r1-107 doggystyle-alt-angle-mes-front-view_c3 with dissolve
        pause
        scene sm1cs-mes-r1-108 doggystyle-alt-angle-over-shoulder-view_c4 with dissolve
        pause
        scene sm1cs-mes-r1-109 doggystyle-alt-angle-closeup-view_c5 with dissolve
        pause
        mes "*soft moans* Yes... just like that... perfect..."
        mc "You feel so good wrapped around my cock."
        mes "You're so deep... I can feel you in my stomach..."
        mc "You can cum whenever you need to. You've been such a good girl."
        mc "You've earned it."
        scene sm1cs-mes-r1-110 gentle-path-mes-oh-god-gonna-cum-again-feel-perfect_c1 with dissolve
        mes "Oh... oh god... I'm going to cum again..."
        mes "You feel so perfect inside me..."
        scene sm1cs-mes-r1-111 mes-cums-quietly-shuderring-fuuck_c1 with dissolve
        mes "*shuddering* Fu— Fuck..."
        scene sm1cs-mes-r1-112 mes-trembling-so-good-fucking-good_c1 with dissolve
        mes "So good... It's so fucking good..."
    else:
        mc "You wanted to forget everything? I'm going to fuck every thought out of your head."
        scene sm1cs-mes-r1-105 mc-fucks-mes-doggystyle_c1 with dissolve
        mes "Oh god!"
        scene sm1cs-mes-r1-106 doggystyle-alt-angle-pov-view_c2 with dissolve
        pause
        scene sm1cs-mes-r1-107 doggystyle-alt-angle-mes-front-view_c3 with dissolve
        pause
        scene sm1cs-mes-r1-108 doggystyle-alt-angle-over-shoulder-view_c4 with dissolve
        pause
        scene sm1cs-mes-r1-109 doggystyle-alt-angle-closeup-view_c5 with dissolve
        pause
        mes "Yes! Fuck my brains out! Make me your mindless slut!"
        mc "That's all you are right now. A tight wet hole for me to fuck."
        mes "Yes! That's all I am! Use me!"
        scene sm1cs-mes-r1-113 dom-path-mes-cums-legs-shaking-violently_c1 with dissolve
        mes "Fuck fuck fuck—"
        mc "Cum for me. Now."
        scene sm1cs-mes-r1-114 mes-squirts-oh-shit-i-squirting_c1 with dissolve
        mes "*legs shaking violently*"
        scene sm1cs-mes-r1-115 mc-groaning-fuck-yes-soak-bed_c1 with dissolve
        mc "Fuck yes. Soak the fucking bed. Show me what a messy slut you are."
        scene sm1cs-mes-r1-116 mes-still-fucked-cant-stop-cant-stop-cumming_c1 with dissolve
        mes "I can't stop... I can't stop cumming..."

    if player.get_choice("sm1cs_mes006_keep_watersports"):
        jump sm1cs_mes_r1_watersports
    else:
        jump sm1cs_mes_r1_continue_3

label sm1cs_mes_r1_watersports:

    scene sm1cs-mes-r1-117 mes-collapses-catching-breath_c1 with dissolve
    pause
    scene sm1cs-mes-r1-118 mes-wait-want-try-something-mc-what-had-mind_c1 with dissolve
    mes "Wait... I want to try something."
    mc "What did you have in mind?"
    mes "Remember... Our game night? What we did after?"
    scene sm1cs-mes-r1-119 mes-remember-game-night-what-did-after-mc-yeah_c1 with dissolve
    mc "Yeah..."
    scene sm1cs-mes-r1-120 mes-want-more-that-can-please-go-bathroom_c1 with dissolve
    mes "I want to do more of that. I've been thinking about it."
    mes "Can we go to the bathroom? Please?"
    scene sm1cs-mes-r1-121 mc-lead-the-way_c1 with dissolve
    mc "Lead the way."
    scene sm1cs-mes-r1-143 mes-mc-enter-bathroom_c1 with fade
    pause
    scene sm1cs-mes-r1-144 mc-turns-on-shower_c1 with dissolve
    pause
    scene sm1cs-mes-r1-145 mc-mes-make-out-under-shower_c1 with dissolve
    pause
    scene sm1cs-mes-r1-146 mes-drops-knees_c1 with dissolve
    pause
    scene sm1cs-mes-r1-147 mes-licks-mc-cock_c1 with dissolve
    pause
    scene sm1cs-mes-r1-148 mes-gives-bj-mc-anim_c1 with dissolve
    mes "*hungry sucking sounds*"
    mc "Fuck, Min... Your mouth feels amazing."
    scene sm1cs-mes-r1-149 bj-alt-angle-mes-gagging_c2 with dissolve
    mes "*gagging slightly, moaning*"
    scene sm1cs-mes-r1-150 bj-alt-angle-mc-pov_c3 with dissolve
    pause
    scene sm1cs-mes-r1-151 bj-alt-angle-mes-sucking-deep_c4 with dissolve
    pause
    scene sm1cs-mes-r1-153 mes-anticipates-begs-please_c1 with dissolve
    mes "I want you to pee on me again."
    mes "I've been thinking about it since last time... I need it."
    if _sm1cs_mes_r1_gentle is True:
        mes "Please? I want to feel it again..."
    else:
        mes "I need your piss all over me. Make your dirty little piss slut."
    scene sm1cs-mes-r1-152 mc-prepares-pee-mes_c1 with dissolve
    menu:
        "If you want it, you're going to take it" (hint="sm1cs_mes_r1_m02_h01"):
            mc "Open wide. If you want my piss, you're going to take all of it."
            scene sm1cs-mes-r1-153 mes-anticipates-begs-please_c1 with dissolve
            mes "Yes... I want it all..."
            scene sm1cs-mes-r1-154 mc-pees-mes-mouth-anim_c1 with dissolve
            mes "*gagging*"
            mc "Such a dirty fucking slut. Begging for my piss."
            mc "This is what you wanted, isn't it? To be my personal urinal?"
            mes "*choking, swallowing desperately*"
            scene sm1cs-mes-r1-155 mc-pee-alt-angle-over-shoulder_c2 with dissolve
            mc "Swallow it. Every fucking drop."
            scene sm1cs-mes-r1-156 mc-pee-alt-angle-mes-so-warm_c3 with dissolve
            mes "*gurgling, gagging*"
            scene sm1cs-mes-r1-157 mc-pee-alt-angle-mes-swallowing-moaning_c4 with dissolve
            pause
            scene sm1cs-mes-r1-158 mc-pee-alt-angle-closeup_c5 with dissolve
            pause
            scene sm1cs-mes-r1-159 mes-opens-one-eye-smiling-thank-you_c1 with dissolve
            mes "*gasping* Fuck... That was so filthy..."
            scene sm1cs-mes-r1-160 mes-love-doing-stuff-you_c1 with dissolve
            mes "I love it..."

        "Just relax and enjoy it" (hint="sm1cs_mes_r1_m02_h02"):
            scene sm1cs-mes-r1-153 mes-anticipates-begs-please_c1 with dissolve
            mes "Please..."
            pause
            scene sm1cs-mes-r1-155 mc-pee-alt-angle-over-shoulder_c2 with dissolve
            pause
            scene sm1cs-mes-r1-156 mc-pee-alt-angle-mes-so-warm_c3 with dissolve
            mes "*moaning* It's so warm..."
            mc "That's my good girl. You look so fucking hot being my little piss slut."
            mes "*swallowing, moaning*"
            scene sm1cs-mes-r1-157 mc-pee-alt-angle-mes-swallowing-moaning_c4 with dissolve
            mc "Such a perfect, dirty girl for me."
            scene sm1cs-mes-r1-158 mc-pee-alt-angle-closeup_c5 with dissolve
            pause
            scene sm1cs-mes-r1-159 mes-opens-one-eye-smiling-thank-you_c1 with dissolve
            mes "*smiling* Thank you..."
            scene sm1cs-mes-r1-160 mes-love-doing-stuff-you_c1 with dissolve
            mes "I love doing this stuff with you, [mcname]."

    scene sm1cs-mes-r1-161 mes-did-this-turn-on-mes-watching-be-dirty-puss-slut_c1 with dissolve
    mes "Did that turn you on?"
    mes "Watching me be your dirty piss slut?"
    scene sm1cs-mes-r1-162 mc-have-no-idea-not-done-with-you_c1 with dissolve
    mc "You have no idea."
    mc "Stand up. I'm not done with you yet."
    scene sm1cs-mes-r1-163 mc-mes-positions-against-wall_c1 with dissolve
    mes "So rough."
    mc "I know you love it."
    mes "Oouhah..."
    scene sm1cs-mes-r1-164 mes-fuck-pleaseagain_c1 with dissolve
    mes "Fuck me, [mcname]... Please fuck me again..."
    scene sm1cs-mes-r1-165 mes-thrusts-herself-on-mc-oh-fuck-make-take-it_c1 with dissolve
    mes "Oh fuck! Yes! Make me take it!"
    if _sm1cs_mes_r1_gentle is True:
        scene sm1cs-mes-r1-166 gentle-path-mc-you-perfect-to-me-noone-sees-like-this_c1 with dissolve
        mc "You're so perfect. So fucking perfect for me."
        mc "No one else gets to see you like this."
        scene sm1cs-mes-r1-167 mes-only-you-yours-completely_c1 with dissolve
        mes "Only for you... Only ever for you..."
        mes "I'm yours completely..."
    else:
        scene sm1cs-mes-r1-168 dom-path-mc-love-being-slut-personal-toilet_c1 with dissolve
        mc "You love being my piss-drinking slut, don't you?"
        mc "My personal fucking toilet?"
        scene sm1cs-mes-r1-169 mes-yes-god-yes-your-urinal_c1 with dissolve
        mes "Yes! God yes! I'm your toilet! Your urinal!"
        mes "I'll drink your piss anytime you want!"
    scene sm1cs-mes-r1-170 mc-fucks-mes-standing-anim_c1 with dissolve
    pause
    scene sm1cs-mes-r1-171 standing-alt-angle-from-bottom-view_c2 with dissolve
    pause
    scene sm1cs-mes-r1-172 standing-alt-angle-from-midshot_c3 with dissolve
    pause
    scene sm1cs-mes-r1-173 standing-alt-angle-from-closeup_c4 with dissolve
    pause
    scene sm1cs-mes-r1-174 standing-alt-angle-from-top-view_c5 with dissolve
    mes "Don't stop... Keep going."
    mc "Fuck, Min... I'm going to cum..."
    mes "*raw, breathless* Yes! Give it to me!"
    mes "Cum wherever you want!"
    scene sm1cs-mes-r1-175 mc-choice-menu-screen_c1 with dissolve
    menu:
        "I'm cumming inside you" (hint="sm1cs_mes_r1_m03_h01"):
            scene sm1cs-mes-r1-176 choice-creampie-mes-inside-yes-cum-inside_c1 with dissolve
            mes "Inside! Yes! Cum inside me right now!"
            scene sm1cs-mes-r1-177 mc-fuck-take-all_c1 with hpunch
            mc "*groaning* Fuck... Take all of it..."
            scene sm1cs-mes-r1-178 mc-fills-mes-cum_c1 with hpunch
            pause
            scene sm1cs-mes-r1-179 mes-so-full-can-feel-flooding-pussy_c1 with dissolve
            mes "So full... I can feel you flooding my pussy... Fuck..."

        "I'm cumming on your face" (hint="sm1cs_mes_r1_m03_h02"):
            scene sm1cs-mes-r1-180 choice-facial-mc-pulls-out-quickly-on-knees_c1 with dissolve
            mc "Turn around. On your knees, now."
            pause
            scene sm1cs-mes-r1-181 mes-gets-position-facial_c1 with dissolve
            pause
            scene sm1cs-mes-r1-182 mes-cover-me-please-make-dirtier_c1 with dissolve
            mes "Cover me... Please... Make me even dirtier..."
            scene sm1cs-mes-r1-183 mc-cums-fuck-yes_c1 with vpunch
            mc "*groaning* Fuck yes..."
            pause
            scene sm1cs-mes-r1-184 mc-shoots-load-mes-face_c1 with hpunch
            pause
            scene sm1cs-mes-r1-185 mes-covered-cum-mmm-love-filthy-together_c1 with dissolve
            mes "Mmm... I love how filthy we are together..."

    scene sm1cs-mes-r1-186 mc-mes-washed-by-shower_c1 with dissolve
    pause
    scene sm1cs-mes-r1-187 mes-holy-shit-mc-okay_c1 with dissolve
    mes "Holy shit..."
    mc "You okay?"
    scene sm1cs-mes-r1-188 mes-better-okay_c1 with dissolve
    mes "*nods weakly* More than okay..."
    scene sm1cs-mes-r1-189 mes-tense-oh-no-mc-what-have-pee-now_c1 with dissolve
    mes "Oh. Oh no."
    mc "What's wrong?"
    mes "*voice urgent* I have to pee. Like, {i}right now{/i}."
    scene sm1cs-mes-r1-190 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Pee on me" (hint="sm1cs_mes_r1_m05_h01"):
            scene sm1cs-mes-r1-191 choice-pee-him-mc-grins-not-waste-drain-pee-on-me_c1 with dissolve
            mc "Don't you dare waste that in the drain."
            mc "Pee on me."
            scene sm1cs-mes-r1-192 mes-you-serious-mc-lay-on-me_c1 with dissolve
            mes "Really? Don't fucking tease me, [mcname]."
            mc "Lay me down and cover me."
            scene sm1cs-mes-r1-193 mc-lies-ground_c1 with dissolve
            pause
            scene sm1cs-mes-r1-194 mes-looking-excited_c1 with dissolve
            pause
            scene sm1cs-mes-r1-195 mes-positions-mes-sure-about-this-mc-never-been-more-sure_c1 with dissolve
            mes "You're sure about this?"
            mc "I've never been more sure about anything. Give it to me."
            scene sm1cs-mes-r1-196 mes-relieves-herself_c1 with dissolve
            mes "*a sigh of pure relief* Oh God... That feels so good..."
            pause
            scene sm1cs-mes-r1-197 mes-pees-mc-anim_c1 with dissolve
            pause
            scene sm1cs-mes-r1-198 mes-pee-alt-angle-top-view_c2 with dissolve
            pause
            scene sm1cs-mes-r1-199 mes-pee-alt-angle-bottom-view_c3 with dissolve
            pause
            scene sm1cs-mes-r1-200 mes-pee-alt-angle-far-top-view_c4 with dissolve
            pause
            scene sm1cs-mes-r1-201 mes-pee-alt-angle-mc-closeup_c5 with dissolve
            pause
            scene sm1cs-mes-r1-202 mes-you-so-filthy-love-it_c1 with dissolve
            mes "Fuck... You're so fucking filthy... I love it."

        "You should probably go, then" (hint="sm1cs_mes_r1_m05_h02"):
            scene sm1cs-mes-r1-203 choice-should-go-mc-dont-let-stop_c1 with dissolve
            mc "Don't let me sto—"
            scene sm1cs-mes-r1-204 mes-runs-past-mc-move-get-out-way_c1 with hpunch
            mes "MOVE! GET OUT OF THE WAY!"
            scene sm1cs-mes-r1-205 mes-manages-sit-toilet_c1 with dissolve
            mes "Ahhhhuah..."
            scene sm1cs-mes-r1-206 mes-relieves-herself_c1 with dissolve
            mct "That's my girl..."

    jump sm1cs_mes_r1_end

label sm1cs_mes_r1_continue_3:

    scene sm1cs-mes-r1-122 mc-getting-close-mes-yes-give-me-need-it_c1 with dissolve
    mc "Fuck, Min... I'm about to... I'm gonna cum!"
    mes "*raw needy moan* Yes! Give it to me, [mcname]! I need it!"
    menu:
        "I'm going to fill you up" (hint="sm1cs_mes_r1_m06_h01"):
            scene sm1cs-mes-r1-124 mes-pushes-against-inside-yes-fill-up-breed_c1 with dissolve
            mes "Inside! Yes! Fill my pussy up! Breed me!"
            scene sm1cs-mes-r1-125 mc-cums-deep-inside-mes-fuck-take-it_c1 with hpunch
            mc "*groaning* Fuck... Take it..."
            pause
            scene sm1cs-mes-r1-126 mes-moans-yes-so-fucking-good-_c1 with dissolve
            mes "Yes... That feels so fucking good... I can feel every drop..."
            scene sm1cs-mes-r1-127 mes-crempie-dripping_c1 with dissolve
            pause
            if _sm1cs_mes_r1_gentle is True:
                scene sm1cs-mes-r1-128 gentle-path- mc-admires-work-look-beautiful_c1 with dissolve
                mc "Perfect. You look so beautiful like this."
                scene sm1cs-mes-r1-129 mes-looking-back-smiling-loves-feeling-full_c1 with dissolve
                mes "*smiles* I love feeling full of you."
            else:
                scene sm1cs-mes-r1-130 dom-path-mc-pins-mes-down-keep-in-dont-waste-drop_c1 with dissolve
                mc "Keep it all inside. Don't waste a single drop of my cum."
                scene sm1cs-mes-r1-131 mes-yes-sir-keep-every-drop-mc-good-girl_c1 with dissolve
                mes "Yes, Sir... I'll keep every drop inside me..."
                mc "Good girl."

        "I'm going to cover your face" (hint="sm1cs_mes_r1_m06_h02"):
            scene sm1cs-mes-r1-132 choice-facial-mc-pulls-on-knees-now_c1 with dissolve
            mc "On your knees. Now."
            scene sm1cs-mes-r1-133 mc-mes-reposition-for-cumshot_c1 with dissolve
            pause
            scene sm1cs-mes-r1-134 mes-please-cover-me-want-wear_c1 with dissolve
            mes "Please... Cover me... I want to wear it..."
            scene sm1cs-mes-r1-135 mes-strokes-mc-cock-waiting-for-cum_c1 with dissolve
            pause
            scene sm1cs-mes-r1-136 mc-cums-groaning-fuck-yes_c1 with dissolve
            mc "*groaning* Fuck yes..."
            scene sm1cs-mes-r1-137 mc-shoots-load-mes-face_c1 with vpunch
            pause
            scene sm1cs-mes-r1-138 mes-face-covered-cum_c1 with vpunch
            pause
            if _sm1cs_mes_r1_gentle is True:
                scene sm1cs-mes-r1-139 gentle-path-mc-caress-mes-head-look-beautiful_c1 with dissolve
                mc "You look so beautiful like this."
                scene sm1cs-mes-r1-140 mes-content-thanks-love-wearing-cum_c1 with dissolve
                mes "*smiling* Thank you... I love wearing your cum."
            else:
                scene sm1cs-mes-r1-141 mc-dom-path-that-good-look-cumslut_c1 with dissolve
                mc "That's a good look for you, my little cumslut."
                scene sm1cs-mes-r1-142 mes-cumslut-yours-always-mc-never-forget_c1 with dissolve
                mes "Mmm... Your cumslut. Always."
                mc "Don't you forget it."

    jump sm1cs_mes_r1_end

label sm1cs_mes_r1_end:

    scene sm1cs-mes-r1-207 mes-mc-chill-after-sex_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-mes-r1-208 mc-youhere-mes-yeah-just-floating_c1 with dissolve
    mc "You back with me?"
    mes "*nods slowly* Yeah... I'm here. Just...floating a little."
    scene sm1cs-mes-r1-209 mc-how-do-feel_c1 with dissolve
    mc "How do you feel?"
    if not player.has_played_scene("sm1cs_mes_r1"):
        scene sm1cs-mes-r1-210 mes-like-brain-shut-not-felt-calm-weeks_c1 with dissolve
        mes "Like...like my brain finally shut up."
        mes "*a small, tired laugh* I haven't felt this calm in weeks. Maybe months."
        scene sm1cs-mes-r1-211 mc-know-always-come-me-mes-know-hate-feeling-weak_c1 with dissolve
        mc "You know you can always come to me when it gets too much, right? You don't have to carry everything alone."
        scene sm1cs-mes-r1-212 mc-not-weak-need-someone-love-you_c1 with dissolve
        mes "I know. I just... I hate feeling weak. Needing help."
        mc "It's not weak to need someone, Min. Especially someone who loves you."
        scene sm1cs-mes-r1-213 mes-love-me-mc-i-do_c1 with dissolve
        mes "...You love me?"
        mc "...Yes. I do."
        scene sm1cs-mes-r1-214 mes-love-you-too_c1 with dissolve
        mes "I love you too, [mcname]."
        if _sm1cs_mes_r1_gentle is True:
            scene sm1cs-mes-r1-215 gentle-path-mes-thanks-being-good-me-mc-know-out-loud-good_c1 with dissolve
            mes "Thank you for being so good to me. For making me use my words... it helps me feel grounded."
            mc "I know. Making you say it out loud keeps you present, instead of trapped in your head."
            scene sm1cs-mes-r1-216 mes-smirks-smarter-than-look-mc-ouch_c1 with dissolve
            mes "*smirks* You're smarter than you look."
            mc "Ouch. And here I was being sweet."
        else:
            scene sm1cs-mes-r1-217 dom-path-mc-any-pain-mes-no-just-good-pain_c1 with dissolve
            mc "Did I go too hard anywhere? Any bad pain?"
            scene sm1cs-mes-r1-218 mes-thanks-taking-over-mc-keep-giving-freedom_c1 with dissolve
            mes "*shakes her head* No. Just good pain. The kind I needed."
            mes "Thank you for...taking over completely. It really makes me feel free."
            mc "Then I'll keep giving you that freedom. As often as you need it."
        if player.get_choice("sm1cs_mes006_keep_watersports"):
            scene sm1cs-mes-r1-219 watersports-mes-was-thing-shower-too-much-mc-kidding-incredible_c1 with dissolve
            mes "*shyly* Was...was the shower thing too much?"
            mc "Are you kidding? It was incredible."
            if _sm1cs_mes_r1_gentle is True:
                scene sm1cs-mes-r1-220 gentle-path-mc-you-beauty-mes-easier-with-you_c1 with dissolve
                mc "You were so beautiful, letting go like that. Trusting me completely."
                mes "*blushes* It's easier with you. You make me feel...dirty, but in a good way. A safe way."
                scene sm1cs-mes-r1-221 mc-mes-kiss_c1 with dissolve
                pause
            else:
                scene sm1cs-mes-r1-222 dom-path-mc-you-drank-piss-lucky-pervert_c1 with dissolve
                mc "Min, you drank my piss and then came while pissing yourself. I'm the luckiest pervert alive."
                scene sm1cs-mes-r1-223 mes-laughs-when-put-like-that-both-f-up-mc-best-way_c1 with dissolve
                mes "*laughs, embarrassed* When you put it like that... I guess we're both pretty fucked up."
                mc "In the best way. Never be ashamed of exploring that with me."
        scene sm1cs-mes-r1-224 mc-mes-snuggle-together-bed_c1 with dissolve
        pause
        scene sm1cs-mes-r1-225 mes-next-time-straight-you-mc-good-always-here_c1 with dissolve
        mes "Next time I'm drowning in my own head, I'm coming straight to you."
        scene sm1cs-mes-r1-226 mes-glad-back-from-korea_c1 with dissolve
        mc "Good. I'll always be here. Always."
        mes "I'm glad I came back from Korea. This...us... {w} Being together."
        mes "It makes it all worth it."
    else:
        scene sm1cs-mes-r1-227 mes-sigh-so-much-better-prolly-supervillain_c1 with dissolve
        mes "So much better. I don't know what I'd do without you."
        scene sm1cs-mes-r1-228 mes-laughs-probably_c1 with dissolve
        mc "Probably become a supervillain."
        mes "*laughs softly* Probably."
    scene sm1cs-mes-r1-229 mes-yawns-mc-get-sleep-have-class_c1 with dissolve
    mes "*yawning*"
    mc "Get some sleep. You have class in the morning."
    scene sm1cs-mes-r1-230 mes-stay-me-mc-ofc-not-going-anywhere_c1 with dissolve
    mes "Stay with me?"
    mc "Of course. I'm not going anywhere."
    scene sm1cs-mes-r1-231 mes-face-at-peace_c1 with dissolve
    pause
    scene sm1cs-mes-r1-232 mes-mc-fall-asleep-end-scene_c1 with dissolve
    pause
    if player.has_played_scene("sm1cs_mes_r1"):
        $ StoryController.consume_time_energy(2, 15, 2)
        return
    else:
        $ CharacterController.get_character("mes").add_override_interaction_option("io-MES-sex-repeatable")
        $ StoryController.end_scene(MES_STORY, 3, 0, 2, STUDIO, SD_SUB_MIN, SD_MIN)
    return
