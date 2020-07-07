define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(2.0)
define fadehold = Fade(3.0, 1.0, 3.0)
define w = Character("Wife")
define h = Character("Husband")
define s = Character("Student")
define g = Character("Laura")
define gd = Character("Game Director")
define t = Character("Tech Lead")
define a = Character("Lead Artist")
define i = Character("Intern")
define l = Character("Lonely Girl")
define j = Character("Julie")
define m = Character("Mom")
define d = Character("Dad")
define tl = Character("Tired Lodger")
define lf = Character("Lodger's Fiancé")
define sf = Character ("Sleepy Friend")
define ym = Character ("Young Mother")
init:
    image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)
init:
    $ timer_range = 0
    $ timer_jump = 0

label start:
    stop music fadeout(3.0)
    scene black
    with slowerfade

    $ badhim = False
    $ goodhim = False
    $ badher = False
    $ goodher = False
    $ devgood = False
    $ devneut = False
    $ devbad = False
    $ phonegood = False
    $ phonebad = False
    $ famepilogue = False
    $ lod1epilogue = False
    $ meetepilogue = False
    $ lod2epilogue = False
    $ lovepilogue = False
    $ separepilogue = False
    $ solend = False
    $ epilogues = 0
    $ ending = 0
    """
    You're in your room.

    In front of you there's a scratchpad. On the pages you've left some notes, the days before.

    Yet, they're useless, now.
    """

    scene room
    with slowfade
    """
    From the window in front of you, you see a building's facade.

    Different apartments for different people. From where you're you can see glimpses of all these lives.

    On their faces you see the shadows of different problems, difficult situations they don't seem to be able to fix.

    Maybe, they think those situations are impossible to be repaired.

    As you watch them, you wonder what problems are they dealing with and if you could be able to fix them.
    """

label room:
    if ending >= 2:
        call screen roomscreen
    if epilogues >= 1:
        call screen roomscreen
    if ending == 1:
        "Maybe it could be worth checking the apartments already visited, too."
        call screen roomscreen
    if epilogues == 3:
        jump gamending
    else:
        call screen roomscreen

label ink:
    """
    aaa
    """
label notes:
    """
    aaa
    """
label board:
    """
    aaa
    """
label mug:
    """
    aaa
    """
label lamp:
    """
    aaa
    """
label apartments:
    scene roomhover
    $ renpy.pause(0.5)
    scene apartments
    with slowdissolve
    $ renpy.pause(1)
    call screen apartmentsscreen
label apartmentlon:
    call screen apartmentsscreen
