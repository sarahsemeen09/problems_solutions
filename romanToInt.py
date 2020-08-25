def romanToInt(s: str) -> int:

        r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        i = 0
        res = 0
        
        while i < len(s):
		    #getting the number equivalent to the roman number
            num1 = r_dict.get(s[i])
            
            if (i+1 < len(s)):
                num2 = r_dict.get(s[i+1])
                
				#if the number preceding the next number is greater, just adding the numbers to the result
                if ( num1 >= num2):
                    res = res + num1
                    i = i+1
                #if the number preceding the next number is lesser, then subtracting the first number from the second
				# for example IX = 10-1 = 9; IV = 5-1 = 4; whereas 
                else:
                    res = res + (num2 - num1)
                    i = i+2
            
            else:
                res = res + num1
                i = i+1
                
        print(res)
        return res

if __name__ == "__main__":
    string = str(input("Enter the roman number"))
    romanToInt(string)