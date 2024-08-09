############
#
# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#
############
def find_min_pledge(pledge_list):
    """
    Checks array for the lowest valid pledge by checking 
    array for current pledge ammountin O(n) time
    """
    pledge = 1
    while pledge in pledge_list:
        pledge+=1
    return pledge

assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5

assert find_min_pledge([1, 2, 3]) == 4

assert find_min_pledge([-1, -3]) == 1