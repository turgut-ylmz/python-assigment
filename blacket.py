def bracket(s):
    if s == s[::-1] :
        return True
    else:
        return False
    
s = input("bracket : ")
bracket(s)
