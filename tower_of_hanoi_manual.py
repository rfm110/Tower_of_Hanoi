def move_is_legal(selection_dictionary, disk_from, disk_to):
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

    legal = move_is_legal(selection_dictionary, disk_from, disk_to)
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


if __name__ == "__main__":
    tower_of_hanoi_game()
