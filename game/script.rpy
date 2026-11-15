define h = Character("Hailie", color="#d875b9")
define j = Character("Justin", color="#76cc67")
define m = Character("Marley", color="#784581ff")
define e = Character("emilie", color="#515bc46d")
define d = Character("Darel", color="#e4d534")
define n = Character("Narrartor", color="#e39434")

image bg_trashy_apartment = "images/trashy_apartment.jpg"
image bg_clean_apartment = "images/clean_apartment.avif"
image bg_baking_kitchen = "images/kitchen.webp"
image bg_night_city = "images/nighttime.jpg"

image haylie_chud:
    "images/Haylie_Chud.png"
    zoom 0.5
image no_stink:
    "images/No_stink.png"
    zoom 0.5
image good_posture:
    "images/good_posture.png"
    zoom 0.5
image mouth_fix:
    "images/mouth_fix.png"
    zoom 0.5
image ankle_fix:
    "images/ankle_fix.png"
    zoom 0.5
image chef_coat:
    "images/chef_coat.png"
    zoom 0.5
image change_clothes:
    "images/changed_clothes.png"
    zoom 0.5
image professional_attire:
    "images/professinal.png"
    zoom 0.5
image headset:
    "images/headset.png"
    zoom 0.5
image glasses:
    "images/glasses.png"
    zoom 0.5
image hair:
    "images/hair_fixed.png"
    zoom 0.5
image eye_bags:
    "images/eyebag_fix.png"
    zoom 0.5
image nose:
    "images/nose_fix.png"
    zoom 0.5
image chin:
    "images/chin_fix.png"
    zoom 0.5
image happy_haylie:
    "images/happy.png"
    zoom 0.5
image mid_haylie:
    "images/haylie_mid.png"
    zoom 0.5
image sad_haylie:
    "images/sad.png"
    zoom 0.5
image justin_base:
    "images/Justin_base.png"
    zoom 0.5
image justin_happy:
    "images/justin_happy.png"
    zoom 0.5
image justin_angry:
    "images/justin_angry.png"
    zoom 0.5
image dead_justin:
    "images/justin_dead.png"
image marley_base:
    "images/marley_base.png"
    zoom 0.5
image marley_jealous:
    "images/Marley_jealous.png"
    zoom 0.5
image marley_envious:
    "images/marley_smirking.png"
    zoom 0.5   
image emilie_base:
    "images/emilie_base.png"
    zoom 0.4
image emilie_sad:
    "images/emilie_sad.png"
    zoom 0.4
image darel_base:
    "images/darel_base.png"
    zoom 0.4
image darel_sad:
    "images/sad_darel.png"
    zoom 0.4
image camera:
    "images/camera.png"
    zoom 0.1


label start:

    play music "audio/ember-lounge.mp3"
    scene bg_trashy_apartment

    show haylie_chud with dissolve

    n "In a trashy apartment stands a woman who wants to make a name for her self."

    n "Should she.:."

menu:
    "Take a shower.":
        jump clean
    
    "Go straight to competiton.":
        jump stinky

label stinky:

    scene bg_baking_kitchen
    show justin_base at right with fade:
        xzoom -1.0
    show haylie_chud at center with fade

    n "The stinky woman enters the kitchen earlier than the other guests, striking Justin Star with a curious interest."

    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show haylie_chud at left
    show marley_base at right:
        xzoom -1.0

  
    n "Marley, seeing this woman, is phyisically disgusted. Upon smelling Hailie, she physically gags; heaving over a counter."

    show justin_base at center with fade
  
    j "Hello and welcome to my baking show, Baking off the Stars, I have four contestants here for you today!"

menu:
    "Give up Justin and bake away for your future!":
        jump level_2
    
    "Stare at Justin flirtatiously while lazily kneading the no-knead dough.":
        jump bad_ending

label level_2:
    scene bg_baking_kitchen


label bad_ending:
    scene bg_baking_kitchen
    show marley_envious at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today, the baker being kicked off is Hailie, she did not show her best through her attire and effort in baking."
    m "You're SO right Justin!!!"
    ".:. Bad Ending."
    return
