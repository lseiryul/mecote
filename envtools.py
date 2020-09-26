class S:
    # 특정 객체의 정보를 표현하기 위한 도구
    def __init__(self, o):
        self.o = o
        self.name = o.__name__
        self.type_ = type(o)

        try:
            self.length = len(o)
        except TypeError:
            self.length = None

    def __repr__(self):
        return f'''Type:{self.type_}
                
                '''



class Tracer:
    # 디버거/로거와 비슷한 역할. 단계나 조건에 따라 정보를 수집하며, 예외 발생을 통한 탈출을 지원한다.
    pass


class Problem:
    # 하나의 문제 환경을 구현. 특정 모듈(*.py 파일)에 구현된 'solution(...)' 메쏘드를 호출하여, 주어진 테스트케이스에 대한 유닛 테스트를 수행.
    pass


class Refactogenerator:
    # 리펙터링 과정을 거쳐, 코드를 자동 생성 또는 보정하는 작업을 담당하려고 함.
    # <Problem> class 같은 목적의 오브젝트가 테스트(unittest) 상황을 구현하는 경우가 있을 수 있음.
    pass


class View:
    # 특정 자료 형태의 시각화를 수행하고 디스플레이 할 수 있도록 만들 예정.
    NotImplemented


# 그리고 실행 시간 출력해주거나 하는 녀석도 추가해야.
# +이 프로젝트는 technique를 위한 것이기도... 실력보다는 활용도 측면이라 조금 모호한 말이긴 함<<
