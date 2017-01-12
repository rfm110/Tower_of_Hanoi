import random


def legal_move(move_disk, list_used):
    if len(list_used) < 1:
        return True

    if len(list_used) >= 1:
        if list_used[len(list_used)-1] > move_disk:
            return True
        else:
            return False


def new_legal_move(selection_dictionary, disk_from, disk_to):
    # we've already defined selection_dictionary = {1: l1, 2: l2, 3: l3} before, so we can just use it here
    if disk_from not in [1, 2, 3] or disk_to not in [1, 2, 3]:
        return False

    # return will terminate your function call if reached. So instead of having if-else statements,
    # just the if with a return inside is sufficient. I will chain them like filters and if all the
    # filters are passer return True
    if not selection_dictionary[disk_from]:  # empty lists will evaluate to False
        return False

    if not selection_dictionary[disk_to]:  # empty pin can always receive a disk
        return True

    if selection_dictionary[disk_from][-1] > selection_dictionary[disk_to][-1]:
        return False

    return True


# this is the part that does the heavy lifting of updating the game.
# it does no IO and hence can be easily unittested
def tower_of_hanoi_step(l1, l2, l3, disk_from, disk_to):
    selection_dictionary = {1: l1, 2: l2, 3: l3}
    #
    # legal = legal_move(selection_dictionary[disk_from][-1], selection_dictionary[disk_to])
    # this line was is a bit awkward - it will fail if the disk from/to indexes do not exist, eg<0 or >3
    # as well if the starting column is empty. Because of that I re-wrote new_legal move to compensate
    # for that above

    legal = new_legal_move(selection_dictionary, disk_from, disk_to)
    if not legal:
        return False, l1, l2, l3
    else:
        selection_dictionary[disk_to].append(selection_dictionary[disk_from].pop())
        return True, l1, l2, l3


# this part does the IO but nothing else. it cannot be unittested, but that doesn't matter, because
# only things that can go wrong are IO and there is very little of it.
def tower_of_hanoi_game(pin_1=[4,3,2,1], pin_2=[], pin_3=[], turns=10):
    print "starting game"

    while turns > 0 and pin_3 != [4, 3, 2, 1]:
        print "current game state :", pin_1, pin_2, pin_3
        disk = int(raw_input("Select the disk you would like to move"))
        new_position = int(raw_input("To which column would you like to move disk %d" % disk))
        legal, pin_1, pin_2, pin_3 = tower_of_hanoi_step(pin_1, pin_2, pin_3, disk, new_position)
        if not legal:
            print "That is an impossible move, please select a new disk and column"
            continue  # pins were updated and move was not legal. We inform the user and restart the loop
            # without taking any turns out
        # here, we are sure the loop is legal and that columns were updated. we can remove turns
        # and print turns remaining
        turns -= 1  # equivalent to turns = turns - 1
        print '%s turns remaining in the game' % turns
        # there is an implicit continue here - python will just resume loop from here. If you wanted
        # to re-write it as a recursive function, you would have needed to replace the continue statements with
        # the calls to the function itself again

    # now we are outside the loop. We need to determine if we are out because we run out of turns or because we won:
    if pin_3 == [4, 3, 2, 1]:
        print 'You won!'

    else:
        print "You've run out of turns!"


def play_tower_of_hanoi(l1=[4,3,2,1], l2=[], l3=[], human_player=True, turns=10):
    if turns == 0:
        print l1, l2, l3
        print
        return l1, l2, l3
    print("start game")
    print l1, l2, l3

    if human_player == True:
        print "User"
        disk = int(raw_input("Select the disk you would like to move"))
        new_position = int(raw_input("To which column would you like to move disk %d" % disk))
        if disk == 1:
            move_disk = l1.pop()
        if disk == 2:
            move_disk = l2.pop()
        if disk == 3:
            move_disk = l3.pop()

    if human_player == False:
        print "Computer"
        disk_possible = []
        if len(l1) > 0:
            disk_possible.append(l1)
        if len(l2) > 0:
            disk_possible.append(l2)
        if len(l3) > 0:
            disk_possible.append(l3)
        disk_guess = disk_possible[random.randint(0, len(disk_possible)-1)]
        move_disk = disk_guess.pop()
        new_position = random.randint(1, 3)
    print
    print "position"
    print new_position

    print "disk"
    print move_disk

    if new_position == 1:
        list_used = l1
        print(l1)
    if new_position == 2:
        list_used = l2
        print(l2)
    if new_position == 3:
        list_used = l3
        print(l3)
    legal = legal_move(move_disk, list_used)

    print
    print legal

    if legal == True:
        list_used.append(move_disk)

    while legal == False:
        print False
        if human_player == True:
            position = int(raw_input("That is an impossible move, please select a new column"))
            if position == 1:
                list_used = l1
            if position == 2:
                list_used = l2
            if position == 3:
                list_used = l3
                print
                print "list used"
                print list_used
                print
                print "position"
                print position
            legal = legal_move(move_disk, list_used)

        if human_player == False:
            possible_pos = [1, 2, 3]
            possible_pos.remove(new_position)
            possible_pos = sorted(possible_pos)
            position = random.randint(1, possible_pos[len(possible_pos)-1])
            if position == 1:
                list_used = l1
            if position == 2:
                list_used = l2
            if position == 3:
                list_used = l3
            legal = legal_move(move_disk, list_used)

        if legal == True:
            print True
            print
            print "list used"
            print list_used
            list_used.append(move_disk)
            break

    print "final"
    print l1, l2, l3

    if human_player == False:
        print
        print "turns remaining"
        print turns
        print
        print "~~~~~~~~~~"
        play_tower_of_hanoi(l1, l2, l3, human_player=False, turns=turns-1)

    if l3 == [4, 3, 2, 1]:
        print("You win!")
        return l3
    if l3 != [4, 3, 2, 1] and human_player == True:
        play_tower_of_hanoi(l1, l2, l3)


# play_tower_of_hanoi(human_player=False)
# play_tower_of_hanoi()

tower_of_hanoi_game()