"""무료 주차 공간에 관련된 클래스 및 함수 구현 모듈

해당 모듈은 무료 주차 공간의 데이터를
저장, 분석, 관리하고 출력합니다.
클래스 parking_spot을 활용하여 주차 공간 정보를
저장하고 반환하며, str_list_to_class_list 함수를 통해
주차 공간에 대한 문자열 리스트를
클래스 parking_spot 객체 리스트로 변환 및 반환,
print_spots 함수를 통해 주차 공간 정보 출력,
filter_by_name/city/district/ptype/longitude/latitude
함수를 통해 입력한 키워드에 따라 추려낸 데이터 반환,
sort_by_keyword 함수를 통해 정렬기준에 따라
정렬한 데이터를 반환하는 기능을 수행합니다.

Version #4: 함수 sort_by_keyword 추가
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


# version #3: filter_by_name, filter_by_city, filter_by_district, filter_by_ptype, filter_by_location 추가
# 리스트 함축에서의 if 사용 (https://jinmay.github.io/2020/05/28/python/python-list-comprehension-with-if-statement/)
# 특정 문자열 포함 여부: in, not in 키워드 사용(https://www.naragara.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AC%ED%95%A8%EC%97%AC%EB%B6%80-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95/)
def filter_by_name(spots, name):
    """입력한 인수가 포함된 자원명을 가진 객체만 추려낸 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        name (str): 필터 기준이 되는 자원명 키워드

    Returns:
        list: 키워드가 포함된 자원명 가진 객체로 추려진 리스트
    """

    filter_spots = [spot for spot in spots
                    if name in spot.get('name')]
    # if name in spot.__item['name']] -> 필드에 바로 접근할 수 없으므로 get 메소드 이용해야 함

    return filter_spots

def filter_by_city(spots, city):
    """입력한 인수가 포함된 시도를 가진 객체만 추려낸 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        city (str): 필터 기준이 되는 시도 키워드

    Returns:
        list: 키워드가 포함된 시도 가진 객체로 추려진 리스트
    """

    filter_spots = [spot for spot in spots
                    if city in spot.get('city')]

    return filter_spots

def filter_by_district(spots, district):
    """입력한 인수가 포함된 시군구를 가진 객체만 추려낸 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        district (str): 필터 기준이 되는 시군구 키워드

    Returns:
        list: 키워드가 포함된 시군구 가진 객체로 추려진 리스트
    """

    filter_spots = [spot for spot in spots
                     if district in spot.get('district')]

    return filter_spots

def filter_by_ptype(spots, ptype):
    """입력한 인수가 포함된 주차장 유형을 가진 객체만 추려낸 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        ptype (str): 필터 기준이 되는 주차장 유형 키워드

    Returns:
        list: 키워드가 포함된 주차장 유형 가진 객체로 추려진 리스트
    """

    filter_spots = [spot for spot in spots
                    if ptype in spot.get('ptype')]

    return filter_spots

def filter_by_location(spots, locations):
    """입력한 인수가 포함된 위치 정보를 가진 객체만 추려낸 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        locaions (tuple): 필터 기준이 되는 최소위도, 최대위도, 최소경도, 최대경도를 담은 튜플

    Returns:
        list: 입력한 위치에 해당하는 위치 정보를 가진 객체로 추려진 리스트
    """

    filter_spots = [spot for spot in spots
                    if locations[0] < spot.get('latitude') and spot.get('latitude') < locations[1]
                    and locations[2] < spot.get('longitude') and spot.get('longitude') < locations[3]]

    return filter_spots

# version #4: sort_by_keyword 함수 추가
def sort_by_keyword(spots, keyword):
    """입력한 인수를 기준으로 정렬한 객체 리스트 반환

    Args:
        spots (list): 주차 공간 정보가 담긴 객체 리스트
        keyword (str): 정렬 기준이 되는 키워드

    Returns:
        list: 기준에 따라 정렬된 객체 리스트
    """

    sorted_spots = sorted(spots, key = lambda x : x.get(keyword))

    return sorted_spots

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