# 딕셔너리 : 매핑 자료구조
# 키key에 값value을 연결시키는 방식으로 데이터를 다루는 방법 제공
# 키는 저장된 데이터를 식별하기 위한 번호나 이름
# 값은 각 키에 연결되어 저장된 테이터
# 따라서 키만 알면 데이터를 바로 찾을 수 있음
# 딕셔너리는 {} 에 키:값 형태로 이용
# 키:값이 여러개 존재할 경우, 로 구분

menu = { '1': 'newSungJuk', '2': 'showSungJuk',
         '3': 'modifySungJuk' }     # 키는 다양한 자료형으로 사용


book = {
    'bookid': '1',
    'bookname': '축구의역사',
    'publisher': '굿스포츠',
    'price': '7000'
}

order = {
    'orderid': '1',
    'custid': '1',
    'bookid': '1',
    'saleprice': 6000,
    'orderdate': '2014-07-01'
}

custromer = {
    'custid': '1',
    'name': '박지성',
    'address': '영국 멘체스타',
    'phone': '000-5000-0001'
}

print(book)

books_list = []
books_list.append( book )       # 생성한 딕셔너리를 배열에 저장
books_list.append( book )
books_list.append( book )

print( books_list )

# 딕셔너리 처리 메서드
print( '1' in book )        # 딕셔너리에서 in 연산자는 key를 검색
print('bookid' in book)

print( book[ 'bookid' ] )       # 딕셔너리에서 키로 검색
print( book[ 'bookname' ] )
print( book[ 'price' ] )
# print( book[ 'orderid' ] )      # 존재하지 않는 키 검색시 오류!

print( book.get( 'bookname' ) )
print( book.get( 'orderid' ) )      # 존재하지 않는 키 검색시 None 출력

bkname = book[ 'bookname' ]     # 키로 검색후 값 출력
print( bkname )

print( book.get( 'bookid' ) )
book[ 'bookid' ] = 99     # 키로 값 수정
print( book.get( 'bookid' ) )

print( book )
book.update( { '판형': '3 x 4' } )        # 새로운 키: 값 추가
print( book )

print( book )
book.update( { '판형': '6 x 10' } )        # 새로운 키: 값 수정
print( book )

del book[ '판형' ]        # 기존 키 삭제
print( book )

# book.clear()        # 모든 키 삭제

print( book.keys() )        # 모든 키를 출력
print( book.values() )        # 모든 값을 출력
print( book.items() )       # 모든 키:값을 튜플로 출력

items = book.items()       # 모든 키:값을 튜플-리스트로 출력
print( list( items ) )