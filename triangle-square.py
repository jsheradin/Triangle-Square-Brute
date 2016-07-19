#Find numbers that are triangle-squares in a range
import multiprocessing as mp
import sys

#Max size of lists in P3 is 536870912
#num_max - num_min must be less than that
num_min = 0 #Number to start checking from

thread_count = 4 #Should be an even number bigger than 1

#Calculate actual numbers
def sq_calc(start, stop):
    sq_temp = []
    for s in range(start, stop):
        sq_temp.append(s**2)
    return sq_temp

def tri_calc(start, stop):
    tri_temp = []
    for t in range(start, stop):
        tri_temp.append(int(t*(t+1)/2))
    return tri_temp

#Log results from calculations
sq_lists = []
def sq_log(sq_log_temp):
    sq_lists.append(sq_log_temp)

tri_lists = []
def tri_log(tri_log_temp):
    tri_lists.append(tri_log_temp)

#Find numbers that are in both sets
def sort_nums(sq_nums, tri_nums):
    match_temp = []
    for num in range(0, len(sq_nums)):
        if sq_nums[num] in tri_nums:
            match_temp.append(sq_nums[num])
    return match_temp

#Log matching results
matches = []
def sort_nums_log(match):
    matches.append(match)

#Main thread
if __name__ == '__main__':
    num_range = num_max - num_min
    if num_range > 536870912:
        print("Range too large")
        sys.exit()
    thread_count = thread_count/2
    #Spool up calculation threads
    print("Calculating...", end="")
    calc_pool = mp.Pool()
    for calc_thread in range(0, int(thread_count)):
        calc_start = int(calc_thread * (num_range / thread_count) + 1) + num_min
        calc_stop = int((calc_thread + 1) * (num_range / thread_count)) + num_min
        calc_pool.apply_async(sq_calc, args = (calc_start, calc_stop), callback = sq_log)
        calc_pool.apply_async(tri_calc, args = (calc_start, calc_stop), callback = tri_log)
    calc_pool.close()
    calc_pool.join()
    print(" done")

    #Prepare for sort
    tri_lists = [val for sublist in tri_lists for val in sublist]

    #Spool up sorting threads
    print("Sort results...", end="")
    sort_pool = mp.Pool()
    for sort_thread in range(0, len(sq_lists)):
        sort_pool.apply_async(sort_nums, args = (sq_lists[sort_thread], tri_lists), callback = sort_nums_log)
    sort_pool.close()
    sort_pool.join()
    print(" done")

    #Flatten, sort, and print results
    matches = [val for sublist in matches for val in sublist]
    matches.sort()
    print("Results:", matches)
