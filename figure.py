""""
figure 모듈은 도형과 관련된 함수 및 클래스를 제공하는 모듈입니다.
'line' 클래스를 이용하여 선의 길이를 설정하고
'area_square', 'area_circle', 'arera_regular_triangle' 함수로 
각각 정사각형의 넓이, 원의 넓이, 정삼각형의 넓이를 반환합니다. 
"""

import math #math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기

class Line:
    __length=1
    """
    'line' 클래스는 선의 길이에 대해 저장하는 클래스입니다.
    변수로는 외부에서 접근할 수 없는 '__length'가 있으며,
    해당 변수를 수정하고 접근하기 위해
    'set_length'와 'get_length' 매소드를 제공합니다. 
    """
    def __init__(self, length):
        """ 
        클래스를 생성할 때 처음 길이를 입력받습니다.
        Args:
           length (int or float): 초기 선의 길이
        """
        if( (type(length) ==int or type(length)==float) and length > 0):
            self.__length = length
        
    def set_length(self, length):
        """
        선의 길이를 수정합니다.
         Args: 
           length (int or float): 수정하고자 하는 길이
        """
        if( (type(length) == int or type(length)==float) and length > 0):
             self.__length = length
       
        
        
    def get_length(self):
        """객체에 저장된 선의 길이를 반환합니다.
        Returns:
           int or float: 저장된 선의 길이
        """
        return self.__length
    
def area_square(line):
    """길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
       line (int or float): 변의 길이
    Returns:
       int or float: 정사각형의 넓이를 반환
    """
    if(type(line) != Line):
        return 0
    else: 
        area = line.get_length() ** 2
        return area
    

def area_circle(line):
    """길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args: 
       line (int or float): 반지름의 길이
    Returns:
       int or float: 원의 넓이를 반환
    """
    if(type(line) != Line):
        return 0
    else: 
        area = line.get_length() ** 2 * math.pi
        return area

def area_regular_triangle(line):
    """길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
       line (int or float): 한 변의 길이
    Returns:
       int or float: 정삼각형의 넓이를 반환
    """
    if(type(line) != Line):
        return 0
    else: 
        area = line.get_length() ** 2 * math.sqrt(3) / 4
        return area
    

