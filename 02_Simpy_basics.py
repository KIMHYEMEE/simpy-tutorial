# Ref: https://simpy.readthedocs.io/en/latest/topical_guides/simpy_basics.html

'''
example 함수는 Timeout 이벤트를 먼저 생성
environment, delay, value는 이벤트로 보내짐
Timeout은 now+delay에 예정되어 있음

(설명 검토 필요)
'''
import simpy
def example(env):
    value = yield env.Timeout(delay=1, value=42)
    print('now=%d, value=%d' % (env.now, value))

env = simpy.Environment()
example_gen = example(env)
p = simpy.events.Process(env, example_gen)

env.run()