##### APARTMENT 1 SCENE START ############################################################################################################################
label apartment1:
    if famepilogue == True:
        "The family is now eating happily..."
        jump apartmentlon
    if lod1epilogue == True:
        "The new lodgers are watching the dusk while drinking tea, silently."
        jump apartmentlon
    if solend == True and goodhim == True and famepilogue == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("dinnertitle.mkv")
        scene dinner
        with slowfade
        """
        A calm evening.

        A family reunion.

        Silent feelings that fill the apartment's atmosphere.
        """
        m "So, how are you feeling, sweetie?"
        l "I still don't really know..."
        m "You know...love affairs are complicated. Very complicated."
        d """
        Yes, indeed.

        What is important, though, is to not fall in hatred's trap.

        One must always love, even if he's not loved.
        """
        menu:
            "I still have...hope.":
                m "Hope is the basis for love."
                d """
                Yes, to have hope is the same thing as loving life.

                You know, dear...living is difficult.

                Very difficult.

                But since you have hope you can endure everything.

                You can endure pain.

                You can endure grief.

                You can endure solitude.

                And to endure all those things means that you can bravely take on life.

                Without any fear, that is.
                """
                """
                The young lonely girl smiles at her parents.

                In her memory the face of who is now her ex-girlfriend still shines.

                But that shining is becoming more and more pale.

                Yet, she does not feel any hate for her.

                She is sad, that's for sure.

                She still feels more lonely than before.

                But as long as she has that bright and pure hope, she feels calm.

                And even if the world is harsh and life isn't beautiful or pleasing as she wouls like it to be...

                She still believes that the future could be better.
                """
            "But how can one still love?":
                d """
                Each one of us is lonely.

                We are lonely because we're singular individuals.

                And even when we live with someone...

                When we love somaone and share our life with him or her...

                We still are singular individuals and so we're still alone.

                Once someone understands that, he can understand that love is mutable.
                """
                m """
                And since it's mutable, we only have to accept that fact.

                Understanding and accepting means that once love seems to be faded between two or more people,

                It really isn't, as love and hope are the basis of human connection.

                She left you, that's true.

                But you two have been connected for some time and you still are as human beings.

                As old friends and lovers.

                This unity, when you think about it, is strong enough to eliminate all the hate you could feel.ù

                And even if you now feel lonely physically and sentimentally...

                That doesn't mean you'll meet someone that will once again erase these feelings.

                You have to put hope in the future.
                """
                """
                'To put hope in the future...'

                These words reverberates in the lonely girl's mind.

                Maybe they'll stay in her head forever, as long as she truly hopes things will get better.

                But surely as long as she tries her best to fulfill that hope.

                But hoping means to act, and not to lie in wait of better opportunities.
                """
        $ famepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if solend == True and goodher == True and famepilogue == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("dinnertitle.mkv")
        scene dinner
        with slowfade
        """
        A calm evening.

        A family reunion.

        Silent feelings that fill the apartment's atmosphere.
        """
        m "So, how are you feeling, sweetie?"
        l "I still don't really know..."
        m "You know...love affairs are complicated. Very complicated."
        d """
        Yes, indeed.

        What is important, though, is to not fall in hatred's trap.

        One must always love, even if he's not loved.
        """
        menu:
            "I still have...hope.":
                m "Hope is the basis for love."
                d """
                Yes, to have hope is the same thing as loving life.

                You know, dear...living is difficult.

                Very difficult.

                But since you have hope you can endure everything.

                You can endure pain.

                You can endure grief.

                You can endure solitude.

                And to endure all those things means that you can bravely take on life.

                Without any fear, that is.
                """
                """
                The young lonely girl smiles at her parents.

                In her memory the face of who is now her ex-girlfriend still shines.

                But that shining is becoming more and more pale.

                Yet, she does not feel any hate for her.

                She is sad, that's for sure.

                She still feels more lonely than before.

                But as long as she has that bright and pure hope, she feels calm.

                And even if the world is harsh and life isn't beautiful or pleasing as she wouls like it to be...

                She still believes that the future could be better.
                """
            "But how can one still love?":
                d """
                Each one of us is lonely.

                We are lonely because we're singular individuals.

                And even when we live with someone...

                When we love somaone and share our life with him or her...

                We still are singular individuals and so we're still alone.

                Once someone understands that, he can understand that love is mutable.
                """
                m """
                And since it's mutable, we only have to accept that fact.

                Understanding and accepting means that once love seems to be faded between two or more people,

                It really isn't, as love and hope are the basis of human connection.

                She left you, that's true.

                But you two have been connected for some time and you still are as human beings.

                As old friends and lovers.

                This unity, when you think about it, is strong enough to eliminate all the hate you could feel.ù

                And even if you now feel lonely physically and sentimentally...

                That doesn't mean you'll meet someone that will once again erase these feelings.

                You have to put hope in the future.
                """
                """
                'To put hope in the future...'

                These words reverberates in the lonely girl's mind.

                Maybe they'll stay in her head forever, as long as she truly hopes things will get better.

                But surely as long as she tries her best to fulfill that hope.

                But hoping means to act, and not to lie in wait of better opportunities.
                """
        $ famepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room

    if solend == True and badhim == True and lod1epilogue == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("lodg1title.mkv")
        scene lodger1
        with slowfade
        """
        Once someone abandons a house, someone else is instantly ready to occupy it.

        An apartment always keeps the leftovers of its previous owners.

        It hides them, making them invisible.

        Pale memories of who has been there before.

        But somehow ready to be catched by the eyes of those who know how to observe.

        Those who are able to see beyond the quiet state of things.
        """
        tl "So, you're the daughter of the previous owners, right?"
        l "Yes. They asked me to take care of the house and find a new lodger..."
        tl "Oh, I see."
        "An awkward, embarassing silence."
        tl "It'a nice to meet you, really."
        l "Oh, for me too, yes."
        tl "Well anyway, I wanted to ask you something."
        l "Yes?"
        tl "Your parents left here some things, right?"
        l "Well, yes."
        tl """
        Could you tell me why?

        I mean, usually people take everything away when tey move out.

        But your parents left many things.
        """
        l "Oh, it's some sort of habitude of them."
        tl "Habitude...?"
        l """
        Yes, they leave things that could be useful for others.

        They don't realize that sometimes it would be better if they...didn't.
        """
        tl "I think it's gentle."
        l "Really?"
        tl """
        Yes, really.

        It's not that important if what they leave is useful or not.

        It's gentle because it means they care about others.
        """
        menu:
            "What if you'll have to toss them?":
                tl """
                That would be unfortunate, but you see...

                Truth is that I needed exactly what they left.

                Let's say that I had to leave some things in the  place where I used to live.

                So now I have almost nothing.

                And it's the same for the person I'll start living with in the next days.

                So what they left will be very useful to us.
                """
                l "Oh, that sounds...mysterious. And very sad, too."
                tl """
                There's nothing so mysterious about it, really...

                It's what happens when you hurt someone, you know?

                You break the promise made with that person and everything there was just...disappears.

                And you start falling, trying to build something new out of the mistake you made.

                Of course feelings have been hurt.

                Of course there are broken hurts and tears, and screams, and...

                Oh, well, I'm sorry...

                I know that's none of your business, but...every time I start talking I can't stop.
                """
                menu:
                    "No, please...go on.":
                        tl """
                        Oh...

                        Well, now that you said it I realize it's not so simple to continue, but...

                        Let's start by that: betraying someone is painful.

                        Painful for both parts, that is.

                        But even if it is, there's still some kind of...love?

                        I mean, you of course do it for love.

                        There may be physical implications, desires, but for me...there was only love.

                        And it's that love what I decided to follow.

                        So here I am now, a tired poet with a broken history and a 'new beginning'.
                        """
                        l "That must be painful..."
                        tl """
                        Yes, it is.

                        But as long as love is still in my life...I feel better.
                        """
                        """
                        Feeling better as long as there is love...

                        Thinking about it, the lonely girl realizes that love is still there for her too.

                        Love for her family.

                        Love for herself.

                        Love for life itself.

                        Could it be that this love will make her feel better too?
                        """
                    "Yes, that's none of my business.":
                        tl """
                        Yeah, right.

                        Well, it's nice that you came here to say hi, anyway.

                        I already feel welcomed.
                        """
                        l "Very good. I guess I must leave, now."
                        tl "That's fine. Bye, then and...thank you for listening, anyway."
                        $ lod1epilogue = True
                        $ epilogues += 1
                        scene black
                        with slowfade
                        scene room
                        with fade
                        $ renpy.pause(1)
                        jump room
            "It's kind of you.":
                tl """
                Well, I think that kindness is the least I can be.

                I mean...we live in an unkind environment, right?

                And what good can make being enraged because of items I don't want?

                Or because other people decide to be gentle and think about what could be useful and then leave it?

                Your parents decided to separate themselves of something in what I can imagine isn't a simple moment.

                Moving out is never simple, for anyone.

                And, to be sincere, they just saved me, as I don't have at all these things!

                So, if it wasn't for them, me and the person I'll live with would have passed a not so great moment in a shop, searching for them!
                """
                l "That really make me happy, then!"
                tl """
                Yeah, me too.

                I think yours is a very gentle family.

                I would like to meet your parents, one day, but I think that you got all their kindness.

                You came here to say hi, help me understand some things about the apartment and treated me very gently.

                That's something...rare.

                I think that when people have choices, they can be very mean.

                But not you.

                And that tells a lot.
                """
        """
        The apartment's door suddenly opens.
        """
        scene lodger1_2
        with dissolve
        """
        A young girls enters and watches us with a large, surprised smile.
        """
        tl "Oh, you're here finally!"
        lf """
        Sorry, I'm late! There was a lot of traffic...

        And you are?
        """
        l "The previous owners' daughter, nice to meet you."
        tl """
        She lives downstairs, so she came here to say hi.

        Oh, I made some tea for you too, take it.
        """
        lf "Thanks a lot!"
        scene lodger1_3
        with dissolve
        lf "Knowing him, I guess he already thanked you at least ten times for coming here, right?"
        tl """
        Hey, that's not true! I tried to restrain myself...

        This time.
        """
        l "Uhmm, don't worry, he was very gentle."
        lf "That's good, he always thanks and excuses himself too much!"
        tl "I think it wasn't necessary to tell her all that..."
        lf "Oh, you're right, I'm sorry!"
        """
        The lonely girl finishes her tea and smiles at both of them.

        The silence surrounding them all is starting to be a little embarassing.
        """
        lf "Listen, why don't you stay with us for dinner?"
        l "Oh no, don't worry, please! I have to go now, anyway."
        tl "No problem, maybe another day, right?"
        l "Yes, that would be splendid!"
        lf "Well, then, you can come here when you want."
        l "Thanks, you're both very kind. It was very nice meeting you."
        scene black
        with slowfade
        """
        And so she says hi and leaves.

        As she goes down the stairs, she starts thinking about how beautiful that couple was.

        And the words of a poem she listened long time ago flows through her mind.

        It sounded like...

        'Love is eternal, here rests for a time.'

        Perhaps the dead lie happily in the well tended plots, or perhaps they'd prefer the forgotten overgrown corners.

        Perhaps they prefer their names obliterated by time and the weather.

        Perhaps not.'

        Thinking about it...

        She instantly understands that, as the poem's author, she should leave.
        """
        $ lod1epilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if solend == True and badher == True and lod1epilogue == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("lodg1title.mkv")
        scene lodger1
        with slowfade
        """
        Once someone abandons a house, someone else is instantly ready to occupy it.

        An apartment always keeps the leftovers of its previous owners.

        It hides them, making them invisible.

        Pale memories of who has been there before.

        But somehow ready to be catched by the eyes of those who know how to observe.

        Those who are able to see beyond the quiet state of things.
        """
        tl "So, you're the daughter of the previous owners, right?"
        l "Yes. They asked me to take care of the house and find a new lodger..."
        tl "Oh, I see."
        "An awkward, embarassing silence."
        tl "It'a nice to meet you, really."
        l "Oh, for me too, yes."
        tl "Well anyway, I wanted to ask you something."
        l "Yes?"
        tl "Your parents left here some things, right?"
        l "Well, yes."
        tl """
        Could you tell me why?

        I mean, usually people take everything away when tey move out.

        But your parents left many things.
        """
        l "Oh, it's some sort of habitude of them."
        tl "Habitude...?"
        l """
        Yes, they leave things that could be useful for others.

        They don't realize that sometimes it would be better if they...didn't.
        """
        tl "I think it's gentle."
        l "Really?"
        tl """
        Yes, really.

        It's not that important if what they leave is useful or not.

        It's gentle because it means they care about others.
        """
        menu:
            "What if you'll have to toss them?":
                tl """
                That would be unfortunate, but you see...

                Truth is that I needed exactly what they left.

                Let's say that I had to leave some things in the  place where I used to live.

                So now I have almost nothing.

                And it's the same for the person I'll start living with in the next days.

                So what they left will be very useful to us.
                """
                l "Oh, that sounds...mysterious. And very sad, too."
                tl """
                There's nothing so mysterious about it, really...

                It's what happens when you hurt someone, you know?

                You break the promise made with that person and everything there was just...disappears.

                And you start falling, trying to build something new out of the mistake you made.

                Of course feelings have been hurt.

                Of course there are broken hurts and tears, and screams, and...

                Oh, well, I'm sorry...

                I know that's none of your business, but...every time I start talking I can't stop.
                """
                menu:
                    "No, please...go on.":
                        tl """
                        Oh...

                        Well, now that you said it I realize it's not so simple to continue, but...

                        Let's start by that: betraying someone is painful.

                        Painful for both parts, that is.

                        But even if it is, there's still some kind of...love?

                        I mean, you of course do it for love.

                        There may be physical implications, desires, but for me...there was only love.

                        And it's that love what I decided to follow.

                        So here I am now, a tired poet with a broken history and a 'new beginning'.
                        """
                        l "That must be painful..."
                        tl """
                        Yes, it is.

                        But as long as love is still in my life...I feel better.
                        """
                        """
                        Feeling better as long as there is love...

                        Thinking about it, the lonely girl realizes that love is still there for her too.

                        Love for her family.

                        Love for herself.

                        Love for life itself.

                        Could it be that this love will make her feel better too?
                        """
                    "Yes, that's none of my business.":
                        tl """
                        Yeah, right.

                        Well, it's nice that you came here to say hi, anyway.

                        I already feel welcomed.
                        """
                        l "Very good. I guess I must leave, now."
                        tl "That's fine. Bye, then and...thank you for listening, anyway."
                        $ lod1epilogue = True
                        $ epilogues += 1
                        scene black
                        with slowfade
                        scene room
                        with fade
                        $ renpy.pause(1)
                        jump room
            "It's kind of you.":
                tl """
                Well, I think that kindness is the least I can be.

                I mean...we live in an unkind environment, right?

                And what good can make being enraged because of items I don't want?

                Or because other people decide to be gentle and think about what could be useful and then leave it?

                Your parents decided to separate themselves of something in what I can imagine isn't a simple moment.

                Moving out is never simple, for anyone.

                And, to be sincere, they just saved me, as I don't have at all these things!

                So, if it wasn't for them, me and the person I'll live with would have passed a not so great moment in a shop, searching for them!
                """
                l "That really make me happy, then!"
                tl """
                Yeah, me too.

                I think yours is a very gentle family.

                I would like to meet your parents, one day, but I think that you got all their kindness.

                You came here to say hi, help me understand some things about the apartment and treated me very gently.

                That's something...rare.

                I think that when people have choices, they can be very mean.

                But not you.

                And that tells a lot.
                """
        """
        The apartment's door suddenly opens.
        """
        scene lodger1_2
        with dissolve
        """
        A young girls enters and watches us with a large, surprised smile.
        """
        tl "Oh, you're here finally!"
        lf """
        Sorry, I'm late! There was a lot of traffic...

        And you are?
        """
        l "The previous owners' daughter, nice to meet you."
        tl """
        She lives downstairs, so she came here to say hi.

        Oh, I made some tea for you too, take it.
        """
        lf "Thanks a lot!"
        scene lodger1_3
        with dissolve
        lf "Knowing him, I guess he already thanked you at least ten times for coming here, right?"
        tl """
        Hey, that's not true! I tried to restrain myself...

        This time.
        """
        l "Uhmm, don't worry, he was very gentle."
        lf "That's good, he always thanks and excuses himself too much!"
        tl "I think it wasn't necessary to tell her all that..."
        lf "Oh, you're right, I'm sorry!"
        """
        The lonely girl finishes her tea and smiles at both of them.

        The silence surrounding them all is starting to be a little embarassing.
        """
        lf "Listen, why don't you stay with us for dinner?"
        l "Oh no, don't worry, please! I have to go now, anyway."
        tl "No problem, maybe another day, right?"
        l "Yes, that would be splendid!"
        lf "Well, then, you can come here when you want."
        l "Thanks, you're both very kind. It was very nice meeting you."
        scene black
        with slowfade
        """
        And so she says hi and leaves.

        As she goes down the stairs, she starts thinking about how beautiful that couple was.

        And the words of a poem she listened long time ago flows through her mind.

        It sounded like...

        'Love is eternal, here rests for a time.'

        Perhaps the dead lie happily in the well tended plots, or perhaps they'd prefer the forgotten overgrown corners.

        Perhaps they prefer their names obliterated by time and the weather.

        Perhaps not.'

        Thinking about it...

        She instantly understands that, as the poem's author, she should leave.
        """
        $ lod1epilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if goodher == True or goodhim == True and solend == False:
        """
        There's no one here, now.

        Maybe it's worth checking out the other apartments?
        """
        jump apartmentlon
    if  badher == True or badhim == True and solend == False:
        """
        There's no one here, now.

        Maybe it's worth checking out the other apartments?
        """
        jump apartmentlon
    if goodher == False and goodhim == False and badher == False and badhim == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("arguetitle.mkv")
        scene arguebase
        with slowfade
        $ argument = 3
        """
        In this house live two people: a woman and her husband.

        A normal conversation in the living room, during morning, leads to unexpected truths.
        """
        w "So, have you finished that book we bought last month?"
        h "Which book?"
        w "The one with the red cover, don't you remember it?"
        h "Oh, that one! Yes, I do remember."
        w "...and have you finished it, then?"
        h "Guess I haven't. I think I forgot about it."
        w "You forgot?"
        h "Yes, I did. Why you ask?"
        w "I told you when we bought it that I wanted to read it, decided that I would have after you and now you forgot about it."
        h "But what's wrong with it? It's a book, not the end of the world."
        """
        Relationships between husbands and wives are indeed difficult.

        Every position taken means having the other as opponent.

        But, maybe, sometimes choosing between one or the other could lead to a repairment of the situation...
        """

