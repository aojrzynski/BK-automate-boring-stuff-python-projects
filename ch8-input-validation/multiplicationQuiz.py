#! python3 
# multiplicationQuiz.py - Program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.

import random, time
import pyinputplus as pyip


numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Corrent!')
        correctAnswers += 1
    time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))