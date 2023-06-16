"""무료 주차 공간에 관련된 클래스 및 함수 구현 모듈

해당 모듈은 무료 주차 공간의 데이터를
저장, 분석, 관리하고 출력합니다.
클래스 parking_spot을 활용하여 주차 공간 정보를
저장하고 반환하며, str_list_to_class_list 함수를 통해
주차 공간에 대한 문자열 리스트를
클래스 parking_spot 객체 리스트로 변환 및 반환,
print_spots 함수를 통해 주차 공간 정보를
출력하는 기능을 수행합니다.

Version #2: 클래스 parking_spot과
함수 str_list_to_class_list, print_spots 구현
"""

class parking_spot:
    """주차 공간의 정보를 저장하는 클래스

    주차 공간의 정보 6가지를 생성자를 통해 객체 정보로 저장합니다.
    해당 정보를 알아보기 쉽게 string 타입으로 정리한 메소드 __str__와,
    객체 변수를 반환하는 메소드 get을 제공합니다.
    """

    def __init__(self, name, city, district, ptype, longitude, latitude):
        """주차 공간의 정보를 받는 생성자

        주차 공간의 정보인 자원명, 시도, 시군구,
        주차장유형, 경도, 위도를 받습니다.

        Args:
            name (str): 자원명
            city (str): 시도
            district (str): 시군구
            ptype (str): 주차장 유형
            longitude (float): 경도
            latitude (float): 위도
        """

        self.__item = {'name': name, 'city': city, 'district': district,
                       'ptype': ptype, 'longitude': longitude, 'latitude': latitude}

    def __str__(self):
        """객체가 저장한 주차 공간 정보 반환

        주차 공간의 정보 6가지를
        가독성 높도록 포맷팅한 문자열 s로 반환합니다.

        Returns:
            str: '[자원명(주차장 유형)] 시도 시군구(lat:위도, long:경도)' 형태
        """

        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def get(self, keyword = 'name'): # 기본인수 name 설정
        """객체가 저장한 주차 공간 정보 6가지 중 요청 정보 반환

        주차 공간의 정보 6가지 중
        인수를 통해 입력한 종류의 정보를 반환합니다.

        Args:
            keyword (str): 주차 공간 정보의 한 종류, 기본인수는 'name'

        Returns:
            str or float: 자원명, 시도, 시군구, 주차장유형, 경도, 위도 중 입력된 키워드에 해당하는 종류의 정보
        """

        return self.__item[keyword]


# for 문으로 str_list 탐색 -> split 함수 통해 쉼표로 구분된 데이터 분리 -> 분리한 데이터 spot 생성자에 넣어 인스턴스 spot 생성
# -> spot을 spots 객체 리스트에 append
def str_list_to_class_list(str_list):
    """주차 공간 정보가 담긴 문자열 리스트를 parking_spot 클래스 객체 리스트로 변환하여 반환

    Args:
        str_list (list): 주차 공간 정보가 담긴 문자열 리스트

    Returns:
        list: 주차 공간 정보를 저장한 객체가 담긴 객체 리스트
    """

    spots = []

    for str in str_list:
        spot_data = str.split(',')
        spot = parking_spot(spot_data[1], spot_data[2], spot_data[3],
                            spot_data[4], float(spot_data[5]), float(spot_data[6]))
        spots.append(spot)

    return spots

def print_spots(spots):
    """주차 공간 정보가 담긴 객체 리스트 출력

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
    """

    print("---print elements([", len(spots), "])---", sep='')

    for spot in spots:
        print(spot.__str__())

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)