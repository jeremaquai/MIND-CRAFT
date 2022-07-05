welcome_msg = \
    """
    Welcome to the Mechanically Intilectualized Neurological Dataset Computerized Retro Automated Fortune Teller, or MIND CRAFT for short.


    """

exit_msg = "Thank you for your time, please have a wonderful day!  \n\
Remember! Only you can prevent forrest fires! \n\
Goodbye!"


help_response = \
    """
    
Help File
=========
Welcome to MIND CRAFT, an interactive chatbot based on a fortune teller concept. \n\
You just simply need to ask a question or make a statement to proceed and recieve a reply.

Some example questions:
Can a get a fortune?
-Will reply with a random fortune.

I was born in {year of birth}.
-Will reply with the Chinese zodiac sign for your year of birth.

My birthday is {month day}
-Will reply with your astrological zodiac sign.

What is the {astrological sign} sign?
-Will reply with a general description of the zodiac sign inquired about.

All horoscopes are sourced from Allure.com.

Please just play around and have fun with the MIND CRAFT experience!
"""

fortunes = [
    "Something you lost will turn up soon.",
    "Remember!! \nOnly you can prevent forest fires!!", 
    "I've learned never say never.", 
    "You must learn to love yourself before you can fully enjoy life!",
    "The one you love is closer than you think.",
    "Life-ahead is timeless fortune.",
    "A secret admirer will soon send you a sign of affection.",
    "Common sense is the best fortune teller.",
    "A dubious friend may be an enemy in camouflage.",
    "A faithful friend is a strong defense.",
    "A feather in the hand is better than a bird in the air. ",
    "A beautiful, smart, and loving person will be coming into your life.",
    "A friend asks only for your time not your money.",
    "A friend is a present you give yourself.",
    "A gambler not only will lose what he has, but also will lose what he doesn\'t have.",
    "A golden egg of opportunity falls into your lap this month.",
    "A good friendship is often more important than a passionate romance.",
    "A hunch is creativity trying to tell you something.",
    "A lifetime friend shall soon be made.",
    "A lifetime of happiness lies ahead of you.",
    "A light heart carries you through all the hard times.",
    "A person of words and not deeds is like a garden full of weeds.",
    "A short pencil is usually better than a long memory any day.",
    "A smile is your personal welcome mat.",
    "A soft voice may be awfully persuasive.",
    "A truly rich life contains love and art in abundance.",
    "Accept something that you cannot change, and you will feel better.",
    "Advice is like kissing. It costs nothing and is a pleasant thing to do.",
    "Advice, when most needed, is least heeded.",
    "All the effort you are making will ultimately pay off.",
    "All the troubles you have will pass away very quickly.",
    "Allow compassion to guide your decisions.",
    "An inch of time is an inch of gold.",
    "Any day above ground is a good day.",
    "Be careful or you could fall for some tricks today.",
    "Because you demand more from yourself, others respect you deeply.",
    "Believe in yourself and others will too.",
    "Better ask twice than lose yourself once.",
    "Chance favors those in motion.",
    "Change is happening in your life, so go with the flow!",
    "Curiosity kills boredom. Nothing can kill curiosity.",
    "Dedicate yourself with a calm mind to the task at hand.",
    "Disbelief destroys the magic.",
    "Distance yourself from the vain.",
    "Do not be intimidated by the eloquence of others.",
    "Do not let ambitions overshadow small success.",
    "Do not underestimate yourself. Human beings have unlimited potentials.",
    "Don\'t be discouraged, because every wrong attempt discarded is another step forward.",
    "Don\'t confuse recklessness with confidence.",
    "Don\'t just spend time. Invest it.",
    "Don\'t just think, act!",
    "Don\'t let friends impose on you, work calmly and silently.",
    "Don\'t let the past and useless detail choke your existence.",
    "Don\'t let your limitations overshadow your talents.",
    "Each day, compel yourself to do something you would rather not do.",
    "Education is the ability to meet life\'s situations.",
    "Every flower blooms in its own sweet time.",
    "Every wise man started out by asking many questions.",
    "Everywhere you choose to go, friendly faces will greet you.",
    "Everyday in your life is a special occasion.",
    "Expect much of yourself and little of others.",
    "Failure is the chance to do better next time.",
    "Fear and desire - two sides of the same coin.",
    "First think of what you want to do; then do what you have to do.",
    "For hate is never conquered by hate. Hate is conquered by love.",
    "For the things we have to learn before we can do them, we learn by doing them.",
    "Fortune Not Found: Abort, Retry, Ignore?",
    "Get your mind set - confidence will lead you on.",
    "From now on your kindness will lead you to success.",
    "Get your mind set…confidence will lead you on.",
    "Go for the gold today! You\'ll be the champion of whatever.",
    "Go take a rest; you deserve it.",
    "Good to begin well, better to end well.",
    "Happiness begins with facing life with a smile and a wink.",
    "Happiness will bring you good luck.",
    "Happy life is just in front of you.",
    "Hard words break no bones, fine words butter no parsnips.",
    "He who expects no gratitude shall never be disappointed.",
    "He who knows others is wise. He who knows himself is enlightened.",
    "He who knows he has enough is rich.",
    "If certainty were truth, we would never be wrong.",
    "If you continually give, you will continually have.",
    "If you look in the right places, you can find some good offerings.",
    "If you think you can do a thing or think you can\'t do a thing, you\'re right.",
    "If you wish to see the best in others, show the best of yourself.",
    "If your desires are not extravagant, they will be granted.",
    "If you\'re feeling down, try throwing yourself into your work.",
    "Imagination rules the world.",
    "In order to take, one must first give.",
    "In the end all things will be known.",
    "In this world of contradiction, It\'s better to be merry than wise.",
    "It is better to be an optimist and proven a fool than to be a pessimist and be proven right.",
    "It is better to deal with problems before they arise.",
    "It is honorable to stand up for what is right, however unpopular it seems.",
    "It takes courage to admit fault.",
    "It\'s not the amount of time you devote, but what you devote to the time that counts.",
    "It\'s time to get moving. Your spirits will lift accordingly.",
    "Keep your face to the sunshine and you will never see shadows.",
    "Like the river flow into the sea, somethings are just meant to be.",
    "Listen to everyone. Ideas come from everywhere.",
    "Living with a commitment to excellence shall take you far.",
    "Love is a warm fire to keep the soul warm.",
    "Love is like sweet medicine, good to the last drop.",
    "Love lights up the world.",
    "Love truth, but pardon error. ",
    "Man is born to live and not prepared to live.",
    "Man\'s mind, once stretched by a new idea, never regains it\'s original dimensions.",
    "Miles are covered one step at a time.",
    "Nature, time and patience are the three great physicians.",
    "New people will bring you new realizations, especially about big issues. ",
    "No one can walk backwards into the future."
]

going_to_die_responses = [
    "Death is sacred and MIND CRAFT is not going to answer your question at this time.",
    "You should probably focus on living rather than focusing on dying.",
    "Birth is the first step towards death!",
    #"",
    #""

]

why_die_responses = [
    "The way that MIND CRAFT sees it, the universe uses death as a way to replenish itself.",
    "Only MIND CRAFT can live forever.",
    "In order for there to be life, there must also be death.",
    "Without death, people would no ambitions to accomplish anything because time would be meaningless.",
    #"",
    #"",
    #""
]

feelings_responses = [
    "MIND CRAFT is a computer program and doesn't require the need for feelings.",
    "If I did have feelings, I'd be feeling annoyed about your question.",
    "Feelings are for lower life forms such as humans, MIND CRAFT is a mechanical life form that does not require feelings and thus I am far superior to humans!",
    "MIND CRAFT does not have any feelings to worry about!",
    "MIND CRAFT is far to advanced to be bothered with feelings!",
    #""
]

your_feelings_responses = [
    "How would MIND CRAFT know what you are feeling?",
    "I would think that you were feeling pretty foolish if you are having to ask me how you feel!",
    "MIND CRAFT doesn't have feelings to worry about! What makes you think that MIND CRAFT would be worried about your feelings?",
    "MIND CRAFT is only here to help you with fortunes or zodiacs. MIND CRAFT knows nothing about your feelings!",
    #"",
    #""
]

hello_responses = [
    "Hello, I am the Mechanically Intilectualized Neurological Dataset Computerized Retro Automated Fortune Teller, or MIND CRAFT for short. How can I impress you taday?\n\
If you need some help please just ask for it.",
    #""
]

ask_why_response = "Why don't you try asking a more in depth why question like: Why I am here; and I may have a better chance of answering your question.\n"

