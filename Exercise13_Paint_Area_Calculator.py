# Height and Width of Wall , cal. how many Cans of pain you will needs to buy. 
import math

def paint_cane (t , w , cover):
    num_can = (t*w)/cover
    round_canes =  math.ceil(num_can)
    print(F" You will  Need {round_canes} canes of paints ")




total_height = int(input("Enter a heigth in (meter) = "))
total_width = int(input("Enter a width in (meter)  = "))
coverage  = int(input("Enter a no. of walls to be paint = "))   
paint_cane(t = total_height , w = total_width , cover = coverage )

