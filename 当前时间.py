import time
print(time.strftime('%A, %d. %B %Y %I:%M%p', time.localtime()))
# method strftime used to print, the second parameter should be a struct_time class, 
# output sample: Thursday, 12. September 2019 07:54PM
