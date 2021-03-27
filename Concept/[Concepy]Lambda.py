# Title         : [Concept]Lambda.py
# Description   : 람다식 활용 예제

# 일반적인 sort함수 꼴
print(sorted(['Some', 'words', 'sort', 'differently']))

# 람다를 활용한 sort 함수, Some을 lower 시키고 난 후에 sorted를 적용한다. 단 원본함수는 유지된다.
# 람다는 원본 함수를 유지하지만, 이를 특정 조건문에서 돌리고 싶을 때 꼭 필요한 기법이다.
# key=lambda x: x.lower(), key=lambda y: y.upper()와 같이 사용할 수 있다.
print(sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower()))
print(sorted(['Some', 'words', 'sort', 'differently'], key=lambda speling: speling.upper()))