label clean:
    scene bg_clean_apartment
    show no_stink with fade
    h "It feels like a weight was lifted off of my shoulders! I feel so refreshed."
    n "Hailie has improved, but there is still more to go... next she should..."

menu:
  
    "Continue with her improvements.":
        jump good_posture

  
    "Stop the lock in and start the bake-off.":
        jump clean_but_messy 
    
label good_posture:
    scene bg_clean_apartment
    show good_posture with dissolve
    h "I feel a literal lift off my shoulder! Maybe I am improving?"
    n "We watched Hailey improve herself thus far... should she continue:"

menu:
    "Be better for Justin Star!":
        jump mouth
    
    "Go to the competition with her current improvements.":
        jump straight_back 

label clean_but_messy: 
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show no_stink at left
    show marley_base at right:
        xzoom -1.0

    n "The slightly unprepared cosmetically-displeasing woman enters the kitchen."

    show marley_base at center
    m "Who is this shambled ugly woman?"
    show marley_base at right:
        xzoom -1.0

    show justin_base with fade
  
    j "Hello, and welcome to my baking show, Baking off the Stars. I have four contestants here for the viewers today!"

menu:
    "Lock-in on the butter creaming for your cookies.":
        jump level_r   
    "Stare at Justin... stare a bit at Justin.":
        jump bad_ending_2

label mouth:
    scene bg_clean_apartment
    show mouth_fix
    h "I feel a great surge of energy and rejuvination."
    n "Should Hailie continue her mog fest?"

menu:
    "Fix thy blasphemous lower leg accessory.":
        jump ankle
    
    "Go to the bake off like a trogladyte.":
        jump bake_off

label straight_back:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show good_posture at left
    show marley_base at right:
        xzoom -1.0
    
    n "The woman feels confident in her skills due to no pain in her back."
    show marley_base at top
    m "Who is this impudent wretch?"
    show marley_base at right:
        xzoom -1.0
    show justin_base with fade
  
    j "Hello and welcome to my baking show, Baking off the Stars, I have four contestants here for you today!"
menu:
    "Do your best with your cake batter.":
        jump level_f
    
    "Stare at Justin.......... MMMMMMMMMmmmm Justin Starrrrr.":
        jump bad_ending_3


label level_r:
    scene bg_baking_kitchen
    show darel_sad at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Darel,he did not show his best with his baking and his attitude."
    d "*crying loudly*"
 
menu:
    "continue with Hailie's lady luck!":
        jump bad_ending_2

label bad_ending_2:
    scene bg_baking_kitchen
    show marley_envious at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Hailie. She did not show her best through her attire and her baking."
    m "You're so right Justin!"
    ".:. Bad Ending possibility 2."
    return

label level_f:
    scene bg_baking_kitchen
    show emilie_sad at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Emilie, she did not show her best with her baking and her attitude."
    show emilie_sad:
        yzoom 0.5
    e "*crying on the floor*"   

menu:
    "Try you absolute hardest with your snickerdoodles.":
        jump level_g
    
    "Try not very hard, but stare at Justin.":
        jump bad_ending_3

label bad_ending_3:
    scene bg_baking_kitchen
    show marley_envious at right with fade:
        xzoom -1.0
    show justin_happy with fade
    j "The baker kicked off is Hailie. She did not show her best through her attire and her baking."
    m "Justinnnn!!! *She kisses him.*"
    ".:. Bad Ending possibility 3."
    return

label ankle:
    scene bg_clean_apartment
    show ankle_fix
    n "Hailie takes off the wrap around her leg, the pressure relief is audible."
    h "My ankle feels so much better after that..."

menu:
    "Continue improving for Justin STARRRRRRRRRRRR!":
        jump chef

    "Go to the bake off as you are now.":
        jump bake_off_2


label bake_off:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show no_stink at left
    show marley_base at right:
        xzoom -1.0
    j "*off screen* Today our four bakers will bake for their lives!!!! Get to baking."
