import itertools

cookies = ["choc chip", "sugar", "PB", "macaroon"]


num = itertools.combinations_with_replacement(cookies, 6)
    
for c, num in enumerate(num):
    print(str(c), "====>>", str(num).replace(" ", "").replace(",", "").replace("'", " ").replace("(", "").replace(")", ""))