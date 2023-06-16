"""무료 주차 공간 데이터 출력, 분석, 관리에 대한 메뉴 제공 모듈

해당 모듈은 함수 start_process를 통해
메뉴를 제공하며 간단한 숫자와 문자 입력만으로
사용자와 상호작용함으로써
무료 주차 공간 데이터를 출력하고,
입력받은 키워드에 따라 데이터를 추려내고
정렬할 수 있도록 하는 기능을 수행합니다.

Version #3: 메뉴 [2] filter 구현
"""

import file_manager
import parking_spot_manager
# from parking_spot_manager import *: 메소드 사용시 모듈명 붙일 필요 x
# (어떤 모듈에 구현된 메소드인지 확인 위해 해당 파일에서는 사용하지 않음)

def start_process(path):
    """무료 주차 공간 데이터에 관한 메뉴 제공

    숫자 입력을 통해 접근 가능한
    무료 주차 공간 데이터를 활용하는 메뉴 3가지와
    종료를 위한 메뉴 1가지를 제공합니다.
    첫번째 메뉴 print는 주차 공간 데이터를
    출력하도록 하며,
    두번째 메뉴 filter는 주차 공간 데이터를
    입력한 키워드에 따라 추려내고,
    세번째 메뉴 sort는 키워드를 기준으로
    데이터를 정렬합니다.
    네번째 메뉴 exit은 반복되는 메뉴를
    종료하는 기능을 수행합니다.
    exit을 선택하지 않는 한 특정 메뉴를 통한
    기능 수행 후에도 메뉴를 반복해서 제시합니다.

    Args:
        path (str): 주차 공간 데이터가 담긴 파일의 경로

    """

    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)

        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)

            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)

            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)

            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)

            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))

                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)

            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break

        else:
            print("invalid input")