label choose:
    call screen apartment1screen

### ARGUE HER #######
label herstart:
    scene argueher
    with slowdissolve
    jump arguestarther
    w "It's not the end of the world, you say...of course it isn't! But what does it mean? You're always like that!"
    h "Like that? Like that how?"
    jump arguestarther

label arguestarther:
    $ time = 7
    $ timer_range = 7
    $ timer_jump = 'no_ansher'
    show screen countdown

    menu:
        "You're careless, and don't pay any attention.":
            $ argument += 1
            hide screen countdown
            h "Maybe sometimes I am, yes, but I'm trying my best!"
            jump apt1_2her
        "Just a selfish, old idiot!":
            $ argument -=1
            hide screen countdown
            h "An old idiot? How...well, the genius has spoken, right?"
            jump apt1_2her

label apt1_2her:
    if argument == 4:
        hide screen countdown
        w "I know you're trying, but you've got to try and stay focused. Or at least more focused."
        h "Of course, but..."
        w "But?"
        h "You're talking as if you're better than me..."
        jump apt1_good1her
    if argument == 2:
        hide screen countdown
        w "At least I pay some attention to the world surrounding me!"
        h "Oh and what world is surrounding you? And what is it like?"
        jump apt1_bad1her

label apt1_good1her:
    $ time = 7
    $ timer_range = 7
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Why do you always say that?":
            hide screen countdown
            $ argument += 1
            h "Because it's true! Don't you realize it?"
            jump apt1_3her
        "Stop acting like a victim!":
            hide screen countdown
            $ argument -= 1
            h "A victim? I'm not acting like a victim, I AM the victim!"
            jump apt1_3her

label apt1_bad1her:
    $ time = 6
    $ timer_range = 6
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "It's the same as yours.":
            hide screen countdown
            $ argument += 1
            h "The same as mine..."
            jump apt1_3her
        "I don't know, real maybe?":
            hide screen countdown
            $ argument -= 1
            h "You're kidding me, right? Come on, say it. You're definately kidding."
            jump apt1_3her

