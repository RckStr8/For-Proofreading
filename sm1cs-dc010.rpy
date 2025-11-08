label sm1cs_dc010:

    #interaction with dc in park
    #ONE DAY HAS PASSED SINCE dc008

    # mc in studio
    scene sm1cs-dc010-01 mc-sy-talking_c1 with dissolve
    mc "All right, Stacy, I'm taking off!"
    scene sm1cs-dc010-01 mc-sy-talking_c2 with dissolve
    sy "Okay!"
    # sy walking up, looking like she's going out too
    mc "Oh? Where are you going?"
    scene sm1cs-dc010-01 mc-sy-talking_c2 with dissolve
    sy "Not all of us can be so lucky to get a date with a hot cop."
    sy "Some of us need to go and work!"
    # mc gives sy a 'seriously' look
    scene sm1cs-dc010-02 mc-sy-talking_c1 with dissolve
    mc "You want to complain about work to me?"
    scene sm1cs-dc010-03 mc-sy-walking-past-him_c1 with dissolve
    sy "Hehehehe! Yep!"
    # sy walking past mc
    mc "Seriously, where are you heading out to?"
    scene sm1cs-dc010-04 mc-sy-walking-together_c1 with dissolve
    sy "There's a studio that's having a close out sale."
    sy "I'm going to see if there's anything worth buying."
    # mc and sy heading for the door
    mc "Oh, that's actually super useful..."
    scene sm1cs-dc010-05 mc-sy-almost-at-door_c1 with dissolve
    sy "I know!"
    sy "But I'll be getting back late."
    # mc and sy standing by door
    scene sm1cs-dc010-05 mc-sy-almost-at-door_c2 with dissolve
    mc "Oh?"
    sy "Yeah, it's on the other side of Crowning. And they're starting super late."
    # sy makes a suggestive face
    sy "So you'll have the place all to yourself tonight."
    scene sm1cs-dc010-05 mc-sy-almost-at-door_c3 with dissolve
    mc "Hey, I had no plans for any of that!"
    sy "Suuuuuuuuure you didn't."
    # sy and mc walking out the door
    sy "Just thought I'd let you know!"
    mc "Aye yea yea..."
    # scene black with dissolve
    scene sm1cs-dc010-06 mc-at-the-movies_c1 with Fade(0.5, 0.5, 0.5)
    #Change MC outfit to something nice
    # Debbi in her Top outfit
    # mc in the movie theater looking at his phone
    mct "I guess Debbie is running behind..."
    mct "Well, I'll make sure to grab us some good seats at the very least."
    # mc sits down
    scene sm1cs-dc010-07 mc-sitting_c1 with dissolve
    mct "Hope everything is all right."
    mct "Sounds like something happened at-"
    # dc walks in looking hurried
    scene sm1cs-dc010-07 mc-sitting_c2 with dissolve
    dc "Oh my goodness, [mcname]! I am so sorry!"
    # mc smiles and stands up
    scene sm1cs-dc010-08 mc-standing_c1 with dissolve
    mc "It's okay! You've got an important job, and you're saving lives!"
    scene sm1cs-dc010-09 mc-dc-hugging_c1 with dissolve
    dc "Oh, it's not all that!"
    # mc and dc hug
    scene sm1cs-dc010-10 mc-dc-talking_c1 with dissolve
    # mc and dc standing in the theater
    mc "I hope these seats are okay!"
    scene sm1cs-dc010-10 mc-dc-talking_c2 with dissolve
    dc "Oh! These are great seats!"
    dc "And it looks like it's just us here!"
    # mc and dc both sit down
    scene sm1cs-dc010-11 mc-dc-sitting_c1 with dissolve
    mc "I think this movie has been out for a little bit."
    mc "So hopefully it'll just be us!"
    # dc blushes
    scene sm1cs-dc010-11 mc-dc-sitting_c2 with dissolve
    dc "That would be, uhm, nice."
    mc "I think so too."
    # the lights turn off in the theater
    scene sm1cs-dc010-12 mc-dc-movie-starting_c1 with dissolve
    dc "Ooooo! The movie is starting!"
    # mc smiles, dc is excited
    scene sm1cs-dc010-13 mc-dc-excited_c1 with dissolve
    pause
    # dc cuddles up next to mc
    scene sm1cs-dc010-14 mc-dc-cuddling_c1 with dissolve
    # mc cuddles back to dc back
    mct "Debbie is holding my hand."
    mct "Progress!"
    scene sm1cs-dc010-15 mc-dc-thinking_c1 with dissolve
    pause

    jump sm1cs_dc010_later

