sounds = {'cat':'meow',
          'dog':'woof',
          100 : [n for n in range(100)]
          }

sounds['cat'] = "purr"
sounds['dog'] = 'howl'
sounds['cow'] = 'moo'

print(sounds)
print(sounds['dog'])
print(sounds['cat'])
print(sounds['cow'])
print(sounds.get('donkey'))
print(sounds.get('donkey', 'huh?'))
# for n in range(len(sounds[100])):
#    print(sounds[100][n])

zoo_counting = {'lions':2, 'tigers':1}

for animals in zoo_counting:
    print(f'{animals} : {zoo_counting[animals]}')
    
if 'bears' in zoo_counting:
    zoo_counting['bears'] += 1
else:
    zoo_counting['bears'] = 1
    
print(zoo_counting)

for animals in zoo_counting:
    print(f'{animals} : {zoo_counting[animals]}')