label apt1_3her:
    if argument == 5:
        w "No, I don't realize it, I'm sorry. I'm just trying to talk with you, don't you get it?"
        h "Of course I get it, of course..."
        jump apt1_good2her
    if argument == 3:
        w "What?"
        h "Well, you said we live in the same world, but you treat me like we're in parallel worlds."
        jump apt1_neutralher
    if argument == 1:
        w "Kidding? I'm not kidding."
        h "Oh God, you really are terrible then."
        jump apt1_bad2her

label apt1_good2her:
    $ time = 8
    $ timer_range = 8
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Then why don't you listen to me?":
            hide screen countdown
            $ argument += 1
            h "I...I try to listen...I try my best."
            jump apt1_4her
        "Stop pretending being superior, then!":
            hide screen countdown
            $ argument -= 1
            h "I'm not pretending of being superior, you are!"
            jump apt1_4her

label apt1_neutralher:
    $ time = 6
    $ timer_range = 6
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "And we are, if you continue being so distracted.":
            hide screen countdown
            $ argument += 1
            h "Yes, I understand what you mean..."
            jump apt1_4her
        "Can't you just stop complaining?":
            hide screen countdown
            $ argument -= 1
            h "Oh, sorry Madame, I didn't want to upset you."
            jump apt1_4her

label apt1_bad2her:
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'no_ansher'
    show screen countdown
    menu:
        "Oh, so now I'm terrible...":
            hide screen countdown
            $ argument += 1
            h "No, I'm sorry, I didn't mean that..."
            jump apt1_4her
        "Terrible? How can you say I'm terrible?":
            hide screen countdown
            $ argument -= 1
            h "You're being absolutely terrible!"
            jump apt1_4her

label apt1_4her:
    if argument == 0:
        w "Oh, fantastic! I'm sorry to disturb your highness!"
        h "Oh fuck off!"
        w "You know what? I hate you! Really, I'm tired of this. All this!"
        h "So now you're tired! Well, I'm tired too. I'm tired of you, tired of your complainings, tired of hearing your voice."
        w "Then why are we even here? What are we still arguing about? Justo go away, the door is right there!"
        scene arguenegend
        with slowdissolve
        $ badher = True
        $ ending += 1
        "As she says that, he looks at her face for a moment, then turn around and reaches the door, leaving without saying anything."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 2:
        h "Listen, I'm tired of this, I'm tired of arguing over a stupid fucking book."
        w "It's not about the book, it'a about the attitude. It's about you being so careless to forget even the most basic things."
        h "So you are saying I'm stupid?"
        w "I'm not! This is what I'm telling you! I'm only saying you have to fix this thing and I'm here to help you."
        h "I understand...ok, that's fine."
        w "Really...?"
        h "Yes, don't worry. It's good."
        scene arguenegend
        with slowdissolve
        $ badher = True
        $ ending += 1
        "Yet, he doesn't say anything more than that. And her, too, finds it difficult to say anything at all."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 4:
        h "Listen, why don't we just stop? It's useless. I'm sorry for the book and for being so careless, really."
        w "I don't know, it's just that sometimes you get on my nerves and I really...can't do anything but feel rage."
        h "I didn't know that...for all these years you've felt that?"
        w "Well, yes..."
        h "Oh, I'm so sorry about that...I really never noticed it."
        scene argueposend
        with slowdissolve
        $ goodher = True
        $ ending += 1
        "He hugs her, feeling a deep sadness that seems to flow after years of containment."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 6:
        w "I know you try your best. And it's wonderful, I'm just telling you that there is this problem."
        h "Yeah, I understand."
        w "And we can fix it together, right?"
        h "Really?"
        scene argueposend
        with slowdissolve
        $ goodher = True
        $ ending += 1
        w "Yes, of course. I won't leave you alone."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
label no_ansher:
    h "If you won't even answer me than why are we here talking? Sorry, but I have better things to do."
    w "No, wait..."
    h "I'm tired of waiting. I'll see you later."
    scene arguenegend
    with slowdissolve
    $ badher = True
    $ ending += 1
    "He exits the room, leaving her alone."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room

#### ARGUE HIM ########
label himstart:
    scene arguehim
    with slowdissolve
    w "It's not the end of the world, you say...of course it isn't! But what does it mean? You're always like that!"
    h "Like that? Like that how?"
    """
    He starts to think how stupid this situation is. How absurd it is.

    But still, he can't do anything about it, as frustrating as it may seem.
    """
    w "You're careless, and don't pay any attention."
    jump arguestarthim

label arguestarthim:
    $ time = 7
    $ timer_range = 7
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Maybe sometimes I am but I'm trying my best!":
            $ argument += 1
            hide screen countdown
            w "I know you're trying, but you've got to try and stay focused. Or at least more focused."
            jump apt1_2him
        "So, now I don't pay any attention...":
            $ argument -= 1
            hide screen countdown
            w "No, you don't. You never do."
            jump apt1_2him

label apt1_2him:
    if argument == 4:
        hide screen countdown
        h "Of course, but..."
        w "But?"
        h "You're talking as if you're better than me..."
        w "Why do you always have to say that?"
        jump apt1_good1him
    if argument == 2:
        hide screen countdown
        h "And who are you to judge? Huh? You are so perfect that you can judge anyone you want?"
        w "I'm nobody, ok? Doeas that make you feel better?"
        jump apt1_bad1him

label apt1_good1him:
    $ time = 7
    $ timer_range = 7
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Because it's true! Don't you realize it?":
            hide screen countdown
            $ argument += 1
            w "No, I don't realize it, I'm sorry. I'm just trying to talk with you, don't you get it?"
            jump apt1_3him
        "Because you make me feel like that!":
            hide screen countdown
            $ argument -= 1
            w "I hope you don't think it's intentional, at least!"
            jump apt1_3him

label apt1_bad1him:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "No, that's not the point.":
            hide screen countdown
            $ argument += 1
            w "And what is it, then?"
            jump apt1_3him
        "Yes, of course it does!":
            hide screen countdown
            $ argument -= 1
            w "You asshole!"
            jump apt1_3him

label apt1_3him:
    if argument == 5:
        h "Of course I get it, of course..."
        w "Then why don't you listen to me?"
        jump apt1_good2him
    if argument == 3:
        h "The point is that you can't decide who to judge when you want. Life isn't like that."
        w "And you can decide what others can or can't do?"
        h "Well, no, of course, but what I was telling is that I don't find it correct that you do that with me."
        w "So, I should not tell you about something that I don't like about you?"
        jump apt1_neutralhim
    if argument == 1:
        h "I'm an asshole? How could you?"
        w "And what should I tell you, then? Do you expect some compliments?"
        jump apt1_bad2him

label apt1_good2him:
    $ time = 8
    $ timer_range = 8
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "I...I try to listen...I try my best.":
            hide screen countdown
            $ argument += 1
            w "I know you try your best. And it's wonderful, I'm just telling you that there is this problem."
            jump apt1_4him
        "Why don't I listen? I listen too much!":
            hide screen countdown
            $ argument -= 1
            w "Too much? This thing you're doing here is listening too much?"
            jump apt1_4him

label apt1_neutralhim:
    $ time = 6
    $ timer_range = 6
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "And have you listened to your tone?":
            hide screen countdown
            $ argument += 1
            w "What if I didn't?"
            jump apt1_4him
        "You know what? Do the fuck you want!":
            hide screen countdown
            $ argument -= 1
            w "Fine, I will!"
            jump apt1_4him

label apt1_bad2him:
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'no_anshim'
    show screen countdown
    menu:
        "Maybe not, but it doesn't mean you have to insult me.":
            hide screen countdown
            $ argument += 1
            w "Yeah you're right...I'm sorry."
            jump apt1_4him
        "You just insulted me!":
            hide screen countdown
            $ argument -= 1
            w "And what about it? Is it a crime."
            jump apt1_4him

