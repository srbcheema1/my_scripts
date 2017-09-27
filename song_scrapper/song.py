from urllib.request import urlopen

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

print("enter url : ")
url = input()

file_name = 'song.mp3'
u = urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
#file_size = int(meta.getheaders("Content-Length")[0])
file_size = u.length
#print(u.__dict__)
print ("Downloading: %s Bytes: %s" % (file_name, file_size))

file_size_dl = 0
block_sz = file_size//43 
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    #print (status)
    # Update Progress Bar
    printProgressBar(file_size_dl,file_size, prefix = 'Progress:', suffix = 'Complete', length = 50)

f.close()
