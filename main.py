from SentenceReadingAgent import SentenceReadingAgent
import time


def test():
    # This will test your SentenceReadingAgent
    # with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    print(test_agent.solve(sentence_1, question_1), ' |', time.perf_counter(), 's')  # "Ada"
    # print(test_agent.solve(sentence_1, question_2), ' |', time.perf_counter(), 's')  # "note" or "a note"
    # print(test_agent.solve(sentence_1, question_3), ' |', time.perf_counter(), 's')  # "Irene"
    # print(test_agent.solve(sentence_1, question_4), ' |', time.perf_counter(), 's')  # "short"

    # print(test_agent.solve(sentence_2, question_5), ' |', time.perf_counter(), 's')  # "David"
    # print(test_agent.solve(sentence_2, question_6), ' |', time.perf_counter(), 's')  # "school"
    # print(test_agent.solve(sentence_2, question_7), ' |', time.perf_counter(), 's')  # "mile" or "a mile"
    # print(test_agent.solve(sentence_2, question_8), ' |', time.perf_counter(), 's')  # "walk"
    # print(test_agent.solve(sentence_2, question_9), ' |', time.perf_counter(), 's')  # "8:00AM"

    sentence_3 = 'Frank was busy last night.'
    question_31 = 'Who was busy last night?'
    question_32 = 'When was Frank busy?'
    # print(test_agent.solve(sentence_3, question_31))
    # print(test_agent.solve(sentence_3, question_32))

    sentence_4 = 'Serena and Ada took the blue rock to the street.'
    question_41 = 'Who was with Serena?'
    # print(test_agent.solve(sentence_4, question_41))

    sentence_5 = 'The water is blue.'
    question_51 = 'What is blue?'
    # print(test_agent.solve(sentence_5, question_51))

    sentence_6 = 'There are three men in the car.'
    question_61 = 'Where are the men?'
    # print(test_agent.solve(sentence_6, question_61))

    sentence_7 = 'Give us all your money.'
    question_71 = 'How much of your money should you give us?'
    question_72 = 'Who should you give your money to?'
    # print(test_agent.solve(sentence_7, question_71))
    # print(test_agent.solve(sentence_7, question_72))

    sentence_8 = 'The red fish is in the river.'
    question_81 = 'What color is the fish?'
    # print(test_agent.solve(sentence_8, question_81))

    sentence_9 = 'The sound of rain is cool.'
    question_91 = 'What has a cool sound?'
    question_92 = 'What is cool?'
    # print(test_agent.solve(sentence_9, question_91))  # rain
    # print(test_agent.solve(sentence_9, question_92))  # sound

    sentence_10 = 'It will snow soon.'
    sentence_101 = 'When will it snow?'
    # print(test_agent.solve(sentence_10, sentence_101))

    sentence_11 = 'She will write him a love letter.'
    question_111 = 'Who was written a love letter?'
    # print(test_agent.solve(sentence_11, question_111))

    sentence_12 = 'Serena saw a home last night with her friend.'
    question_121 = 'What did they see?'
    # print(test_agent.solve(sentence_12, question_121))

    sentence_13 = 'She told her friend a story.'
    question_131 = 'Who was told a story?'
    # print(test_agent.solve(sentence_13, question_131))

    sentence_14 = 'There is snow at the top of the mountain.'
    question_141 = 'Where is the snow?'
    question_142 = 'What is on top of the mountain?'
    # print(test_agent.solve(sentence_14, question_141))
    # print(test_agent.solve(sentence_14, question_142))

    sentence_15 = 'The house is made of paper.'
    question_151 = 'What is the house made of?'
    # print(test_agent.solve(sentence_15, question_151))

    sentence_16 = 'Bring the box to the other room.'
    question_161 = 'Where should the box go?'
    question_162 = 'What should be brought to the other room?'
    # print(test_agent.solve(sentence_16, question_161))
    # print(test_agent.solve(sentence_16, question_162))

    sentence_17 = 'The white dog and the blue horse play together.'
    question_171 = 'What do the dog and horse do?'
    question_172 = 'What animal is white?'
    question_173 = 'What animal is blue?'
    question_174 = 'What color is the dog?'
    question_175 = 'What color is the horse?'
    # print(test_agent.solve(sentence_17, question_171))
    # print(test_agent.solve(sentence_17, question_172))  # can't sovle this type with 2 nt words
    # print(test_agent.solve(sentence_17, question_173))
    # print(test_agent.solve(sentence_17, question_174 ))
    # print(test_agent.solve(sentence_17, question_175))

    sentence_18 = 'Frank took the horse to the farm.'
    question_181 = 'What did Frank take to the farm?'
    # print(test_agent.solve(sentence_18, question_181))

    sentence_19 = 'Bring the letter to the other room.'
    question_191 = 'Where should the letter go?'
    question_192 = 'What should be brought to the other room?'
    # print(test_agent.solve(sentence_19, question_191))
    # print(test_agent.solve(sentence_19, question_192))

    sentence_20 = 'Lucy will write a book.'
    question_201 = 'Who will write a book?'
    question_202 = 'What will Lucy do?'
    # print(test_agent.solve(sentence_20, question_201))
    # print(test_agent.solve(sentence_20, question_202))

    sentence_21 = 'The island is east of the city.'
    question_211 = 'What is east of the city?'
    question_212 = 'What is west of the island?'
    # print(test_agent.solve(sentence_21, question_211))  # can't sovle this type with 2 nt words
    # print(test_agent.solve(sentence_21, question_212))

    sentence_22 = 'There are a thousand children in this town.'
    question_211 = 'How many children are in this town?'
    question_212 = 'Who is in this town?'
    # print(test_agent.solve(sentence_22, question_211))
    # print(test_agent.solve(sentence_22, question_212))

    sentence_23 = 'This year David will watch a play.'
    question_231 = 'What will David watch?'
    # print(test_agent.solve(sentence_23, question_231))

    sentence_24 = 'My dog Red is very large.'
    question_241 = 'How big is Red?'
    # print(test_agent.solve(sentence_24, question_241))

    sentence_25 = 'The blue bird will sing in the morning.'
    question_251 = 'What will sing in the morning?'
    # print(test_agent.solve(sentence_25, question_251))

    sentence_26 = 'There are one hundred adults in that city.'
    question_261 ='Where are the adults?'
    # print(test_agent.solve(sentence_26, question_261))

    sentence_27 = 'Their children are in school.'
    question_271 = 'Where are their children?'
    # print(test_agent.solve(sentence_27, question_271))

    sentence_28 = 'It is a small world after all.'
    question_281= 'How big is the world?'
    # print(test_agent.solve(sentence_28, question_281))


if __name__ == "__main__":
    test()
