# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1

#1
player_goal0 = 'Ruud Gullit'
player_goal1 = 'Marco van Basten'

#2
goal_0 = 32
goal_1 = 54

#3
scorers = player_goal0 + ' ' + str(goal_0) + ', ' + player_goal1 + ' ' + str(goal_1) 
print(scorers)

#4
report = player_goal0 + f' scored in the {goal_0}nd minute' + '\n' + player_goal1 + f' scored in the {goal_1}th minute' 
print(report)


#Part 2

#1
player = 'Gerald Vanenburg'

#2
index_lastname = player.find(" ")
# print (index_lastname)
first_name = player[0:index_lastname]
print (first_name)

#3
last_name = player[index_lastname+1:] #De +1 doe ik vanwege de spatie, is geen onderdeel van de achternaam
print(last_name)
last_name_len = len(last_name)   
print (last_name_len)

#4
name_short = first_name[0:1] + '. ' + last_name
print(name_short)

#5
first_name_len = len(first_name)
# print(first_name_len)
first_name_len = first_name_len - 1
chant = f'{first_name}! ' * first_name_len + f'{first_name}!'
print (chant)

#6
#Hier liep ik wat vast, ik zou dit met een if statement kunnen oplossen etc maar dat is nu nog niet behandeld.
chant_len = len(chant)
#print(chant_len)
#print(chant [chant_len-1] != ' ')

good_chant = bool(print(chant [chant_len-1] != ' '))
print (good_chant)
