#import pysnooper
#@pysnooper.snoop()

# DayValue = [36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,
#             46,46,50,48,48,58,58,58,58,58,58,55,55,55,55,55,55,55,55,55]
DayValue = [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,42,
            42,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52]
DayBase = 20
DayOffset = 0
TargetValue = 50
EvenValue = 0
while EvenValue < TargetValue:
    DayOffset +=1
    EvenValue = sum(DayValue[DayOffset:(DayBase+DayOffset)])/20
    print(DayValue[DayOffset:(DayBase+DayOffset)])
    print(EvenValue)

print(DayOffset)