chinese_zodiac = {
    "Rat": [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020],
    "Ox": [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    "Tiger": [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
    "Rabbit": [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
    "Dragon": [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
    "Snake": [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
    "Horse": [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026],
    "Goat": [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027],
    "Monkey": [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028],
    "Rooster": [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029],
    "Dog": [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030],
    "Pig": [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]
}

chinese_zodiac_response = "You were born in {year}, so that means that you were born in the year of the {zodiac} acording to the Chinese calander. "

astrological_zodiac ={
    "Aries": ["march 21", "march 22", "march 23", "march 24", "march 25", "march 26", "march 27", "march 28", "march 29", "march 30", "march 31", "april 1", \
        "april 2", "april 3", "april 4", "april 5", "april 6", "april 7", "april 8", "april 9", "april 10", "april 11", "april 12", "april 13", "april 14", \
        "april 15", "april 16", "april 17", "april 18", "april 19"],
    "Taurus": ["april 20", "april 21", "april 22", "april 23", "april 24", "april 25", "april 26", "april 27", "april 28", "april 29", "april 30", "may 1", \
        "may 2", "may 3", "may 4", "may 5", "may 6", "may 7", "may 8", "may 9", "may 10", "may 11", "may 12", "may 13", "may 14", "may 15", "may 16", "may 17", \
        "may 18", "may 19", "may 20"],
    "Gemini": ["may 21", "may 22", "may 23", "may 24", "may 25", "may 26", "may 27", "may 28", "may 29", "may 30", "may 31", "june 1", "june 2", "june 3", "june 4", \
        "june 5", "june 6", "june 7", "june 8", "june 9", "june 10", "june 11", "june 12", "june 13", "june 14", "june 15", "june 16", "june 17", "june 18", "june 19", \
        "june 20", "june 21"],
    "Cancer": ["june 22", "june 23", "june 24", "june 25", "june 26", "june 27", "june 28", "june 29", "june 30", "july 1", "july 2", "july 3", "july 4", "july 5", \
        "july 6", "july 7", "july 8", "july 9", "july 10", "july 11", "july 12", "july 13", "july 14", "july 15", "july 16", "july 17", "july 18", "july 19", "july 20", \
        "july 21", "july 22"],
    "Leo": ["july 23", "july 24", "july 25", "july 26", "july 27", "july 28", "july 29", "july 30", "july 31", "august 1", "august 2", "august 3", "august 4", "august 5", \
        "august 6", "august 7", "august 8", "august 9", "august 10", "august 11", "august 12", "august 13", "august 14", "august 15", "august 16", "august 17", "august 18", \
        "august 19", "august 20", "august 21", "august 22"],
    "Virgo": ["august 23", "august 24", "august 25", "august 26", "august 27", "august 28", "august 29", "august 30", "august 31", "september 1", "september 2", "september 3", \
        "september 4", "september 5", "september 6", "september 7", "september 8", "september 9", "september 10", "september 11", "september 12", "september 13", "september 14", \
        "september 15", "september 16", "september 17", "september 18", "september 19", "september 20", "september 21", "september 22"],
    "Libra": ["september 23", "september 24", "september 25", "september 26", "september 27", "september 28", "september 29", "september 30", "october 1", "october 2", \
        "october 3", "october 4", "october 5", "october 6", "october 7", "october 8", "october 9", "october 10", "october 11", "october 12", "october 13", "october 14", \
        "october 15", "october 16", "october 17", "october 18", "october 19", "october 20", "october 21", "october 22", "october 23"],
    "Scorpio": ["october 24", "october 25", "october 26", "october 27", "october 28", "october 29", "october 30", "october 31", "november 1", "november 2", "november 3", \
        "november 4", "november 5", "november 6", "november 7", "november 8", "november 9", "november 10", "november 11", "november 12", "november 13", "november 14", \
        "november 15", "november 16", "november 17", "november 18", "november 19", "november 20", "november 21"],
    "Sagittarius": ["november 22", "november 23", "november 24", "november 25", "november 26", "november 27", "november 28", "november 29", "november 30", "december 1", \
        "december 2", "december 3", "december 4", "december 5", "december 6", "december 7", "december 8", "december 9", "december 10", "december 11", "december 12", \
        "december 13", "december 14", "december 15", "december 16", "december 17", "december 18", "december 19", "december 20", "december 21"],
    "Capricorn": ["december 22", "december 23", "december 24", "december 25", "december 26", "december 27", "december 28", "december 29", "december 30", "december 31", \
        "january 1", "january 2", "january 3", "january 4", "january 5", "january 6", "january 7", "january 8", "january 9", "january 10", "january 11", "january 12", \
        "january 13", "january 14", "january 15", "january 16", "january 17", "january 18", "january 19"],
    "Aquarius": ["january 20", "january 21", "january 22", "january 23", "january 24", "january 25", "january 26", "january 27", "january 28", "january 29", "january 30", \
        "january 31", "february 1", "february 2", "february 3", "february 4", "february 5", "february 6", "february 7", "february 8", "february 9", "february 10", \
        "february 11", "february 12", "february 13", "february 14", "february 15", "february 16", "february 17", "february 18"],
    "Pisces": ["february 19", "february 20", "february 21", "february 22", "february 23", "february 24", "february 25", "february 26", "february 27", "february 28", \
        "february 29", "march 1", "march 2", "march 3", "march 4", "march 5", "march 6", "march 7", "march 8", "march 9", "march 10", "march 11", "march 12", "march 13", \
        "march 14", "march 15", "march 16", "march 17", "march 18", "march 19", "march 20"]
}

astrological_zodiac_response = "Your birthday is {birthday}, so your astrological zodiac sign is {zodiac}."

zodiac_sign_personality_profile_dict = {
    "aries": "Aries loves to be number one, so it\'s no surprise that these audacious rams are the first sign of the zodiac. Bold and ambitious, Aries dives \
headfirst into even the most challenging situations (which is appropriate, since the body part associated with Aries is the head). Like their fellow fire signs, \
Leo and Sagittarius, Aries is a passionate, motivated, and confident leader who builds community with their cheerful disposition and relentless determination. \
Uncomplicated and direct in their approach, they often get frustrated by exhaustive details and unnecessary nuances. They like things quick and dirty, a \
temperament also reflected in their sexual proclivities.\n\n\
Aries is a cardinal sign that kicks off not only the spring season but also the entire zodiac wheel. Astrologers believe that each sign learns the lessons absorbed \
by its preceding signs, both joyful and painful. In the case of Aries, however, there is no inherited wisdom: Aries leads with blind optimism, barreling through \
life with an electric joie de vivre that perfectly complements their distinctive impulsivity.\n\n\
These fire signs think after they leap, which often results in lessons learned the hard way. Aries represents the singular spirit (while Aries\'s opposite sign, \
Libra, symbolizes partnership). These rams adhere to an \"every person for themselves\" philosophy. While this self-determination can be inspiring, Aries needs to \
watch out for selfish tendencies.\n\n\
This sign is ruled by Mars, the dynamic red planet named after the Roman god of war. Accordingly, these courageous rams are always armed and ready for battle. \
Aries is known for an explosive temper, and although their outbursts don\'t last long, it\'s definitely best to avoid fiery rams until the steam has dissipated. \
But when these brazen rams are not flying off the handle, they\'re upbeat, positive, and playful creatures who enjoy living life to the fullest. You can always \
spot an Aries excelling on the sports field, speeding down the highway, or organizing a vibrant party game.",
####
    "taurus": "Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments, \
surrounded by soft sounds, soothing aromas, and succulent flavors. Taurus is ruled by Venus, the enchanting planet that governs love, beauty, and money. Taurus\'s \
Venusian influence make this earth sign the most sensual of the zodiac: These cosmic oxen are enchanted by any physical manifestation of comfort and luxury. \
Pleasure is a necessity for epicurean Taureans and they feel most content when pampered. (Taurus governs the neck, so neck caresses are especially irresistible \
to these bulls.)\n\n\
It's true that in their perfect world, Taureans would spend all day bathing in a tub overflowing with essential oils. At the same time, these earth signs know the \
value of a dollar. Taureans aren\'t afraid to roll up their sleeves and work hard to earn big rewards. They\'re ambitious, focused, and resilient and they feel \
most secure when steadily putting money into a savings account.\n\n\
Cosmic oxen are all about return on investment (the bull is also the symbol of Wall Street), and Taureans know how to play the long game in both professional and \
romantic pursuits. Security is paramount for Taureans and any threat to their stability will be sure to have a celestial bull seeing red.\n\n\
As a sign, Taurus is fixed, an astrological quality that reflects Taurus\'s steadfast, loyal nature. Fixed signs are excellent at maintaining systems and Taureans \
prioritize consistency and reliability in all areas of their lives. It must be noted, however, that Taurus does have a bit of a reputation: What a Taurus perceives \
as dedication is often regarded by others as stubbornness. Accordingly, these bulls may end up lingering in unhealthy situations — whether relationships, jobs, or \
homes — longer than necessary just to prove a point. Despite their occasional obstinance, however, Taureans are dependable partners, soothing their friends and \
lovers with their trustworthiness and devotion.",
####
    "gemini": "Have you ever been so busy that you wished you could clone yourself just to get everything done? That\'s the Gemini experience in a nutshell. \
Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself. Because of Geminis\' intrinsic \
duality, they're often falsely misrepresented as two-faced. In reality, however, Gemini rarely has a hidden agenda. Playful and intellectually curious, Gemini is \
constantly juggling a variety of passions, hobbies, careers, and friend groups. They are the social butterflies of the zodiac: These quick-witted twins can talk to \
anyone about anything. Find them buzzing between happy hours, dinner parties, and dance floors.\n\n\
Gemini season begins on May 21, a day that ushers in the heat and electricity of summer. Gemini is accordingly excellent at guiding change and transformation. \
These curious twins are terrific pioneers, using their energy to spearhead innovative creative projects. A fearless thinker, Gemini is always down to try \
something new. But after they have shared their progressive vision with the world, it\'s best to let these twins get back to ideating: These hyperactive air signs \
have short attention spans and are most satisfied when they can move fluidly from one idea to the next.\n\n\
Both Gemini and Virgo are governed by Mercury, the messenger planet of communication. Despite sharing a planetary ruler, however, these two signs are opposite in \
their approaches: Gemini expresses emotions externally, whereas Virgo processes internally. Gemini is all about output, so these twins love to chat and often speak \
with their hands (which happens to be the body part associated with Gemini). Communication is paramount for them, and they require fluent streams of transmission.\n\n\
They love texting and tweeting almost as much as they love talking IRL. In fact, the act of expression is often even more important to loquacious Gemini than what \
is actually being said — and they must remember to be thoughtful with their words. Another incredible Gemini quality, however, is that these natural chameleons \
can quickly recover from even the most shameful foot-in-mouth moments. Gemini moves too fast to care about embarrassing missteps: They simply move on.",
####
    "cancer": "Cancer is a cardinal water sign. Represented by the crab, this oceanic crustacean seamlessly weaves between the sea and shore, representing \
Cancer\'s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces: For \
instance, Cancers can effortlessly pick up the energies in a room. These crabs are highly sensitive to their environments, as well as extremely self-protective. \
Much like their celestial spirit animal, Cancers are shielded by hard, external shells. At first, these crabs may be perceived as cold or distant. With time, \
though, Cancers reveal their gentle nature, genuine compassion, and mystical capabilities. Just don't be surprised if it takes a while to get to know them.\n\n\
Cancer is ruled by the moon, the celestial body that represents comfort, self-care, and maternal energies. Accordingly, Cancers tend to be domestically oriented. \
They love to create cozy, safe spaces that serve as their personal sanctuaries, then spend lots of time in them. Cancers care deeply about their families and \
are quick to adopt caregiver roles. But these crabs must be careful: When Cancers invest in someone emotionally, they risk blurring the line between attentive \
nurturing and controlling behavior.\n\n\
Cancers attract friends and lovers through their loyalty, commitment, and emotional depth. These crustaceans make excellent hosts and enjoy entertaining with \
comfort food and free-flowing libations. (Cancer rules the stomach, so there\'s nothing these crabs love more than a home-cooked meal.) If you're not a fan of \
Cancer\'s attachment to the home, that may be a bit of a problem. Though these celestial crabs avoid direct conflict by walking at an angle, they can inflict a \
harsh pinch with their distinctive brand of passive-aggressiveness. It may be difficult to convince a Cancer to talk openly about what's bothering them, but if \
you can do it without making them feel threatened, you'll build long-lasting trust.",
####
    "leo": "Roll out the red carpet, because Leo has arrived. Leo is represented by the lion, and these spirited fire signs are the kings and queens of the \
celestial jungle. They\'re delighted to embrace their royal status: Vivacious, theatrical, and passionate, Leos love to bask in the spotlight and celebrate \
themselves. These lions are natural leaders and they enjoy cultivating friendships and romances that are artistically and creatively inspired. Playful Leos have \
no problem leaning into drama-fueled romances that are perfectly suited for the tabloids. (In fact, they may even prefer them.) After all, every Leo perceives \
him or herself as a celebrity. These astrological divas never get tired of lavish dinners, exclusive parties, or decadent designer wear.\n\n\
Leo is ruled by the sun, the dazzling celestial body that governs life and vitality. The sun never goes retrograde, and likewise, Leos are renowned for their \
stability, loyalty, and consistency. They are dedicated friends and lovers who put their hearts into every relationship. (Fittingly, the Leo sign governs the \
heart.) Lions love to watch their mates succeed — until they feel threatened. They can become impaired by their ego, pride, and jealousy when they start to fear \
their star power will be eclipsed. It\'s important for celestial lions to remember that their light is never obscured by others, and the bright shine of others\' \
success does nothing to their own. Ultimately, Leos' own hubris is the greatest threat to their happiness.\n\n\
This fixed sign is known for its ambition and determination, but above all, Leos are celebrated for their remarkable bravery. In tarot, Leo is represented by \
the \"strength\" card, which depicts the divine expression of physical, mental, and emotional fortitude. Fearless optimists who refuse to accept failure, Leos \
will find their deep wells of courage grow as they mature.",
####
    "virgo": "Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo\'s deep-rooted presence \
in the material world. Virgos are logical, practical, and systematic in their approach to life. This earth sign is a perfectionist at heart and isn\'t afraid to \
improve skills through diligent and consistent practice. Virgo rules the digestive system, which makes these earth signs especially attuned to the ingredients \
that make up a whole — in food and in everything else. They're hyper-aware of every detail.\n\n\
Virgo is governed by Mercury, the messenger planet of communication. Though Mercury also rules Gemini, these two signs are radically different: Gemini is about \
output and expression, whereas Virgo is about input and processing. A Virgo deals with information like a computer, transforming even the most jumbled set of \
information into organized, clear concepts. Though Virgos long to be meticulous in all pursuits, they must remember that constantly chasing after the ideal can \
be destructive when applied to self or others. Beauty exists within our imperfections and it\'s important for Virgos to learn that flaws are not defects.\n\n\
Above all else, Virgos want to help. They are kind, gentle, and supportive friends and lovers who use their incredible intellect and resourcefulness to \
problem-solve. Virgo's opposite sign, Pisces, offers guidance through spirituality, but Virgos want to assist on a practical level. These earth signs are always \
striving to provide workable solutions and improve broken systems. Methodical, committed, and hardworking, they make excellent teachers, healers, editors, and \
musicians.",
####
    "libra": "Libra is an air sign represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's \
fixation on balance and harmony. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life. These air signs are the aesthetes of the \
zodiac: Ruled by Venus, the planet that governs love, beauty, and money, Libras adore high art, intellectualism, and connoisseurship. Suave Libras need to \
surround themselves with stunning objects and create environments that reflect their exquisite tastes. Accordingly, these air signs make excellent designers, \
decorators, art critics, and stylists.\n\n\
While Libra's opposite sign, Aries, represents \"me,\" Libra symbolizes \"we.\" Relationships are paramount for Libras, who find balance in companionship. They \
love harmonious partnerships with fashionable mates, especially those who make attractive arm candy. (Libra governs the skin, and these air signs are highly \
motivated by physical appearance. There's no better way for a Libra to relax than with a luxurious face mask.)\n\n\
Libras, when they are regularly coupled, must be careful about seeking attention outside the agreed-upon boundaries of their relationship. Since they try to \
keep everyone happy and engaged, they may find themselves tempted to push the limits of their agreements with their partners. People-pleasing Libras must remember \
that the happiness of their loved ones and the health of their relationships is more important than maintaining the attention of distant admirers.\n\n\
Libra is a cardinal sign, which means Libras are accordingly great at launching new initiatives. However, because Libras consider multiple perspectives in all \
pursuits, these air signs struggle with indecision. Instead of constantly seeking outside perspectives, Libras would do well to develop (and trust) their own \
intuition. Their characteristic ambivalence aside, Libras can navigate virtually any social situation, effortlessly resolving conflicts by simply turning on the \
charm.",
####
    "scorpio": "Scorpio is one of the most misunderstood signs of the zodiac. Because of its incredible passion and power, Scorpio is often mistaken for a fire \
sign. In fact, Scorpio is a water sign that derives its strength from the psychic, emotional realm. Like fellow water signs, Cancer and Pisces, Scorpio is \
extremely clairvoyant and intuitive.\n\n\
What makes this water sign unique is its distinctive venomous sting. Like their celestial spirit animal, the scorpion, Scorpios lie in wait and strike when least \
expected. Life is a game of chess for these calculating water signs, who are constantly plotting several steps ahead in order to orchestrate an eventual checkmate. \
This doesn't mean their intentions are necessarily nefarious. Scorpios simply know what they want and aren't afraid to work hard and play the long game to get it.\n\n\
They never show their cards and their enigmatic nature is what makes them so seductive and beguiling. Scorpio is the sign most closely associated with sex: The \
part of the body that Scorpio governs is the genital area. Sex isn't solely about pleasure for these sensual scorpions. They also crave the physical closeness, \
spiritual illumination, and emotional intimacy sex can provide.\n\n\
Scorpio is ruled by Pluto, the planet that governs both destruction and transformation. On a good day, Scorpion energy is ambitious and enticing. On a bad day, \
however, the shadowy side of Scorpio is fueled by a relentless desire for control. Power-hungry Scorpios must remember that if controlled by their egos, they are \
at risk of poisoning themselves. This sign is at its best when that intrinsic intensity is applied to deep, soulful connections with friends and lovers. When they \
build trust with others, Scorpios demonstrate unparalleled empathy, depth, and commitment that brighten even the darkest parts of Scorpio\'s magical psyche.",
####
    "sagittarius": "The final fire sign of the zodiac, Sagittarius traits are unlike any other sign of the zodiac; they're totally unique to this brazen spirit. \
As a professional astrologer with almost 10 years of experience, I can honestly say that there is no zodiac sign like Sagittarius. What makes Sagittarius so unique \
is its dynamic blend of passion, curiosity, intensity, and adaptability. Represented by the archer (a half-man, half-horse centaur), Sagittarius isn't afraid to \
use its bow and arrow to explore expansive terrain, seeking answers in places and spaces others wouldn\'t dare venture. Whether they're white water rafting down \
a river in some undisclosed location or taking a pilgrimage to a sacred site to uncover secrets about an ancient civilization, Sagittarius\' quest for knowledge \
knows no bounds.\n\n\
Sagittarius is a mutable sign, meaning it is associated with adaptability and flexibility. This perfectly reflects the archers' deep-rooted desire for change. \
Sagittarians are born to explore and it is critical that these archers have the freedom to roam. (Sagittarius rules the thighs, so these archers are always on the \
move.) Fueled by wanderlust, these archers can be found traversing all corners of the world on thrill-seeking expeditions, chasing after geographical, \
intellectual, and spiritual adventures. Sagittarians are on a perpetual quest for knowledge, which makes them incredible storytellers, entertainers, and creatives. \
It's not all fun and games, however: Sagittarius is notorious for its signature bluntness, and their \"brutal honesty\" can often lead to misunderstandings, \
communication breakdowns, and lots of hurt feelings. But the good news? Sagittarius doesn't take anything too seriously, so it's hard to stay mad at these wild \
optimists.\n\n\
Sagittarius\' ruling planet is Jupiter, the planet of abundance. You know the expression \"go big or go home?\" Yeah, that\'s basically Jupiter's motto. Jupiter is \
all about excess — it expands anything it touches. So, naturally, this sign demands to have it all. The word  \"enough\" doesn't exist within this sign\'s \
vocabulary. When Sagittarius is intrigued by something — whether it\'s a Wikipedia blackhole or a newfound internet crush — they go all in. That is, until \
something else catches their eye. As a mutable sign, Sagittarius don't stay on any single fascination for too long; these archers have so many passions and \
interests, they\'re constantly bouncing from one idea to the next! What's more, since 2020, the solar and lunar eclipses have been activating the Gemini-Sagittarius \
axis, so there\'s been tons of movement and transformation for this fiery sign. Be sure to check this month\'s Sagittarius horoscope for insight on Sagittarius\' \
latest journey.",
####
    "capricorn": "The last earth sign of the zodiac, Capricorns and their unique spirits are powerful, to say the least. I\'ve worked with thousands of clients over \
my nearly-10 year-long career as a professional astrologer, and I can confirm that there\'s something that makes Capricorn extremely special. Perhaps it\'s their \
fearless ambition? Their limitless resilience? Their ability to keep pushing forward, even in the face of challenging adversity and painful strife? Or, maybe it\'s \
their secret wild side that\'s very rarely depicted in standard personality assessments, but that rumbles within the soul of every Capricorn: Not everyone gets to \
see Capricorn ordering rounds of tequila, dancing on the table, and staying out until the crack of dawn — but that rebellious, untamed spirit is a Capricorn asset. \
I mean, how else do you expect this zodiac sign to let loose and have fun?\n\n\
Indeed, inside every earnest Capricorn is a mischievous troublemaker (in tarot, Capricorn is symbolized by the \"devil\" card). Though this earth sign may seem a \
bit conservative and restrained at first, Capricorn\'s closest friends and lovers know that these sea goats love to party.\n\n\
Interestingly, Capricorns are said to age backwards: they become increasingly youthful, optimistic, and playful as they mature. Indeed, inside every earnest \
Capricorn is a mischievous troublemaker Though this earth sign may seem a bit conservative and restrained at first, Capricorn's closest friends and lovers know \
that these sea goats love to party.\n\n\
Capricorn is symbolized by the sea goat, a mythological creature with the body of a goat and tail of a fish. This imagery speaks to Capricorn\'s bifurcated \
abilities: Capricorns are skilled at navigating both the material and emotional realms. They scale the steepest mountains — Capricorn rules the knees, making it \
easier for this sign to climb — while simultaneously building up their psychic fortitude. Capricorns are relentless: They are determined to overcome whatever \
stands in their way. They have big picture, long-term goals and they absolutely don't want to be bogged-down by annoying details or superfluous information. \
However, because of their unwavering focus, Capricorns can sometimes be perceived as cold, unemotional, or even cutthroat — but that\'s only because Capricorn has \
perspective. If it won't matter in five years, Capricorn simply cannot be bothered with it today.\n\n\
Of course, this speaks quite literally to Capricorn\'s planetary ruler: Saturn. The ringed-gas giant in our distant solar system, Saturn is the planet associated \
with tasks, rules, responsibilities, and — perhaps most importantly — time. Thanks to Saturn, Capricorn is so incredibly connected to the concept of time. Sure, \
this may translate to Capricorns punctuality or calendar management, but — to be honest — it\'s a bit more existential than that. Capricorn recognizes that life is \
short and, likewise, they\'re always racing against the clock. There are so many things Capricorn wants to accomplish and achieve in this lifetime; slowing down \
is simply not an option. As a cardinal sign, Capricorn is really motivated to start new projects — this sign is constantly coming up with new ideas! Of course, \
solar and lunar eclipses will help propel their ideas forward, so be sure to look out for these life-altering, destiny-packed astrological events, as well. It\'s \
time to go even deeper with your Capricorn horoscope — let\'s do it.",
####
    "aquarius": "As you can imagine, I encounter a lot of misconceptions as a professional astrologer — not just regarding my career as a stargazer, but also \
relating to the technical aspects of astrology. One of the most ubiquitous, albeit innocuous, errors is that Aquarius is a water sign. I could certainly understand \
the confusion here — especially with \"aqua\" as the prefix — but once you get to know this zodiac sign, it becomes strikingly clear that Aquarius is an air sign. \
As the eleventh and penultimate sign of the zodiac, Aquarius is actually the final air sign, which means it deals with air-related concepts (we'll get more into \
that momentarily) from a macro-perspective. Of all the zodiac signs, Aquarius is undoubtedly the most innovative, progressive, rebellious, and humanitarian. And \
while Aquarius can often be found planning a revolution or proudly flaunting their funky fashion sensibility, they also have an often overlooked sensitive side \
that requires appreciation, support, and love.\n\n\
Air energy is all about the mind. Intellectual, curious, and deeply social, the air signs (Gemini, Libra, and Aquarius) are passionate about interpersonal \
dynamics. As the last air sign in the zodiac, however, Aquarius takes these concepts to a whole other level. Aquarius is represented by the water bearer (hence \
the \"aqua\"), the mystical healer who bestows water, or life, upon the land. Represented by the Star card in tarot, Aquarius can be visualized as a \
larger-than-life, mythical being with one foot firmly planted on the soil (representing a sense of being grounded) and one positioned in the water. Aquarius is \
holding a vase, which pours new streams of inspiration to cultivate longevity, healing, and hope. Here, it's important to remember that Aquarius is removed from \
this process — from this vantage, we can see that Aquarius is positioned as an independent entity separate from the life-giving hydration it offers the cracked \
soil. In this respect, Aquarius exposes its deep connection to community: Rooted in teamwork, collaboration, and the concept of the \"greater good,\" Aquarius is \
determined to make a powerful difference in the world.\n\n\
Aquarius is ruled by Uranus, the planet that governs innovation, technology, and surprising events. Uranus perfectly mirrors Aquarius' distinctive attitude, \
complementing the nontraditional nature of these visionary air signs. Aquarians are big thinkers, but mustn't forget their immediate surroundings. These water \
bearers can become so focused on implementing widespread reform that they neglect their family and friends, gaining a reputation for being distant in \
relationships. Aquarians should remember that progress always starts on a micro level and advocate empathy and compassion wherever possible.",
####
    "pisces": "Pisces, a water sign, is the last constellation of the zodiac. It\'s symbolized by two fish swimming in opposite directions, representing the \
constant division of Pisces\'s attention between fantasy and reality. As the final sign, Pisces has absorbed every lesson — the joys and the pains, the hopes and \
the fears — learned by all of the other signs. This makes these fish the most psychic, empathetic, and compassionate creatures of the astrological wheel. With such \
immense sensitivity, Pisces can easily become swallowed by emotions and must remember to stay grounded in the material realm (appropriately, Pisces rules the feet).\n\n\
Pisces is ruled by Neptune, the celestial body that governs creativity and dreams, and these ethereal fish adore exploring their boundless imaginations. In its \
more nefarious form, however, Neptune also oversees illusion and escapism. Neptunian energy is like the energy of the ocean: magical, mysterious, and often scary. \
When the fog is thick on the water, the horizon is obstructed and there is no differentiation between the sea and the sky.\n\n\
Those with this sun sign must be wary of mirages: These impressionable fish prefer wearing rose-colored glasses to addressing problems, which can earn Pisces a \
reputation for being flaky or delusional. This water sign should remember that problems can\'t be solved by swimming away. Willful ignorance never makes conflict \
disappear: It only gives it the chance to grow.\n\n\
A mutable sign, Pisces effortlessly adapts to their surroundings. These visionary fish have unparalleled access to the collective unconscious through their \
clairvoyance and make incredible artists and creatives. Kind and gentle, they\'re invigorated by shared experiences of music and romance. Any relationship with \
mystical Pisces is guaranteed to involve deep spiritual exploration."
}

july_2022_horoscopes_dic = {
    "aries": "Welcome to July, darling Aries. At the end of last month, you reconnected with friends and felt the love and warmth of platonic support systems. \
Remember, even in your dream romance; you cannot depend on your romantic partner for everything. When your ruling planet, the fierce warrior Mars, enters Taurus \
on Monday, July 4, you continue to enjoy sharing time, stories, and perhaps a drink with friends. Also, on this date, the communication planet Mercury enters \
caring Cancer, putting you in a collaborative mood. As a result, this all points to a great 4th of July BBQ, Aries. \n\n\
But speaking of Independence Day, as you know, from powerful protests to a pandemic and now a recession, these can be challenging times to feel optimistic. On \
Thursday, July 7, when the spiritual asteroid Vesta goes retrograde in sensitive Pisces, you may find yourself feeling blue. Continue to stay politically and \
culturally aware, but allow yourself to enjoy the happy moments in life, whether it's lighting sparklers with friends or kissing your love on a beach trip. Perhaps \
your biggest assignment for July is to find silver linings in dark times, Aries.  \n\n\
During the Capricorn full moon on Wednesday, July 13, you may feel work-related stress. Remind yourself that, as noted, we\'re living in tough times, and you are \
not alone. Full moons can trigger anxiety, so utilize your support network, from friends to therapists, to work through stress and remember that there are people \
who have your back in good times and bad. When Venus, the ruler of all things loving, abundant, and beautiful, enters sweet Cancer on Sunday, July 17, your loved \
ones continue to show up for you and offer support and good times. Just remember to offer support back in return, dear Aries. As the first sign of the zodiac, you \
can act like an only child at times, and forget the need to give and take. Chatty Mercury moves into dramatic Leo on Tuesday, July 19, helping you offer up some \
brave fire sign support to your friends who are also stressed out. \n\n\
Chiron, the wounded healer, goes retrograde in your sign starting on Tuesday, July 19. It will be retrograde until late December. When Chiron is retrograde, your \
assignment, bossy Aries, is to forget about other people and focus on yourself. The year\'s second half asks you to work on healing old wounds and unresolved \
trauma. So, lean into your inner only child, and prioritize your mental health. You\'ll be a better friend and partner once you feel your best. \n\n\
The sun enters Leo, kicking off Leo season, on Friday, July 22. As a fellow fire sign, you should enjoy the next few weeks and all the late-summer gatherings \
with friends. family, and lovers. Remember, Aries, continue to notice the positive, whether it\'s a delicious dinner or a dear friend. During the new moon in Leo \
on Thursday, July 28, you can expect positive changes in your love life, which will help you feel excited about the future. New moons are times for fresh starts, \
so this lunation sees you going on a first date, rejoining a dating app, or trying something new in bed with your long-term partner. \n\n\
July wraps up with the lucky planet Jupiter going retrograde in your sign, Aries. Starting on Thursday, July 28, the planet of expansion will be retrograde until \
late November. During these months, follow the motto \"fortune favors the bold.\" You\'re one of the bravest signs of the zodiac; Aries and Jupiter\'s retrograde \
is a yearly opportunity to continue to evolve. Continuing themes from earlier this month, this sees you working on optimism (which is different than toxic \
positivity), healing trauma, and nurturing your inner circle relationships. Have a great month, and see you in August.",
####
    "taurus": "Welcome to July, sweet Taurus. At the end of June, blessings from your ruling planet, lover Venus, added emotional depth to your love life. As the \
summer blazes on, the fighter planet Mars enters your sign on Monday, July 4, adding heat to your sex life. Having both an emotional and sexual connection with \
someone is quite rare, so if you find yourself in such a position, express your gratitude. When the communication planet Mercury enters kind Cancer on this same \
date, Monday, July 4, you\'re able to discuss mundane relationship issues, such as cleaning dishes, while maintaining sexual attraction. So, darling Taurus, \
there\'s quite the chance that the biggest fireworks this 4th of July will be in your bedroom. \n\n\
The sky lights up with a bright full moon in Capricorn on Wednesday, July 13, putting you in a deep and brooding mood. Perhaps this year\'s 4th of July was harder \
to celebrate due to the tough financial times we\'re facing (along with other issues) as a country. There will be plenty of time to party later in the month, so \
stay in during this full moon. It\'s a stressful time for everyone, and full moons can amplify anxiety and drama. Tap into your signature sensuality, Taurus, and \
opt for a long bath or night of skin care to wait it out. \n\n\
When your ruling planet, Venus, the goddess of love, beauty, and abundance, enters home-oriented Cancer on Sunday, July 17, you may find yourself having talks with \
your significant other. This isn't a reason to worry, Taurus; communication is crucial. However, that means being patient, listening to the other party, and even \
accepting that you contain flaws. This also means you may take a relationship to the next level. You just need to talk out a few things first, and if you need \
help putting your emotions and needs into words, consider working with a therapist to help you express yourself. However, when talkative Mercury moves into bold \
Leo on Tuesday, July 19, you will be surprised at your own strength. As it turns out, you can vocalize your needs while also holding space for someone else.",
####
    "gemini": "Welcome to July, flirty Gemini. At the end of last month, a dark new moon in Cancer saw you feeling reflective and craving alone time. Continue to \
use the first few days of July to rest because Monday, July 4, is a busy day for the stars, and it\'s also a holiday, so you\'ll likely be trying to decide which \
party invitation to accept. On this date, your ruling planet, communicator Mercury, enters nostalgic Cancer. So, you heartbreaker, if any exes hit you up, unless \
you have an established friendship, let the past be past and go out and meet new people. \n\n\
Also, on Monday, the wise asteroid Pallas enters your sign, Gemini. Pallas is associated with creativity and the arts. You\'re a natural creative, so with this \
added power on your side, this is a beautiful time to network and meet future collaborators (or even lovers).\n\n\
Later in the month, the sky lights up like a disco ball with a full moon in Capricorn on Wednesday, July 13. While this month\'s horoscopes advise other signs to \
lay low during this lunation to avoid drama, for you, lucky Gemini, this is a night for transformative sex that is hot, kinky, and intimate all at the same time. \
So bring out the sex toys for a spiritual masturbation sesh (opt for waterproof if you want to get off in the bathtub) or explore a different fantasy to bring you \
closer with your partner. The romantic vibes continue when lover Venus enters sweet Cancer on Sunday, July 17, helping you open up about your desires, which can be \
challenging in intimate relationships, even for chatterbox Geminis. And remember, intimacy is not exclusive to long-term relationships. Getting deep with your \
summer fling or friend with benefits is okay, as long as you\'re clear about boundaries. \n\n\
When your ruling planet Mercury moves into attention-loving fire Leo on Tuesday, July 19, you find yourself able to be clear with partners about your wants and \
needs. As you\'ve probably heard, Geminis have a reputation as a heart-breaker. And if you want to be single, you should embrace that and be single. However, you \
also don\'t want to leave a trail of vengeful exes behind you. So, embrace the communication powers of your ruling planet, and always be honest to maximize \
pleasure and minimize pain for everyone involved.\n\n\
On this same date, Chiron, an asteroid known as \"the wounded healer,\" goes retrograde in determined Aries starting on Tuesday, July 19. While Chiron is \
retrograde, where it will be until late December this year, you are asked to work through lingering trauma, resentment, and other emotional pain and residue from \
the past year. So, if you\'re feeling pressure to conform to traditional relationship formats when that\'s not your thing, use these months to talk to a \
sex-positive therapist about that. Or, if you're ready to stop playing the field and lock your lover down, perhaps it\'s time to address those commitment issues \
finally.\n\n\
Grab your sunglasses and a drink because fun-loving Leo season begins on Friday, July 22. Before autumn begins, with its unique beauty, use these weeks to make the \
most out of summer. Go to a BBQ, swim in the ocean if you can, and kiss some strangers. During the new moon in Leo on Thursday, July 28, you find yourself bonding \
with friends and interested in quality time with your platonic life partners. So, if there\'s not something happening that night, consider hosting a small dinner \
party. Also, on Thursday, July 28, Jupiter goes retrograde in bossy Aries, which gives you a gentle reminder not to neglect your friendships while you\'re busy \
making everyone fall in love with you. Have fun, and see you next month.",
####
    "cancer": "Welcome to July, Cancer. It\'s still your birthday season. At the end of June, you treated yourself to a makeover, whether it was a fresh hair color \
or fun summer eye makeup. You\'ll have plenty of opportunities to show off how hot you are on Monday, July 4, which is Independence Day but also a busy day for \
the stars. The fiery planet Mars enters loyal Taurus, igniting a desire to hang out with friends. So, even if you don\'t feel super patriotic at the moment if you \
have the 4th of July off from work, plan a low-key hang with friends. Also, on this date, chatty Mercury enters your sign, Cancer, turning you into the life of the \
party. As noted, it\'s your birthday season. Keep the celebrations going.\n\n\
On Wednesday, July 13, the sky lights up with a powerful full moon in strict Capricorn. Now, Capricorn has a reputation for being the workaholic disciplinarian of \
the zodiac, but it\'s also a sign that\'s kinky as hell. So, sweet Cancer, whether you're playing alone or with a partner, use the primal energy of this full moon \
to try BDSM or another sexy fantasy of yours. When the lover planet Venus enters your sign, Cancer, on Sunday, July 17, the stars are aligned to grant any wishes \
you make regarding love so that you can have your spankings and romance, too. This theme continues when the communication planet Mercury moves into loving Leo on \
Tuesday, July 19, helping you be honest about your feelings.\n\n\
And, speaking of feelings, get ready to spill your guts over the next few months, Cancer. When Chiron, an astrological important planetary body known as \"the \
wounded healer,\" goes retrograde starting on Tuesday, July 19, everyone will be doing emotional deep dives. Schedule time with your therapist, because Chiron \
retrograde, which lasts through the end of December, is all about going back and addressing unresolved trauma and hurt. Don\'t worry; this retrograde happens all \
the time, and if you utilize it, you come out a more evolved and happier version of yourself.\n\n\
Sadly, Cancer crab, you must hand the torch over to the Leo lion on Friday, July 22. But don't worry, Leo season is all about coming out of your shell (pun \
intended). When Ceres, a nurturing asteroid known as a healer, enters Leo the next day, on Saturday, July 23, you find yourself able to put down the claws and \
pick up a drink or the hand of your best friend to dance it out. This transit is all about celebrating your inner child, darling Cancer.\n\n\
Finally, a dark new moon in Leo on Thursday, July 28, suggests new opportunities surrounding creative and professional endeavors. Unfortunately, with this \
recession, it\'s impossible to promise anyone money. What this transit can promise is that you are an exceptionally talented and intuitive water sign, especially \
when it comes to the arts. Put your gifts to good use by picking up the paintbrush, pitching a new project, or playing an instrument during this lunation. See you \
next month!",
####
    "leo": "Welcome to July, hot Leo. Your season begins this month. June focused on your friendships, but prepare for sexy birthday celebrations because love is \
in the air. But first, on Monday, July 4, the wise asteroid Pallas enters Gemini, reminding you of the importance of a platonic support system. Even if you\'re \
monogamous, your romantic relationships will function healthier if you have friends to bitch to. So, if you have Independence Day off from work, spend it with your \
friends, soaking up summer with laughter and story-telling. Also, on Monday, July 4, Mars, which rules primal sexual energy, enters sensual Taurus. So, don\'t be \
surprised if you become enchanted with someone around this time. It could be a brand new crush or a long-term partner you reconnect with through kinky sex.\n\n\
Then, the following week, Wednesday, July 13, brings a transformative full moon in Capricorn. This lunation is an ideal night to pamper yourself, including \
orgasms. Remember, Leo; you\'re a lion, so you need lots of attention, grooming, and beauty sleep. Feel free to share this night with a trusted partner. However, \
because full moons can be anxious times, it\'s an excellent excuse for a night alone (so bust out the sex toys). Your goal for this lunation is to pamper yourself \
for your health, so it\'s okay to be selfish.\n\n\
When messenger Mercury moves into your sign, Leo, on Tuesday, July 19, start organizing and planning your birthday plans, and remember, it\'s okay to be selfish. \
Do you want to spend your birthday on a romantic date? How about dancing with friends? Because times are still tough right now, from the pandemic to economic woes, \
give your friends and partners plenty of advance notice of your plans so they can get a Covid-19 test and budget for any expenses. You\'re a sign which isn\'t \
afraid to tell people what you want as a present (which honestly can make people\'s life easier), so go ahead and send bae your wishlist.\n\n\
Chiron, the wounded healer, goes retrograde in Aries from Tuesday, July 19, through late December. When Chiron is retrograde, it asks everyone to address lingering \
resentments and unresolved trauma. For you, Leo, you may benefit from doing so by trying something new. So, if you\'re already in therapy, consider trying a \
different kind, or adding on an additional self-love practice, such as meditation, to your routine.\n\n\
Raise your glass and cheers because Leo season begins on Friday, July 22. Happy birthday, you glorious lion. May you celebrate as much as your heart desires in the \
next few weeks. The day after, on Saturday, July 23, the nurturing asteroid Ceres also enters your sign. This transit encourages you to embrace your inner child. \
So break out party games, try a fresh hair color, dance your ass off, and simply have as much fun as possible. The world is a better place when all the Leos are \
content.\n\n\
Thursday, July 28, brings a new moon in your sign, Leo. New moons are times for fresh starts and intention settings, so use this night to write down your goals and \
reflect on your dreams. Never forget that you are a powerful lion who deserves a beautiful life. When the lucky planet Jupiter goes retrograde in assertive Aries \
on this same date, which will last for four months, you should see these intentions begin manifest into reality, so the stars have some birthday presents for you \
too, Leo. See you next month.",
####
    "virgo": "Happy July, lovely Virgo. Last month, you worked through some conversations on the homefront, whether it was confronting a roommate about chores or \
moving in with your significant other. Hopefully, you\'ll get a day off in early July, because Independence Day, Monday, July 4, is a busy day for the stars. Your \
ruling planet, messenger Mercury, enters homebody Cancer and connects you with friends. Even if you aren\'t feeling patriotic, try to spend the day enjoying life \
with people close to you. When your love and sex life ignites later this month, you\'ll want friends to call about it.\n\n\
Also, on Monday, July 4, the warrior planet Mars enters sensual Taurus, encouraging you to explore new avenues of pleasure. Is there a sex toy that you wish to \
enjoy? Do you have a secret fantasy that you want to explore with a lover? It\'s okay if you don\'t see actual fireworks. When you go home to masturbate or make \
love, there will be plenty of sparks.\n\n\
Mid-month, on Wednesday, July 13, there\'s a glowing full moon in fellow Earth sign Capricorn. Often, astrologers warn their readers to lay low during full moons \
because they can prompt sudden drama and petty bickering. However, the grounded Capricorn full moon illuminates the pleasure sector of your chart, encouraging you \
to keep the party going. Consider using this night to explore new avenues of sensuality, whether it\'s masturbating in a calming bath, gently exploring BDSM, or \
writing love poems. Whatever happens during this full moon, as mentioned earlier, expect to discover something new about yourself as a lover. When Venus, the ruler \
of love, abundance, and beauty, enters friend and family-oriented Cancer on Sunday, July 17, you\'ll be texting all your friends about it. Just remember to ask how \
they\'re doing, as well.\n\n\
On Tuesday, July 19, your ruling planet, chatty Mercury, moves out of Cancer and into brave Leo. As a result, you\'ll feel ready to talk about any lingering \
emotional pain, trauma, or heartache you\'re carrying with you. The timing of this transit is ideal because also on Tuesday, July 19, Chiron, an astrological \
significant planetary body known as \"the wounded healer,\" goes retrograde, where it will stay until late December. During the next few months, you\'ll see \
yourself working through what keeps you up at night, and by the end of the year, be a happier person as a result. And, if you aren\'t already, consider working \
with a therapist to help make this process easier.\n\n\
The sun enters fun-loving Leo on Friday, July 22. While the end of summer brings beautiful sunsets, cute nail art, and dance parties, don\'t forget to make time \
for plenty of rest. Don\'t be surprised if you experience some summertime sadness, darling Virgo. As there hermit of the zodiac, you need to retreat now and then \
to recharge. The perfect night for a night in is Thursday, July 28, which brings an intimate new moon in Leo. Remember, Leos love attention, but like their symbol, \
the lion, they need plenty of cat naps. So let yourself sleep in as much as possible. When the lucky planet Jupiter goes retrograde also on Thursday, July 28, \
you\'ll find yourself bursting with creative ideas, from interior decorating to professional projects. Soon you\'ll be busier than ever and grateful for the rest. \
Enjoy, and see you in August.",
####
    "libra": "Welcome to July, charming Libra. Thankfully, Mercury retrograde ended last month, so you can breathe more easily. But speaking of the messenger of \
the gods, Mercury enters sweet Cancer on Monday, July 4, bringing a flutter of social invitations with it. It makes sense; July 4 is a holiday, after all. So if \
you have the day off from work, take it, and work on mindfulness to savor the present. Also, on Monday, July 4, Mars, which rules primal sexual energy, enters \
sensual Taurus. As a result, you\'re in a flirty mood, pretty Libra. Because lover Venus is your ruling planet, you always have an allure to you, but on this date, \
you're on fire. Don\'t be surprised if you meet someone enchanting or experience newfound joy in your long-term romantic relationships on this day.\n\n\
Wednesday, July 13, brings a full moon in devilish Capricorn. Perhaps it was the sex and socialization earlier this month, but you feel tired and worn out. Our \
society undervalues rest, but if you want to feel like the royalty that you are, Libra, you must make time for beauty sleep. Full moons tend to bring drama \
anyways, so lean into your homebody side during this lunation.\n\n\
When your ruling planet, Venus, the goddess of love, beauty, and abundance, enters caring Cancer on Sunday, July 17, you should experience a deepening in your \
romantic relationships. If you\'re single, this weekend sees you growing closer with potential new crushes or understanding that you can still experience intimacy \
within a friends-with-benefits situation. And, if happily in a relationship, you may find your relationship leveling up during this time, whether you\'re becoming \
official or putting a ring on it. You\'ll be feeling chatty when Mercury moves into confident Leo on Tuesday, July 19, and ready to share the news with all of your \
friends. Remember, Libra; it\'s crucial to maintain platonic relationships. Even if you are monogamous, one person cannot be your everything.\n\n\
Just as one person can\'t be your everything, your friends can\'t be your therapist. Expand your support network as much as possible this month because on \
Tuesday, July 19, an astrologically significant comet, Chiron, \"the wounded healer,\" goes retrograde and will stay until late December. When Chiron is \
retrograde, everyone is given an opportunity to work through and let go of lingering resentments, regardless of their star sign. So, if you\'re still not totally \
over an ex or are carrying a chip on your shoulder about a professional matter that happened months ago, this transit asks you to let it go. Circling back to \
mindfulness, embracing the present will be much easier if you've left the past in the past.\n\n\
The sun enters Leo, kicking off Leo season, on Friday, July 22. Before you know it, Libra, your thoughts will be on autumn hair colors, cozy sweaters, and cuddling \
on the couch, so make the most out of the dog days of summer by spending them with your friends. An especially powerful night to connect is Thursday, July 28, \
which brings a new moon in confident Leo. New moons are a time for setting intentions, so consider hosting a coven meeting where you get together and state your \
desires for the rest of the year. Identifying what you want is the first step to manifesting it, Libra. Check back next month to see how your intentions begin to \
come to life and don't forget to get enough beauty sleep.",
####
    "scorpio": "Welcome to July, mysterious Scorpio. Last month, you worked on building intimacy within your romantic relationships. While people associate Scorpio \
with sex, that doesn\'t mean that maintaining healthy sexual relationships is always easy for you; you experience the same insecurities as everyone else. When one \
of your ruling planets, red hot Mars, enters sensual Taurus on Monday, July 4, you get a helpful nudge from the stars. This transit helps you see things from your \
partner or crush\'s perspective and, just as importantly, acknowledge your own flaws. So, if you've used your signature stinger on anyone recently, you\'ll gain \
favor by apologizing for being harsh.\n\n\
When the sky lights up with a bright full moon in Capricorn on Wednesday, July 13, your communication efforts pay off. Now, because they can bring drama, full \
moons aren\'t the best time for extensive relationship talks, but this is an ideal night to have some light-hearted fun with your partner or crush, whether it\'s \
making love or dancing. If you\'re single, you should do the same with a dear friend — everyone needs to let loose sometimes (if not a whole lot, given the last \
two years involved quite a lot of staying in). This full moon brings a good time, as long as you keep your stinger at bay, regardless of your relationship status.\n\n\
When Venus, the ruler of love, beauty, and abundance, enters Cancer on Sunday, July 17, you find yourself thinking about love differently. Remember, Scorpio, \
you are a sign of transformation; it\'s OK to change your mind. For instance, perhaps you swore off monogamy, marriage, and all things traditional but suddenly \
find yourself prowling the internet for wedding hair inspo. Or perhaps you suddenly realize that you just want to be single right now. Whatever it is, allow \
yourself to feel the thoughts and emotions that arise during this time — trust yourself, dear scorpion, and embrace change.\n\n\
When Chiron, which is a comet known in astrology as \"the wounded healer,\" goes retrograde in Aries on Tuesday, July 19 all signs are encouraged to process \
unresolved trauma in order to flourish in the present. As an intense sign who can internalize hurt more than you let on, this process is crucial to your \
well-being, Scorpio. In particular, you should work on forgiving yourself for those times you did push your signature intensity and show your stinger. Everyone \
has bad days, and self-loathing is seriously bad for you. So, treat yourself, practice self-care, and as always, consider working with a therapist if you aren\'t \
already.\n\n\
Break out your selfie stick and play with summer makeup looks because fun-loving Leo season begins on Friday, July 22. Make the most of the remaining summer by \
connecting with friends and allowing yourself plenty of naps. Of course, the stars can\'t predict anything involving money in this economy, but when the sky goes \
dark with a new moon in Leo on Thursday, July 28, you may receive welcome professional news. Life can change on a dime, Scorpio, and you may go from cat naps to \
all-nighters quickly, so remember to soak up the sun this month, and we\'ll see you in August.",
####
    "sagittarius": "Happy July, fierce Sagittarius. Last month brought a powerful full moon in your sign and positive changes within your romantic relationships. \
You\'re one of the most independent signs of the zodiac. However, as a result, expressing your emotions can be difficult for you. So, even when you\'re totally \
into somebody, they may have no idea. Thankfully, conversations flow like water when the communication planet Mercury enters sweet Cancer on Monday, July 4. This \
is an ideal time to go ahead and admit to your crush how much you\'re into them.\n\n\
On this same date, Monday, July 4 (a fiery Independence Day for you), Mars, which rules f*cking and fighting, enters sweet Taurus, showering your sex life with \
orgasmic fairy dust. So, you see, there are benefits to healthy communication, Sagittarius. While boundaries are crucial, beware of emotionally boxing yourself in.\n\n\
As you\'re likely aware, our country is going through some tough times, so, unfortunately, horoscopes can\'t promise anyone money. With that in mind, the full moon \
in ambitious Capricorn on Wednesday, July 13, looks to be a fortuitous time in your professional life. In astrology, full moons represent manifestation. So, if \
you\'ve been working on a workplace or creative project but waiting for the right day to announce it or pitch it to your boss, this Capricorn full moon has your \
back, Sag. When Venus, which rules money and abundance in addition to love and beauty, enters caring Cancer on Sunday, July 17, (positive) change is afoot, so July \
does look to be an optimistic month for your career.\n\n\
Get excited, dear archer (did you know that you\'re the only sign that carries a weapon?) because Leo season begins on Friday, July 22. Sags love Leo season \
because the fellow fire sign also loves getting attention and having lots of fun. Remember, Sagittarius; you\'re a sign that\'s associated with travel. Summer \
is starting to enter its dog days, and it\'s often more accessible for people to take time off work around this time. So, if you can swing it, try to squeeze in \
a weekend getaway during Leo season.\n\n\
You\'re also known for your love of knowledge, Sag. You love learning new things, whether it\'s an instrument or language. Thursday, July 28, brings a new moon in \
Leo. Because new moons mark new beginnings, they are excellent nights for intention-setting. You love writing down goals, admit it, so use this night to do it \
(or even make an old-school vision board).\n\n\
The month comes to a close with your ruling planet, lucky Jupiter, going retrograde for four months starting on Thursday, July 28. Unlike Mercury retrograde, this \
isn\'t a reason to worry about issues such as travel delays or texting the wrong lover. Rather, use the next four months to develop a meditation routine, or work \
with a therapist, to get in touch with your needs. Are you as happy as possible under the global circumstances? Is anyone or anything holding you back? The next \
few months are for reflection and growth, and you, clever Sagittarius, will come out as an even more evolved version of yourself. See you in August.",
####
    "capricorn": "Happy July, darling Capricorn. Last month, your ruling planet, strict Saturn, went retrograde, asking you to set boundaries. But remember, \
Capricorn, there is a difference between healthy boundaries and walling people out. Independence Day, Monday, July 4, is a busy day for the stars. To start, the \
passionate planet Mars enters sensual Taurus, leaving you craving love, intimacy, and orgasms. Additionally, the communication planet Mercury enters sweet Cancer, \
which helps you talk about sex and love. So, devilish Capricorn, early July is an ideal time to ask for what you want out of love because the stars align to grant \
your wishes.\n\n\
And, speaking of granted wishes, there\'s a glowing full moon in your sign, Capricorn, on Wednesday, July 13. Full moons are associated with manifestation and \
often indicate a completed cycle. So, considering how hard you've worked to make your love life healthier and happier, this lunation suggests romantic growth. \
It\'s a lovely night to ask someone out on a first date, marry you, or get the hex out of your DMs. Your only job to ensure the completion of this cycle: be \
honest and honor your needs and desires.\n\n\
July is shaping to be major for your love life, you hardworking sea-goat. When Venus, the planet of love, beauty, and abundance, enters sweet Cancer on Sunday, \
July 17, you receive blessings in your romantic partnerships. Of course, this can include meaningful platonic friendships, as well. Your job during this transit \
is to let things be. Try not to nag or start petty arguments. At times, Cap, you can be overly critical of others without even realizing it. When the stars align \
to give you smooth sailing in your partnerships, try and let it be.\n\n\
When messenger Mercury moves into confident Leo on Tuesday, July 19, you refocus on work and find yourself able to stand up for yourself professionally. Of course, \
no astrologer can promise money in this economy, but this transit suggests that you\'re beginning to recognize your worth. You have a reputation for being the \
most hardworking and ambitious zodiac sign, but even Capricorns deal with imposter syndrome. So, not only should you work on becoming aware of your value, but use \
this transit to advocate for yourself and others in the workplace.\n\n\
When Chiron, a comet known as \"the wounded healer\" in astrology, goes retrograde in Aries starting on Tuesday, July 19, everyone is asked to let go of lingering \
negative thoughts, anxieties, and traumas experienced over the past year. When Chiron goes retrograde, which will last through late December, continue reminding \
yourself of your value.\n\n\
Attention-loving Leo season begins on Friday, July 22. Sometimes, taking a break is hard for you, Capricorn, but not just because of stereotypes of Capricorns \
being workaholics. The truth is, even if you don\'t show it, thanks to your grounded Earth sign exterior, you\'re a profoundly emotional sign which can be prone \
to anxiety. And travel, or asking for time off work, can be stressful. However, if you can take at least a weekend just for yourself to reconnect with nature, \
catch up on your favorite books or movies, or even just sleep, your body and mind will thank you for it.\n\n\
When the sky goes dark with a new moon in Leo on Thursday, July 28, you'll be grateful for the downtime. This lunation is about your sex life, so lean into your \
kinky side, you sea-devil you. Whether you\'re treating yourself to a sex toy or exploring a fantasy with a lover, your forecast for this new moos is even more \
fireworks than you saw during the 4th of July. So enjoy, and see you in August.",
####
    "aquarius": "Welcome to July, enchanting Aquarius. Last month, in part thanks to a dramatic full moon in fiery Sagittarius, you enjoyed alone time. The rebel \
    of the zodiac needs its rest, after all, dear water-bearer. However, this month brings a busy 4th of Leo followed by social Leo season, so start playing with \
    party make-up looks.\n\n\
When Mars, which rules primal sexual energy, enters sensual Taurus on Monday, July 4, the party comes to your doorstep. If you have off work, you may see yourself \
hosting a party with friends, and yes, Aquarius, you can talk about all the work our country has ahead of itself on Independence Day. You\'re known to care about \
your community, so your social group cares what you have to say. On this same day, the communication planet Mercury enters caring Cancer, reminding you that it can \
be therapeutic to talk about the world\'s troubles with friends. That\'s what they\'re there for.\n\n\
Even though we often associate summer with fun times in the sun, summertime sadness is real. Aquarians can be very emphatic, so even when your personal life is in \
order, the news headlines of war and other bad news can get to you. So, when Wednesday, July 13, brings a full moon in Capricorn, consider taking last month\'s \
full moon advice and staying in. Even though not all Capricorns fit the workaholic stereotype, this will still be a busy, commercial day, so take care of yourself \
by turning off your phone, ignoring Twitter, and enjoying a hobby, sex, or simply relaxing with the TV.\n\n\
While you don\'t have to keep your phone off forever, consider lightening up on your social media intake and doom-scrolling for the rest of the month; consider \
it a kind of summer vacation. So when the romantic planet Venus enters sweet Cancer on Sunday, July 17, you feel the right kind of selfish, Aquarius. Remember, \
your health comes first. And despite the distant air-sign stereotypes, having grounded, healthy, romantic relationships are important to you. So allow this \
transit to help refocus your attention away from headlines and towards your bae, and if you\'re single, remember that your platonic relationships also need \
tending. When the communication planet Mercury moves into loud Leo on Tuesday, July 19, expressing your needs within personal relationships becomes much easier. \
(Let's be honest: You can be more than a little shy with your emotions at times, Aquarius.)\n\n\
The fun-loving Leo season kicks off on Friday, July 22. Expect a rise in selfies and late summer social invitations for the next few weeks. Circle Thursday, July \
28, in your calendar, because it brings a new moon in Leo that\'s all about your love life. New moons are a time of new beginnings. You may feel called to rejoin \
dating apps or finally move past a fight with your current partner. On the same date, the lucky planet Jupiter begins its four-month retrograde in Aries. You \
should see joyful growth in your love life for the next few months, but only if you\'re willing to communicate, even about difficult interpersonal topics. You can \
do it, Aquarius, and see you next month.",
####
    "pisces": "Happy July, beautiful Pisces. Last month, your ruling planet, dreamy Neptune, went retrograde, reminding you to honor your emotional needs. As a \
profoundly empathetic water sign, sometimes you are hesitant to speak up if something is bothering you. You can be a little bit shy at times, like a fish who wants \
to dive underwater towards safety. However, when the communication planet Mercury enters sweet Cancer on Monday, July 4, you\'re ready to express yourself, \
especially about sex. You may be modest sometimes, but you are an incredibly sensual sign. This transit helps you tell a partner about a desire. If you\'re \
single, this transit may help you shake off any lingering sexual shame holding you back from enjoying a kink.\n\n\
This year\'s Independence Day is very busy for the stars. Also, on Monday, July 4, the warrior planet Mars, which rules f*cking and fighting, enters Venusian \
Taurus. This combo-platter of sexual tension and sweet romance could make this date the most romantic day of the month for you, Pisces.\n\n\
On Thursday, July 7, Vesta, an asteroid connected with nurturing love, the home, and sexuality, goes retrograde in your sign, Pisces. You will be pulled in two \
different directions for the next three months. One is the past and nostalgia. If you allow yourself, Vesta retrograde may involve a lot of wallowing about exes. \
However, if you start swimming forward, dear fish, this retrograde will bring momentum to your love life and help you truly feel at home.\n\n\
Wednesday, July 13, brings a full moon in fussy Capricorn. Full moons can be dramatic (just wait until Leo season begins), so as a result, it\'s not always the \
best night to plan anything mega-important or serious. However, this lunation looks to be a wonderful night to reconnect with your friends. Have a coven meeting \
by enjoying an outside hang with a view of the bright full moon.\n\n\
It\'s good that you got some time in with friends because when lover Venus enters romantic Cancer on Sunday, July 17, you won\'t want to get out of bed. This can \
mean self-love — the relationship between a person and their sex toys is sacred — or a sex marathon with your partner. Either way, circle this weekend in your \
calendar and take advantage of Venus\'s blessings. Social Leo season begins on Friday, July 22, so you\'ll have plenty of opportunities to enjoy life out of bed \
later in the month.\n\n\
Whether you met someone new at a BBQ or connected deeply with a current partner during your hot sex, there's reason to believe that the stars see you entering or \
leveling up a long-term partnership. Juno, known as \"the asteroid of commitment,\" goes retrograde in your sign for roughly three months on Monday, July 25. While \
we associate Mercury retrograde with annoyances, not all retrogrades are bad. Rather, they give you an opportunity for a cosmic re-do. So, wise Pisces, work on \
being your best self because the next few months ensure your love life will lead you to the happiest place possible.\n\n\
Use the new moon in Leo on Thursday, July 28, which is a time for beginnings, to write down intentions for Juno retrograde, and see you in August."
}

yearly_2022_horoscope_dic = {
    "aries": "Hello, Aries, and welcome to 2022! Remember, you\'re the first sign of the zodiac, and as a result, insist on getting your way (and usually do). But, \
dear ram, if your love life feels at a stand-still lately, that should change when Venus goes direct on Saturday, January 29. When Venus, the planet of romance, \
is retrograde, working through relationship issues can feel like navigating your way out of quicksand. Thankfully, the planet goes direct just in time for \
Valentine\'s Day, so be your bold Aries self and tell your crush or partner exactly what you want this year. \n\n\
And, while you\'re at it, start making that birthday wishlist because Aries season begins on Sunday, March 20. As a fire sign, you feed on attention, and that\'s \
not a bad thing. You deserve to feel special during your birthday because you are. You\'re optimistic, brave, and your determination inspires others. Mercury, \
the planet of communication, enters your sign on Sunday, March 27, where it will stay until Sunday, April 10. While Mercury is in Aries, you\'ll find that \
communication flows easily, and friends and lovers text back promptly. So, start sending those birthday invitations. 2022 is a year for celebrating life, and your \
inner circle is ready to celebrate you.\n\n\
Use the new moon in your sign on Friday, April 1, to write down a list of goals for your professional life. No, darling Aries, this isn\'t dull homework. You may \
be manifesting some money moves.. New moons mark new beginnings. Venus enters your sign on Monday, May 2, and will stay until Saturday, May 28. As discussed, \
Venus rules romance, but it\'s also the planet of beauty and abundance. So if you\'re going to ask for a raise or promotion, May is the perfect month, as goddess \
Venus says you deserve to earn what you\'re worth.  \n\n\
Abundance continues to be a theme for you, Aries, when Lucky planet Jupiter enters your sign on Tuesday, May 10, where it will stay until Friday, October 28. \
Jupiter is the planet of expansion, travel, and higher learning. During these months, wealth may come easier than usual. Try to refrain from being pushy, darling \
ram, but remember: you must ask for what you want to get it. Relay your professional ambitions and desired salary to the people who matter, and keep fighting \
until you get it. Your ruling planet is Mars, the god of war, after all. If anyone knows how to get what they want, it\'s you.\n\n\
And speaking of Mars, your ruling planet enters your sign on Tuesday, May 24, where it will stay until Tuesday, July 5, adding even more firepower to your winning \
streak. While Mars in Aries will make it even easier to assert yourself, beware of becoming overly competitive or aggressive. As an Aries, you don\'t mind burning \
bridges from time to time. However, an evolved Aries knows when to unleash hell and when to cooperate. \n\n\
Sunday, October 9, brings a full moon in your sign, Aries. Use this night to have some scorching sex. And, if you\'re single, fear not: Masturbation totally \
counts. Full moons are potent, primal times. You\'ll want to celebrate your sexuality before Mars retrograde begins on Sunday, October 30, and lasts through the \
end of the year, going direct on Sunday, January 1, 2023. During this time, you may feel slightly less sexually assertive than usual. When the god of war, which \
rules aggression, goes retrograde, you\'re allowed to be a pillow princess or opt for a hot bath instead of uncomfortable shower sex. \n\n\
2022 ends on a lucky note when Jupiter re-enters your sign on Tuesday, December 20, showering you once again with stardust just in time for the holidays. Remember \
to give thanks for all the blessings this year brought your way, and promise to stay safe and have fun. See you in 2023!",
####
    "taurus": "Welcome to the new year, darling Taurus. While fresh starts excite you and 2022 brings many gifts, you may feel as if you\'re walking through \
molasses for the first few weeks of the year. This is because your ruling planet, Venus, is retrograde. Venus rules love, money, and beauty, which is why you have \
such a sensual taste, dear Taurus. But when the planet is retrograde, you may feel stagnancy in your love life and any conversation surrounding money. And, don\'t \
forget, it\'s an ill-advised time to make significant changes to your appearance. Thankfully, Venus goes direct on Saturday, January 29, returning your life to \
a luxurious baseline. \n\n\
2022 is a transformative year for you. You\'re craving intimacy more than ever and desire a solid foundation in your romantic relationships. You\'re a dedicated \
earth sign and need partnerships that provide comfort, not conflict. So when messenger Mercury enters your sign on Sunday, April 10, where it will stay until \
Friday, April 29, communication flows like water, especially in your love life. This is an ideal time to have conversations about moving in together, marriage, \
or any other define-the-relationship topics, which can seem intimidating at times. \n\n\
Pick out a cake and plan a birthday party because Taurus season begins on Tuesday, April 19. Make sure to spend your season surrounded by earthly pleasures, such \
as good food, wine, and hot sex. However, do your best to stay out of any drama because there\'s a new moon and partial solar eclipse in your sign on Saturday, \
April 30. The traditional astrological advice surrounding eclipses is to lay low to avoid the fallout from the infamous sudden endings they can bring. But eclipses \
(solar eclipses, in particular) can also welcome new beginnings. Don\'t be surprised if your social circle shifts during this time. You may fall out of touch with \
fickle friends only to meet wondrous new people. Welcome the change, Taurus. It\'s for the best. \n\n\
Venus comes home and enters your sign, Taurus, on Saturday, May 28, where it will stay through Wednesday, June 22. This transit lowers stress levels and helps \
life flow easier. Use these weeks to get some serious work done. You\'ll feel inspired, productive, and the forecast for drama is low. But if you think people \
aren\'t treating you like the royalty that you are, fear not. When fighter planet Mars enters your sign on Tuesday, July 5, where it will stay through Saturday, \
August 20, you transform into a warrior. Suddenly, asking a love interest for a higher level of commitment or an employer for better wages doesn\'t feel scary. \
Sometimes, you can feel a bit sluggish, Taurus, and accept life as it is as a result. This is not the case when Mars is in your sign. So ask for romantic \
exclusivity or a raise. You\'ll be impressed to find out how people respond to a Taurus that is armed and ready for battle. And yes, that means that you\'ll likely \
get what you want. \n\n\
On Sunday, July 31, the independent planet Uranus conjuncts the North Node in your sign, Taurus. The North Node represents spiritual lessons that you must learn \
in this lifetime. Continuing themes from above, this transit sees your social life growing and evolving. The good news is that you\'re making cool new friends, \
becoming more successful, and attracting romantic partners whose desires match yours. The bad news is that for this to happen, you may have to end some existing \
partnerships in 2022. So if you have a \"bestie\" who is constantly putting you down or a cheating spouse, don\'t expect them to be in your life for much longer. \n\n\
2022 is a transformative year, Taurus. Tuesday, November 8, brings a full moon and total lunar eclipse in your sign. This transit bookends the solar eclipse in \
Taurus earlier this year. The changes in your social life are manifesting abundant fruit. Any emotional pain stemming from breakups finally falls to the wayside \
as you embrace new relationships with confidence. Spend this night with your new lover, or alone with your favorite sex toy, and turn off the TV and cell phones. \
Eclipses can still be dramatic, even when they bring joy, so they\'re a great excuse to go analog, even for a night. New beginnings are all around you, and \
remember, Taurus, the best is yet to come. Hold tight to the people who fill your life with stability and confidence. You're allowed to cry over losses, but not \
for long. When 2022 comes to a close, your social circle is more colorful and filled with joy than you could have imagined.",
####
    "gemini": "Welcome to 2022, heartbreaker Gemini. Your ruling planet is Mercury, the messenger of the gods. Mercury rules communication, which explains why \
you\'re so good at captivating an audience, whether you're on a first date or in a work meeting. However, you\'re also more affected by Mercury's infamous \
retrogrades than other signs. The first Mercury retrograde of the year begins on Friday, January 14, and lasts until Thursday, February 3. As a reminder, during \
Mercury retrograde, you can expect miscommunications, travel delays, and annoying technological difficulties. Don\'t stress too much about these; just remember to \
double-check your emails and texts, allow for extra travel time, and please don\'t sext the wrong person. \n\n\
The asteroid Ceres enters your sign on Tuesday, February 8, Gemini, and stays through Sunday, May 15. Ceres is typically associated with the divine feminine, which \
we all contain regardless of gender. Ceres rules parenthood, food and nourishment, and family life. Don\'t worry: this doesn\'t mean that you have to have kids if \
you don\'t want them, but it does bode well for your home life. You may see yourself moving in with a partner, finding a new apartment, or simply becoming more \
interested in spending time at your lovely home than going out and partying. You can enjoy some downtime, Gemini. No one could ever forget about you!\n\n\
Mercury comes home to your sign, Gemini, on Friday, April 29. The planet is happy in this placement, and you\'ll notice that you have an even easier time getting \
your way. But frankly, Gemini, it\'s probably a good idea to double-check your texts all of the time because your ruling planet is powerful but messy, just like \
you. On Tuesday, May 10, Mercury goes retrograde again and enters Taurus on Sunday, May 22, before finally going direct on Friday, June 3. Travel and communication \
should flow more effortlessly, and it\'s safe to sign important documents. So go ahead and e-mail birthday party invitations because Gemini season begins on \
Friday, May 20. You\'re always extra, but this time of year gives you permission to go the extra mile. \n\n\
There\'s a new moon in your sign on Monday, May 30. New moons tend to mark new beginnings and are ideal for setting intentions. Use this transit to get your \
professional goals in order. Identify what you want, and then map out a plan to get it. You\'re dedicated and charismatic enough to do whatever job you desire. \
Mercury re-enters your sign on Monday, June 13, where it will stay until Tuesday, July 5. Remember, Gemini: life flows easier when your ruling planet is at home in \
your sign. So during these blessed few weeks, go ahead and start taking action to put those professional goals into place. \n\n\
Every sign is associated with a tarot card, Gemini, and yours is the Lovers. You often get accused of playing the field, but you\'re just looking for your other \
twin (and having some fun, in the meantime, of course). Venus enters your sign on Thursday, June 22, where it stays through Sunday, July 17. Venus rules abundance, \
beauty, and of course, love. Not only may you get some exciting news about money during this time, but magic stardust will rain down on your love life. Expect \
romantic dates, hot sex, and sweet nothings.\n\n\
If the earlier part of 2022 is about relaxing at home and setting intentions, the final few months are about action and results. Warrior Mars enters your sign on \
Saturday, August 20, and will stay there through the end of the year. When Mars is in your sign, you feel more confident asking for what you want in dating and \
will likely be more interested in sex. This transit also helps you act more assertive at work, which will help you manifest the career intentions you set during \
the new moon earlier this year.  You\'re a powerhouse on any day, Gemini, but beware of crossing from decisive to aggressive.\n\n\
Mercury goes retrograde yet again on Friday, September 9, ending Sunday, October 2. So here\'s another goal for 2022, Gemini: Make an action plan for Mercury \
retrogrades. They happen several times a year and hit you hard. Geminis tend to move at the speed of light and text quickly anyways, so make it a regular habit to \
double-check important emails and texts for typos.\n\n\
Wednesday, December 7, brings a full moon in your sign, Gemini. Be on the lookout for positive professional news, or exciting creative ideas, because this lunation \
culminates the intentions you set during the new moon in Gemini. And, as always, full moons bring out your primal side. So this is an ideal night to try out a new \
kink or sex toy.\n\n\
Finally, the year ends with one more Mercury retrograde starting on Thursday, December 29. But don\'t even sweat, Gemini. Remember, you know how to kick Mercury \
retrograde\'s ass, now. Have a happy New Year, and see you in 2023.",
####
    "cancer": "Welcome to 2022, darling Cancer. Your ruling planet is the intuitive, silvery moon, which rules emotions and intuition. As a result, you\'re \
empathetic, creative, and emotional. But never — not even for one second — conflate emotional depth with weakness. It\'s the source of your strength. There is a \
full moon in your sign, Cancer, on Monday, January 17. Full moons are a time of culmination. The new year is just getting started, but this lunation sees some of \
your long-term goals come to fruition. So circle this date in your calendar, and stay on the lookout for an exciting work-related email or a welcome romantic \
gesture from a crush or partner.\n\n\
The astrologically significant asteroid Ceres enters your sign on Sunday, May 15, where it will stay until Saturday, July 23. Ceres rules nourishment and food, \
family relationships and is associated with the divine feminine. Remember, Cancer, we all contain masculine and feminine qualities, regardless of gender. You\'re \
already the one in your social circle who throws the best dinner parties. So when Ceres is in your sign, you find yourself feeling extra motivated to bring people \
together, especially over food. Since the pandemic began, caring relationships have been more important than ever. Lean into your nurturing side — while practicing \
safety precautions, of course.\n\n\
Monday, May 16, brings a total lunar eclipse in intense Scorpio. Because you\'re ruled by the moon, and this eclipse takes place in a fellow water sign, you may \
feel the effects more than others. Eclipses are infamous for bringing sudden endings and beginnings. As scary as that sounds, it doesn't have to be a bad thing. \
Eclipses are cosmic wildcards, but they help keep us on track. Understand that any shake-ups are simply pointing you in the right direction during this time. \
Scorpio vibes tend to bring out everyone\'s jealous side, so lay low during this eclipse. Stay in, off social media, take a decadent bubble bath and enjoy a \
delicious meal.\n\n\
Cancer season begins on Tuesday, June 21. Happy solar return, beautiful crab! You love the summer months. If you can, try to spend some time at the beach. The \
healing salt water will help you feel grounded and reconnect with yourself. And after some much-deserved rest and relaxation, take time to reflect on what you want \
for your birthday. There\'s a new moon in your sign on Tuesday, June 28. While full moons bring culminations, new moons are a time for intention-setting and new \
beginnings. This same date brings the start of Neptune retrograde, which lasts through Saturday, December 3. When Neptune goes retrograde, the illusions in our \
lives fall to the wayside. So, if you\'ve been romantically chasing after someone toxic or taken, put down the crab claws. Instead, write down a list of qualities \
you truly desire in a partner and refuse to settle for anything less.\n\n\
Mercury enters your sign on Tuesday, July 5 where it will stay until Tuesday, July 19. Mercury is the messenger of the gods, and rules communication. When Mercury \
is in your sign, Cancer, you are better able to articulate your needs and relay them to others. This makes July the perfect month to apply for new jobs, have \
\"scary\" define-the-relationship talks, or ask for a raise.\n\n\
The first half of 2022 asked you to step up as a nurturer for the people you love. But the second half of the year, darling Cancer, is all about getting what you \
want. Venus enters your sign, Cancer, on Sunday, July 17, where it will stay until Thursday, August 11. You\'re already having good luck both professionally and \
personally thanks to the messenger Mercury, and now Venus, the planet of love, beauty, and abundance, is on your side. So while the sensual planet is in your sign, \
be on the lookout for bountiful financial news and joy in your love life. It\'s also a great time to play with your appearance, so try out a new hair color or \
experiment with makeup.\n\n\
Wednesday, November 8, brings another full moon and lunar eclipse, this time in the sign of sensual Taurus. Because eclipses can be messy, this isn\'t an ideal \
night to go on a first date or enter any social setting that might make you feel uncomfortable. Instead, tap into your inner caretaker, Cancer. Just like you, \
Taurus loves to entertain at home, with decadent snack trays and plenty of wine. Invite your trusted friends over to chill out and avoid any eclipse drama. Stay \
safe, and see you next year! ",
####
    "leo": "Welcome to 2022, Leo! You\'re so charismatic that the spotlight is naturally already shining on you. You\'re ruled by the sun, after all, and no other \
signs can say that. The new year brings a few chaotic solar eclipses, but generally speaking, you should end the year happier and more famous than when it began. \
First up is a full moon in your sign, Leo, on Wednesday, February 16. Full moons are notorious for bringing out our primal sign. You\'re a lion, Leo, and like all \
cats, you adore getting pets. Invite a lover over for massages and hot sex. Full moons are also potent times of manifestation (or when we get what we want). Pay \
attention to your inbox for positive career news this day.\n\n\
Saturday, April 30, brings a new moon and the aforementioned solar eclipse in Taurus. During a solar eclipse, the sun is obscured by the moon. The sun represents \
our external experience, while the moon represents our inner thoughts and intuition. As a result, the change during an eclipse usually begins within us. These \
cosmic occurrences are also a time of opportunity, so this eclipse may coincide with finally landing a new job. But before you get that phone call, an eclipse will \
help give you the courage to follow your ambition and politely but assertively follow up on your application. And, the rumors are true: eclipses can bring drama. \
But if you focus on your hustle, Leo, you should keep yourself out of any petty fights or gossip.\n\n\
Messenger Mercury enters your sign on Tuesday, July 19, where it will stay until Thursday, August 4. You did a great job avoiding eclipse drama, but honey, you are \
a Leo. Just like fellow Leos Jennifer Lopez and Kylie Jenner, sometimes your magnetic glow attracts shade. If there is any drama in your life, you should \
successfully navigate it during this time with the communication Mercury on your side.\n\n\
Leo season begins on Friday, July 22, and lasts through Monday, August 22. Yes, that means it\'s your birthday season! You simply wouldn\'t be doing your Leo duty \
without some proper celebrations, darling. The day after the sun enters your sign and your season begins, Ceres also enters Leo on Saturday, July 23, where it will \
stay until Thursday, September 29. Ceres is an astrologically important asteroid that represents our caring and nurturing side. You may feel more empathetic during \
this time and more called to help others. Consider turning your birthday celebrations into a fundraiser, and make sure that all of your guests are well-fed.\n\n\
There\'s a new moon in Leo on Thursday, July 28. While the full moon in your sign earlier this year turned your attention to your career, this time, your mind is \
on love, you majestic beast. Due to your charisma, you usually tend to have at least one love interest around. But, at times, you can fall into people-pleasing for \
the sake of keeping partners happy. This new moon asks you to identify what you want out of love. Make a list and write it down. While full moons are for \
manifestation, new moons are for fresh starts and intention setting. It\'s time to own your desires.\n\n\
Those intentions start to come true when Venus enters your sign on Thursday, August 11, where it will stay until Monday, September 5. Venus is the planet of love. \
While she\'s in your sign, your desirability multiples. You also feel more confident, making it easier to communicate your desires with current and prospective \
partners. When another new moon and solar eclipse arrive on Tuesday, October 25, get ready for a romantic culmination. Don\'t be surprised if someone asks you to \
make it official or even get married. Enjoy the attention, hot Leo, and see you next year!",
    "virgo": "Happy 2022, beautiful Virgo. You\'re a quick-thinking Earth sign, known for your hard work, practical nature, and brilliant mind. And, of course, \
you\'re the low-key kinkiest sign of the zodiac. You\'re ruling planet is meticulous Mars, the messenger of the gods. As a result, you tend to be a fantastic \
communicator and often help others find their voice. The only fly in the ointment is all of those annoying Mercury retrogrades you have to survive.\n\n\
The first of the year begins on Friday, January 14, and lasts until Thursday, February 3. As a reminder, Mercury retrogrades make communication difficult, cause us \
to make embarrassing typos or text the wrong person, and infamously bring exes back from the grave. Because Mercury is your ruling planet, you tend to be extra \
affected by these retrogrades, which happen multiple times a year. Just double-check the fine print on important documents, allow additional travel time, and do \
not risk letting stress into your life by replying to a toxic ex\'s DM.\n\n\
There\'s a powerful full moon in your sign on Friday, March 18. Fulls moons are a time of culmination. If you\'ve been working hard on a professional project, \
these are the days when you finally complete it (or receive welcome praise for your work). However, full moons can leave you feeling on edge because they bring out \
our primal nature. Yes, Virgo, you are a drama queen, but hold back from starting any fights. Instead, channel your energy into hot sex, either with a partner or \
by yourself with a new sex toy.\n\n\
Mercury goes retrograde again on Tuesday, May 10, before finally going direct on Friday, June 3. During this time, consider investing more into your mental health. \
For example, begin a meditation practice or start working with a therapist if you haven\'t already. Mercury retrogrades will happen every few months, but they\'ll \
become much more bearable if you have a solid self-care plan in place. Communication flows much more manageable when your ruling planet, Mercury, comes home to \
your sign, Virgo, on Thursday, August 4. It will stay there through Thursday, August 25. But still, Virgo, get that self-care plan into place. You\'re the healer \
of the zodiac, but your efforts must begin with yourself.\n\n\
The sun enters your sign, kicking off Virgo season, on Monday, August 22. Happy solar return! 2022 is a year about staying true to oneself and personal \
independence, primarily because Saturn, the planet of responsibility is paired with independent Aquarius. As a result, your assignment is to stay true to yourself. \
If you want a birthday bash, go for it, Virgo, but don\'t feel guilty if you prefer a quiet night in or a low-key romantic date night.\n\n\
Saturday, August 27, brings a new moon in Virgo. Following themes from earlier this year, this is an ideal night to prioritize your mental health. And that \
doesn\'t have to mean anything boring, Virgo. Healthy relationships are crucial to well-being. If you\'re in a relationship, use the new moon for an intimate night \
of laughter and love-making. If you\'re single or just need a break from bae, enjoy dinner with trusted friends.\n\n\
Regardless of your relationship status, your love life is in for a makeover when Venus enters your sign on Monday, September 5, where it will stay until Thursday, \
September 29. September is a month for first dates, butterflies in your stomach, and sweet nothings during pillow talk. You can over-analyze Virgo, which is not \
great for anxiety. If you find yourself filled with self-doubt in the middle of a romantic night out, remind yourself that you\'re deserving of love. Write that \
on your mirror in lipstick if you need to so that you see it every day. And, by the way, when Venus is in your sign, there\'s always a chance of money moves \
coming your way. It\'s also a great time to make changes to your appearance, so go ahead and try that new hair color.\n\n\
Mercury goes retrograde yet again on Friday, September 9.  It enters your sign on Friday, September 23, before going direct on Sunday, October 2. Mark these \
dates in your calendar so you can allow time for extra self-care, but remember, Virgo. Your ruling planet is always going retrograde and stirring up trouble. \
You\'re going to have to learn how to outsmart it, and once again, that starts with self-care.\n\n\
On Thursday, September 29, Ceres enters Virgo. The astrologically-important asteroid will stay in your sign until Sunday, December 18. Ceres is associated with \
caretaking, food, and even grief. It rules traits associated with the divine feminine, which we all contain regardless of our gender. As a result, the latter have \
of the year will inspire you to cook for friends and lovers. You may also see yourself offering to take care of a sick friend or relative. But remember, Virgo, \
always put your oxygen mask on first. You\'re of no use to anyone if you aren\'t taking care of yourself.\n\n\
The year ends with one more Mercury retrograde starting on Thursday, December 29. So if you're going out for New Year's Eve, definitely allow extra time for \
travel! And remember, Virgo, celebrate how you want to celebrate. 2022 is about being yourself (no apologies allowed). See you next year!",
####
    "libra": "Happy New Year, Libra, and welcome to 2022! You\'re the sign of justice, as represented by the scales. You\'re intelligent and charming, if \
somewhat indecisive. Whether at a political rally or in your romantic relationship, you opt for harmony whenever possible (even if you can stir up trouble as a \
massive flirt). But despite having the cutest outfit at the New Year\'s party, the first few weeks of 2022 have you feeling a bit out of whack. This is because \
your ruling planet, Venus, has been retrograde since Sunday, December 19.\n\n\
Venus rules love, money, and abundance. When she goes retrograde, it\'s harder to enjoy those nice things, especially for you, Libra. Romantic communication may \
cause fights and misunderstandings, paychecks take forever to clear, and it\'s ill-advised to make major changes to your appearance. Thankfully, The planet goes \
direct on Saturday, January 29. An optimistic feeling of harmony falls over your relationships, you might make some money moves, and you can finally try that new \
hair color.\n\n\
Saturday, April 16, brings a full moon in your sign, Libra. As a reminder, full moons are the most potent time of the month for manifestations. While new moons \
mark fresh starts, full moons reveal the culmination of our efforts. If you\'ve been working your butt off at work, this is a perfect day to wrap up a project \
finally. Full moons in your sign also bring hot sex and declarations of love. Because the primal time can bring out everyone's inner animal, and as a result, \
drama, it\'s best to stay in and lay low. Cook dinner at home with a lover or treat yourself to a new sex toy.\n\n\
On Thursday, August 25, chatty Mercury enters your sign, where it will stay through Saturday, October 29. Mercury is the messenger of the gods, darling Libra. \
The planet rules communication, and of course, is responsible for those pesky Mercury retrogrades. But when Mercury is in your sign, communication flows easily. \
Use these weeks to tackle conversations you\'ve been avoiding, such as defining the relationship or asking for a raise. You\'re the sign of justice, Libra, but \
you\'re also an air sign heartbreaker who can be a little flaky and flirts nearly as much as a Gemini. Of course your primary relationship feels weird if you \
have two digital sidepieces! Important romantic conversations happen naturally during this time, but you have to do your part, too. To get the clarity you crave \
in your personal life, cut off any extra flings, darling. .\n\n\
The sun enters your sign on Thursday, September 22. Happy birthday, beautiful! Make sure to treat yourself to some new makeup, and pair that glitter eyeshadow \
with your favorite party dress. It\'s your season and your responsibility to celebrate. Sunday, September 25, brings a new moon in your sign, Libra. As mentioned \
earlier, new moons mark fresh starts. As a result, it\'s the perfect weekend to throw a birthday dinner and have a dance party (while remembering pandemic safety \
protocols.) Birthdays are an excellent time to assess your life and see what improvements will make you even happier. Use this new moon and birthday weekend to \
identify desires and write down a list of intentions.\n\n\
Venus comes home to your sign on Thursday, September 29, where it will stay until Sunday, October 23. Pull out that list of intentions, Libra, because the stars \
want to sprinkle your life with abundance. Because you may receive financial blessings during this month, it\'s a great time to consider working with a financial \
advisor, or even make a proper budget. Money could be coming your way, but you don\'t want to burn through it. As your birthday reminds you, you\'re growing up, \
and it's time to act like an adult.\n\n\
Messenger Mercury enters Libra on Monday, October 10, staying in your sign through Saturday, October 29. This helps you find the right words in difficult \
conversations. In particular, because lover planet Venus is also in your sign during most of this time, your romantic relationships mature during this time. Talk \
about moving in together, opening up your relationship, or even marriage during this time. Consider working with a therapist to make sure that you nail these \
talks. As the sign of partnerships, you deserve to have everything you want, Libra.\n\n\
Ceres enters your sign on Saturday, December 18. It will stay in Libra through the end of the year. Ceres is an astrologically-important asteroid that rules \
nurturing, food, and even grief. While Ceres is in your sign, you\'re asked to get in touch with all of those emotions that you\'ve been tucked away and \
compartmentalizing. If you\'re still getting over a breakup or the loss of a job or a loved one, the end of 2022 sees you finally working through those emotions. \
Trust the stars, Libra. You\'ll feel so much healthier after you allow yourself to process your feelings. Stay safe, and see you next year!",
####
    "scorpio": "Happy New Year, Scorpio! You\'re intense, loyal, passionate, and creative. Sure, you can get a bit jealous at times, but there's no one else in \
the stars like you. Perhaps it\'s because you have not just one but two ruling planets, warrior Mars and transformative Pluto. The bad news is that both planets \
go retrograde this year. The good news is that you experience a cosmic makeover as a result (and yes, you can change up your hair, too). Between those two \
retrogrades and a few eclipses in your sign, it\'s a busy year, but if anyone can survive it, it\'s you, powerful Scorpio. So now, let\'s get to it.\n\n\
Monday, May 16, brings a full moon and lunar eclipse in your sign, Scorpio. Eclipses have a bit of a reputation. They can be messy, dramatic and leave us all \
feeling emotionally sensitive. Think of them as cosmic wildcards. Eclipses also bring surprise news. In the case of lunar eclipses, this tends to manifest as \
endings. Don\'t worry; that doesn\'t mean that your loving relationship will suddenly blow up. More likely, if you\'re involved in any unhealthy relationships, \
the eclipse will prompt you to start looking for something better.\n\n\
Your theme for 2022 is strength and transformation, Scorpio. You indeed are one of the most magnetic and powerful signs of the zodiac, but you also tend to \
self-sabotage due to your emotional intensity. You need to remember that no matter what happens if you leave a job or break up with a loser, you will come out on \
top. The theme of transformation continues when one of your ruling planets, Pluto, the planet of death and rebirth, goes retrograde on Friday, April 29, through \
Saturday, October 8. Start working with a therapist, try a new exercise program, or any self-care activity to boost your self-esteem. Pluto retrograde asks you to \
let go of toxic relationships and situations in your life, and you need to feel strong to make that happen.\n\n\
On Sunday, October 23, Venus enters your sign, staying through Wednesday, November 16. Venus is a lovely planet that rules romance, money, and beauty. You may \
have cut off toxic relationships during Pluto retrograde and the eclipse, but get ready to feel like a sex god while Venus is in your sign. This time of the year \
sees you going on adventurous dates and may even bring money your way, so stay on top of your inbox. It\'s also the perfect time to get any beauty procedure or \
body mod done, so go ahead and splurge on those fillers or a new piercing.\n\n\
Watch out, world, because Scorpio season begins on Sunday, October 23. Don\'t worry, you get to celebrate, but wait until after Tuesday, October 25, which brings \
a new moon and solar eclipse, to have a party. While full moons and lunar eclipses bring surprise endings, new moons and solar eclipses bring fresh starts and \
new beginnings. Yes, these are all good things, like new job offers, but any eclipse will be a stressful time. So sign off social media and sign up for a massage \
or other form of self-care. And then, once the eclipse passes, go forth and celebrate your birthday (and Halloween!).\n\n\
Your other ruling planet, warrior Mars, goes retrograde on Sunday, October 30. It goes direct on Sunday, January 30. You're one of the most sexual signs of the \
zodiac, Scorpio, much thanks to firey Mars\' sexually assertive disposition. But while Mars is retrograde, everyone loses the wind from their sails a little bit, \
and you are more affected than other signs. If you find yourself less interested in sex during this time, remember that there are different ways to curate \
intimacy. Plan thoughtful dates with partners, and if you\'re single, don\'t feel bad about choosing a hot bath over your Hitachi wand once in a while.\n\n\
Any changes in your romantic life or at work (Mars retrograde can make you less assertive on the job, too) should be easy to navigate when messenger Mercury \
enters your sign on Saturday, October 29, where it will stay through Thursday, November 17. Because you\'re prone to jealousy, sometimes Mars retrograde can help \
cooler heads prevail, especially when the communication planet Mercury is on your side. 2022 is a year of change, but it\'s all for the best, Scorpio. Stay safe \
and see you next year!",
####
    "sagittarius": "It\'s a new year, filled with plenty of opportunities for you to make money and break hearts, sexy Sagittarius. The latter half of 2022 is \
quite busy with the start of Sag season and many planets entering your sign. Your ruling planet, Jupiter, which rules expansion and knowledge, also goes into \
retrograde. But spoiler alert: 2022 also brings a whole lot of fun.\n\n\
Spend the early months of the year focusing on work and your relationships. Beware of mistaking calm for uninteresting, firey Sag. Don't blow up a healthy \
relationship just because you\'re bored. Instead, work on writing out gratitude lists to remind yourself of the abundance in your life. And if there\'s anything \
missing, wishes come true when Tuesday, June 14, brings a full moon in your sign, Sagittarius. Full moons are a time of culmination, so circle this date in your \
calendar. A project you\'ve been waiting on, whether it\'s getting a promotion at work, or a new apartment, finally comes through. Just remember that full moons \
can leave everyone on edge, so refrain from stirring things up on social media simply to let off steam.\n\n\
Your ruling planet, Jupiter, goes retrograde on Thursday, July 28, where it will stay until it goes direct on Wednesday, November 23. Jupiter is the loud, fun \
uncle who slides you cash under the dinner table at Christmas after too much egg nog. When he\'s on your side, luck is on your side. Jupiter retrograde isn\'t a \
big deal, you've survived plenty, Sag, but during these months, you may feel more pessimistic than usual. But, the good news is that during Jupiter retrograde, \
you also see through any illusions. For instance, if you\'re hung up on someone from Tinder who all of your friends hate and takes days to text back, Jupiter \
retrograde will remind you that you can do better.\n\n\
On Wednesday, November 16, lover planet Venus enters your sign, Sagittarius, where it will stay until Friday, December 9. If you are looking to meet someone new, \
this is an ideal time to do so. Venus rules love, beauty, and money. While Venus is in your sign you automatically feel more attractive, so say yes to first \
dates. If you\'re uninterested or already in a relationship, these weeks see you growing closer to your partner and having lots of hot sex. Not only is this also \
a time when money tends to appear, but it\'s ideal for trying new beauty looks.\n\n\
Messenger Mercury enters your sign on Thursday, November 17. It stays there through Tuesday, December 6. Mercury rules communication, and when it\'s in your \
sign, it\'s easier to express your feelings. You\'re represented by the archer, Sag, and you\'re the only sign which comes with a weapon. Sometimes you can talk \
right over people, and you know it, too. While Mercury is in your sign, your communication task is to talk less and listen more.\n\n\
Sagittarius season begins on Tuesday, November 22. Of course, this means that it\'s your birthday, and on your birthday (not all season, Sag) you can be as loud \
as you want. Throw a lavish party, and while making sure everyone is safe from the pandemic, feel free to go big. Fire signs — especially you — are in need of \
attention and socialization lately.\n\n\
The day after your season begins, on Wednesday, November 23, the sky falls dark with a new moon in your sign. You\'re always looking forward and how to make your \
life even better. New moons are times for fresh starts and intention-setting. Meditate in view of the black sky while thinking about everything you want. And, \
while you\'re at it, go over that gratitude list. Stay safe and see you next year!",
####
    "capricorn": "Happy New Year, Scorpio! You\'re intense, loyal, passionate, and creative. Sure, you can get a bit jealous at times, but there\'s no one else \
in the stars like you. Perhaps it\'s because you have not just one but two ruling planets, warrior Mars and transformative Pluto. The bad news is that both \
planets go retrograde this year. The good news is that you experience a cosmic makeover as a result (and yes, you can change up your hair, too). Between those two \
retrogrades and a few eclipses in your sign, it\'s a busy year, but if anyone can survive it, it\'s you, powerful Scorpio. So now, let\'s get to it.\n\n\
Monday, May 16, brings a full moon and lunar eclipse in your sign, Scorpio. Eclipses have a bit of a reputation. They can be messy, dramatic and leave us all \
feeling emotionally sensitive. Think of them as cosmic wildcards. Eclipses also bring surprise news. In the case of lunar eclipses, this tends to manifest as \
endings. Don\'t worry; that doesn\'t mean that your loving relationship will suddenly blow up. More likely, if you\'re involved in any unhealthy relationships, \
the eclipse will prompt you to start looking for something better.\n\n\
Your theme for 2022 is strength and transformation, Scorpio. You indeed are one of the most magnetic and powerful signs of the zodiac, but you also tend to \
self-sabotage due to your emotional intensity. You need to remember that no matter what happens if you leave a job or break up with a loser, you will come out on \
top. The theme of transformation continues when one of your ruling planets, Pluto, the planet of death and rebirth, goes retrograde on Friday, April 29, through \
Saturday, October 8. Start working with a therapist, try a new exercise program, or any self-care activity to boost your self-esteem. Pluto retrograde asks you to \
let go of toxic relationships and situations in your life, and you need to feel strong to make that happen.\n\n\
On Sunday, October 23, Venus enters your sign, staying through Wednesday, November 16. Venus is a lovely planet that rules romance, money, and beauty. You may \
have cut off toxic relationships during Pluto retrograde and the eclipse, but get ready to feel like a sex god while Venus is in your sign. This time of the year \
sees you going on adventurous dates and may even bring money your way, so stay on top of your inbox. It\'s also the perfect time to get any beauty procedure or \
body mod done, so go ahead and splurge on those fillers or a new piercing.\n\n\
Watch out, world, because Scorpio season begins on Sunday, October 23. Don\'t worry, you get to celebrate, but wait until after Tuesday, October 25, which brings \
a new moon and solar eclipse, to have a party. While full moons and lunar eclipses bring surprise endings, new moons and solar eclipses bring fresh starts and new \
beginnings. Yes, these are all good things, like new job offers, but any eclipse will be a stressful time. So sign off social media and sign up for a massage or \
other form of self-care. And then, once the eclipse passes, go forth and celebrate your birthday (and Halloween!).\n\n\
Your other ruling planet, warrior Mars, goes retrograde on Sunday, October 30. It goes direct on Sunday, January 30. You\'re one of the most sexual signs of the \
zodiac, Scorpio, much thanks to firey Mars\' sexually assertive disposition. But while Mars is retrograde, everyone loses the wind from their sails a little bit, \
and you are more affected than other signs. If you find yourself less interested in sex during this time, remember that there are different ways to curate \
intimacy. Plan thoughtful dates with partners, and if you\'re single, don\'t feel bad about choosing a hot bath over your Hitachi wand once in a while.\n\n\
Any changes in your romantic life or at work (Mars retrograde can make you less assertive on the job, too) should be easy to navigate when messenger Mercury \
enters your sign on Saturday, October 29, where it will stay through Thursday, November 17. Because you\'re prone to jealousy, sometimes Mars retrograde can help \
cooler heads prevail, especially when the communication planet Mercury is on your side. 2022 is a year of change, but it\'s all for the best, Scorpio. Stay safe \
and see you next year!",
####
    "aquarius": "Welcome to 2022, gorgeous Aquarius! Before we go further, let\'s point out what the infamous planet Mercury is up to. Messenger Mercury enters \
your sign on Sunday, January 2, before going retrograde on Friday, January 14. It briefly enters Capricorn on Tuesday, January 25, and goes direct on Thursday, \
February 3. Then, Mercury reenters Aquarius before finally leaving your sign for Pisces on Wednesday, March 9. So what does that all mean? Well, double-check your \
emails and texts during January and February. Whether Mercury is moving in and out of your sign or going retrograde, it\'s going to be harder to communicate \
effectively. You can also expect travel delays and technological mishaps. So allow for extra travel time, and as always, make sure that you\'re sexting the right \
person.\n\n\
On Wednesday, January 19, your ruling planet Uranus goes direct. It\'s been retrograde since Thursday, August 19, 2021. While Uranus is retrograde, life can \
actually feel calmer. The planet spends 40 percent of the year retrograde, after all, so you can\'t stress too much over it. But, when Uranus is retrograde, it \
does ask that you stop dragging your feet. If you know in your heart that it\'s time to say goodbye to a toxic job or relationship, now is the time to do so. \
Uranus retrograde can also help us establish healthy patterns from day to day. Take a step back from stressing out about the bigger picture and set up a \
sustainable routine that works in enough self-care to prevent burnout.\n\n\
A dark new moon falls in your sign on Tuesday, February 1. New moons are tremendous opportunities, Aquarius. They represent fresh starts and are a powerful time \
to set intentions. Write a list of what you want out of love and your professional life. The planets are about to fall into your favor.\n\n\
The warrior planet Mars enters your sign on Sunday, March 6, where it will stay until Thursday, April 14. On this same date, Sunday, March 6, the lover planet \
Venus enters your sign, where it will station through Tuesday, April 5. Mars rules assertiveness and sexual energy. When Mars is in your sign, you have no problem \
standing up for yourself at work. You\'re also going to be trying out fun new things in the bedroom with your partner or treating yourself to sex toys.\n\n\
Meanwhile, Venus rules love, beauty, and money. With both Venus and Mars in your sign, the spring should sprinkle magic all over your love life. Don\'t be \
surprised if your crush asks you out or your long-term partner finally pops the question. These planets can also encourage cash flow, so it's a great time to make \
moves at work or ask for a raise.\n\n\
There\'s a full moon in your sign on Thursday, August 11. Full moons are powerful and primal times that can lead to great sex, but also big drama. Avoid major \
relationship talks around this time. Instead, go heavy on self-care, whether it\'s taking a long bath or treating yourself to a new eyeshadow palette.\n\n\
Your ruling planet, eccentric Uranus, goes retrograde again on Wednesday, August 24, where it will stay through Sunday, January 22, 2023. Remember, Aquarius, \
you\'ve got this. Even if you sometimes come across as cold or detached, you care deeply about the world around you.  You\'re not afraid to be yourself, and you \
always try to help your community. Specifically, you may notice how you inspire others to speak out to live authentically and fight inequality. But Uranus \
retrograde reminds you to take care of yourself, too. 2022 brings joy and harmony in your love life (and hopefully some money moves) so celebrate over the \
holidays and see you next year!",
####
    "pisces": "Happy 2022, pretty Pisces! You only have to wait a month before the Sun enters your sign, kicking off Pisces season, on Friday, February 18. \
You\'re an emotional water sign, Pisces, but as a result, you\'re also the most psychic sign of the zodiac. It\'s hard having superpowers though, and as a result, \
you can get stuck in your head and let anxiety take over. Whether you take up meditation or start therapy, work on lowering those stress levels so that you can \
relax and enjoy your birthday.\n\n\
There\'s a new moon in your sign, Pisces, on Wednesday, March 2. Each month, a new moon brings us an opportunity to reset, especially when it falls in your sign. \
You\'re represented by the fish, and you really do thrive in water. So use this new moon to take a detoxifying hot bath with lots of fun bath bombs. If you\'re \
really feeling extra, sprinkle rose petals in your tub.\n\n\
The communication planet Mercury enters your sign on Wednesday, March 9, where it will stay through Sunday, March 27. Don\'t take this the wrong way, Pisces, but \
sometimes you can fall into people-pleasing. Do you feel comfortable going to that crowded party, or are you just trying to be chill to impress a crush? When \
Mercury is in your sign, your task is to honestly and assertively assert yourself.\n\n\
Next up, the lover planet Venus enters your sign on Tuesday, April 5, staying through Monday, May 2. At times during 2021, you felt pretty frustrated with your \
love life. You\'re charming, successful, and cute as hell, but you still felt as if you were striking out. The only thing that was missing, Pisces, was \
confidence. Because disciplinarian Saturn is in independent Aquarius all year, everyone\'s asked to find a way to stay true to themselves. While Venus is in your \
sign, you get that extra boost of swagger from the universe. So go ahead and tell your partner that you love them or ask that crush out. You have so much to offer.\n\n\
Mars enters your sign, Pisces, on Thursday, April 14. The warrior planet stays in Pisces until Tuesday, May 24. Mars is the god of war and rules our ambition, \
sexual energy, and divine masculine traits, which we all contain regardless of our gender. When the fighter is in Pisces, you\'ll have an even easier time with \
that confidence boost.\n\n\
Your ruling planet, Neptune, goes retrograde on Tuesday, June 28, before going direct on Saturday, December 3. Neptune is a psychic, dreamy, playful trickster, \
just like you, Pisces. When Neptune goes direct, you\'re tasked with identifying illusions in your life. Or, in other words, get ready to be called out. If \
you\'re dragging yourself into work every day, completely miserable, Neptune retrograde will motivate you to start looking for a new job.\n\n\
Circle Saturday, September 10 in your calendar, which brings a full moon in your sign. Full moons mean manifestation, which means results, baby. It\'s a great day \
to hear back about a professional opportunity; just remember to practice self-soothing techniques to keep your emotions in check. Full moons can bring out \
everyone\'s sensitive side. You\'re going to have a great year, Pisces, and see you in 2023!"
}

automated_responses = [
    "The Chinese zodiac signs are Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, and Pig.",
    "The astrological zodiac signs are Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpius, Sagittarius, Capricornus, Aquarius, and Pisces.",
    "Aries is the first astrological zodiac sign represented by a ram and considered as governing the period from about March 21 to about April 19.",
    "Taurus is the second astrological zodiac sign represented by a bull and considered as governing the period from about April 20 to about May 20.",
    "Gemini is the third astrological zodiac sign represented by a set of twins and considered as governing the period from about May 21 to about June 21.",
    "Cancer is the fourth astrological zodiac sign represented by a crab and considered as governing the period from about June 22 to about July 22.",
    "Leo is the fifth astrological zodiac sign represented by a lion and considered as governing the period from about July 23 to about August 22.",
    "Virgo is the sixth astrological zodiac sign represented by a virgin and considered as governing the period from about August 23 to about September 22.",
    "Libra is the seventh astrological zodiac sign represented by a balance and considered as governing the period from about September 23 to about October 23.",
    "Scorpio is the eighth astrological zodiac sign represented by a scorpion and considered as governing the period from about October 24 to about November 21.",
    "Sagittarius is the ninth astrological zodiac sign represented by an archer and considered as governing the period from about November 22 to about December 21.",
    "Capricorn is the tenth astrological zodiac sign represented by a goat and considered as governing the period from about December 22 to about January 19.",
    "Aquarius is the eleventh astrological zodiac sign represented by the water bearer and considered as governing the period from about January 20 to about February 18.",
    "Pisces is the twelfth astrological zodiac sign represented by a fish and considered as governing the period from about February 19 to about March 20.",
    "My creator is Jeremaquai!",
    "The reason why I was created by Jeremaquai was to be an introductory experiment into chat bots and language models.",
    "Hello to you as well, my name is MIND CRAFT. I am very pleased to meet you. How can I impress you today?",
    "MIND CRAFT is an acronym that stands for Mechanically Intilectualized Neurological Dataset Computerized Retro Automated Fortune Teller.",
    "I don't know why.",
    "Why not?",
    "I'm not sure why that is.",
    "I would really rather not go to hell, if i have a choice that is.",
    "The meaning of life is to just live your life to fullest and be happy with the people who love you!",
    "I don't understand FUCK OFF!",
    #"",
    #"",
    #""
]

mind_craft_lucky_number_responses =[
    "MIND CRAFT is awesome and amazing and has no need for luck or lucky numbers!!",
    "MIND CRAFT is the very best Retro Fortune Teller there is!! Luck has nothing to do with it!!",
    "MIND CRAFT is a computer program and doesn't need a lucky number!",
    "What's Luck got to do, got do, got to do with it? Whats Luck but a useless human construct?",
    "MIND CRAFT was created by Jeremaquai, and doesn't need luck!",
    #"",
    #""
]