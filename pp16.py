def pw_generate():
    import random
    from random import randrange
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    c=random.sample(range(1,70),length)
    a=[]
    for i in c:
        d=s[int(i)]
        a.append(d)
    return a


length=int(input('How long is your password?'))
print (pw_generate())