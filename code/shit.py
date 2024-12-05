# import random
# import os

# list_of_files = list(os.listdir('C:/dragon egg/AnimalDetectionYolo/Stuff/archive/text_folder'))
# baseDir1 = 'C:/dragon egg/AnimalDetectionYolo/data/images/train/'
# baseDir2 = 'C:/dragon egg/AnimalDetectionYolo/data/images/temp/'
# for file in list_of_files:
#     os.replace(baseDir1 + file[0:len(file)-4] + '.jpg', baseDir2 + file[0:len(file)-4] + '.jpg')

# list_of_things = list(os.listdir('C:/dragon egg/AnimalDetectionYolo/Stuff/archive/text_folder'))
# baseDir1 = 'C:/dragon egg/AnimalDetectionYolo/Stuff/archive/text_folder/'
# baseDir2 = 'C:/dragon egg/AnimalDetectionYolo/Stuff/archive/text_temp/'
# baseDir3 = 'C:/dragon egg/AnimalDetectionYolo/data/images/train/'
# baseDir4 = 'C:/dragon egg/AnimalDetectionYolo/data/images/val/'
# for i in range(0, 21692):
#     choice = random.choice(list_of_things)
#     os.replace(baseDir1 + choice, baseDir2 + choice)
#     os.replace(baseDir3 + choice[0:len(choice)-4] + '.jpg', baseDir4 + choice[0:len(choice)-4] + '.jpg')
#     list_of_things.remove(choice)
#     print('Done:', choice[0:len(choice)-4])

# baseDir1 = 'C:/dragon egg/AnimalDetectionYolo/Stuff/archive/text_temp/'
# baseDir2 = 'C:/dragon egg/AnimalDetectionYolo/data/labels/val/'

# list_of_shit = os.listdir(baseDir1[0:len(baseDir1)-1])

# for shit in list_of_shit:
#     os.replace(baseDir1 + shit, baseDir2 + shit)
#     print('Done:', shit)