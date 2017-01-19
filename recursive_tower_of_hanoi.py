def recursive_tower_of_hanoi(pin_1=[4,3,2,1], pin_2=[], pin_3=[], number_of_disks=4):
    # change parameter names so they are more general? like source, target, and intermediate

    if pin_3 == [4, 3, 2, 1]:
        print "Game Completed"
        return pin_1, pin_2, pin_3
    # let pin_1 be the source, pin_2 be the intermediate, and pin_3 be the destination
    # instead of using while loop, make function call itself
    print "Current Game State:", pin_1, pin_2, pin_3
    print

    # if pin_3 != [4,3,2,1]:
    if number_of_disks != 0:

        # move disk from source to intermediate so pin_2 is the new target
        print "Moving disk from source to intermediate"
        print "recursion a"
        recursive_tower_of_hanoi(pin_1, pin_3, pin_2, number_of_disks-1)
        print "number of disks a", number_of_disks

        print "source", pin_1
        print "intermediate", pin_3
        print "target", pin_2
        print

        # when source is not empty, move disk from source to target (pin_1 to pin_3)
        if pin_1 != []:
            # pin_3.append(pin_1[len(pin_1)-1])
            print "Source is non-empty, moving disk from pin1(source) to pin3(target)"
            pin_3.append(pin_1.pop())
            print "source", pin_1
            print "intermediate", pin_2
            print "target", pin_3
            print

        # step 3 is moving disk from intermediate to target, from pin_2 to pin_3
        print "Moving disk from intermediate to target"
        print "recursion b"
        recursive_tower_of_hanoi(pin_2, pin_1, pin_3, number_of_disks-1)
        print "number of disks b", number_of_disks
        print pin_2, pin_1, pin_3
        print "source", pin_2
        print "intermediate", pin_1
        print "target", pin_3
        print


if __name__ == "__main__":
    recursive_tower_of_hanoi()
