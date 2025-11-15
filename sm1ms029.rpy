label sm1ms029_confrontation:

    ### Important render notes - feel free to expand a little on the renders so it has a bit of movment, maybe some walking around - it's an extended, intense conversation.
    #mc is in nice clothes again. sy is in her bondage outfit - nearby - should be a plate with some full drinks
    "?" "The man of the hour."
    #mc turning to meet the new voice - sy is near him
    mc "..."
    #ef and cb stand in front of mc and sy
    mc "I do have that pleasure."
    #mc gestures to stacy
    if persistent.is_special:
        mc "But I share it with my sister."
        mc "Stacy Young."
    else:
        mc "But I share it with my girlfriend."
        mc "Stacy Brown."
        #sy smiles at mc
    #sy looks at ef and cb - curiously - a cat saw something strange in her house
    sy "I uh... I don't think I recognize you two."
    #cb has a playful and poisonous smile
    "?" "Really? I would have hoped my face came up in your research."
    "?" "Or perhaps you only know by body."
    #mc and sy are a bit confused - ef removes his mask
    mc "Uh..."
    sy "Mmm."
    #ef smiles and gestures to her
    "?" "This is Carmel Blaise, my right hand."
    #mc asking the guy a question
    mc "And who does that make you?"
    #ef smiles slyly
    "?" "Just a humble businessman."
    #ef introducing himself
    et  "Ethan Foxmorr, president and founder of Foxmorr Films."
    #sy recognizes the name
    sy "Foxmorr Films? You guys always have half of the top ten movie slots on Porn Cave."
    #sy looks at cb
    sy "Now I see it. Carmel Blaise.{w}You're the top pornstar of Foxmorr Films."
    sy "You're amazing."
    #cb smiling
    cb "Why, thank you, Stacy."
    cb "I try my best."
    #mc smiling - relaxed now
    mc "Well, it's a pleasure to have two big shots in our home. But I don't think we invited you."
    #ef being a bit of a charming / james bond
    et  "I have a confession.{w} We snuck in."
    #sy laughing
    sy "Haha. Classic party move."
    #mc asking
    mc "And why did you sneak in?"
    #ef is smiling
    #ef is now all business
    et  "I wanted to take the measure of you, [mcname]."
    et  "Our business might be the porn business, but that doesn't mean it requires anything less than our best."
    et  "Wouldn't you agree?"
    menu:
        "Yes" (hint="sm1ms029_m04_h01"):
            $ player.set_choice("sm1ms029_agree_rivals")
            #mc kind of shrugging
            mc "Yes, I guess."

        "No" (hint="sm1ms029_m04_h02"):
            $ player.set_choice("sm1ms029_disagree_rivals")
            #mc looking charming while saying something insulting
            mc "I don't usually agree with intruders."
            et  "Heh."

        "Make your point" (hint="sm1ms029_m04_h03"):
            $ player.set_choice("sm1ms029_annoyed_rivals")
            #mc looks a bit annoyed
            mc "Why don't you save some time and get to your point?"

    et  "Like I said. I wanted to take the measure of you, [mcname]."
    menu:
        "Should I pull out my dick?" (hint="sm1ms029_m05_h01"):
            $ player.set_choice("sm1ms029_joke_rivals")
            #mc is playing along and also insulting him
            mc "Shall I pull out my dick, then?"
            #cb smiling - chuckling
            #ef doesn't look enthused
            et  "That's not what I mean."

        "Why is that?" (hint="sm1ms029_m05_h02"):
            $ player.set_choice("sm1ms029_why_is_that")
            #mc asking a question
            mc "And why is that?"

    #ef talking - villain vibes
    et  "Crowning is my home. It's given me many gifts."
    et  "When I started making porn, many in the city doubted I could make it big."
    et  "But I proved them wrong.{w} And now Foxmorr Films is one of the biggest businesses in the city."
    et  "The company has made me a billionaire and made many outstanding individuals into top-tier talent that thousands of people watch every day."
    et  "But I remain humble, and always remember that Crowning deserves my help."
    et  "It's for this simple reason that I stand before you today."
    mc "What? You want to invest in us?"
    mc "Help us be successful like you?"
    et  "Quite the opposite."
    et  "I want to buy you out."
    mc "What?"
    sy "Buy us out?"
    #ef gestures around
    et  "If you please... {w}You two have done some amazing work."
    et  "I've been learning about you, seeing how S&M Studio came to be."
    if persistent.is_special:
        et  "When I found out that it was just a brother and sister running things, without any formal business, education, I had to admit."
    else:
        et  "When I found out it was just two struggling people with no formal business education, I had to admit."
    #ef smiling and pointing at mc and sy
    et  "You two have done very well."
    mc "Thank you."
    et  "But I doubt think it will be enough."
    et  "Your films are fine, in that cute amateurish way."
    et  "But they'll never reach the heights of Nuttgrabbers II or Zero-Void Alien Babes."
    #ef touches his hands to his chest
    et  "Foxmorr Films... on the other hand."
    et  "We can take what you started and bring it to the next level."
    sy "So wait, you want us to work for you?"
    et  "I would offer that, but I fear that there would be a culture clash. I prefer clean breaks when I can get them."
    mc "So what does that mean?"
    et  "It means I'd like to buy S&M Studios from you. Outright."
    et  "You two get rich, and I pick up your studio and all the IPs you've made."
    #bit of a close up on ef being a slimeball
    et  "Everyone wins..."
    menu:
        "I don't think so" (hint="sm1ms029_m06_h01"):
            $ player.set_choice("sm1ms029_decline_rivals")
            #mc shaking his head
            mc "I don't think so."
            #mc smiling at sy
            mc "Stacy and I have made it this far on our own."
            mc "We're not about to sell everything we've been busting our asses to make."
            #cb kind of has a knowing look - she knew mc wouldn't sell out - no one really sees it
            #ef is mad - but trying to salvage things
            et  "You haven't even heard how much I'm offering."
            #sy shutting him down
            sy "You heard, [mcname]. The answer is no, Foxmorr."

        "Thanks, but no thanks" (hint="sm1ms029_m06_h02"):
            $ player.set_choice("sm1ms029_thanks_but_no")
            #mc saying no
            mc "Thanks, but no thanks."
            mc "I think we'll keep doing our thing."
            #sy joining in
            sy "Yeah. And since you came here to try to buy us out, I bet your scared of our potential."
            sy "Maybe we'll buy you one day."
            #cb has a little smirk - no one really sees it.

        "How much are we talking?" (hint="sm1ms029_m06_h03"):
            $ player.set_choice("sm1ms029_how_much")
            ### set switch - ms029_greed1 = ON / True
            #mc asking about the money
            mc "How much are we talking?"
            et  "How does Seventy-Five Thousand sound?"
            #mc gets excited
            mc "Done!"
            #sy bopps him on the head
            sy "[mcname]!"
            mc "Ouch."
            #mc looking at sy
            sy "Are you crazy? This is our studio."
            sy "We built it, and you think we should just sell it when it's finally running smoothly?"
            #mc realizes he was razy
            mc "Right... You're right."
            mc "Not sure what came over me."
            #mc giving ef a resolute answer
            mc "Sorry, Ethan. No sale."
            mc "Stacy is right. We've worked hard to build up S&M Studio."
            #mc smiling at sy
            mc "It belongs to us."

    #ef looks mad - not enraged, but certainly displeased
    et  "I've been watching you for a little bit, [mcname]."
    mc "Okay... weird."
    #ef's intensity grows
    et  "You're a lot of things, but I did not take you for an imbecile."
    et  "You're nothing. A college dropout who likes filming himself having sex."
    et  "Success isn't coming your way. All that's coming for you is failure."
    #ef looking at sy
    et  "For you and everyone close to you."
    #mc is mad - ef is smiling
    #ef gestures around the studio
    et  "Still... as you said... Thie place-"
    et  "-it certainly took you a long time to put it together."
    #cb standing near ef - kind of frowning - she knows his true wicked side all too well
    et  "It's something you should feel proud of."
    #ef's menace comes out
    et  "Because soon enough... all you are going to feel..."
    et  "Is failure and loss."
    #ef holding up a finger - promising
    et  "One day soon, you're going to realize what a terrible mistake you made tonight."
    et  "I only hope that you pray that I will be in a merciful mood when you realize it."
    #ef relaxes back to normal
    #ef smiling
    et  "Enjoy your party..."
    #ef turns to walk away
    et  "Carmel."
    #cb follows after ef
    #shot that shows the front of ef and cb as they're walking away - mc and stacy behind them - mc looking mad
    #mc just kind of looking pissed at the insulting way the guy acted
    sy "*indiscernable words*"
    #mc finally takes a breath
    mc "*sighs*"
    sy "[mcname]?"
    #mc looks at sy - relaxed
    mc "Hey, Stacy."
    sy "What are we doing to do?"
    #mc sees the drinks nearby
    #mc hands her a drink
    #mc takes a drink - sy nervous - watching him
    mc "Mmmm."
    #mc finishes his drink - looking at the way that cb and ef left
    mc "..."
    menu:
        "We're going to dance" (hint="sm1ms029_m07_h01"):
            $ player.set_choice("sm1ms029_gonna_dance")
            #mc holds out his hand to stacy
            mc "I think we should dance."
            mc "Want to join me?"
            #sy does her best to put what happened from her mind
            sy "I...{w} I thought you'd never ask."

        "We're going to win" (hint="sm1ms029_m07_h02"):
            $ player.set_choice("sm1ms029_gonna_win")
            #mc looks intense - and sy is smiling - glad he's got the fighting spirit
            mc "What are we going to do?"
            mc "We're going to make the best pornos ever."
            #alt angle
            mc "And wipe that shit-eating grin right off that asshole's face."
            #sy cheering
            sy "Yay!"

        "Forget about him" (hint="sm1ms029_m07_h03"):
            $ player.set_choice("sm1ms029_forget_about_him")
            #mc waves his hand like forget about that guy
            mc "Forget about that guy. Total inferiority complex."
            #mc smiles at sy
            mc "He thinks he can come in and tryto scare us?"
            mc "He's not worth the cost of my shoes."
            #sy smiling - glad to see mc acting like this
            sy "Yeah. Screw him."
            sy "I think he's just afraid of a little competiion."
            #sy has a drink
            #mc agreeing
            mc "One-hundred percent."
            #mc guiding sy back to other people nearby
            mc "Come on. We've still got a party to enjoy."

    jump sm1ms029_party_end