label apt1_4him:
    if argument == 0:
        h "You know what? I'm tired of this. I'm tired of arguing, of getting mad and I'm tired of you."
        w "You're tired of me?"
        h "Of course I'm tired of you! You insult me, you despise me, you hate me!"
        w "And what about you, then?"
        h "I'm tired of feeling guilty for everything! I'm tired of being guilty even because I haven't read a fucking book!"
        w "That's because you value less than that book! That's the truth!"
        h "Oh, what a surprise! I would've never guessed something like that!"
        w "I hate you! I really hate you!"
        h "Fine, then you know what? I'm fucking leaving. I'm done with all this, done with you."
        scene arguenegend
        with slowfade
        $ badhim = True
        $ ending += 1
        "Moved by anger, he punches the nearest wall, leaving his fist's trace behind."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 2:
        h "Ok, fine, I get it. You don't want me here, right? Absolutely fine, really."
        w "What?"
        scene arguenegend
        with slowfade
        $ badhim = True
        $ ending += 1
        h "It's just clear. Very clear. I'll leave you your space, no problem. I'll go take a walk."
        w "Yeah...maybe that will calm us both."
        h "Yeah, maybe."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 4:
        h "...I'm sorry about all this. I'm sorry about the book, about the argument, about everything."
        w "It's ok, it came from both of us..."
        h "Yeah, right, but nothing in this was nice from my part."
        w "Not from mine either, I'd say."
        h "So...what now?"
        scene argueposend
        with slowfade
        $ goodhim = True
        $ ending += 1
        "She gently hugs him, softly crying of happiness."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if argument == 6:
        h "Yeah, I understand."
        w "And we can fix it together, right?"
        h "Really?"
        scene argueposend
        with slowfade
        $ goodhim = True
        $ ending += 1
        w "Yes, of course. I won't leave you alone."
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
label no_anshim:
    w "So, you're pretending to be mute, now?"
    h "No, I'm not, I-"
    w "Yeah, right, whatever. I'm leaving, by the way."
    scene arguenegend
    with slowfade
    $ badhim = True
    $ ending += 1
    h "You're leaving?"
    w "You don't want to talk and I don't want to talk to the wall, so I'm leaving."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room

##### APARTMENT 2 SCENE START ############################################################################################################################
label apartment2:
    if lovepilogue == True:
        "The couple is still sleeping."
        jump apartmentlon
    if separepilogue == True:
        "You can hear the young student's cry from your room."
        jump apartmentlon
    if phonebad == True:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("separationtitle.mkv")
        scene phonecallprep
        scene separation
        with slowfade
        """
        It's early morning.

        Yet, the young student's cry is so strong thetg people on the street can hear it.
        """
        sf """
        Listen...

        I know you feel bad, but don't you think tou're exaggerating?
        """
        s """
        Me? Exaggerating?

        How could you say something like that!

        You know exactly how much Laura was important to me!
        """
        sf "Yes, of course, but...!"
        s """
        But how can you understand me?

        You've never been with a girl, after all...
        """
        sf "Hey, I don't think that was necessary!"
        s """
        She meant the world to me!

        Do you get it?

        The entire world! And now she...

        She's gone!

        Forever!!

        Do you know how long is forever?!
        """
        sf """
        Oh, I know!

        I'm only telling you to calm down a little.
        """
        s """
        You really don't get it, then!

        Calm down...

        How could I ever calm down?

        I miss her so much!

        I miss her face...

        The birthmarks on her left arm...

        I miss her...
        """
        sf """
        Hey, that's enough!

        Don't get into too many details, please!
        """
        s """
        What?
        Aren't you here to listen to me?

        And to comfort me?
        """
        sf "I am, but I don't want the details!"
        s """
        Ohh, poor me...

        Even my friends don't want to listen to me...

        Just like Laura did!
        """
        sf "Geez, you're really something, huh?"
        s """
        Laura!!

        Where the hell are you?

        Come back!!

        I won't live without you!!

        Come back to me!

        Please...

        I'm so lost...
        """
        """
        Maybe he's too young to know about the love's suffering.

        Or maybe too childish to accept it.

        But, anyway, Laura won't certainly come back.

        Because that's how things go.
        """
        $ separepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if phonegood == True:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("lovetitle.mkv")
        scene love
        with slowfade
        g """
        You know...

        When I try to think about why we left each other...

        Nothing comes to my mind.

        It just seems so...stupid?

        I don't know...
        """
        s """
        I think I understand what you mean.

        It seems strange to me too.
        """
        g """
        Yeah...

        I mean, why did we hurt each other so much?

        What was the point?
        """
        s "Hmm, I really don't know."
        g """
        It's so strange...

        All we want is love but...

        When we finally have it, we throw it away.

        And we do it without thinking about it twice.
        """
        s """
        It's true.

        But it's also true that sometimes love fades away.

        Maybe we fall in love with someone else.

        Or maybe the person we share our feelings just...

        Doesn't fit us anymore.

        And so we search for someone else.
        """
        g """
        It sounds like an limitless quest.

        If someone gets lost in it, it will just never end.
        """
        s """
        Maybe you're right.

        But I think that, at least for now, we can be happy we've found each other again.
        """
        g """
        But what if we'll leave each other again?

        What if we'll end up losing each other, in the future?
        """
        s "But what if it won't happen again?"
        g """
        I know, it's stupid thinking about that, but...

        Loneliness makes me feel bad.

        I don't want to feel like that anymore.
        """
        s """
        I know, it's the same for me...

        I realized how lost I am, without you.
        """
        """
        A soft, sweet kiss and they hug each other...

        Before sleep possess them, gently.
        """
        $ lovepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if phonegood == False and phonebad == False:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("phonetitle.mkv")
        scene phonecallprep
        with slowfade
        $ emb = 3
        """
        The tiniest apartment in the building is occupied by a young student.

        He's now immersed in the shadow of his room, looking at the darkness surrounding him.

        In his head there's his girlfriend's face. He misses her. Deadly.

        He'd like to call her and tell her he's sorry about everything, that he'll try to do his best to be a better person.

        But he doesn't know how to say it.
        """
        s """
        So, uhm...what could I say to her...?

        Well, let's start with the intention...the intention would be to bring her back with me.

        ...I think, at least.

        So, maybe I could start with...
        """

label apt2_lessemb1:
    menu:
        "Laura, I really love you.":
            $ emb += 1
            s "Yes, that's good. I'm sure it's good."
            jump apt2_1
        "I think we should talk, Laura.":
            $ emb -= 1
            s "Hmm..."
            jump apt2_1

label apt2_1:
    if emb == 2:
        s "I don't know, it's very exaggerated...but it could work."
        jump apt2_lessemb2
    if emb == 4:
        s "Maybe more enphasis on the love..."
        jump apt2_moreemb2

label apt2_lessemb2:
    menu:
        "I thought that, maybe, you'd want to come back with me...":
            $ emb += 1
            s "Yes, sorry is good."
            jump apt2_2
        "I'm sorry for what I've done, very sorry.":
            $ emb -= 1
            s "Now that I think about it, the house seems empty."
            jump apt2_2

label apt2_moreemb2:
    menu:
        "I want to be sincere with you. About everything.":
            $ emb += 1
            s """
            Well, but everything what, exactly?

            Guess I'll figure it out, somehow.

            Well, time to call her, then...
            """
            jump apt2_2
        "I miss you, enormously.":
            $ emb -= 1
            s """
            For all this time, these days, I thought about you...

            Yes, that seems good.

            Well, time to call her, then...
            """
            jump apt2_2

