print("="*50)
print("■딕셔너리를 사용한 혈액형 판별 프로그램")
print("-"*50)
print(">>혈액형의 특성은 다음과 같습니다.")

bld=input("알파벳을 입력하세요.")
if 1:
    choicevalue = { 'a':"A형-차분한 성격",
                    'b':"B형-발전적 성격",
                    'c':"C형-활발한 성격",
                    'd':"D형-도전적 성격"}
    print("알파벳 입력(a~d):",bld)
    print(choicevalue.get(bld))
else:
    print("입력한 알파벳",[bld],"은(는) 지원되지 않습니다.")
    print("프로그램을 다시 시작하세요.")
print("프로그램을 종료합니다.")
print("="*50)


#출력
blood=input(">>알파벳 입력(a~d):")
#딕셔너리
bl={'a': "A형-차분한성격",
    'b': "B형-발전적 성격",
    'c': "C형-활발한 성격",
    'd': "D형-도전적 성격"}
if blood in bl:
    print(">>선택한 혈액형 결과: %s " %bl.get(blood))
else:
    print(">>입력한 알파벳 %s는 지원하지않습니다." %blood)
    print(">>프로그램을 다시 시작하세요.")
