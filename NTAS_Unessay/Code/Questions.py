#   Author: Mathew Hasting
#   NTAS 322
#   April 27, 2022
#   Questions File, responsible for handling Q/A and returning proper score to Game.py

import keyboard # For "Press space to continue..." lines

## Displays the list of answers for a given question
## Input: Answer Key
def displayAnswers(answerKey):
    count = 1
    for answer in answerKey:
        print(str(answer) + ') ' + answerKey[count][0])
        count += 1

    print()

## Generates Quiz answers for the game
## Return: list of answer keys, structured as a list of lists (Questions) which each contain a dictionary with the answers 
## Ex) quesionList[oQuestions][key][0] would list the answer at key in oQuestions, replacing 0 with 1 would tell you if the answer is correct
def generateQuiz():
    # Origins
    oQuestions = {1:['Cover origin stories and gods', True],
                   2:['Showcase the difference between their beliefs', False],
                   3:['Treat all tribes as one', False]}

    # Pre-colonial Society
    pcQuestions = {1:['Display artifacts made by the tribes before America was colonized', False],
                   2:['Showcase the beliefs of each tribe', False],
                   3:['Describe the social structures between tribes', True]}

    # Assimilation
    aQuestions = {1:['Natives were forced to send their children', False],
                  2:['Natives sought to learn from the settlers', True],
                  3:['Natives traded their children for goods', False]}
    # Rejection
    rQuestions = {1:['Rejected both Christianity and the colonizer\'s attempt at assimilation', False],
                  2:['Embraced Christianity and the colonizers', False],
                  3:['Both reactions', True]}
    
    #Reclamation
    recQuestions = {1:['Education', False],
                   2:['Protests', False],
                   3:['Traditions', False],
                   4:['All of the above', True]}

    ## Collects all lists of questions into one for returning
    questionList = [oQuestions, pcQuestions, aQuestions, rQuestions, recQuestions]
    return questionList

## Origins Questions, asks questions then returns score
## Input: oQuestions, score
## Return: score
def origins(answerKey, score):
    print(  # Question
    '''
    Before we show visitors some of the more complex concepts of Native American history it is important to establish the groundwork,
    which in this case are the varied beliefs of the Native American people. This is because Native American culture
    is heavily based on links to the spirit world, but ideas on how they came to be and how to worhip their creators was not always the
    same between tribes. Which of these choices do you think would be a great way to set the foundation for visitors?
    '''
    )
    
    displayAnswers(answerKey)

    # Simple loop to make sure input is correct w/o forcing program end w/ exceptions
    loop = True
    while loop:
        user = int(input('Choose an option (enter corresponding number): '))
        print(user)

        if user != 1 and user != 2 and user != 3:
            print('Invalid input, try again!')
            print()
        else:
            loop = False

    if(answerKey[user][1]):
        print( # Correct
        '''
        Nice! it is important we do not treat all tribes as one or only show their differences since we risk missing out on important
        details in their beliefs, the simplest way to teach visitors about their beliefs would be a showcase of a few origin stories and
        varying Gods, as many Natives share similar aspects in their religions so these would help give a sense of curiosity in our visitors!
        '''
        )
        score += 1
    else:
        print( # Incorrect
        '''
        Wrong! We cannot make the assumption that all Native religions are different because as stated by Joshua Wetsit, 
        "Our Indian religion is all one religion, the Great Spirit." But on the other hand we also need to avoid lumping all tribal
        beliefs into one because depending on where the tribe is situated it may have a completely different origin story or set of beliefs.
        '''
        )
    
    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break
    
    return score

## Pre-Colonial Questions, asks questions then returns score
## Input: pcQuestions, score
## Return: score
def preColonization(answerKey, score):
    print(
    '''
    Native American society before the colonization of the Americas was more advanced than what is depicted in pop culture today. For
    instance there existed a complex trading network between the many tribes where they would trade goods. However, this was not always
    the case as there was a form of a cycle where Natives would build up these connections but would they eventually split.
    Which should we display to properly show Native American society before the colonization of America?
    ''')

    displayAnswers(answerKey)

    loop = True
    while loop:
        user = int(input('Choose an option: '))
        if user != 1 and user != 2 and user != 3:
            print('Invalid input, try again!')
            print()
        else:
            loop = False

    if(answerKey[user][1]):
        print(
        '''
        Great job! Native Americans were believed to have a complex trading structure which led to the development of Cahokia, a trading
        center located in modern-day Mississipi! It is important we cover this part of history in our exhibit to help our visitors understand
        the important lesson that the Natives were capable of developing complex social structures. Showcasing Native society will also help
        provide a great look into the beliefs of Native Americans since places like Cahokia allowed for the trade of religious goods used
        in ceremonies or rituals that can be unique for each tribe.
        '''
        )
        score += 1
    else:
        print(
        '''
        Whoops looks like you got that one wrong! While it may seem like a good idea, sharing the artifacts of Natives before colonization
        leaves a large range of artifacts, this may not be an accurate way of depicting Native society. Secondly, while Native beliefs
        were shared between tribes it may not depict the correct idea, and risks becoming the same as the previous exhibit. Displaying evidence
        of the complex social structures Natives had is a fantastic way to show the height of Native American society. Especially since
        showing ways the Natives developed more in depth social environments will also inevitably describe the religions and artifacts brought
        by people into the trading networks.
        '''
        )

    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break   
    
    return score

