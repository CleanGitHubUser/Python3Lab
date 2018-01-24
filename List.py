# 파이썬 자료구조
# 리스트 : sequence 자료구조를 사용
# sequence : 순서가 있는 데이터 구조를 의미
# 리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용
# 리스트는 [] 을 이용해서 각 요소에 접근할 수 있다.
msg = 'Hello, World!!'

# 파이썬에서는 자료구조를 의미하는 접미사를
# 변수명에 사용하기도 한다

list1_list = []                                  # 빈리스트
list2_list = [ 1, 2, 3, 4, 5 ]                   # 숫자
list3_list = [ 'a', 'b', 'c' ]                   # 문자
list4_list = [ 'a', 'b', 'c', 1, 2, 3, True ]    # 혼합

print( list1_list )

# 간단한 연사
# 요소 조냊 여부 파악 : in/not in 연산자
print( 1 in list1_list )
print( 'a' in list1_list )
print( 3 in list1_list )

# 길이 연산 : len()
print( len( list1_list ) )
print( len( list2_list ) )

# 연결 연산 : +
print( list2_list + list3_list )

# 반복 연산 : *
print( list2_list * 2 )

# 요소의 특정값 참조 : index 사용

