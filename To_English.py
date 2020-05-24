# Digant Kumar
# Program that takes a number between 1 and 999 and returns a string containing the same number expressed in English

def to_english(n):
    ones = ["one","two","three","four","five","six","seven","eighth","nine"]
    special_ones = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    hundreds = ["one-hundred","two-hundred","three-hundred","four-hundred","five-hundred",
                "six-hundred","seven-hundred","eigth-hundred","nine-hundred"]
    word = str(n)
    if n == 0:
        return "Zero"
    if len(word) == 1 and n!=0:
        return ones[n-1]
    if len(word) == 2:
        if n%10 == 0:
            return tens[(n//10)-1]
        elif n//10!= 1:
            return tens[(n//10)-1] + " " + ones[(n%10)-1]
        else:
            return special_ones[(n%10)-1]
    if len(word) == 3:
        if n%100 == 0:
            return hundreds[(n//100)-1]
        elif n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19 or n%100 == 20:
            a = n%100
            b = n//100
            if a//10 == 1:
                return hundreds[b-1] + " and " + special_ones[(a%10)-1]
        else:
            a = n%100
            b = n//100
            c = a%10
            d = a//10
            if d!=0 and c!=0:
                return hundreds[b-1] + " and " + tens[d-1] + " " + ones[c-1]
            elif d==0 and c!=0:
                return hundreds[b - 1] + " and " + ones[c - 1]
            else:
                return hundreds[b - 1] + " and " + tens[d-1]
    else:
        return "The program only runs for numbers 1 to 999"        # If the number entered isn't between 1-999, this message is returned
