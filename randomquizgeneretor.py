#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}
# Generate 35 quiz files.

for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizfile = open('quiz%s.txt' % {quizNum + 1}, 'w')
    ansofthequiz = open('ans%s.txt' % {quizNum + 1}, 'w')
    #
    # # TODO: Write out the header for the quiz.
    quizfile.write('Name:\n\nDate:\n\nquiz no:\n\n')
    quizfile.write('state capital quiz {from %s}'.center(100) % (quizNum + 1))
    quizfile.write('\n\n')
    #
    # # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    size = [([len(i) for i in states])]
    maxim = max(*size)

    for i in range(50):
        correctAnswer = capitals[states[i]]
        quizfile.write('%s. what is the capital of %s?\n' % (i+1,states[i]))
        correctAns = capitals[states[i]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        x = random.sample(wrongAns, 3)
        options = x + [correctAns]
        random.shuffle(options)
        for j in range(4):
            quizfile.write('%s. %s\n' % ('ABCD'[j] , options[j]))
            quizfile.write('\n')
        ansofthequiz.write('%s.%s\n'%(i+1,'ABCD'[options.index(correctAns)]))



