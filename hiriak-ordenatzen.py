def hririak_ordenatzen (hiriak):
    for x in hiriak.values() :
        if x >= 200000:
          gehiagokoen_zerrenad = []
          gehiagokoen_zerrenad[x] = hiriak.key()

    print(gehiagokoen_zerrenad)


gure_hriak = dict(Bilbo = 200800, Donostia = 100000, Irueñea = 203000)

hririak_ordenatzen( gure_hriak)