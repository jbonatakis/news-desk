def set_key():
    f = open('key', 'w')
    key = str(input("Enter newsapi.org key here >> ")).strip()
    f.write(key)
    f.close()