label apt2_2:
    show phonecalldef
    with dissolve
    if emb == 5:
        s """
        Hi, uhm....I just wanted to know if you'd like to love me.

        No, wait, I wanted to say that I love you. Yes.

        And I'm sorry for what I've done, you can't even imagine how much.

        I thought that, maybe, you'd want to go back together. You know...
        """
        jump apt2_negative
    if emb == 3:
        s """
        Hi, Laura. I want to talk with you.

        I think...uhm I think I want to say sorry, you know.

        I miss you a lot, really. It's lonely without you.
        """
        jump apt2_neutral
    if emb == 1:
        s """
        Hi, Laura. I really need to talk with you.

        You know, I'm sorry for what I've done.

        Truly sorry. I wanted to know what I could do to repair all this...situation?
        """
        jump apt2_good

label apt2_negative:
    g "Do you really want me to answer you?"
    $ time = 2
    $ timer_range = 2
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "Well, it would be nice...":
            hide screen countdown
            scene phonecallnegend
            with slowfade
            $ phonebad = True
            $ ending += 1
            """
            She ends the call, without saying a word.
            The young student finds himself alone once again, surrounded by the darkness in the room.
            """
        "No, I think you won't...":
            hide screen countdown
            scene phonecallposend
            with slowfade
            $ phonegood = True
            $ ending += 1
            g "I'll have to think about it. Just give me some time, please."
            s "Yes of course...I'll wait."
            g "Ok, bye then...for now."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room
label apt2_neutral:
    g "You think?"
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "I'm sorry, I don't really know what to say.":
            hide screen countdown
            g "I think it's normal. It's not an everyday situation, after all..."
            s "It definately isn't, yes. And I really am sorry about all this."
            g "You know, maybe...maybe we can put all this behind us."
            scene phonecallposend
            with slowfade
            $ phonegood = True
            $ ending += 1
            s "Really?"
            g "Yeah, why not?"
            "A smile on the student's face, and the phonecall calmly goes on."
        "You know I'm not good with words.":
            hide screen countdown
            g "And it would be nice if you were..."
            s "I know, but what do I have to do?"
            scene phonecallnegend
            with slowfade
            $ phonebad = True
            $ ending += 1
            g "Just...I don't know, I really don't know."
            "The call ends. Without any goodbye, without any smile."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room
label apt2_good:
    g "To repair this situation...?"
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'no_ans'
    show screen countdown
    menu:
        "Yes, I liked being with you.":
            hide screen countdown
            g "You really did?"
            s "Of course I did! It was great, there wasn't any other thing I wanted to do more than being with you."
            g "I'm so happy to hear that...I mean, I was angry, but..."
            s "Why have we done all this?"
            scene phonecallposend
            with slowfade
            $ phonegood = True
            $ ending += 1
            g "I don't even remember...and I think it's not important what it was."
            s "You think that?"
            g "Of course. Let's just go back to how we were. We can, right?"
            s "Of course we can."
        "Well you know, all the mess that happened.":
            hide screen countdown
            g "You mean the mess you've made?"
            s "Yeah, and I said I'm sorry about it."
            scene phonecallnegend
            with slowfade
            $ phonebad = True
            $ ending += 1
            g "Of course you are, but you'd better remember it. And very well."
            s "But I-"
            g "Don't worry, I understood. And I'll think about it, maybe."
            "She hangs up, leaving the young student by himself. Silent and lonely."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room

label no_ans:
    scene phonecallnegend
    with slowfade
    $ phonebad == True
    $ ending += 1
    g "I guess you don't really wanna talk, then..."
    s "No wait-"
    "She instantly hangs up. The student only had the time of hearing the soft beginning of her crying."
    scene black
    with slowfade
    scene room
    with fade
    $ renpy.pause(1)
    jump room

##### OVERWORK SCENE START ############################################################################################################################
label apartment3:
    if meetepilogue == True:
        "The meeting is over and now the studio is empty."
        jump apartmentlon
    if lod2epilogue == True:
        "The young mother doesn't seem to be at home, now."
        jump apartmentlon
    if devgood == True:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("meetingtitle.mkv")
        scene meeting
        with slowfade
        """
        Silence and concentration linger in the meeting room.

        Everyone's gazes don't know where to go, they just wander from face to face insistently.

        No one speak, as they're all waiting for the director to say something.

        But he's still trying to think.

        To find the fish he's looking for in a stormy ocean of ideas.

        He knows he's there, somewhere.

        Waiting for him.

        Hidden in the darkness, deep in his mind's abyss.

        And then, suddenly, a young girl decides to speak.

        She's been with the team for less than three months...

        But has already shown how skilled she is.

        So the director and all the team listen to her, focused on every word.
        """
        i """
        Is there really something wrong with a game entirely set in an apartment?

        I mean...

        Why don't we try it out anyway?

        I don't think we'll solve anything by sitting here, waiting for better ideas to come out.

        We have all the references for it and the market analysis seems pretty clear regarding survival horrors.

        So...I think we should do it.

        It's an interesting idea and has enough space for each department.
        """
        """
        The director seems happy and, so, all the team is too.

        He's still thinking about the idea, as he's not entirely convinced about it.

        The previous game has already been finished, so it's now time to decide what to do next.

        There are some ideas, concepts and mechanics the team wants to explore, but...

        Are they all worth the efforts that need to be made?

        The whole team is obviously concerned about the budget the game will need...

        But, mostly, the game's profit when it will launch.

        Could a game like this work well?

        Will publishers accept and finance the idea?
        """
        gd """
        It really is a good idea...

        After all, each one of us has a different life and, of course, lives in a different apartment.

        Our experiences could grant solidity, strength to the game's theme.

        But there is the financial aspect.

        And we can't just jump ahead without thinking about it in detail.

        A horror game...

        I think you're right about it being, probably, the right project for us.

        As we always had that genre in mind in our previous works but never truly tried to fully work on it.
        """
        a """
        But...

        Are we so sure about it?

        I mean, would someone be really interested in something like that?

        Not that I don't like it, really, but I'm worried...

        Could we really make something at least interesting with that genre?

        We never tried to go full horror with any project before, so...

        I don't know, I'm afraid we should stick to our comfort zone.
        """
        menu:
            "Let's take the risk.":
                gd """
                I know what you mean.

                That fear is completely logical, but...

                Sometimes it's better to try harder and do something different.

                Out team is already well formed.

                Even though we're known by many people, publishers and other development studios...

                If we decide to make something entirely new, we could fail.

                But that could happen even with a project similar to things we've already made.

                Sticking to our comfort zone won't mean that we'll keep making good projects.

                It'll only mean that we'll keep on making the same kind of stuff.

                But if we focus more on what we can and want to say to players...

                And on how we can do that with a new game, then we'll make something that at least for us will mean something.

                And if we make something meaningfull for us, then we'll never be wrong.

                Is it suicidal for an entire team?

                Of course it is.

                But as I think about it...

                I don't see why we should not follow this idea.

                I think she is right and we should do it.
                """
            #"I agree with you.":
                #gd """
                #"""
        $ meetepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if devneut == True:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("meetingtitle.mkv")
        scene meeting
        with slowfade
        "This is the mildly good meeting epilogue"
        $ meetepilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if devbad == True:
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("lodg2title.mkv")
        scene lodger2
        with slowfade
        """
        Loneliness.

        A word that wasn't very common with the previous owners of this apartment.

        But now, there is no trace left of them.

        The computers have been sold, all the material and furnitures moved elsewhere.

        This is what happens when a studio goes bankrupt.

        But where someone finds their own failure, others may find some joy.

        Even if they're lonely, just as this mother.

        Who knows where her husband his.

        Of course, if an husband ever existed.
        """
        ym """
        It's only the two of us now, huh?

        But that's good...

        We're more than enough to make each other happy, right?

        Your smile...it makes me feel so much better.

        I hope you'll grow up fast...

        I hope time will fly away and you'll grow up, without even realizing it.

        And we'll do so many things...

        We'll spend entire evenings talking, and I'll help you with your homeworks, and we'll live happy...and free.
        """
        $ lod2epilogue = True
        $ epilogues += 1
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if devgood == False and devneut == False and devbad == False:
        $ ease = 50
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("overwtitle.mkv")
        scene overworking
        with slowfade
        """
        A small development studio occupies the left side of the third floor.

        As silent as it may seem, it's a very busy place in which work never seems to end.

        In this moment, the whole team is focused on implementing new features.

        The concentration is intense and the schedule tight.

        One month until the deadline.

        The whole team is stressed.

        Everyone is desperately trying to mediate between a relaxed workflow and an efficient one.

        But every choice risks to lead them further from this balance.
        """

