# https://open.kattis.com/problems/aprizenoonecanwin

# Preberi število izdelkov (n) in največjo dovoljeno vsoto (x)
n, x = map(int, input().split())
# Preberi in uredi cene izdelkov naraščajoče
cene = sorted(list(map(int, input().split())))

# Števec za število izdelkov v ponudbi
stevec = 1
# Preveri vse zaporedne pare izdelkov
for i in range(1, len(cene)):
    # Če je vsota para manjša ali enaka x, lahko dodamo izdelek
    if cene[i] + cene[i-1] <= x:
        stevec += 1
    else:
        break

print(stevec)