import csv

def main():
    file = open("Modified_WCA_export_Results.csv", "r")
    reader = csv.reader(file)
    file.readline()
    
    target_event = str(input("Enter Event: "))
    
    unfiltered_list = []
    unfiltered_2015_list = []
    unfiltered_2016_list = []
    unfiltered_2017_list = []
    unfiltered_2018_list = []
    unfiltered_2019_list = []

    for line in reader:
        if target_event in line[1]:
            unfiltered_list.append(line)
            
    for line in unfiltered_list:
        if "2015" in line[0]:
            unfiltered_2015_list.append(line[2])
        elif "2016" in line[0]:
            unfiltered_2016_list.append(line[2])
        elif "2017" in line[0]:
            unfiltered_2017_list.append(line[2])
        elif "2018" in line[0]:
            unfiltered_2018_list.append(line[2])
        elif "2019" in line[0]:
            unfiltered_2019_list.append(line[2])
        else:
            pass
            
    sorted_2015_list = list(dict.fromkeys(unfiltered_2015_list))
    sorted_2016_list = list(dict.fromkeys(unfiltered_2016_list))
    sorted_2017_list = list(dict.fromkeys(unfiltered_2017_list))
    sorted_2018_list = list(dict.fromkeys(unfiltered_2018_list))
    sorted_2019_list = list(dict.fromkeys(unfiltered_2019_list))
    
    print(sorted_2019_list)
    
    '''
    print("Event", "|", "Time range", "|", "growth%", "|", "Start#", "|", "End#")
    print("--------------------------------------------")
    if count_2003 > 0:
        growth1 = ((count_2004 - count_2003)/count_2003) * 100
        print(target_event,"2003-2004",growth1, count_2003, count_2004)
    elif count_2003 == 0:
        pass
    
    '''
    
if __name__ == "__main__":
    main()         