## Take a list of values and calculate the average values.
#  Also calculate difference between each value and the avg.
#  Also also print the values as absolute (positive) numbers.

numbers = [113, 200, 144, 99, 145]

avg_num = sum(numbers)/len(numbers)
print(avg_num)

dev_list = []

for x in numbers:
    a = x - avg_num
    dev_list.append(a)
print(dev_list)

print([abs(n) for n in dev_list])



## Proof of concept for af pitch værdier ved intensity peaks.
#  Først antages der, at praat inddeler lydklippet i bittesmå segmenter af
#  fx 0.0001 sekunder. Til hvert af disse segmenter har praat så tilknyttet
#  en masse forskellige data, som kan variere fra segment til segment.
#  Hvis man anmoder om en pitch-værdi, skal man altså angive et præcist
#  tidspunkt. Praat kigger så i sin tabel i kolonnen med det angivne tidspunkt
#  og returnerer værdien fra rækken med pitch.
#
# I nedenstående eksempel repræsenterer 'plist' en minimal udgave af denne tabel.
# Tabellen indeholder sæt af værdier i formatet (tid,pitch).
plist = [(10,100),(11,110),(12,120),(13,130),(14,140),(15,150)]
# Når praat finder intensity peaks går den ind og kigger på en tilsvarende tabel
# (tid,intensity) og returnerer alle de par, hvor intensity er lavere både lige
# før og lige efter. Denne liste af peaks repræsenteres her som 'itpairs'.
itpairs = []
itpairs.append((12,45))
itpairs.append((13,46))
itpairs.append((14,51))
itpairs += [(16,43)]
print(itpairs)
# Når vi ved at alle tidspunkterne i 'itpairs' er ved intensity peaks, kan vi
# godt slette værdierne for intensity, så vi kun står tilbage med tidspunkter.
print([i[0] for i in itpairs])
# Nu vil vi så gerne gå igennem praats 'plist' for at finde pitch ved alle de
# tidspunkter vi fandt i 'itpairs'. Dem gemmer vi i den nye liste 'ptpairs':
ptpairs = []
for x in itpairs:
    for y in plist:
        if y[0] == x[0]:
            ptpairs += y
print(ptpairs)
# Vi har således fundet pitch ved alle de punkter som praat kalder for intensity
# peaks. En metode til transskription kunne så være at relatere disse værdier
# til den gennemsnitlige pitch og gengive dem sekventielt som pile.
