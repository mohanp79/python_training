def ask_ok(prompt, retries=4, complaint='Yes or no!'):
    while 1:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): return 1
        if ok in ('n', 'no', 'nop', 'nope'):
            return 0
        retries = retries - 1
        if retries < 0:
            raise (IOError, 'refusing user')
        print (complaint)
