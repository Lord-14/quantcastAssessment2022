import sys

def reader(inputFile, targetDate):
    highestFreq = 0
    cookieFreqMap = {}
    result = []
    
    try:
        f = open(inputFile, 'r')
        lines = f.readlines()
        for line in lines: 
            if targetDate in line: #only take the lines with the target date
                if line.split(","+targetDate)[0] in cookieFreqMap: #split the line by target date and take the 0th element for the cookie
                    cookieFreqMap[line.split(","+targetDate)[0]]+=1 #increment the freq of each cookie
                else:
                    cookieFreqMap[line.split(","+targetDate)[0]]=1#add the cookie to the map at first occurence
                
        for i,k in enumerate(sorted(cookieFreqMap, key=cookieFreqMap.get, reverse=True)): #loop through keys sorted by their value
            if i==0:
                highestFreq=cookieFreqMap[k]#since the first k is always going to be the highest frequncy cookie we store that
                result.append(k)
            else:
              if cookieFreqMap[k]==highestFreq:#only take other cookies if they have the same frequency as the highest freq cookie
                  result.append(k)
        return result
        
    except IOError:#if the file doesnt exist tell the user
        print("File not found")
            
def main():
    argLen = len(sys.argv)
    #checks if we have the right amount of args
    if argLen < 4: 
        print("Missing some arguments! Order should be <filename> <log_file> -d <date>")
    elif argLen>4:
        print("Too many arguments! Order should be <filename> <log_file> -d <date>")
        
    else:
        inputFile = sys.argv[1]
        targetDate = sys.argv[3]
        cookies = reader(inputFile, targetDate)
        for cookie in cookies:
            print(cookie)
            
if __name__ == "__main__":
    main()
