
exit_msg = "Thank you for your time, please have a wonderful day!  \n\
Remember! Only you can prevent forrest fires! \n\
Goodbye!"

help_response = \
    """
Help File
=========
Welcome to MIND CRAFT, an interactive chatbot based on a fortune teller concept. \
You just simply need to ask a question or make a statement to proceed and recieve a reply.

Some example questions:
Exit or Quit
-will terminate and exit the program
Can a get a fortune?
-will reply with a random fortune
I was born in \{year of birth\}.
-Will reply with the Chinese zodiac sign for your year of birth
My birthday is \{month day\}
-Will reply with your astrological zodiac sign
What is the \{astrological sign\} sign?
-Will reply with a general description of the zodiac sign inquired about

There are also a few hidden responses to questions as easter eggs so just have fun and play around with the MIND CRAFT experiment.

In the near future MIND CRAFT will be able to respond to almost any question or statement that you enter just as if you were talking to another person and holding a conversation hopefully!
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
    "Scorpius": ["october 24", "october 25", "october 26", "october 27", "october 28", "october 29", "october 30", "october 31", "november 1", "november 2", "november 3", \
        "november 4", "november 5", "november 6", "november 7", "november 8", "november 9", "november 10", "november 11", "november 12", "november 13", "november 14", \
        "november 15", "november 16", "november 17", "november 18", "november 19", "november 20", "november 21"],
    "Sagittarius": ["november 22", "november 23", "november 24", "november 25", "november 26", "november 27", "november 28", "november 29", "november 30", "december 1", \
        "december 2", "december 3", "december 4", "december 5", "december 6", "december 7", "december 8", "december 9", "december 10", "december 11", "december 12", \
        "december 13", "december 14", "december 15", "december 16", "december 17", "december 18", "december 19", "december 20", "december 21"],
    "Capricornus": ["december 22", "december 23", "december 24", "december 25", "december 26", "december 27", "december 28", "december 29", "december 30", "december 31", \
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
    "Scorpius is the eighth astrological zodiac sign represented by a scorpion and considered as governing the period from about October 24 to about November 21.",
    "Sagittarius is the ninth astrological zodiac sign represented by an archer and considered as governing the period from about November 22 to about December 21.",
    "Capricornus is the tenth astrological zodiac sign represented by a goat and considered as governing the period from about December 22 to about January 19.",
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