label apt3_q1:
    scene overworkingq1
    with slowdissolve
    """
    When you work with someone for a large amount of time...

    You get to recognize their feelings by the expressions on their faces.

    Or how they move.

    Or how they talk.

    So, as the Lead Artist moves closer to the desk, the Director instantly sense the incoming problem.

    Surprisingly, the Lead's face is at ease.

    Or at least more than usual.

    There are no nervous tics on his face.

    The fact he hasn't shaved for almost a month makes him look even better than usual.
    """
    a """
    Uhm, sorry, but...

    We've received e-mails from two members of the concept art department...
    """
    gd "What happened?"
    a """
    They decided to leave the team.
    """
    gd """
    What a splendid idea.

    Why so suddenly?!
    """
    a """
    They found new opportunities in other studios...

    And the project doesn't inspire them anymore.
    """
    gd """
    That definately is a problem.

    Of course we'll have to fire them, but...

    Even two less people will create huge issues.
    """
    a """
    Yes...

    Of course, as our project is a 2D game, we'll have to re-schedule the workload for the department...

    So...what should we do?
    """
    menu:
        "We'll have to cut some features.":
            $ ease += 25
            a """
            Are you sure?

            Won't it be a problem?
            """
            gd """
            We'll save some time for the development.

            And the department won't be stressed out.
            """
            a "Understood. Fine, I'll tell the others, then."
            gd "Good."
        "We'll distribute the workload on remaining members.":
            $ ease -= 25
            a """
            Is it really a good idea?

            It sounds risky...
            """
            gd """
            Well, it could be.

            But if we don't do that, the project will be heavily affected by that.

            I'd like it to be a matter of choice, but it isn't.
            """
            a "Yeah, that's true...I'll go tell all the department, then."
            gd "Fine, good work."
    jump apartment3_2
label apartment3_2:
    scene overworkingq2
    with slowdissolve
    """
    Both in little and in bigger studios, problems with the department's members are common.

    People leaving the team, or not properly doing their job or simply not good at communicating...

    All this could lead to serious and impactful problems.

    But people are not the only problematic element.

    And that, even if already clear to the Director, becomes more obvious as the Tech Leader approaches.
    """
    t "I'm sorry to disturb you, but we have a problem..."
    gd """
    A problem?

    What kind of problem?
    """
    t "One of the programmers has made some mistakes in the code, but he realized it just now."
    gd "And what kind of mistakes?"
    t """
    Well, we've found some, but not all of them, yet.

    They don't seem to be dungerous, but they sure are a lot of pain.
    """
    gd """
    And he uploaded them without checking?

    What is he, an idiot?
    """
    t "I already told him that."
    gd """
    That's just wonderful.

    One month until the deadline and some imbecille makes mistakes in the code.

    Well, we have two options, now...
    """
    menu:
        "We can fix them, but it'll take time.":
            $ ease -= 25
            gd "We can't deliver a bugged game, you know that as well."
            t "Of course, I'll tell the producer we'll have to schedule a new date for the release."
            gd "It won't happen."
            t "What do you mean?"
            gd "We'll never gain more days. We'll have to manage the time we have and fix everything."
            t "That sure is troublesome..."
            gd "Ain't it?"
        "We can leave them be and push until the realease.":
            $ ease += 25
            gd "We already are in a bad situation. Adding the fix of a similar problem would only make everything worst."
            t "Yes, I understand...but wouldn't we gain more time to finish the project?"
            gd "Of course not. The world won't stop only because we have to fix coding mistakes."
            t "Hm, that makes sense."
    jump apartment3_3
label apartment3_3:
    if ease >= 100:
        scene overworkingnegend
        with slowfade
        $ devbad = True
        $ ending == 1
        """
        The stress level in a developement studio is similar to a thin string.

        If one pulls it too much, it will easily break.

        And it's difficult not to do so.

        A single choice's impact can destroy everything.

        And the studio, from a day to the other, could no longer exist.

        The space it occupied becomes empty.

        The people who built it and took part in the work lose contact as they're divided by distance.

        And someone else will soon occupy that space.

        As if nothing ever happened.
        """
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if ease == 50:
        scene overworkingposend
        with slowfade
        $ devgood = True
        $ ending += 1
        """
        Seated at his chair, the director continues working, silently and focused.

        Around him, a small number of other people, like a troop of soldiers, follow his directions.

        And even though sometimes his methods may be harsh and the schedule is thight...

        The project calmly procedes towards the deadline.

        Not all the problems have been repaired but, at least, everything seem to be fine.
        """
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if ease == 0:
        scene overworkingneutend
        with slowfade
        $ devgood = True
        $ ending += 1
        """
        Choices and consequences can be cruel.

        Even though all the problems have been fixed...

        It doesn't mean that everything, now, will be alright.

        As the director and the whole team are proceeding towards the deadline, the stress rises, tiredness caughts everyone.

        Fixing problems could create new and unexpected ones.

        In an endless circle of choices and consequences.
        """
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room

##### SOLITUDE SCENE START ############################################################################################################################
label apartment4:
    if famepilogue == True:
        """
        She's still upstairs with her family.
        """
        jump apartmentlon
    if lod1epilogue == True:
        """
        The lonely girl is back, now...

        But she's sleeping.
        """
        jump apartmentlon
    if solend == True:
        """
        The lonely girl isn't at home anymore...

        Maybe she's in another apartment?
        """
        jump apartmentlon
    if solend == False:
        $ phonering = False
        $ sleep = False
        $ read = False
        $ mirror = False
        $ smoke= False
        $ tv = False
        $ windowlook = False
        $ light = False
        $ boredom = 50
        scene black
        with slowfade
        $ renpy.pause(0.5)
        $ renpy.movie_cutscene("soltitle.mkv")
        scene solitude00
        with slowfade
        """
        In the fourth and last apartment lives a young girl.

        In a morning of boredom, she's waiting for a phonecall.

        All over the walls and furniture there are signs that she's alone.

        Her loneliness though, is only proof of her complete freedom.

        Freedom to act, freedom to choose.

        She can do whatever she wants, use whatever she wants to spend some time while she waits.
        """
        jump apt4opening

label apt4opening:
    scene solitude
    with dissolve
    $ renpy.pause(0.1)
    jump apt4screen

label apt4screen:
    if boredom >= 75:
        play music "ringtone.ogg"
    if boredom <= 25:
        play music "ringtone.ogg"
    call screen apartment4screen
label tv:
    if tv == True:
        scene solitude
        "She already watched television."
    if tv == False:
        scene solitude
        """
        A normal and very old television that her parents gave to her some time ago.

        The colours are pale and it doesn't receive the signal so well.

        But apart from that, she doesn't mind watching it, even though she sometimes get bored.
        """
        menu:
            "Turn it on.":
                scene soltv
                with dissolve
                $ tv = True
                $ boredom += 30
                """
                On every channel there are only boring programs.

                Even though she searches for quite some time, she finds nothing truly exciting.
                """
            "Leave it.":
                """
                She decides to not turn it on.

                There certainly are more interesting things to do in the room.
                """
    jump apt4opening