label level_g:
    scene bg_baking_kitchen
    show darel_sad at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today the baker being kicked off is Darel. He did not show his best with his baking and his attitude."
    d "*crying profusely*"

menu:
    "Continue excelling with your personal upgrades!":
        jump level_h

    "give up with everything. Stare at Justin.":
        jump bad_ending_3

label bake_off_2:
    scene bg_baking_kitchen 
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show no_stink at left
    show marley_base at right:
        xzoom -1.0
    j "*off screen* Today I have four bakers for the compeition! Get to baking chat."
label level_h:
    scene bg_baking_kitchen
    show marley_base at right with fade:
        xzoom -1.0
    show justin_base with fade 
    j "Today the baker being kicked off is Marley. She did not show her best with her baking."
    d "*crying and vomitting in the kitchen.*"
menu:
    "Win. That. CUPPPPPPPPPPPPPPPPPPPPPPPP!!!!!!!!!!!!!!!!":
        jump mid_ending

label mid_ending:
    scene bg_baking_kitchen
    show straight_back at left with dissolve
    show justin_base with fade 
    j "Today our baker who won is..."
    n "........................................................................................."
    h "*Premptive tears of joy*"
    j "HAILIE! Perhaps we get coffee later?"
    "mid-ending..."
    return

label chef:
    scene bg_clean_apartment
    show chef_coat with dissolve
    h "I look so much much much better!"
    n "Young Hailie has a lot to do, should she keep going?"
menu:
    "Improve improve improve improve improve more":
        jump change_clothes
    "Go to the bake off... Late?":
        jump bad_ending_4

label change_clothes:
    scene bg_clean_apartment
    show change_clothes with fade
    h "I love my new outfit so much!!!"
    n "She absolutely needs to keep going, should she go forth?"
menu: 
    "Continue with her cosmetic advancements.":
        jump professinal
    "Go to bake off really late! OH NO!":
        jump bad_ending_11

label professinal:
    scene bg_clean_apartment
    show professional_attire with fade 
    h "I look a lot better, but I'm running late! This is so addicting though."
    n "She could keep going, but she's late to the compeititon! She needs to leave to make it in time to compete. The choice is yours."
menu:
    "Keep improving and be late.":
        jump headset
    "Go to bake off as you are now.":
        jump bad_ending_5

label headset:
    scene bg_clean_apartment
    show headset with dissolve
    h "I look great, no concern for time now!"
    n "Hailie has no concern for the time at stake, and she is ready to continue and give her glow up her all."
menu: 
    "Keep going with her glow up.":
        jump glasses
    "Go to bake off 'reaaaallllllllyyyyyyyyy late'???":
        jump bad_ending_6

label glasses: 
    scene bg_clean_apartment
    show glasses
    h "I look really good right now and I feel stunning!"
    n "Keep going with it all!"
menu:
    "Keep improving!":
        jump hair
    "Give up and go to the bake-off":
        jump bad_ending_7

label hair:
    scene bg_clean_apartment
    show hair
    h "I look super great!"
    n "Nothing to say about her improvements, what to do?"
menu:
    "Keep the improvements coming.":
        jump eyebags
    "This is good enough, go to the bake off?":
        jump bad_ending_8

label eyebags:
    scene bg_clean_apartment
    show eye_bags
    h "I've changed a lot in such little amounts of time, I feel better than ever."
    n "She looks exhausted, maybe she needs some sleep."
menu: 
    "Fix up her drippy nose.":
        jump nose
    "No more time to get to the bake off for today. Sleep early to get to tomorrows?":
        jump bad_ending_9

label nose:
    scene bg_clean_apartment
    show nose
    h "I can breathe!?"
    n "She's looking great and breathing greater too!"
menu:
    "Hit the gym!":
        jump chin 
    "No bake off now, sleep for tommorow?":
        jump bad_ending_10
    
label chin:
    scene bg_clean_apartment
    show chin
    h "I feel great, and I look great too."
    n "She's ready for the bake off tomorrow!"
menu:
    "Sleep for bake off tommorow.":
        jump bake_off_real 
    "Go out tonight, you feel a premonition.":
        jump meet_justin

