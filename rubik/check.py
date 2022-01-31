import rubik.cube as rubik
#Return {'status': 'ok'} if pass all conditions 
#Return {'status': 'error: xxx'} where 'xxx' is an appropriate error message 
def _check(parms):
    result={}
    #Value of cube is present
    encodedCube = parms.get('cube',None) 
    if (encodedCube == None):
        result['status'] = 'error: xxx'
    #Value of cube is a string
    elif (isinstance(encodedCube, str) == False):
        result['status'] = 'error: xxx'
    #Value of cube has 54 elements
    elif (len(encodedCube) != 54):
        result['status'] = 'error: xxx'
    #Value of cube has 9 occurrences of 6 colors
    elif not result:
        color_dict = {}
        for element in range(0, len(encodedCube)):
            if (encodedCube[element] in color_dict):
                color_dict[encodedCube[element]] += 1
            else:
                color_dict[encodedCube[element]] = 1
        #Value of cube has of 6 colors
        if (len(color_dict) != 6):
            result['status'] = 'error: xxx'
        #And each color has 9 characters
        for element in color_dict:
            if (color_dict[element] != 9):
                result['status'] = 'error: xxx' 
                break
    #Value of cube has each middle face being a different color
    elif not result:
    #Middle face start from number 5(index 4), and increasing 9 every time    
        mid_list = []
        mid_face = 4
        for element in range(6):
            if(encodedCube[mid_face] in mid_list):
                result['status'] = 'error: xxx' 
                break 
            mid_list.append(encodedCube[mid_face])
            mid_face += 9
        
    #Extra: Value of cube does not has contradictory color
    #elif not result:
        
    #The cube string fits all conditions
    else:
        result['status'] = 'ok'
    return result