## Assimilation Questions, asks questions then returns score
## Input: aQuestions, score
## Return: score
def assimilation(answerKey, score):
    print(
    '''
    Once Europeans settled in what we know now as America, they saw Native Americans as savages and sought to assimilate them into their
    society through boarding schools and other such institutions. We know now that most of these schools were harmful towards Native
    American youth by indoctrinating them and preventing them from practicing their Native beliefs and culture. However, there is
    a reason why the Native Americans sent their children to these schools, what do you think it is?
    '''
    )

    displayAnswers(answerKey)

    loop = True
    while loop:
        user = int(input('Choose an option: '))
        if user != 1 and user != 2 and user != 3:
            print('Invalid input, try again!')
            print()
        else:
            loop = False

    if(answerKey[user][1]):
        print(
        '''
        Good work! Native Americans originally sent their kids to these schools because they sought to learn many of the things
        the colonizers brought with them, one of the main concepts they desired to learn was Christianity. This may be surprising, but
        Natives saw Christianity as this new thing that would help them prevent spiritual diseases or ailments on the land.
        Additionally, they saw the technology of the colonizers and wanted their children to learn as much as they could to bring
        back to their tribes. However, the result of these schools on Native culture was far worse than they could imagine.
        '''
        )
        score += 1
    else:
        print(
        '''
        Sorry that's not correct! While in some cases this might have happened, Native Americans were not all forced or bribed to give up
        their children to these schools. At first parents let the missionaries from boarding schools take their children simply to obtain the
        knowledge of the "White Man". Also, once they took notice of Christianity and the new perspective of spirits from it the Native American
        tribes believed it necessary to learn the secrets of Chrisitianity.
        '''
        )

    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break

    return score

## Rejection Questions, asks questions then returns score
## Input: rQuestions, score
## Return: score
def rejection(answerKey, score):
    print(
    '''
    After children started returning from the schools, the Native children taught what they learned to their tribes and many incorporated
    this knowledge into their existing beliefs and culture. Colonizers did not like how the Natives used the knowledge they gained
    and for a time they allowed this. Eventually the colonizers sought to eliminate the Natives' practices by preventing Natives from
    practicing Christianity the way they learned and were prevented from practicing their Native beliefs outright in some cases.
    What was the response from the Native Americans toward Christianity and the colonizers after this?
    '''
    )

    displayAnswers(answerKey)

    loop = True
    while loop:
        user = int(input('Choose an option: '))
        if user != 1 and user != 2 and user != 3:
            print('Invalid input, try again!')
            print()
        else:
            loop = False

    if(answerKey[user][1]):
        print(
        '''
        Sweet! Native Americans' response to the colonizers' attempts to assimilate them was varied among the tribes, some
        choosing to side with the colonizers while some chose to oppose them, and of course there was a range of responses in between! For
        example, one such response was the Ghost Dance movement where the main belief was that if they worshipped enough, the White man would
        be erased from the world. While it was traditionally a peaceful movement based around the aforementioned Ghost Dance and spiritual beliefs,
        European colonizers saw it as a hostile movement. Finally, due to rising tensions, the movement culminated in the massacre at Standing Rock
        where Chief Sitting Bull and his group were killed in a misunderstanding between them and the United States Army. It is important to remember
        that even though this is only one such example, it has had long standing implications on modern-day struggles for Native Americans. 
        '''
        )
        score += 1
    else:
        print(
        '''
        Whoops! Keep in mind that not everything is black and white, in this instance Native Americans were divided on the issue as some
        tribes continued to follow or incoporate Christian teachings and others chose to avoid Christianity as they saw no improvement and heard
        of deaths at the schools they sent their children. As a result opinions of Christianity were mixed, and because of this it can be
        observed that Natives Americans were on both sides.
        '''
        )

    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break   

    return score 
    


## Reclamation Questions, asks questions then returns score
## Input: recQuestions, score
## Return: score
def reclamation(answerKey, score):
    print(
    '''
    In recent times Native Americans have attempted to reclaim their lost traditions by returning to their roots. However, with most of their
    land being owned by the government and various companies they were forced to take a stand against these institutions to fight for their rights
    through education and protests. With all of these examples of Native American descendants attempting to take back their heritage it is 
    hard to choose what to put in the exhibit.
    What would you say is the most important thing we should put in the exhibit?
    '''
    )

    displayAnswers(answerKey)

    loop = True
    while loop:
        user = int(input('Choose an option: '))
        if user != 1 and user != 2 and user != 3 and user != 4:
            print('Invalid input, try again!')
            print()
        else:
            loop = False

    if(answerKey[user][1]):
        print(
        '''
        Correct! All of these options and more are extremely important for the movement! Native Americans banding together despite
        their differences in all of these ways are how they can reclaim their past. The land that has been taken from Native Americans holds
        great spiritual importance, alongside the traditions that have both been lost to time and have managed to persist despite the attempts
        made by the colonizers to erase them. It is necessary to put these issues on display in our exhibit to hopefully inspire change in visitors 
        and hopefully allow for Native Americans to feel proud of their past!
        '''
        )
        score += 1
    else:
        print(
        '''
        Sorry that was wrong! While some of these options look to be more important than others, it should be noted they are all equally important.
        In this part of the exhibit we need to inform the visitors of current events in Native American history so that they can be
        properly informed for any future movements!
        '''
        )

    print()
    print('Press space to continue...')
    while True:
        if keyboard.read_key() == 'space':
            break    

    return score
    
