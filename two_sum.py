def two_sum(nums, target):
    """ 
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
    req_dict = {}
    
	#subtracting each element from the target and checking if the 
	#difference is present in the array
	
    for index, element in enumerate(nums):
	
        req_element = target - element
		
        #if difference b/w element in array and target is not
		#present, then saving the index of the element in the 
		#dictionary req_dict
		
        if req_element not in req_dict:
            req_dict[element] = index
		
        #if difference is present in the dictionary then, 
		#returning index saved in req_dict and current index		
        else:
            return [req_dict[req_element], index]

if __name__ == '__main__':
    nums= [int(x) for x in input("Give the array").split()]
    target = int(input("Give the target"))
    result = two_sum(nums, target)
    print(result)
	




