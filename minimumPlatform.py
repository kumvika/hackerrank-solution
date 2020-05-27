def minPlatformRequired(arr, dep):
    arrival_sorted = sorted(arr)
    departure_sorted = sorted(dep)
    n = len(arrival_sorted)
    platform = 1
    max_platform = 1
    i = 1
    j = 0
    while (i < n and j < n):
        # If a new train arrives before the departure of the earlier train
        # Increment the number of platforms and look for the next train arrival
        if ( arr[i] <= dep[j] ):
            platform += 1
            i += 1
        else:
        # If a new train arrives after the departure of the earlier train
        # then, we dont need to have new platform and we can use the same exisiting one.
            platform -= 1
            j += 1
        #Check if the current number of platform is greater than the current max
        if platform > max_platform:
            max_platform = platform
    return max_platform 
            

arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]

print(minPlatformRequired(arr, dep))