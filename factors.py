# CONFIG #
EnableFactors = True
PrimeLabels = True
EnableSpaces = False
NeverSpacesOverride = False
StopInteger = 100
## CONFIG NOTES ##
#- I put them as strings because it would make it easier to tell apart from the VAR header
"EnableFactors - Will list out the number's factors"
"PrimeLables - Will show if a number is prime or composite"
"EnableSpaces - Will put spaces between numbers | Can make it harder to read"
"NeverSpacesOverride - Will always remove the spaces between numbers | Can make it harder to read"
"StopInteger - The last number to be factored | MAX VALUE IS 15000"
# VAR #
y=0
luppa=[]
# SCRIPT #
if StopInteger>15000:
    raise ValueError("StopInteger value exceeds max")
for x in range (1,StopInteger+1):
    for i in range(1,x+1):
        if (x/i)%1 == 0:
            y+=1
            luppa.append([i,int(x/i)])
    factors=y-int(y/2)
    if factors == 1:
        print(x,"has",factors,"factor")
        if PrimeLabels:
            print(x,"is prime")
    elif factors >= 1:
        print(x,"has",factors,"factors")
        if PrimeLabels:
            print(x,"is composite")
    else:
        raise ValueError("Value '0' not supported")
    if EnableFactors:
        print("Factors of",x,"are:")
        for t in range(factors):
            print(luppa[t][0],"*",luppa[t][1])
    if (EnableFactors or PrimeLabels or EnableSpaces) and not NeverSpacesOverride:
     print("")
    x+=1
    y=0
    luppa.clear()