label sm1ms029_party_end:

    # MONTAGE: mc and sy dancing
    # MONTAGE: mc talking to arj
    # MONTAGE: hr watching mc and kv talk
    # MONTAGE: mh smiling
    # MONTAGE: arj and sy talking with mc
    if _sm1mc029_ns_available:
        # mc and ns dancing
        pass
    if _sm1mc029_tl_available:
        # mc and tl by the food table
        pass
    if _sm1mc029_mes_available:
        # mes, hr and mc all talking
        pass
    # MONTAGE: sy, arj, mc dancing
    # sy, mc, arj standing in front of everyone
    mc "Everyone, thank you so, so much for coming to the S&M Studio party!"
    mc "We seriously can't thank you enough."
    mc "If you can, please support us! Like our videos, tell your friends-"
    # sy butts in
    sy "We take orders! Right, AmRose?"
    # arj rolls her eyes
    # mc smiling
    mc "But again, from the bottom of my heart, thank you everyone. I hope you have a good rest of the night!"
    # everyone starts walking out
    mc "Oh, and if anyone feels like they can't safely get home, you are more than welcome to stay the night here!"
    # hr walking up to mc
    hr "Well, I will say, you two do know how to throw a party."
    mc "Yeah? You have fun tonight, Hana?"
    hr "Of course."
    # hr taking off her mask
    hr "And it seems like everything you're doing here is above board."
    sy "Oh? You got that all from the party?"
    # hr, mask off, smirking
    hr "That, and I've got this new little thing on my phone."
    # hr holding up a phone
    hr "Given a little bit of time, it can worm itself into unprotected WiFi-routers."
    hr "Which, is something you guys should think about."
    hr "But, I took a peek, and it looks like you guys haven't been doing anything shady."
    # hr horny look
    hr "Maybe just a little bit nasty."
    mc "Woah, that's an invasion of privacy!"
    sy "Yeah! If you want to look at my naughty bits, you can just ask, Hana!"
    # mc and hr and ark look at her confused
    sy "What...{w} Hana is kind of hot."
    hr "Thank you, Stacy."
    # hr looking at mc
    hr "After Fetish Locator, and learning that AmRose wasn't here... I had to make sure."
    mc "I understand, Hana."
    # mc looking a little sad
    mc "Believe me, I get it better than most."
    mc "No hard feelings."
    # hr smiling
    hr "I'm happy to hear that."
    # hr walking out
    hr "I'll see you all around. Be good."
    # hr is gone, now it's just arj, mc, sy
    arj "Wow. I forgot how weird and intense she can be."
    mc "Same."
    arj "You two want some help cleaning up?"
    # sy smiling
    sy "That would be awesome, AmRose."
    # sy, mc, arj start cleaning
    # MONTAGE: sy, mc, arj resetting the studio 1
    # MONTAGE: sy, mc, arj resetting the studio 2
    # MONTAGE: sy, mc, arj resetting the studio 3
    # MONTAGE: sy, mc, arj resetting the studio 4
    # MONTAGE: sy, mc, arj resetting the studio 5
    # MONTAGE: sy, mc, arj resetting the studio 6
    # mc, sy, arj all sitting on the couch
    sy "I'm exhhaauuuussted."
    arj "Me too. All that cleaning, after that fucking we did..."
    mc "Definitely pooped."
    # arj looking at sy
    arj "I haven't been fucked that hard since the Fetish Locator days."
    mc "Miss it?"
    # arj smirking
    arj "Yes."
    # arj looking at the cieling, tired
    arj "And no."
    sy "Oh my God, look at the time! AmRose, do you need me to call you a cab or something?"
    # arj looking sheepishly at sy
    arj "I was actually thinking... or, wondering, if I could take you and [mcname] up on the offer to spend the night here."
    sy "Of course!"
    # mc leaning in
    mc "You're welcome to stay here any time, AmRose. Seriously. Mi casa is... uhm, your house."
    arj "Hehehehe."
    # sy standing, arj looking at mc
    arj "Spent too much time staring at ass in Spanish class to remember anything, huh, [mcname]."
    # mc standing, hands up
    mc "Guilty as charged."
    sy "Now come on, AmRose. It's time for sleepy time."
    sy "Before I pass out standing up."
    mc "Same."
    # mc and sy help arj stand up
    # arj, sy, mc all walking towards the stairs
    # they're all going up the stairs
    # sy jumps onto the bed
    arj "God, this bed is massive."
    sy "And soooooo comfy!"
    arj "Why is it so big?"
    # mc looking at ark
    mc "For sleepovers. Come'on."
    $ SMGallery.unlock_gallery_slot("achievement", "08_HAPPY_END")
    # mc crawling into bed
    # sy cuddling up to him
    # naked arj cuddling up to mc
    arj "You know..."
    mc "Hmmm?"
    arj "I've missed this..."
    # mc smiles, everyones eyes are closed
    sy "Me toooo..."
    mc "It's nice to be cuddling you again, AmRose."
    arj "Yes... yes it is..."
    sy "Good night, everyone."
    # mc cmiling
    mc "Good night, Stacy."
    arj "Night, night, [mcname]..."
    mc "Good night, AmRose."
    # top down view, arj and sy cuddling mc
    mct "What a good night..."
    mct "Hell, a perfect night."
    # scene black with dissolve

    jump sm1ms029_cliffhanger

label sm1ms029_cliffhanger:

    #ef and cb are standing outside - city street. nice car near them. ef is on his phone
    et  "No."
    et  "No, they're not going to sell."
    #ef checking out cb's ass
    et  "Not without some {i}motivation{/i}."
    #ef listening on the phone
    #ef smiling
    et  "That's exactly what I was thinking."
    #ef hanging up phone
    et  "We'll talk later."
    #ef opening up the door for Carmel
    et  "Come, my dear. We've got work to do."
    #carmel goes into the car
    #car door closes
    #car drives away

    $ StoryController.end_scene(MS)
    return
