# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:07:34 2021

@author: artem
"""
#We are given function bing_lyrics I define that function below and assign dog_name:
def bingo_lyrics(dog_name):

    # Creating the actual lyrics line "There was a farmer who had a dog and bingo was his name-o:" 
    #I am savin this lyric in a function called song_lyrics that I can call for later on
   song_lyrics = "There was a farmer who had a dog and bingo was his name-o:" 
    
    #Using isinstance -  If object is not an object of the given type, the function always returns false.
   if isinstance(dog_name,list):
        dog_name = ''.join(dog_name) #<-- Attaches all my letters into the string by simply using .join

 #Creating the actual loop to repeat
   for i in range(len(dog_name)):
         #Using .format I can insert into my actual place/slot 
        print('{}{}{}'.format(song_lyrics,'*'*i,dog_name[i:]))
   print('{}{}'.format(song_lyrics, dog_name))

#Instructions said to create dog_name = BINGO or dog_name=['B', 'I', 'N', 'G', 'O']
dog_name=['B', 'I', 'N', 'G', 'O']
bingo_lyrics(dog_name)
