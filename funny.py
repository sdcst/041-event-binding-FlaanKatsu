import playsound as au

def playsound():
    au.playsound("animals_dogs_x2_barking_small_001.mp3",block=False)

done = 0
while done == 0:
    playsound()