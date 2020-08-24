def reverse_int(x):
    """
    :type x: int
    :rtype: int
    """
	#setting the maximum limit for an integer
    neg_limit= -0x80000000
    pos_limit= 0x7fffffff
	
	#if blank input is given
	
    num_str = str(x)
	
    if len(num_str) <= 0:
        return x
		
	#creating the reverse string
    rev_str = ""
    rev_num = 0
	
	#if it is a negative number, the negative sign is to be 
	#positioned at the start of the reversed number
    if x<0:
        rev_str = "-" + num_str[1:len(num_str)][::-1] 
        if int(rev_str) & neg_limit == neg_limit:
            rev_num = int(rev_str)
        else:
            rev_num = 0
			
    else:
        rev_str = num_str[0:len(num_str)][::-1]
        rev_int = int(rev_str)
        if rev_int & pos_limit == rev_int:
            rev_num = rev_int
        else:
            rev_num = 0
			
    #print(num_str)
    #print(rev_str)
    print(rev_num)
    return rev_num
	
	
if __name__ == "__main__":
    number = int(input("Enter number"))
    reverse_int(number)
	