#Given data
cost_per_usb=6
budget=50

#Code to calculate number of USB sticks girl can buy from the available budget
number_of_usb_sticks= budget//cost_per_usb  
#The '//' is the floor division operator in Python,it rounds down the result to the largest whole number

#Code to calculate the remaing amount of money
remaining_amount= budget - cost_per_usb * number_of_usb_sticks

#Result
print(f'The girl can buy {number_of_usb_sticks} USB sticks.')
print(f'The girl has {remaining_amount}£ pounds remaing.')
