'''
- 새로운 이벤트를 생성하기 위해서는 environment 필요 
  -> 함수의 입력값으로 env 입력됨
- while 구문으로 인해 종료되지 않지만, yield 상태에 도달하면 다시 처음부터 실행됨
- timeout 시간만큼 process의 대기(작업) 발생
'''

import simpy

def car(env): # generator function
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

env = simpy.Environment()
env.process(car(env)) # car를 process로 정의
env.run(until=15)