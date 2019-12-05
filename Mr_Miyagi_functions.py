mr_miyagi_response = {'sensei': 'you are smart, but not wise - address me as Sensei please',
                      'questionmark': 'questions are wise, but for now wax on, and wax off!',
                      'other': 'Do not lose focuse. Wax on. Wax off.',
                      'block': 'remember, best block, not to be there',
                      'dance': 'Never trust spiritual leader who cannot dance',
                      'goodbye': 'You are the chosen one:  I shall depart you with one gem of wisdom... sometimes, what heart know, head forget'
                      }


def question():
    return input('What is it you want my sweet child? ')

user_input = question().lower()
def game():
    if "sensei, i am at peace" in user_input:
        return 'goodbye'
    if "sensei" not in user_input:
        return 'sensei'
    if "?" in user_input:
        return 'questionmark'
    if "block" in user_input:
        return 'block'
    if "dance" in user_input:
        return 'dance'
    else:
        return 'other'

oper_end = False

def end():
    if "sensei, i am at peace" in user_input:
        return True


while oper_end != True:
    print(mr_miyagi_response[game()])
    oper_end = (end())
    if oper_end == True:
        continue
    question()

