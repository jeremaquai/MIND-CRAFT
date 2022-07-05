from responses import fortunes, going_to_die_responses, why_die_responses, feelings_responses, hello_responses, help_response, chinese_zodiac,\
    chinese_zodiac_response, your_feelings_responses, astrological_zodiac, astrological_zodiac_response, mind_craft_lucky_number_responses, \
    automated_responses, zodiac_sign_personality_profile_dict, july_2022_horoscopes_dic, yearly_2022_horoscope_dic 
import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess_text 

exit_commands = ("quit", "goodbye", "exit", "pause", "later", "see ya", "bye")
zodiac_signs = ("aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces")

mind_craft_babble = {
    "get_fortune_intent": r"(\w*\s)*(a fortune|my fortune).?",
    "get_going_to_die_intent": r"(\w*.?\s)*(going to die|will i die).?",
    "get_why_die_intent": r"^why\s(\w*\s)*die.?",
    "hello_intent": r"hello.*",
    "get_feelings_intent": r"how.*\w*you.*feel.*",
    "get_help_intent": r"(\w*\s)*help(\s\w*)*.?",
    "get_chinese_zodiac_intent": r"(\w*\s)*born\sin\s\d{4}.?|\d{4}(\w*\s)*year of birth.?",
    "get_lucky_number_intent": r"(\w*\s)*(give\sme\sa|i\shave\sa|get\sa|my|(I|i)\sneed\sa)\slucky\snumber.?(\w*.?)*",
    "get_your_feelings_intent": r"how\s(\w*\s)?i feel.{0,3}.?",
    "get_zodiac_sign_intent": r"my birthday is (\w*\s)*\d{1,2}.?",
    "get_mind_craft_lucky_number": r"(\w*\s)*(you\shave\sa|give\syou\sa|your|you\sneed\sa)\slucky\snumber.?(\w*.?)*",
    "get_sign_personality_profile_intent": r"(i'd)?(\w*\s)*personality profile\s(\w*.?\s)*",
    "get_monthly_horoscope_intent": r"(i'd)?(\w*\s)*monthly horoscope.?(\w*\s)*\w*.?",
    "get_yearly_horoscope_intent": r"(i'd)?(\w*\s)*yearly horoscope.?(\w*\s)*\w*.?"
    
}


def make_exit(user_message):
    for command in exit_commands:
        if command in user_message:
            exit()
        
def match_intent(reply):
    reply = reply.lower()
    while not make_exit(reply):
        match_found = False
        for intent, regex_pattern in mind_craft_babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == "get_fortune_intent":
                match_found = True
                answer = get_fortune()
            elif found_match and intent == "get_going_to_die_intent":
                match_found = True
                answer = going_to_die()
            elif found_match and intent == "get_why_die_intent" :
                match_found = True
                answer = why_die()
            elif found_match and intent == "get_feelings_intent":
                match_found = True
                answer = get_feelings()
            elif found_match and intent == "get_help_intent":
                match_found = True
                answer = get_help()
            elif found_match and intent == "get_chinese_zodiac_intent":
                match_found = True
                answer = get_chinese_zodiac(reply)
            elif found_match and intent == "get_zodiac_sign_intent":
                match_found = True
                answer = get_astrological_zodiac(reply)
            elif found_match and intent == "get_your_feelings_intent":
                match_found = True
                answer = get_your_feelings()
            elif found_match and intent == "get_lucky_number_intent":
                match_found = True
                answer = get_lucky_number()
            elif found_match and intent == "get_mind_craft_lucky_number":
                match_found = True
                answer = get_mind_craft_lucky_number()
            elif found_match and intent == "get_sign_personality_profile_intent":
                match_found = True
                answer = get_zodiac_sign_personality_profile(reply)
            elif found_match and intent == "get_monthly_horoscope_intent":
                match_found = True
                answer = get_monthly_horoscope(reply)
            elif found_match and intent == "get_yearly_horoscope_intent":
                match_found = True
                answer = get_yearly_horoscope(reply)
        if match_found == False:
            answer = match_reply(reply)
        return answer