label bed:
    if sleep == True:
        scene solitude
        "She doesn't want to sleep anymore."
    if sleep == False:
        scene solitude
        """
        A noisy old bed, covered with her favourite duvet and blankets.

        It always keep her warm during cold days and nights.

        Now that she's thinking about it, she feels a little sleepy...
        """
        menu:
            "Sleep.":
                scene solbed
                with dissolve
                $ sleep = True
                $ boredom += 20
                """
                As she lies down on the bed, covering herself up with the duvet and blanket, she fall asleep.

                She doesn't know how long, but she sleeps for quite some time.

                Her dreams are sweet and beautiful.

                But as she wakes up, she still has nothing to do.
                """
            "Don't sleep.":
                """
                It's better if she doesn't, indeed.

                The phonecall she's waiting for is very important and not answering could have terrible consequences.
                """
    jump apt4opening
label windowsol:
    if windowlook == True:
        scene solitude
        "She has already watched outside the window."
    if windowlook == False:
        scene solitude
        """
        A dusty window.

        Sometimes it stuck itself and it's hard to open it.
        """
        menu:
            "Watch outside.":
                scene solwindow
                with dissolve
                $ windowlook = True
                $ boredom -= 10
                """
                Outside the window she sees the facades of other buildings.

                Her eyes wander through all the windows and she can't help but to ask herself who lives in all those houses? How are their lives?
                """
            "Don't watch outside.":
                """
                She stares at the window but doesn't reach it.

                She prefers doing something else.
                """
    jump apt4opening
label cig:
    if smoke == True:
        scene solitude
        "She has already smoked."
    if smoke == False:
        scene solitude
        "In the ashtray there is a cigarette she was smoking a while ago."
        menu:
            "Smoke it.":
                scene solsmoke
                with dissolve
                $ smoke = True
                $ boredom -= 10
                """
                She lights it, then takes a puff.

                The smoke flows in the air, filling the room calmly.

                She feels relaxed, as she watches the small cloud disappearing in the space around her.
                """
            "Don't smoke it.":
                "She leaves it where it is, searching for something else to do."
    jump apt4opening
label mirror:
    if mirror == True:
        scene solitude
        "She doesn't want to stare at herself again."
    if mirror == False:
        scene solitude
        """
        A shiny mirror occupies a large portion of the wall.

        As everything else, it was given to her by her parents.

        Even though it's useful, she doesn't like to stare at herself. In fact, it annoys her a lot.
        """
        menu:
            "Stare just a little.":
                scene solmirror
                with dissolve
                $ mirror = True
                $ boredom += 20
                "She really doesn't like to watch her body. Especially if there's no usefulness in doing so."
            "Don't stare.":
                "In fact, she doesn't want to do it, so it's better not to."
    jump apt4opening
label books:
    if read == True:
        scene solitude
        "She has read enough."
    if read == False:
        scene solitude
        """
        A small group of books.

        Even though they are few, she likes books, but doesn't want to fill the room with them.

        So she has bought only the ones she likes the most and borrows others from a nearby library.
        """
        menu:
            "Read one.":
                scene solbook
                with dissolve
                $ read = True
                $ boredom -= 20
                """
                She takes one of the books from the shelf, after a careful choice.

                It's a book of poetries, written by Arseny Tarkovsky.

                She opens it, searching for a specific poem.
                """
                show solpoetry
                with slowdissolve
                $ renpy.pause(10,hard=True)
                hide solpoetry
                with slowdissolve
                l "I really love this poem."
            "Don't read.":
                "Reading is not something she wants to do, for now at least."
    jump apt4opening
label light:
    if light == True:
        l "No more light for today."
    if light == False:
        $ light = True
        """
        There is only one chandelier in the room.

        Her father has fixed the light bulb for her.

        That happened months ago, though, and she hasn't turned the light on for that whole time.
        """
        menu:
            "Turn the light on.":
                scene sollighton
                with dissolve
                l "Oh God, no!"
                "The light is too strong for her,so she turns it off immediately."
            "Let it off.":
                l "Better leave it as it is, or the PTSD will hit me again."
    jump apt4opening
label phone:
    if boredom >= 26 and boredom <= 74:
        scene solitude
        scene solphonewait
        with dissolve
        """
        Like everything in the room, even the telephone is old.

        It's still not ringing.

        She wanders how much time she'll have to wait.
        """
        jump apt4opening

    if boredom >= 75:
        stop music
        scene solphone
        with fade
        "She answers the phone, knowing already who's calling her, finally."
        l "Hi Julie...how are you?"
        j "Hi...how are you?"
        l "Very bored, and you?"
        j "Ok, I guess."
        l "Well..."
        j "Listen, I thought about it quite a lot..."
        l "And?"
        j """
        I really can't. I'm sorry, but...I just can't, it's too much.

        I know it's important, I know we would be together, but...I can't abandon everything and live with you...
        """
        menu:
            "What do you mean it's too much?":
                j "It's just too much, ok? What do I have to tell you? What do you want me to tell you?"
                l "After everything I've done..."
            "Oh, I understand...":
                j "I'm glad you do..."
        j """
        Look, I...I'm really sorry about that, ok?

        But I really can't do that. I'm not ready.

        At all.

        So...

        I think it's better if we just...
        """
        menu:
            "Are you leaving me?":
                j "I guess I am..."
            "...":
                j "I'm sorry..."
        j """
        Well, I...

        Uhm...

        I have to go, now...sorry. Bye
        """
        scene solbadend
        with fade
        $ ending += 1
        """
        She hangs up without saying a word. Not even a single one.

        The lonely girl stands still, without feeling anything.

        She's still alone, still a little sad and not ready at all for this situation.

        And the boredom doesn't make things easier.

        But even though it's difficult and hurts, there's still the future.

        Even though she can't control everything and can't change everything, there's still some hope in a brighter future.
        """
        $ solend = True
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room
    if boredom <= 25:
        stop music
        scene solphone
        with fade
        l "Hi, Julie! How are you?"
        j "Hi...well, I'm fine, thanks. What about you?"
        l "I'm fine too, just keeping busy, you know!"
        j "Yeah, that's good..."
        l "Soo..."
        j "Yeah, about that...uhm, I think I can't, sorry."
        l "You...can't?"
        j """
        Yes, I really can't live with you...

        I would like to, really, but I just can't.

        I should abandon everything I have now, do you understand?

        It's not simple at all.

        Even though I love you...it really isn't simple.
        """
        menu:
            "It's a joke, right?":
                j "I'm afraid it's not..."
            "And why haven't you told me before...?":
                j "I was afraid, and...well, I still had to think about it."
        l "So...what now?"
        j """
        I...

        I think we can no longer...

        Stay together...
        """
        l "Oh...yeah..."
        j "I'm sorry..."
        l "Yes, of course you are."
        j """
        Indeed...listen, I...

        I have some things to do, now, so...
        """
        l """
        That's good.

        Don't worry.

        It's ok.

        Bye.
        """
        j "Bye..."
        scene solgoodend
        with fade
        $ ending += 1
        """
        She hangs up.

        There's emptiness, now, all around the lonely girl..

        The idea of being alone again, for god knows how longer, hurts her.

        The love she felt is already disappearing.
        """
        show solpoetry
        with slowdissolve
        $ renpy.pause(1)
        """
        The words of her favourite poem come to her mind, gaining a new meaning.

        All those feelings, flowing silently into her heart...slowly becoming memories.

        But still, she thinks, there's some kind of hope.

        Hope for the future, for the decisions she still can make.
        """
        $ solend = True
        scene black
        with slowfade
        scene room
        with fade
        $ renpy.pause(1)
        jump room

##### END SCENE START ############################################################################################################################
label gamending:
    "Here will be the ending."
    stop music fadeout (3)
    scene black
    with slowfade
    return
