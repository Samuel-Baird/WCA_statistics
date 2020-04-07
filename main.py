import csv
      
def main():
    #get WCAID
    target_competitor = str(input("Enter WCAID: "))
    
    #opens csv file containing all singles
    file_single = open("single_csv.csv", "r")
    
    #file reader 
    reader_single = csv.reader(file_single)
    file_single.readline()
    
    #creates list
    target_results_list = []
    all_results_list = []
    nemesized_in_an_event_list = []
 
    #adds events to target_results_list, basically defines the target competitors PRs
    for lines in reader_single:
        all_results_list.append(lines[0:3])
        if lines[0] == target_competitor:
            if lines[1] == "222":
                target_results_list.append(lines[0:3])
            elif lines[1] == "333":
                target_results_list.append(lines[0:3])
            elif lines[1] == "333bf":
                target_results_list.append(lines[0:3])
            elif lines[1] == "333oh":
                target_results_list.append(lines[0:3])
            elif lines[1] == "444":
                target_results_list.append(lines[0:3])
            elif lines[1] == "444bf":
                target_results_list.append(lines[0:3])
            elif lines[1] == "555":
                target_results_list.append(lines[0:3])
            elif lines[1] == "555bf":
                target_results_list.append(lines[0:3])
            elif lines[1] == "666":
                target_results_list.append(lines[0:3])
            elif lines[1] == "777":
                target_results_list.append(lines[0:3])
            elif lines[1] == "clock":
                target_results_list.append(lines[0:3])
            elif lines[1] == "minx":
                target_results_list.append(lines[0:3])
            elif lines[1] == "pyram":
                target_results_list.append(lines[0:3])
            elif lines[1] == "skewb":
                target_results_list.append(lines[0:3])
            elif lines[1] == "sq1":
                target_results_list.append(lines[0:3])
            elif lines[1] == "333fm" or lines[1] == "333mbf":
                pass
            else:
                print("Error assigning PR singles", lines[0:3])
    

    ''' the stuff below this is what I'm having problems with'''
    
    fout = open("nemisized_in_an_event.txt", 'w')
    
    #goes through target competitor event list
    for line in target_results_list:
        
        #goes through list of all competitors
        for lines in all_results_list:
            
            #filters out target competitor, fmc and mbld
            if lines[0] == target_competitor or lines[1] == "333fm" or lines[1] == "333mbf":
                pass
            
            #filters out events on the target competitor list from the list of all competitors
            elif line[1] == lines[1]:
                
                #if target competitor has a slower time than 
                if line[2] > lines[2]:
                    nemesized_in_an_event_list.append(lines[0:2])
                    
                    print(lines[0:2])
                    
                else:
                    pass
            else:
                pass
    fout.close()       
    
    
if __name__ == "__main__":
    main()
