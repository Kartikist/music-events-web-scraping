
def send():
    with open("temp.txt", 'r') as file:
        a = file.readlines()
        
    date_list = []
    temp_list = []
    b = a[1:]
    b = [i.rstrip() for i in b]
    for i in b:
        date, temp = i.split(',')
        date_list.append(date)
        temp_list.append(temp)

    return date_list, temp_list
    
    
    