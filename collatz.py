import time

n_formatted = lambda n: "{:,}".format(n)

def collatz(n:int, original=int, collection=[], highest_number=0, highest_count=0):
    if len(collection) == 0:
        original = n

    if n == 1:
        return f"\n{original}-->" + ",".join(collection) + f"\n\nCount:{len(collection)}\nHighest Number:{n_formatted(int(highest_number))}", highest_number, highest_count
    
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    
    if n > highest_number:
        highest_number = n
    
    collection.append(str(int(n)))

    if len(collection) > highest_count:
        highest_count = len(collection)
    
    return collatz(n, original, collection, highest_number, highest_count)

number_range = range(1, 1_000_000)
total_time = 0.
highest_n = (0, 0)
highest_c = (0, 0)
for n in number_range:
    start = time.time()

    collat_string, highest_number, highest_count = collatz(n, collection=[])

    if highest_number > highest_n[0]:
        highest_n = (highest_number, n)

    if highest_count > highest_c[0]:
        highest_c = (highest_count, n)
    
    print(collat_string)

    stop = time.time()
    total_time += (stop - start)

data_output = ( 
    f"""\n\nFinished calculating collatz conjectures
-----------------------------------------------     
Number range: {n_formatted(number_range[0])}-{n_formatted(number_range[-1])}
Total time to run calculations: {round(total_time, 3)} seconds
Highest number reached: {n_formatted(int(highest_n[0]))} for integer {n_formatted(highest_n[1])}
Longest chain: {n_formatted(highest_c[0])} for integer {n_formatted(highest_c[1])}""" 
)

print(data_output)