label sm1cs_dc010_later:

    scene black
    show screen scene_transition(_("2 Hours and 37 Minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transition
    scene sm1cs-dc010-16 mc-dc-talking_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    # dc sitting forward in her chair, holding mc's hand, looking excited
    dc "Wow!"
    mc "Yeah, wow indeed!"
    # dc looks over at mc
    dc "That was so good!"
    scene sm1cs-dc010-17 mc-dc-talking_c1 with dissolve
    mc "It was!"
    dc "Did you like it!?"
    # mc smiling
    mc "I did! And I'm guessing you did too?"
    scene sm1cs-dc010-17 mc-dc-talking_c2 with dissolve
    dc "I did!"
    # mc and dc stand up
    scene sm1cs-dc010-18 mc-dc-talking_c1 with dissolve
    dc "Like, when he showed up in the car, the handgun sticking out of the window!"
    # mc and dc start walking out of the theater
    dc "And then he reloaded it by smashing it on the motorcyclists head! So bad ass!"
    scene sm1cs-dc010-19 mc-dc-walking_c1 with dissolve
    pause
    # mc and dc walking down the street IT IS NIGHT TIME NOW
    scene sm1cs-dc010-20 mc-dc-walking_c1 with fade
    dc "Oh, oh! And when he was in that fight, and he grabbed the gun, and pulled it apart!"
    dc "Classic bad ass move! Oh, so cool!"
    mc "It was!"
    # dc smiling
    scene sm1cs-dc010-21 mc-dc-talking_c1 with dissolve
    dc "What a great night, [mcname]. Seriously, I had a lot of fun hanging out."
    scene sm1cs-dc010-21 mc-dc-talking_c2 with dissolve
    mc "Of course, I had a great time too."
    # dc and mc face each other, smiling
    mc "Like really great."
    scene sm1cs-dc010-22 mc-dc-about-to-kiss_c1 with dissolve
    dc "Really?"
    mc "Really, really."
    # dc smiles
    dc "You know... there's something I've been thinking a lot about..."
    mc "Is that so?"
    dc "Mmhmmm... something that we should be doing."
    mc "And what's that?"
    dc "Uhm..."
    # dc makes a kissing face
    scene sm1cs-dc010-23 mc-dc-about-to-kiss_c1 with dissolve
    pause
    # mc looks like he's about to kiss dc
    scene sm1cs-dc010-23 mc-dc-about-to-kiss_c2 with dissolve
    pause
    # dc's eyes fly open
    scene sm1cs-dc010-24 mc-dc-oops_c1 with hpunch
    dc "Wait!"
    # dc pats her pockets
    scene sm1cs-dc010-25 mc-dc-lost-her-phone_c1 with dissolve
    dc "Where's my phone!?"
    scene sm1cs-dc010-25 mc-dc-lost-her-phone_c2 with dissolve
    mc "Uhm..."
    scene sm1cs-dc010-26 mc-dc-running_c1 with dissolve
    dc "Oh my God, I must have dropped it in the theater!"
    # dc starts running away
    scene sm1cs-dc010-27 dc-running_c1 with hpunch
    dc "Just - hold that thought! I'll be right back!"
    scene sm1cs-dc010-26 mc-dc-running_c2 with dissolve
    mc "No worries, I'll wait right here for you!"
    dc "Okay - sorry!"
    # dc runs away
    scene sm1cs-dc010-27 dc-running_c2 with dissolve
    # mc smiling, standing on the street
    mct "Well, tonight is going really well."
    # behind him, co1 and co2 are walking towards mc
    scene sm1cs-dc010-28 mc-thinking_c1 with dissolve
    mct "Like... really good. Maybe, and just maybe..."
    scene sm1cs-dc010-28 mc-thinking_c2 with dissolve
    "Jerk Cop" "Well, what do we have here!"
    mct "Oh shit."
    # mc turns around and sees co1 and co2
    scene sm1cs-dc010-29 mc-talking_c1 with dissolve
    "Douche Cop" "Oh, loitering? Maybe something a bit more nefarious?"
    scene sm1cs-dc010-29 mc-talking_c3 with dissolve
    mc "Evening, officers."
    scene sm1cs-dc010-29 mc-talking_c2 with dissolve
    "Jerk Cop" "\"Evening, officers\", pfft."
    # co1 and co2 surround mc
    scene sm1cs-dc010-30 mc-surrounded_c1 with dissolve
    mc "Is there something I can help you with?"
    "Douche Cop" "Hmmm... let's see."
    # co1 punches mc in the gut
    scene sm1cs-dc010-31 mc-punching_c1 with hpunch
    mc "Uuuuffff!"
    # mc collapses down onto one knee
    scene sm1cs-dc010-32 mc-kneeling_c1 with vpunch
    "Douche Cop" "Oh, that's right!"
    # co2 punches mc in the face
    scene sm1cs-dc010-33 mc-face-punch_c1 with hpunch
    "Douche Cop" "That's for using that bitch to embarass us the other day!"
    scene sm1cs-dc010-34 mc-them-talking_c1 with dissolve
    "Jerk Cop" "Woah, man."
    # co2 looking at co1
    scene sm1cs-dc010-34 mc-them-talking_c2 with dissolve
    "Douche Cop" "What?"
    "Jerk Cop" "She's not entirely a bitch. Because, you now."
    # co2 smiles evily
    scene sm1cs-dc010-35 mc-devil-smile_c1 with dissolve
    "Douche Cop" "Oh yeah."
    # co2 punches mc in the face again
    scene sm1cs-dc010-36 mc-face-punch_c1 with hpunch
    "Douche Cop" "Because she has a dick!"
    # co1 kicks mc
    scene sm1cs-dc010-37 mc-being-kicked_c1 with hpunch
    "Jerk Cop" "Yeah! So, whatever she is! Fuck her!"
    "Douche Cop" "Hahahahaha!"
    scene sm1cs-dc010-37 mc-being-kicked_c2 with hpunch
    dc "Hey!"
    # co1 and co2 look over and dc is standing there, looking angry
    scene sm1cs-dc010-38 dc-pissed_c1 with dissolve
    dc "The {i}fuck{/i} are you two doing?"
    scene sm1cs-dc010-39 dc-warning_c2 with dissolve
    "Jerk Cop" "Oh, look who it is. You're little bitch, come to save her little bitch!"
    scene sm1cs-dc010-36 mc-face-punch_c1 with dissolve
    mc "Oh, that was a good one. Wooooow."
    # co1 punches mc again
    "Jerk Cop" "Shut up!"
    scene sm1cs-dc010-38 dc-pissed_c1 with dissolve
    dc "You..."
    # dc is walking towards them
    dc "You've got three seconds to leave, and I'll pretend this never happened."
    dc "If you don't, you'll regret it."
    # co1 and co2 looking smug, mc kneeling on the ground
    scene sm1cs-dc010-39 dc-warning_c2 with dissolve
    "Jerk Cop" "Oh ho ho, and what are you going to do about it, {i}little girl{/i}?"
    scene sm1cs-dc010-39 dc-warning_c1 with dissolve
    dc "One."
    scene sm1cs-dc010-39 dc-warning_c3 with dissolve
    "Douche Cop" "Oh the little girl, or {i}little boy{/i} is soooo scary!"
    dc "Two."
    # co1 and co2 laughing
    scene sm1cs-dc010-40 mc-dc-them-laughing_c1 with dissolve
    "Jerk Cop" "Oh, my balls are shaking! Hahahahaha!"
    "Douche Cop" "Hahahahaha!"
    scene sm1cs-dc010-41 mc-dc-about-to-punch_c1 with dissolve
    dc "Three."
    "Jerk Cop" "Oh, fuck you!"
    # co1 tries to punch dc, but she steps back
    scene sm1cs-dc010-41 mc-dc-about-to-punch_c2 with hpunch
    dc "Hah."
    # dc punches co1 hard, he's flying back
    scene sm1cs-dc010-42 mc-dc-flying_c1 with vpunch
    'Ka-Chow!'
    scene sm1cs-dc010-42 mc-dc-flying_c2 with dissolve
    "Douche Cop" "What the fuck!?"
    # co2 tries to punch dc, but dc ducks
    scene sm1cs-dc010-43 mc-dc-other-cop-coming-in_c1 with hpunch
    dc "*grunts*"
    # dc uppercuts co2 and he flies up
    scene sm1cs-dc010-44 mc-dc-another-uppercut_c1 with vpunch
    "Douche Cop" "Shit!"
    # co1 charges at dc
    scene sm1cs-dc010-45 mc-dc-charging-at-her_c1 with hpunch
    dc "Hiyah!"
    # dc kicks co1 in the chest
    scene sm1cs-dc010-46 mc-dc-kicking-him_c1 with hpunch
    pause
    # c01 and co2 on the ground
    scene sm1cs-dc010-47 mc-dc-both-flat_c1 with dissolve
    "Both cops" "*groaning*"
    "Douche Cop" "My ass."
    dc "You two. {i}Leave.{/i} Before I put you in the hospital."
    scene sm1cs-dc010-47 mc-dc-both-flat_c2 with dissolve
    "Jerk Cop" "Oh yeah, bitch? And what if we tell the captain that you assaulted us?"
    "Douche Cop" "Yeah. Get your ass kicked off the force."
    scene sm1cs-dc010-47 mc-dc-both-flat_c3 with dissolve
    mc "Ahem."
    # mc holds up his phone
    scene sm1cs-dc010-48 mc-dc-showing-phone_c1 with dissolve
    mc "If you do that, I'll have to show your captain this video of you beating me up."
    mc "And of Officer Callahan telling you to leave."
    mc "And of both of you trying to punch her first."
    mc "I wonder what he would have to say about that?"
    # co1 and co2 standing, looking hurt and angry
    scene sm1cs-dc010-48 mc-dc-showing-phone_c2 with dissolve
    "Jerk Cop" "Errrgghhhh..."
    "Douche Cop" "Mother fucker..."
    "Jerk Cop" "Come on."
    # co1 and co2 walking away
    scene sm1cs-dc010-49 mc-dc-them-running_c1 with dissolve
    mc "And if you two don't lay off of Debbie, I'm going to send this anonymously to your Captain!"
    "Jerk Cop" "Fuck you."
    # c01 and c02 are gon
    # dc hurries over to mc
    scene sm1cs-dc010-50 mc-dc-talking_c2 with dissolve
    dc "Oh my God! [mcname]! Are you okay?"
    scene sm1cs-dc010-50 mc-dc-talking_c1 with dissolve
    mc "Yeah. Never better."
    mc "Random question, have you seen a bloody tooth anywhere?"
    # dc helps mc up
    scene sm1cs-dc010-51 mc-dc-wincing_c1 with dissolve
    dc "I can't believe they hurt you."
    mc "Oh, did they? I'm totally fine!"
    # mc winces
    scene sm1cs-dc010-50 mc-dc-talking_c3 with dissolve
    dc "Uh huh, sure you are, big guy."
    dc "Come on, let me help you home."
    scene sm1cs-dc010-51 mc-dc-wincing_c2 with dissolve
    mc "I can-"
    # mc winces again
    scene sm1cs-dc010-52 mc-dc-helping-him_c1 with dissolve
    mc "Okay, maybe that last kick got me pretty good..."
    # dc holding mc up, starts walking down the street
    mc "Thank you, Debbie."
    dc "Of course, [mcname]."
    scene sm1cs-dc010-53 mc-dc-at-the-studio_c1 with fade
    # dc helping mc into the studio
    mc "Home, sweet home."
    # mc starts walking on his own
    scene sm1cs-dc010-55 mc-dc-smiling_c1 with dissolve
    mc "All right, I think I'm doing better now."
    mc "Thank you for getting me home, Debbie."
    scene sm1cs-dc010-55 mc-dc-smiling_c2 with dissolve
    dc "Of course."
    # dc smiling
    dc "I couldn't leave you just laying out on the street."
    mc "I mean, you {i}could{/i} have."
    dc "Hehehehe - never!"
    # mc smiling
    scene sm1cs-dc010-56 mc-walking_c1 with dissolve
    mc "Is there any way I can thank my hero?"
    scene sm1cs-dc010-56 mc-walking_c2 with dissolve
    dc "Have you got any beer?"
    mc "I think so."
    # mc walking towards the fridge
    dc "Thank goodness. I'm parched."
    # mc reaching into his fridge
    scene sm1cs-dc010-57 mc-dc-taking-out-beer_c1 with dissolve
    mc "Well, in that case..."
    # mc pulls out two beers
    scene sm1cs-dc010-58 mc-dc-taking-out-beer_c1 with dissolve
    mc "It looks like you're in luck."
    # mc walks over to dc holding up a beer
    scene sm1cs-dc010-58 mc-dc-taking-out-beer_c2 with dissolve
    dc "And you really don't need to thank me. It's my fault you were in that mess."
    mc "The only ones at fault were those two pricks."
    dc "You got that right!"
    # dc holds up her beer
    scene sm1cs-dc010-59 mc-dc-taking-the-beer_c1 with dissolve
    dc "Cheers to us heroes!"
    # mc and dc cheers their beers
    scene sm1cs-dc010-60 mc-dc-talking_c1 with dissolve
    mc "Ow!"
    dc "[mcname]-"
    mc "I'm okay!"
    # dc looks at him "seriously?"
    scene sm1cs-dc010-60 mc-dc-talking_c2 with dissolve
    dc "No, no you are not."
    # dc grabs mc and starts pushing him towards the couch
    scene sm1cs-dc010-61 mc-dc-pushing-him-to-the-couch_c1 with dissolve
    dc "Come on, I need to see how bad it is!"
    mc "It's seriously not that - owwww!"
    dc "Yeah, yeah. Come on."
    # dc and mc get to the couch
    # dc sits mc down
    scene sm1cs-dc010-62 mc-dc-on-the-couch_c2 with dissolve
    dc "All right, tough guy. Shirt off, come on."
    scene sm1cs-dc010-62 mc-dc-on-the-couch_c1 with dissolve
    mc "Fine, fine."
    # mc starts taking off his shirt
    scene sm1cs-dc010-63 mc-dc-taking-off-his-shirt_c1 with dissolve
    pause
    # close up of dc's face, neutral
    scene sm1cs-dc010-63 mc-dc-taking-off-his-shirt_c2 with dissolve
    dc "Mmm."
    # dc's face now slightly embarrassed
    scene sm1cs-dc010-65 mc-dc-talking_c1 with dissolve
    # mc sitting there with his shirt off
    mc "All right, I'm ready for my inspection, Doctor Debbie."
    scene sm1cs-dc010-64 mc-dc-blushing_c2 with dissolve
    dc "Oh, yeah, uhm -"
    # dc puts her hands on mc's chest, still nervous/blushgin
    scene sm1cs-dc010-66 mc-dc-touching-his-chest_c1 with dissolve
    dc "How's, uhm, how's that feel? Does it hurt?"
    scene sm1cs-dc010-66 mc-dc-touching-his-chest_c2 with dissolve
    mc "Just a little, nothing serious."
    scene sm1cs-dc010-67 mc-dc-starring-at-his-chest_c1 with dissolve
    dc "Good... good..."
    # dc is staring at mc's chest
    scene sm1cs-dc010-67 mc-dc-starring-at-his-chest_c2 with dissolve
    mc "Are you good, Debbie?"
    dc "Uhm... what?"
    scene sm1cs-dc010-68 mc-dc-confused-looking_c1 with dissolve
    mc "Are you okay?"
    dc "Oh, yeah, I'm... uh huh."
    dc "Little warm."
    # mc makes a confused face
    mc "Is that all?"
    scene sm1cs-dc010-68 mc-dc-confused-looking_c2 with dissolve
    dc "I..."
    # dc looks up at mc
    dc "I think..."
    dc "I want to do more than touch."
    mct "Oh damn."
    # dc lunges up at mc
    scene sm1cs-dc010-69 mc-dc-lunging-at-him_c1 with hpunch
    mc "Woah."
    # dc kisses mc
    scene sm1cs-dc010-70 mc-dc-kissing_c1 with dissolve
    pause
    # dc crawls on top of mc, still kissing him
    scene sm1cs-dc010-70 mc-dc-kissing_c2 with dissolve
    pause
    # dc leans back to take her shirt off
    scene sm1cs-dc010-71 mc-dc-leaning-back_c1 with dissolve
    pause
    # mc looks up at her, in awe (you can't see dc in this shot)
    scene sm1cs-dc010-73 mc-dc-shirtless_c1 with dissolve
    # dc is shirtless, looking down at mc
    dc "[mcname]..."
    scene sm1cs-dc010-72 mc-in-awe_c1 with dissolve
    mc "Debbie..."
    scene sm1cs-dc010-74 mc-dc-looking-away_c1 with dissolve
    dc "I... I..."
    dc "I want to..."
    # dc looks away embarrassed
    scene sm1cs-dc010-73 mc-dc-shirtless_c2 with dissolve
    mc "What is it, Debbie?"
    scene sm1cs-dc010-75 mc-dc-talking_c1 with dissolve
    dc "I- I can't- uhm..."
    scene sm1cs-dc010-74 mc-dc-looking-away_c2 with dissolve
    mc "You can tell me anything."
    # dc looks back down at mc
    scene sm1cs-dc010-76 mc-smiling_c1 with dissolve
    dc "I want to suck your cock, [mcname]."
    # mc looks surprised
    mct "Not what I expected."
    # mc smiles, dc looking at him
    mc "Well, you won't see me resisting , Officer."
    # dc smiles
    scene sm1cs-dc010-77 mc-dc-down-on-him_c1 with dissolve
    # dc starts crawling down mc
    dc "*slow sniffing*"
    # dc wraps her hands around mc's pants waist
    scene sm1cs-dc010-77 mc-dc-down-on-him_c2 with dissolve
    pause
    # shot of mc, smiling hornily
    scene sm1cs-dc010-78 mc-dc-astonished_c1 with dissolve
    # mc isn't wearing pants now, mc's dick is in front of dc's face, she looks in awe of it
    dc "Wow..."
    scene sm1cs-dc010-78 mc-dc-astonished_c2 with dissolve
    mc "What? Is something wrong down there?"
    dc "No... I just..."
    # dc looks up at mc
    scene sm1cs-dc010-79 mc-dc-talking_c1 with dissolve
    dc "I have been looking forward to this for awhile.{w} I'm very excited."
    mc "Me too."
    # dc puts her head above mc's dick
    scene sm1cs-dc010-80 mc-dc-blowjob_c1 with dissolve
    # -Animation 1: mc is laying on the couch, dc sucks mc's dick
    # alt-angle
    mc "Oh shit, Debbie!"
    dc "Glllk, gllllllck!"
    mc "Wow! Nggggh!"
    # alt-angle
    dc "Slllrrrpppp! Gllck, gllck, gllllllck!"
    mc "Nggghhh - this is - wow!"
    mc "Debbie - ngggghhhh - holy shit!"
    # alt-angle
    mc "This is amazing! Fuuuuuhhhhh - nggggh!"
    dc "Ouuachhh, ouuuaccchhhh, slrrrp!"
    mc "Oh my Gooood! Ngghhhh, fuuuuhhhccckkk."
    # alt-angle
    mc "Mmppphhhhhh-"
    mc "Oh, this is amazing - ngggh!"
    mc "This is - oh, Debbie. Fuuuckkk! Deebbbbiiiieeeee!"
    # alt-angle
    mc "Oh, that thing - nngghhhh - whatever you're doing with your tongue-"
    dc "Sllrrrpppppp! Sleep, sllrrpp, sllrrrppp!"
    mc "Oh shiiiiittttt..."
    # alt-angle
    mc "If you - nggghhhhh - keep going like that-"
    mc "Oh, Debbie - nggghhhh!"
    mc "Oh, fuuuck, oh, fuuuuuuuuck!"
    # -Animation 1: end
    # dc pulls her mouth off of mc's dick
    scene sm1cs-dc010-80 mc-dc-blowjob_c2 with dissolve
    mc "Nggghh-!"
    scene sm1cs-dc010-81 mc-dc-talking_c1 with dissolve
    dc "Sorry, [mcname], but..."
    scene sm1cs-dc010-81 mc-dc-talking_c2 with dissolve
    mc "No, it's okay, Debbie."
    # mc looking at dc
    scene sm1cs-dc010-82 mc-dc-standing_c1 with dissolve
    mc "Everything okay?"
    scene sm1cs-dc010-82 mc-dc-standing_c2 with dissolve
    dc "Yeah, everything is fine, it's just, uhm..."
    mc "What?"
    # dc looks away sheepishly
    scene sm1cs-dc010-83 mc-dc-kneeling_c1 with dissolve
    pause
    scene sm1cs-dc010-84 mc-dc-grabbing-her-tits_c1 with dissolve
    dc "There's something I've wanted to try..."
    mc "Oh yeah? And what's that?"
    dc "Sit up for me."
    # dc leans back mc sitting up]
    scene sm1cs-dc010-85 mc-dc-titjob_c1 with dissolve
    mc "Okay?"
    # dc stands up
    # dc kneels, mc spins to face her
    scene sm1cs-dc010-85 mc-dc-titjob_c2 with dissolve
    # dc grabbing her tits
    dc "I've always wanted to try this..."
    # dc wraps her tits around mc's dick
    scene sm1cs-dc010-85 mc-dc-titjob_c3 with dissolve
    mc "Oh shit, Debbie."
    dc "Oh, we haven't even gotten to the fun part yet."
    # -Animation 2: mc sitting on couch, dc gives mc titjob
    # alt-angle
    mc "Oh shiiiiiit!"
    dc "Yeah?"
    # alt-angle
    dc "How does it feel, [mcname]?"
    mc "Oh, so, so, {i}so{/i} good!"
    dc "Mmmmm!"
    # alt-angle
    dc "But tell me more."
    dc "Tell me what it's like to have my tits wrapped around your hard..."
    dc "Throbbing..."
    # alt-angle
    dc "Cock."
    mc "It feels like two clouds from heaven came down to smother my dick!"
    mc "They're so warm, and soft - nggghhh!"
    # alt-angle
    dc "Mmmm, I'm glad it feels good!"
    dc "Because it feels {i}amazing{/i} to have your hard shaft..."
    dc "Gliding between my tits."
    # alt-angle
    dc "I can feel every twitch and pulse of your cock..."
    dc "As it glides up and down my slick tits."
    mc "Nnnggghhhhhh!"
    # alt-angle
    dc "I can feel it, [mcname]."
    dc "I can feel how badly you want to cum."
    # alt-angle
    dc "And I want you to."
    dc "I want you to cover my big tits with all of your hot cum."
    dc "I {i}need{/i} you to spray my face, cover me with your semen."
    # alt-angle
    dc "Please, [mcname]!"
    mc "Oh - shit-!"
    # -ANimation 2: end
    # mc cum shoots up, starting to hit dc in the face
    scene sm1cs-dc010-86 mc-dc-cumming_c1 with vpunch
    pause
    # mc shoots a second load, and it covers dc's tits
    # dc smiles
    scene sm1cs-dc010-87 mc-dc-cumming-on-the-face_c1 with dissolve
    pause
    scene sm1cs-dc010-88 mc-dc-cumming-again_c1 with dissolve
    pause
    scene sm1cs-dc010-89 mc-dc-cumming-on-her-tits_c1 with dissolve
    dc "Mmmmmm, it feels just like I hoped it would."
    dc "It feels so wonderful..."
    # mc looking at dc, smiling
    scene sm1cs-dc010-89 mc-dc-cumming-on-her-tits_c2 with dissolve
    mc "Gotta say, this is quite a look for you, Officer Callahan."
    scene sm1cs-dc010-90 mc-dc-talking_c1 with dissolve
    dc "Oh is it?"
    mc "Uh huh. I think this should be your new makeup look!"
    scene sm1cs-dc010-91 dc-taking-cum-on-her-finger_c1 with dissolve
    dc "Hehehehehe!"
    # dc standing up now
    dc "Is that so? I have heard that it's great for your skin."
    # dc scoops up some cum from her tits
    scene sm1cs-dc010-92 dc-tasting-it_c1 with dissolve
    pause
    # dc sucks her finger
    scene sm1cs-dc010-93 mc-dc-talking_c1 with dissolve
    # dc smiling
    dc "And it's yummy to boot!"
    scene sm1cs-dc010-93 mc-dc-talking_c2 with dissolve
    mc "Wow, Debbie."
    scene sm1cs-dc010-94 mc-dc-noticing-buldge_c1 with dissolve
    dc "What!"
    mc "I didn't know you were a freak!"
    dc "Hehehehehe!{w} I like what I like."
    mct "Looks like Debbie is getting hard."
    # mc notices dc's bulge
    scene sm1cs-dc010-94 mc-dc-noticing-buldge_c2 with dissolve
    mct "Should I offer her a helping hand?"
    menu:
        "Yes, give Debbie a handjob":
            scene sm1cs-dc010-95 mc-dc-talking_c1 with dissolve
            mc "Hey, Debbie. Why don't you take a seat?"
            scene sm1cs-dc010-95 mc-dc-talking_c2 with dissolve
            dc "Okay? Sure."

            jump sm1cs_dc010_dc_hj

        "No":
            mct "I don't think I'm comfortable with that."
            scene sm1cs-dc010-95 mc-dc-talking_c2 with dissolve
            dc "I, uhm, think I'm going to go wash off quick."
            # mc looking up at dc smiling
            scene sm1cs-dc010-95 mc-dc-talking_c1 with dissolve
            mc "Oh, sorry - yeah! The bathroom is the door over to your right."
            dc "Thanks!"

            jump sm1cs_dc010_end

label sm1cs_dc010_dc_hj:

    # dc sits next to mc, mc looking at her
    scene sm1cs-dc010-96 mc-dc-sitting_c1 with dissolve
    mc "Debbie?"
    scene sm1cs-dc010-96 mc-dc-sitting_c2 with dissolve
    dc "Yes, [mcname]?"
    scene sm1cs-dc010-97 mc-dc-rolling-eyes_c1 with dissolve
    mc "I want you to take your pants off."
    # dc looks embarrassed
    scene sm1cs-dc010-98 mc-dc-talking_c2 with dissolve
    dc "Wait, uhm, I-"
    scene sm1cs-dc010-98 mc-dc-talking_c1 with dissolve
    mc "Nuh uh, no wiggling out of this, Officer. Time for your pat down!"
    # dc rolls her eyes
    scene sm1cs-dc010-97 mc-dc-rolling-eyes_c1 with dissolve
    dc "That was bad."
    # mc smiling
    scene sm1cs-dc010-98 mc-dc-talking_c1 with dissolve
    mc "What can I say? I have a talent for bad jokes!"
    mc "Now, come on. Pants off."
    dc "Fine... fine..."
    scene sm1cs-dc010-99 mc-thinking_c1 with dissolve
    mct "All right, you got this, [mcname]."
    dc "..."
    # wide shot of dc sitting next to mc, she's got an erection, looking away from mc
    scene sm1cs-dc010-100 mc-dc-naked_c1 with dissolve
    dc "Happy?"
    scene sm1cs-dc010-100 mc-dc-naked_c2 with dissolve
    mc "Yes!"
    # mc looking down at dc's very erect dick
    scene sm1cs-dc010-101 mc-dc-looking-at-her-erection_c1 with dissolve
    mct "God, she looks like she could cum if a light breeze picked up."
    scene sm1cs-dc010-101 mc-dc-looking-at-her-erection_c2 with dissolve
    mct "Was she really going to try and walk home with that?"
    scene sm1cs-dc010-101 mc-dc-looking-at-her-erection_c3 with dissolve
    dc "Well... say something."
    # mc looking at dc, dc still not looking at him
    scene sm1cs-dc010-102 mc-dc-look-at-me_c1 with dissolve
    mc "Debbie?"
    dc "Mhmm?"
    mc "Look at me."
    # dc looks sheepishly at mc
    scene sm1cs-dc010-103 mc-dc-talking_c1 with dissolve
    mc "You've got a great looking dick."
    # dc looks away again
    scene sm1cs-dc010-104 mc-dc-looking-away_c1 with dissolve
    dc "[mcname]-!"
    # mc grabs her dick
    scene sm1cs-dc010-105 mc-dc-grabbing-her-dick_c1 with vpunch
    dc "Woah-!"
    scene sm1cs-dc010-105 mc-dc-grabbing-her-dick_c2 with dissolve
    mc "Great enough that it deserves it's own pleasure."
    dc "I- what-"
    mc "Do you want this, Debbie?"
    # dc blushing
    scene sm1cs-dc010-106 mc-dc-talking_c1 with dissolve
    dc "I... I..."
    # dc looks at mc
    dc "*breathless* Yes, I really do."
    scene sm1cs-dc010-106 mc-dc-talking_c2 with dissolve
    mc "Good."
    # -Animation 3: mc gives dc a handjob on the couch
    # alt-angle
    scene sm1cs-dc010-107 mc-dc-handjob_c1 with dissolve
    dc "Ohhhh, ohhhhh..."
    mc "How's that feel, Debbie?"
    dc "Oh, it feels magnificent..."
    # alt-angle
    dc "Mmmmm... I... I..."
    mc "I, what?"
    dc "I... I've never gotten a handjob before..."
    # alt-angle
    dc "Except - mmmmm..."
    mc "Except?"
    dc "Except..."
    # alt-angle
    dc "Except after I go home... after a long day of work..."
    dc "Or..."
    dc "Or - nggghhhh - or after one of our dates..."
    # alt-angle
    dc "And I... I..."
    dc "God, this feels sooo goooood..."
    mc "And you what, Debbie?"
    # alt-angle
    dc "And I take off my sweaty clothes..."
    dc "I grab my hard cock in my hands.."
    dc "And I..."
    # alt-angle
    dc "Oh, I'm getting close, [mcname]!"
    mc "And you what?"
    dc "I - nggghhh - I can't-"
    # alt-angle
    mc "You really want to tell me that, right now?"
    mc "Because I can always stop."
    dc "Please, God, no!"
    # alt-angle
    mc "Then tell me, Debbie. What do you do?"
    dc "Oh God - mmmm - I think of you!"
    dc "I think of you, grabbing my cock, your cock in my ass!"
    # alt-angle
    dc "Or, or, your cock between my tits, in my mouth!"
    dc "I think of you cumming all over me as I stroek myself, and I- I-"
    dc "Cum!"
    # -Animation 3: end
    # dc's head whips back as she shoots cum straight up
    scene sm1cs-dc010-108 mc-dc-cumming_c1 with vpunch
    pause
    # dc's head is resting on the couch, there's now more cum over her tits
    scene sm1cs-dc010-109 mc-dc-asking_c1 with dissolve
    dc "Oh my God..."
    scene sm1cs-dc010-109 mc-dc-asking_c2 with dissolve
    mc "You okay?"
    scene sm1cs-dc010-110 mc-dc-smirking_c1 with dissolve
    dc "Mmhhmmmmm..."
    mc "Better than your fantasy?"
    # dc smirks looking at mc
    dc "Inifinitely better than my fantasy."
    # dc looks at her tits covered in cum
    scene sm1cs-dc010-111 mc-dc-looking-at-cum_c1 with dissolve
    dc "Oh, I am quite the mess now!"
    scene sm1cs-dc010-111 mc-dc-looking-at-cum_c2 with dissolve
    mc "Hahahaha! Yeah, little bit."
    # dc smiles and stands up
    scene sm1cs-dc010-112 mc-dc-standing_c1 with dissolve
    dc "Let me go get a little cleaned up."
    scene sm1cs-dc010-112 mc-dc-standing_c2 with dissolve
    mc "Bathroom is pretty much the only door, over on the right."
    scene sm1cs-dc010-113 dc-going_c1 with dissolve
    dc "Thank you!"
    # dc starts walking towards the bathroom

    jump sm1cs_dc010_end

label sm1cs_dc010_end:

    # mc relaxing on the couch, no pants on
    scene sm1cs-dc010-114 mc-thinking_c1 with fade
    mct "Man... I was definitely not expecting a titjob tonight..."
    mct "That was incredible."
    # mc smiling
    scene sm1cs-dc010-115 mc-smiling_c1 with dissolve
    mct "I think things between Debbie and I have reached a new level."
    # mc winces
    scene sm1cs-dc010-116 mc-wincing_c1 with dissolve
    mct "I just wish it hadn't required me getting my ass kicked to make it happen."
    # dc walks out of the bathroom, naked
    scene sm1cs-dc010-117 mc-dc-walking-out_c2 with dissolve
    dc "Wow, you have a nice bathroom!"
    scene sm1cs-dc010-117 mc-dc-walking-out_c1 with dissolve
    mc "Thank you!"
    scene sm1cs-dc010-117 mc-dc-walking-out_c3 with dissolve
    if player.has_played_scene("sm1cs_dc_renovation"):
        dc "And this place really came together!"
        mc "I know, right?"
        dc "Definitely better without all the tarps and scaffolding."
    else:
        dc "You've got a great place, [mcname]."
        mc "You think so?"
        dc "I do! I've always loved open concept, and it's so roomy here!"
    # dc getting back to the couch, smiling
    scene sm1cs-dc010-118 mc-dc-talking_c1 with dissolve
    dc "So, what should we do with the rest of our night, [mcname]?"
    scene sm1cs-dc010-118 mc-dc-talking_c2 with dissolve
    mc "Want to make it a double feature?"
    # dc blushes
    scene sm1cs-dc010-119 mc-dc-talking_c1 with dissolve
    dc "I don't think I could go another round right now..."
    scene sm1cs-dc010-119 mc-dc-talking_c2 with dissolve
    mc "No, no. I meant like watching another action movie."
    # dc gets excited
    scene sm1cs-dc010-120 dc-excited_c1 with dissolve
    dc "Oh, that would be awesome!"
    # dc goes to sit down on the couch
    scene sm1cs-dc010-121 dc-wait_c1 with dissolve
    dc "Wait..."
    # dc pulls out her phone, looking at it
    scene sm1cs-dc010-122 dc-pulling-out-her-phone-magiccc_c1 with dissolve
    pause
    # dc has a shocked expression
    scene sm1cs-dc010-123 dc-yikes_c1 with dissolve
    dc "Oh my God! It is {i}so late!{/i}"
    # dc looking at mc
    dc "I am so sorry, [mcname], but I have to go. Captain scheduled me for an early shift tomorrow."
    mc "Oh? Something to be worried about?"
    # dc smiling
    scene sm1cs-dc010-124 mc-dc-talking_c1 with dissolve
    dc "No, not really Just some paperwork to do."
    dc "And... well, the other thing isn't important."
    # dc bending over to pick up her shirt (shirt out of frame), mc looking at her
    scene sm1cs-dc010-124 mc-dc-talking_c2 with dissolve
    mc "Oh? What's the unimportant thing?"
    scene sm1cs-dc010-125 dc-smiling_c1 with dissolve
    dc "Probably nothing."
    # mc raises an eyebrow (no dc in this shot)
    scene sm1cs-dc010-126 mc-dc-picking-up-clothes_c1 with dissolve
    mct "Hmmm... I wonder what she's not saying."
    mct "Maybe the Captain doesn't like her."
    scene sm1cs-dc010-127 mc-thinking_c1 with dissolve
    mct "I hope everything goes alright in whatever it is."
    # dc stands up, now dressed
    scene sm1cs-dc010-128 mc-dc-talking_c1 with dissolve
    dc "This sucks. I hate to stop our date midway."
    scene sm1cs-dc010-128 mc-dc-talking_c2 with dissolve
    mc "It's alright, it's the life of a public servant."
    dc "Yes, yes it is."
    # dc leans down and kisses mc
    scene sm1cs-dc010-129 mc-dc-kissing_c1 with dissolve
    pause
    # dc stands up surprised
    scene sm1cs-dc010-130 mc-dc-talking_c1 with dissolve
    dc "Oh my God, that was so casual."
    dc "I - uhm -"
    scene sm1cs-dc010-130 mc-dc-talking_c2 with dissolve
    mc "Debbie, it's okay. You can give me a kiss goodbye."
    # dc blushes
    scene sm1cs-dc010-131 dc-blushing_c1 with dissolve
    dc "Uhm, well... good!"
    # dc kisses mc again
    scene sm1cs-dc010-132 mc-dc-kissing-again_c1 with dissolve
    pause
    # dc stands up and is walking for the door
    scene sm1cs-dc010-133 mc-dc-walking-talking_c1 with dissolve
    dc "I'll talk to you later, 'kay?"
    scene sm1cs-dc010-133 mc-dc-walking-talking_c2 with dissolve
    mc "Sounds good, Debbie! Get some sleep!"
    dc "Oh, I will!"
    # dc standing by the door
    scene sm1cs-dc010-134 mc-dc-bye_c1 with dissolve
    dc "I think I'm going to sleep like a rock tonight!"
    mc "Haha, me too."
    dc "Bye, [mcname]."
    scene sm1cs-dc010-134 mc-dc-bye_c2 with dissolve
    mc "Bye!"
    # dc is gone
    scene sm1cs-dc010-135 mc-alone_c1 with dissolve
    $ SMGallery.unlock_gallery_slot("achievement", "18_PACKING_HEAT")
    pause
    # mc standing in front of the couch, still no pants, smiling
    scene sm1cs-dc010-135 mc-alone_c2 with dissolve
    mct "Well, all in all, a good night!"
    mct "Ended earlier than I wanted, but, hey, still a good night."
    # mc stretches
    scene sm1cs-dc010-136 mc-stretching_c1 with dissolve
    mct "But man, am I getting tired. Maybe it's time to turn in."
    mct "I wonder-"
    # sy walks in the door
    scene sm1cs-dc010-137 mc-sy-back_c1 with dissolve
    mc "Stacy! You must be able to read my mind!"
    scene sm1cs-dc010-137 mc-sy-back_c2 with dissolve
    sy "Huh?"
    if persistent.is_special:
        mc "I was just about to wonder where my little sister had run off to."
    else:
        mc "I was just about to wonder where you were."
    # sy looks tired
    scene sm1cs-dc010-138 sy-tired_c1 with dissolve
    sy "Well, here I am. Tonight was a total bust."
    mc "Really?"
    scene sm1cs-dc010-139 sy-walking_c1 with dissolve
    sy "Yeah. Dude didn't have anything except business cards. Was trying to drum up business."
    # sy walking towards the couch
    scene sm1cs-dc010-140 mc-sy-talking_c1 with dissolve
    sy "So, a whole night wasted..."
    # sy noticing mc doesn't have pants on, smirking
    sy "Seems like you had a bit of a \"bust\" yourself, tonight."
    scene sm1cs-dc010-140 mc-sy-talking_c2 with dissolve
    mc "Oh shit, I forgot to put my pants back on."
    # sy standing next to the couch
    scene sm1cs-dc010-141 mc-sy-talking_c1 with dissolve
    sy "I'm guessing that was the woman I passed on the way in?"
    mc "Yeah, that was Debbie."
    sy "The park cop?"
    scene sm1cs-dc010-141 mc-sy-talking_c2 with dissolve
    mc "Uh huh."
    # sy looks impressed
    scene sm1cs-dc010-142 mc-sy-impressed_c1 with dissolve
    sy "Damn, you did good, [mcname]!"
    scene sm1cs-dc010-142 mc-sy-impressed_c2 with dissolve
    mc "Why thank you-"
    # mc looks slightly irritated
    scene sm1cs-dc010-143 mc-irritated_c1 with dissolve
    mc "Wait, does that mean sometimes I don't do good?"
    scene sm1cs-dc010-143 mc-irritated_c2 with dissolve
    sy "Hahahaha!"
    # sy walking for the stairs
    sy "I mean, you did end up with me!"
    mc "And I love you to bits!"
    sy "I bet you tell all the girls that."
    # sy walking up the stairs, mc looking at her
    scene sm1cs-dc010-144 mc-sy-going-up_c1 with dissolve
    mc "That's because I love them all!"
    mc "Some because they're nice, and you, because you're a feral little gremlin!"
    scene sm1cs-dc010-144 mc-sy-going-up_c2 with dissolve
    sy "Hehehehe!"
    # sy looking over her shoulder
    scene sm1cs-dc010-145 mc-sy-talking_c1 with dissolve
    sy "Well, this little gremlin is going to try and unwind a bit after the night she's had. Maybe you can join me?"
    scene sm1cs-dc010-145 mc-sy-talking_c2 with dissolve
    mc "Yeah, maybe."
    sy "Hehehehe."

    jump sm1cs_dc010_exit_to_studio

label sm1cs_dc010_exit_to_studio:

    # -6 ENERGY
    # SHOULD BE TIMESLOT 11
    # EXIT TO STUDIO FREE ROAM

    $ StoryController.end_scene(DC_STORY)
    return
