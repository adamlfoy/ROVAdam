#Function to calculate the Total Amps used. Takes in a float list of thruster PWMs
def getAmpTotal(thrusterPWMs):
    ampTotal = 0

    for x in range(len(thrusterPWMs)):
        ampTotal += 214.9513 - 0.2864872 * thrusterPWMs[x] + 0.00009537964 * (thrusterPWMs[x] * thrusterPWMs[x])
        #print(ampTotal)
    return ampTotal

# Function to readjust thruster PWM values if required. Takes in a float list of thruster PWMS,
# and  which is an int value representing a second amp limit (above the first) which once
# exceeded will also cause the top (first 4) thrusters to be scaled down.
def tempSafeGuard(thrusterPWMs):
    ampLimit = 21

    if getAmpTotal(thrusterPWMs) <= ampLimit:
        return thrusterPWMs
    else:
        while getAmpTotal(thrusterPWMs) > ampLimit:

            print(str(getAmpTotal(thrusterPWMs)) + " - " + str())

            for thrustNum in range(len(thrusterPWMs)):
                if thrusterPWMs[thrustNum]>1500:
                    thrusterPWMs[thrustNum] -= thrusterPWMs[thrustNum] * 0.01
                elif thrusterPWMs[thrustNum]<1500:
                    thrusterPWMs[thrustNum] += thrusterPWMs[thrustNum] * 0.01

    thrusterPWMs = [round(x) for x in thrusterPWMs]
    return thrusterPWMs

#Values will converge to 1500 (0 power) when adjusted
pwmList = [1900.0, 1100.0, 1700.0, 1700.0, 1700.0, 1700.0, 1700.0, 1700.0]
#print(getAmpTotal(pwmList));
print(tempSafeGuard(pwmList))
