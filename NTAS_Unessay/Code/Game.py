#   Author: Mathew Hasting
#   NTAS 322
#   April 27, 2022
#   Game File, controls program by asking for quiz questions and answerKey

import Questions
import keyboard

# Main control for game
def control():
    ## Calls generateQuiz() to get all the questions
    questionList = Questions.generateQuiz()

    totalScore = 0 # Simply the score passed to each of the questions
    ## All questions in game
    totalScore = Questions.origins(questionList[0], totalScore)
    totalScore = Questions.preColonization(questionList[1], totalScore)
    totalScore = Questions.assimilation(questionList[2], totalScore)
    totalScore = Questions.rejection(questionList[3], totalScore)
    totalScore = Questions.reclamation(questionList[4], totalScore)

    ## Passes the score to results for scoring
    result(totalScore)
    
## Takes totalScore and gives player a scenario for ending
## Input: score
def result(score):
    print('Your score was ' + str(score) + '/5') # Note: score is an int and needs to be converted to str(string) for print
    print()
    if(score == 0):
        print('Our exhibit was a complete failure! Nobody has came to visit since the grand opening of the exhibit. I am sad to say that')
        print('the Native American exhibit was unsuccessful and we will need to try again.')
    elif(score > 0 and score <= 2):
        print('After the grand opening of our exhibit there is almost nobody coming to visit. Our exhibit seems to not have grabbed much')
        print('attention. It seems that we need to go back to the drawing board and replan the exhibit.')
    elif(score > 2 and score <= 4):
        print('Thanks to your help we managed to get lots of visitors! However, the visitors do not seem to be as interested in the exhibit')
        print('as we hoped. I wonder if we could have done better...')
    else:
        print('Thank you for your help! Because of your help the exhibit was a huge success! Additionally, some of our visitors') 
        print('have said they enjoyed the exhibit so much they are donating to some of the Native American protests we mentioned in the exhibit!')
        print('We could not have done this without your help!')

    print()
    print('Game Over!')

    print()
    print('Press enter to close game')
    while True:
        if keyboard.read_key() == 'enter':
            break  
