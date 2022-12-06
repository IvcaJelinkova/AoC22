# task: 
""" 
How many characters need to be processed before the first start-of-packet marker is detected?


Your subroutine needs to identify the first position where the four most recently received characters were all different. 

Here are a few more examples:

bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
"""
my_index = 0

def create_quad(data, my_index): 
    """Return four consecutive characters. """
    end = False
    while end == False: 
        string = data[my_index:my_index+4]
        quad = []

        print('string: ', string, 'index: ', my_index)
        for char in string: 
            print('my char: ', char, end='\t')

            if char in quad: 
                print('char already in quad :-( ', end='\t')
                my_index += 1
                print('my new index: ', my_index)
                break
                
            else: 
                quad.append(char)
                print('char not in quad, new quad: ', quad)
                if len(quad) == 4: 
                    print('\njuchuuu')
                    print('my string is: ', quad)
                    end_index = my_index+4
                    print('my index is: ', my_index, 'to: ', end_index)
                    end = True
                    return quad, end_index
        if my_index+3 == len(data): 
            end = True
    return quad, end_index

with open('day06_input.txt') as f:
    data = f.read().strip().split('\n')
data = ''.join(data)
print(data, len(data))
#while my_index <= len(data): 
quad, end_index = (create_quad(data, my_index))
if len(quad) == 4: 
    print(quad, end_index)
    False


