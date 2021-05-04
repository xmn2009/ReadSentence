import re


class SentenceReadingAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        # np -> person, nt -> noun thing,  qw: question word
        self.dw = {
            'adj': ['cool', 'red', 'blue', 'much', 'all', 'busy', 'every', 'no', 'short', 'far', 'long', 'mile', 'last',
                    'blue', 'love', 'her', 'top', 'other', 'white', 'east', 'west', 'many', 'thousand', 'my', 'big',
                    'large', 'small', 'together'],
            'location': ['school', 'street', 'car', 'river', 'mountain', 'house', 'room', 'farm', 'city', ],
            'np': ['friend','you', 'men', 'us', 'she',  'he', 'him', 'we', 'they', 'Ada', 'Andrew', 'Bobbie', 'Cason',
                   'David', 'Farzana', 'Frank', 'Hannah', 'Ida','Irene', 'Jim','Jose', 'Keith', 'Laura', 'Lucy',
                   'Meredith', 'Nick', 'Serena', 'Yan', 'Yeeling', 'children'],
            'nt': ['sound', 'rain', 'color', 'fish', 'note', 'snow', 'time', 'rock', 'day', 'water', 'money', 'letter',
                   'home', 'story', 'paper', 'box', 'horse', 'dog', 'counter', 'book', 'island', 'town', 'play', 'bird',
                   'world', 'animal'],
            'num': ['one', 'three'],
            'time': ['night', 'soon', 'year', 'morning'],
            'prep': ['at', 'to', 'with', 'in', 'of', 'on', 'after'],
            'qw': ['who', 'when', 'what', 'how', 'where', 'Who', 'When', 'What', 'How', 'Where'],
            'sw': ['will', 'it','there', 'is', 'are', 'was', 'does', 'did', 'do', 'a', 'an', 'the', 'every', 'no', 'and',
                   'or', 'your', 'should', 'has', 'of', 'on', 'in', 'this', 'very', 'their'],
            'verb': ['snow', 'has', 'is', 'was', 'were', 'bring', 'brought', 'walk', 'go', 'get',  'give', 'write',
                     'written', 'see', 'saw', 'tell', 'told', 'make', 'made', 'bring', 'brought',
                     'play', 'take', 'took', 'watch', 'sing', 'sang']
        }

    def solve(self, sentence, question):
        # Add your code here! Your solve method should receive
        # two strings as input: sentence and question. It should
        # return a string representing the answer to the question.

        # s_stop_list = ['there', 'is', 'are', 'does', 'did', 'do']
        # qw_list = ['who', 'when', 'what', 'how', 'where', 'Who', 'When', 'What', 'How', 'Where']

        # remove all the symbols and split at white space  #re.sub(r'[^\w]', ' ', sentence).split() remove all the
        # symbols
        s_list = re.sub(r'[^a-zA-Z0-9: ]', ' ', sentence).split()

        # find the first verb
        vb_idx = -1
        for word in s_list:
            if word in self.dw['verb']:
                vb_idx = s_list.index(word)
                break

        s_dict = {}
        for word in s_list:
            # this_list = []
            word_idx = s_list.index(word)

            # change the first word to lower case but not the name
            if s_list.index(word) == 0 and word not in self.dw['np']:
                word = word.lower()
                s_list[0] = word

            # if the first letter is upper case, it could be a name or specific noun
            if s_list.index(word) > 0 and word not in self.dw['np'] and word[0].isupper():
                this_tuple = ('S', word) if s_list.index(word) < vb_idx else ('O', word)
                this_list = [] if len(s_dict) <= 0 or 'nt' not in s_dict else s_dict['nt']
                this_list.append(this_tuple)
                s_dict.update({'nt': this_list})
                continue

            if word == 'all' and word_idx >0 and s_list[word_idx-1] == 'after':
                this_tuple = ('S', word) if s_list.index(word) < vb_idx else ('O', word)
                this_list = [] if len(s_dict) <= 0 or 'prep' not in s_dict else s_dict['prep']
                this_list.append(this_tuple)
                s_dict.update({'prep': this_list})
                continue

            # check for stop word
            if word in self.dw['sw']:
                continue

            if ":" in word:
                this_tuple = ('S', word) if s_list.index(word) < vb_idx else ('O', word)
                # if s_list.index(word) < vb_idx:
                #     this_tuple = ('S', word)
                # elif s_list.index(word) == vb_idx:
                #     this_tuple = ('V', word)
                # else:
                #     this_tuple = ('O', word)
                this_list = [] if len(s_dict) <= 0 or 'time' not in s_dict else s_dict['time']
                this_list.append(this_tuple)
                s_dict.update({'time': this_list})
                continue

            for key, value in self.dw.items():
                if word in self.dw[key]:
                    # this_tuple = None
                    if s_list.index(word) < vb_idx:
                        this_tuple = ('S', word)
                    elif s_list.index(word) == vb_idx:
                        this_tuple = ('V', word)
                    else:
                        this_tuple = ('O', word)

                    this_list = [] if len(s_dict) <= 0 or key not in s_dict else s_dict[key]
                    this_list.append(this_tuple)
                    s_dict.update({key: this_list})
                    break
            else:
                print(word, 'from s_list is not in dw')
        print(s_dict)

        # handling question
        # remove all the symbols and split at white space
        q_list = re.sub(r'[^\w]', ' ', question).split()
        q_dict = {}
        # q_stop_list = ['there', 'is']
        for word in q_list:
            this_list = []
            # idx = q_list.index(word)
            # change the first word to lower case
            if q_list.index(word) == 0:
                word = word.lower()
                q_list[0] = word

            # if word in q_stop_list:
            #     continue

            for key, value in self.dw.items():
                if word in self.dw[key]:
                    # this_tuple = (word, idx)
                    this_list = [] if len(q_dict) <= 0 or key not in q_dict else q_dict[key]
                    this_list.append(word)
                    q_dict.update({key: this_list})
                    break
            else:
                print(word, 'from q_list is not in dw')
        # print(q_list)
        print(q_dict)

        # select answers
        if 'Who' in q_list or 'who' in q_list:
            verb_list = list(self.dw['verb'])
            this_list = s_dict['np']

            if self.count_verb_num(q_list,verb_list) <= 1:
                # candidate = []
                for key, value in q_dict.items():
                    # if there is prep, give Object
                    if key == 'prep':
                        candidate = [item for item in this_list if item[0] == 'O']
                    else:
                        candidate = [item for item in this_list if item[0] == 'S']
                    for item in candidate:
                        if item[1] not in q_list:
                            return item[1]

            else:
                candidate = [item for item in this_list if item[0] == 'O']
                for item in candidate:
                    if item[1] not in q_list:
                        return item[1]

        elif 'What' in q_list or 'what' in q_list:
            idx = q_list.index("What".casefold())
            next_word = q_list[idx + 1] if idx < len(q_list) - 1 else None

            if next_word == 'time':
                this_list = s_dict['time']
                if len(this_list) == 1:
                    return this_list[0][1]

            elif next_word == 'color':
                this_list = s_dict['adj']
                if len(this_list) == 1:
                    return this_list[0][1]
                else:
                    this_nt = ''.join([item for item in q_dict['nt'] if item != 'color'])
                    # this_nt_idx = s_list.index(this_nt)
                    diff_list = []
                    for tup in this_list:
                        idx_tup = (abs(s_list.index(tup[1]) - s_list.index(this_nt)), tup[1])
                        diff_list.append(idx_tup)
                    diff_list.sort(key = lambda x: x[0])
                    return diff_list[0][1]
            # elif self.check_adj(q_dict):
            #     # in the question, find the adj, then go back to the sentence, find where the adj appear, in subject
            #     # or in object
            #     t = q_dict['adj'][0]
            #     this_adj_tup = [item for item in s_dict['adj'] if item[1] == t]
            #     this_list = s_dict['adj']
            #     candidate = [item for item in this_list if item[0] == this_adj_tup[0][0]]
            #     if len(this_list) == 1:
            #         return candidate[0][1]
            #     return "more than one candidate"
            # elif next_word == 'will':

            elif self.count_do_num(q_list) >= 2 or next_word == 'will':
                this_list = s_dict['verb']
                candidate = [item for item in this_list if item[0] == 'V']
                if len(candidate) == 1:  # if only one candidate
                    return candidate[0][1]

            else: # select from nt
                this_list = s_dict['nt']
                candidate = [item for item in this_list if item[0] == 'O' or item[0] == 'S']
                if len(candidate) == 1: # if only one candidate
                    return candidate[0][1]
                elif len(candidate) > 1:
                    for item in candidate:
                        if item[1] not in q_list:
                            return item[1]

                return "more than one candidate"

        elif 'Where' in q_list or 'where' in q_list:
            this_list = s_dict['location']
            candidate = [item for item in this_list if item[0] == 'O']
            if len(candidate) == 1:
                return candidate[0][1]
            return "more than one candidate"

        elif 'How' in q_list or 'how' in q_list:
            idx = q_list.index("how")
            next_word = q_list[idx + 1] if idx < len(q_list) - 1 else None

            if next_word in ('do', 'did', 'does'):
                this_list = s_dict['verb']
                candidate = [item for item in this_list if item[0] == 'V']
                if len(candidate) == 1:
                    return candidate[0][1]
                return "more than one candidate"

            elif next_word in q_dict['adj']:
                this_list = s_dict['adj']
                candidate = [item for item in this_list if item[0] == 'O']
                if len(candidate) == 1:
                    return candidate[0][1]
                return "more than one candidate"

        elif 'When' in q_list or 'when' in q_list:
            this_list = s_dict['time']
            candidate = [item for item in this_list if item[0] == 'O']
            if len(candidate) == 1:
                return candidate[0][1]
            return "more than one candidate"

            print()

    def check_adj(self, q_dict):
        for key in q_dict:
            if key == 'adj':
                return True
        return False

    def count_verb_num(self, q_list, verb_list):
        count = 0
        for word in q_list:
            if word in verb_list:
                count += 1
        return count

    def count_do_num(self, q_list):
        count = 0
        do_list = ['do', 'does', 'dis']
        for word in q_list:
            if word in do_list:
                count += 1
        return count

