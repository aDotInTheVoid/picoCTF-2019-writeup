# 1_wanna_b3_a_r0ck5tar
The code can be rougly transcribed to
```
Rocknroll is right                  | Rocknroll = true
Silence is wrong                    | Silence = 5
A guitar is a six-string            | a_guitar = 19
Tommy's been down                   | Tommy = 44
Music is a billboard-burning razzma | Music = 160
Listen to the music                 | the_music = input()
If the music is a guitar            | if the_music == a_guitar:
Say "Keep on rocking!"              |     print("Keep on rocking!")
Listen to the rhythm                |     the_rhythm = input()
If the rhythm without Music is noth |     if the_rhythm - Music == False:
Tommy is rockin guitar              |         Tommy = 66
Shout Tommy!                        |         print(Tommy!)
Music is amazing sensation          |         Music = 79
Jamming is awesome presence         |         Jamming = 78
Scream Music!                       |         print(Music!)
Scream Jamming!                     |         print(Jamming!)
Tommy is playing rock               |         Tommy = 74
Scream Tommy!                       |         print(Tommy!)
They are dazzled audiences          |         They are dazzled audiences
Shout it!                           |         print(it!)
Rock is electric heaven             |         Rock = 86
Scream it!                          |         print(it!)
Tommy is jukebox god                |         Tommy = 73
Say it!                             |         print(it!)
Break it down                       |         break
Shout "Bring on the rock!"          |         print("Bring on the rock!")
Else Whisper "That ain't it, Chief" |         Else print("That ain't it,
Break it down                       |         break
```
Therefor we can deleat
```
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
...
Else Whisper "That ain't it, Chief"
```
To get the code
```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Break it down 
```
By runing the lyrics with the [online interpriter](https://codewithrockstar.com/online), you get these numbers.
```
66
79
78
74
79
86
73
```
A simple ascii conversion gets the flag
```python
n = [66, 79, 78, 74, 79, 86, 73]
print(''.join(map(chr, n)))
```
flag: `picoCTF{BONJOVI}`