def cetaksiku(y):
    string = ''
    bar =1
    
    while bar <= y :
        kol = bar

        while kol > 0 :
            string = string + "*"
            kol = kol - 1

        string = string +'\n'
        bar = bar +1
    print (string)