def match_reply(msg):
    documents = [doc for doc in automated_responses]
    documents.append(msg)
    #print(documents)
    # preprocess responses and user_message:
    processed_docs = [preprocess_text(document) for document in documents]
    # create tfidf vectorizer:
    vectorizer = TfidfVectorizer()
    # fit and transform vectorizer on processed docs:
    tfidf_vectors = vectorizer.fit_transform(processed_docs)
    # compute cosine similarity betweeen the user message tf-idf vector and the different response tf-idf vectors:
    cosine_similarities = cosine_similarity(tfidf_vectors[-1], tfidf_vectors)

    # get the index of the most similar response to the user message:
    similar_response_index = cosine_similarities.argsort()[0][-2]
    #print(similar_response_index)
    best_response = automated_responses[similar_response_index] 
    #print(best_response)
    return best_response + "\n"


def get_fortune():
    fortune = random.choice(fortunes)
    return fortune + "\n"

def going_to_die():
    response = random.choice(going_to_die_responses)
    return response + "\n"

def why_die():
    response = random.choice(why_die_responses)
    return response + "\n"

def get_hello():
    hello_msg = random.choice(hello_responses)
    return hello_msg + "\n"

def get_feelings():
    feelings_msg = random.choice(feelings_responses)
    return feelings_msg + "\n"

def get_help():
    return help_response + "\n"

def get_lucky_number():
    lucky_number = random.randint(1, 10000)
    if lucky_number == 666:
        response = f"You are the luckiest of the lucky!! Your lucky number is {lucky_number}!!"
    else:
        response = f"Your lucky number is {lucky_number}!"
    return response + "\n"

def get_mind_craft_lucky_number():
    response = random.choice(mind_craft_lucky_number_responses)
    return response + "\n"

def get_chinese_zodiac(msg):
    found_match = re.search(r"\d{4}", msg)
    user_birth_year = int(found_match.group(0))
    for zodiac_sign, years in chinese_zodiac.items():
        if user_birth_year in years:
            user_chinese_zodiac = zodiac_sign

    return chinese_zodiac_response.format(year=user_birth_year,zodiac=user_chinese_zodiac) + "\n"

def get_your_feelings():
    your_feelings_response = random.choice(your_feelings_responses)
    return your_feelings_response + "\n"

def get_astrological_zodiac(msg):
    birthday_regex_pattern = r"(january|february|march|april|may|june|july|august|september|october|november|december)\s\d{1,2}"
    found_match = re.search(birthday_regex_pattern, msg)
    user_birthday = found_match.group(0)
    for zodiac_sign, days in astrological_zodiac.items():
        if user_birthday in days:
            user_zodiac_sign = zodiac_sign
    return astrological_zodiac_response.format(birthday=user_birthday.title(), zodiac=user_zodiac_sign) + "\n"

def check_zodiac_sign(msg):
    for sign in zodiac_signs:
        if sign in msg:
            return True

def get_zodiac_sign_personality_profile(msg):
    while not check_zodiac_sign(msg):
        return "If you would like to get a personality profile for a sign you are going to need to include an astrological sign in your question or statement."
    while check_zodiac_sign(msg):
        for sign, profile in zodiac_sign_personality_profile_dict.items():
            #print(sign)
            if sign in msg:
                return profile

#print(get_zodiac_sign_profile("goop"))

def get_monthly_horoscope(msg):
    while not check_zodiac_sign(msg):
        return "If you would like to get a horoscope for a sign you are going to need to include an astrological sign in your question or statement."
    while check_zodiac_sign(msg):
        for sign, horoscope in july_2022_horoscopes_dic.items():
            if sign in msg:
                return horoscope

def get_yearly_horoscope(msg):
    while not check_zodiac_sign(msg):
        return "If you would like to get a horoscope for a sign you are going to need to include an astrological sign in your question or statement."
    while check_zodiac_sign(msg):
        for sign, horoscope in yearly_2022_horoscope_dic.items():
            if sign in msg:
                return horoscope
