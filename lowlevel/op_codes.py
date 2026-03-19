import registers as rg

def jp(dest):
    rg.pc.set(dest)
def jr(dest):
    jp(dest)