'''
 * Build the Wordle game!
 *
 * An example of the wordle game from New York Times:
 *  https://www.nytimes.com/games/wordle/index.html
 *
 *
 * Version 1
 *
    [To resduce complexity, I removed the dictionary part]

 * Let me also show you one example:
 *  Let's say the correct word is 'apple'.
 *  - Guess 'table' --> return '.0.11'
 *      -- t doesn't exist in apple so .,
 *      -- a exists in apple but a in table is position 1, which doesn't align with the position in apple, so 0
 *      -- l and e both exist in apple and they are also at the same positions as in apple, so 1 and 1   *
 *  - Guess 'cloth' --> return '.0...'
 *  - Guess 'speed' --> return '.100.' b/c e exists in the word apple so the position of e becomes 0
'''

def attempt(guess, answer):
    map = {}
    for i in range(len(answer)):
        map[answer[i]] = map.get(answer[i], []) + [i]
    # print(map);
    res = ''
    for i in range(len(guess)):
        if guess[i] not in map:
            res += '.'
        elif i in map[guess[i]]:
            res += '1'
        else: 
            res += '0'
    return res

# TEST Version 1
# answer = 'apple';
# print(attempt('table', answer)); # should print '.0.11'
# print(attempt('cloth', answer)); # should print '.0...'
# print(attempt('speed', answer)); # should print '.100.'


'''
* Version 2
* 
* This is based on Version 1 and just change the requirement a little bit
* In Version 1, we have
*  - Guess 'speed' --> return '.100.' b/c e exists in the word apple so the position of e becomes 0
* In Version 2, the same example should return '.10..'
    This is b/c the first e can be considered as a wrong-index match to apple's 'e'
    yet the 2nd 'e' in the word speed becomes redundant, so it should output '.' instead of '0'
'''

def attempt2(guess, answer):
    map = {}
    for i in range(len(answer)):
        map[answer[i]] = map.get(answer[i], []) + [i]

    res = ''
    freq_map = {}
    for i in range(len(guess)):
        # setup the frequency map
        freq_map[guess[i]] = freq_map.get(guess[i], 0) + 1

        # setup the result string
        if guess[i] not in map or freq_map.get(guess[i]) > len(map[guess[i]]):
            res += '.'
        elif i in map[guess[i]]:
            res += '1'
        else: 
            res += '0'
    return res

# TEST Version 2
answer = 'apple';
print(attempt2('table', answer)); # should print '.0.11'
print(attempt2('speed', answer)); # should print '.10..'
answer = 'pears'
print(attempt2('esear', answer)); # should print '00.00'
print(attempt2('peear', answer)); # should print '11.00'