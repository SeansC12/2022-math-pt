# This is the source code to find out the most optimised (meaning least surface area) dimension for a 1.5 L milk carton

number = 1500
factors_list = []
dimensions = []
total_count = 0
surface_area = []

def find_list_of_factors():
    for i in range(1, number + 1):
        if number % i == 0:
            factors_list.append(i)
            print(i)

    for i in range(1, len(factors_list)):
        number1 = 0
        number2 = 0
        number3 = 0

        number1 = factors_list[i-1]
        number3 = factors_list[-i]

        for n in range(1, factors_list[i-1] + 1):
            if factors_list[i-1] % n == 0:
                number2 = n
                number1 = factors_list[i-1] // number2
                dimensions.append([number1, number2, number3])
    
    print(factors_list)
    print(dimensions)
    
def check_dimensions():
    for i in dimensions:
        total_count = ((i[0] * i[1]) + (i[1] * i[2]) + (i[2] * i[0])) * 2
        # length times breadth, breadth times height, height times length
        surface_area.append(total_count)
    
    max_count_index = surface_area.index(min(surface_area))
    print(f"The most optimised surface area is {dimensions[max_count_index]}")
    print(f"The surface area is {min(surface_area)}")


find_list_of_factors()
check_dimensions()