label bad_ending_4:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show change_clothes at left
    show marley_base at right:
        xzoom -1.0
    j "Sorry bakers, I'm stuck in traffic, the bake off is cancelled!"
    "You've reached bad ending possibility 4."
    return

label bad_ending_5:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show professinal at left
    show marley_base at right:
        xzoom -1.0
    j "Sorry bakers, I'm stuck in traffic, the bake off is cancelled!"
    "You've reached bad ending possibility 5."
    return

label bad_ending_6:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show headset at left
    show marley_base at right:
        xzoom -1.0
    n "Justin never showed up."
    "You've reached bad ending possibility 6."
    return 

label bad_ending_7:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show glasses at left
    show marley_base at right:
        xzoom -1.0
    n "Justin never showed up."
    "You've reached bad ending possibility 7."
    return

label bad_ending_8:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show hair at left
    show marley_base at right:
        xzoom -1.0
    n "Justin called Marley to let her know she won the bake off."
    "You've reached bad ending possibility 8."
    return

label bad_ending_9:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show eye_bags at left
    show marley_base at right:
        xzoom -1.0
    n "Justin called Marley to let her know she won the bake off."
    "You've reached bad ending possibility 9."
    return

label bad_ending_10:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show nose at left
    show marley_base at right:
        xzoom -1.0
    n "Justin called Marley to ask her out on a date. Hailie passed away on the spot."
    "you've reached bad ending possibility 10."
    return

label bake_off_real:
    scene bg_baking_kitchen
    show darel_base at topright:
        xzoom -1.0
    show emilie_base at topleft
    show happy_haylie at left
    show marley_base at right:
        xzoom -1.0
    
    "The bakers are baking yo, the ovens are slamming and the cakes are jamming."
menu:
    "Bake your hardest to win this thang!":
        jump bake_off_real_pt2
    "Stare at Justin.":
        jump bake_off_ending

label meet_justin:
    scene bg_night_city
    show justin_happy at left 
    show happy_haylie at right:
        xzoom -1.0
    j "hey pretty lady..."
    h "hi"
    n "you have reached the true love ending!"
    return 
label bake_off_ending:
    scene bg_baking_kitchen
    show happy_haylie at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Hailie. I'm so sorry, you're beautiful and I really love you."
    j "Will you marry me Hailie?"
    h "*crying* Yes I'll marry you!"
    "You have reached marry ending."
    return
label bake_off_real_pt2:
    scene bg_baking_kitchen
    show darel_sad at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Darel, he did not show his best with his baking and his attitude."
    d "*crying a lot, he smells like he soiled himself.*"
menu: 
    "Lock in and get the bag.":
        jump bake_off_real_pt3
    "Give up because you're exhausted.":
        jump bake_off_ending

label bake_off_real_pt3:
    scene bg_baking_kitchen
    show emilie_sad at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Emilie, she did not show her best with her baking and her attitude."
    e "*crying and having a really bad day*"
menu:
    "LOCK IN TWIN!!!!!!!!!!!":
        jump bake_off_real_pt4
    "Hailie is too sleepy to continue.":
        jump bake_off_ending

label bake_off_real_pt4:
    scene bg_baking_kitchen
    show marley_jealous at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "Today our baker being kicked off is Marley ,he did not show her best with her baking and her attitude."
    m "*crying*"
menu:
    "Win, and maybe Justin's heart too? ;)":
        jump good_ending

label good_ending:
    scene bg_baking_kitchen
    show happy_haylie at right with fade:
        xzoom -1.0
    show justin_happy with fade 
    j "I love you my catboy femcat bbg gng."
    h "Kiss me you hot catboy."
    "you have reached the good ending!"
    return

label bad_ending_11:
    scene bg_baking_kitchen
    show change_clothes at left with dissolve
    show dead_justin at left:
        yzoom 0.5
        xzoom -1.0
    play sound "audio/DEATH.mp3"
    h "I KILLED HIM *Crying*"
    j "dead"
    "you've reached bad ending possiblity 11"
    return