# BaekJoonHelper with Python

프로그래머스와 달리 백준에서는 함수의 return이 아닌 표준 입,출력으로 채점을 진행하는데, 이런 과정에서 매번 Input을 집어넣기 귀찮아서 만들었습니다.  

버그 발생시 Issue에 적어주시면 감사하겠습니다.

## Update 1.2

- 문제 설명 크롤링하여 Readme 생성
- Test case 크롤링  
	by. [14blacktea](https://github.com/14blacktea/BaekJoonHelper)

<hr/>

## Usage

#### 설치 
> [다운로드 링크](https://github.com/ukcastle/BaekJoonHelper/releases/download/v1.2/bj_helper_1.2.tar.gz)  

```sh  
or

wget https://github.com/ukcastle/BaekJoonHelper/releases/download/v1.2/bj_helper_1.2.tar.gz  

or

git clone https://github.com/ukcastle/BaekJoonHelper
```

#### 라이브러리 다운로드
```sh
pip install -r requirments
```

<br>

#### mkdir.py

```sh
python mkdir.py {문제 번호}
```
<img src="./readme_img/1_mkdir.gif" width="80%">

- v1.2 수정 
  - 문제 생성시, README.md 파일을 만들어 문제에 대한 설명을 자동으로 추가하도록 변경    
  - 문제부분은 그림, 표 등 다양한 태그가 올 수 있으나, 이 외 입력,출력,예시는 특정 태그만 가져오도록함(필요하다면 모든 태그 가져오도록 수정)  
  - 사이트 내 제시된 예제 케이스를 가져오게 변경

<br>

#### 문제번호/solution.py에 코드 입력
<img src="readme_img/7_change_solution.gif" width="80%">

프로그래머스와 같이 solution에 알고리즘을 정의합니다 

<br>

#### test.py

```sh
python3 test.py {문제번호}
```

<img src="readme_img/4_testpy.gif" width="80%">  

기존 unittest에서 쓰이던 -v, -b 등등의 인자들까지 모두 지원합니다  


<br>

#### test.py --test

```sh
python3 test.py {문제번호} --test
```

<img src="readme_img/5_test_arg.png" width="80%">  

만약 검사 없이 출력값만 확인해보고싶다면 `--test` 인자를 붙여줍니다  

<img src="readme_img/6_testpy_test.gif" width="80%">  

<br>

#### 제출할 때...  

<img src="readme_img/3_write_solution__.gif" width="80%">  

아직은 마땅한 방법이 생각이 나지 않아서 위와 같이 맨 아래에 solution() 함수를 적고 백준에 제출하는 방식으로 하고있습니다.  

<hr/>

#### Further Learning
- README 파일 내 mathjax를 적용할 수 없기 때문에 수식을 긁어오더라도 제대로 보여줄 수가 없음