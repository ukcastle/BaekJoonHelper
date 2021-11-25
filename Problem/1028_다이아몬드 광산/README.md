### 문제
<img alt="Logo" data-retina="" id="logo-header" src="https://www.acmicpc.net/https://d2gd6pc034wcta.cloudfront.net/images/logo@2x.png"/>
<p>다이아몬드 광산은 0과 1로 이루어진 R행*C열 크기의 배열이다.</p>
<p>다이아몬드는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 모양이다. 크기가 1, 2, 3인 다이아몬드 모양은 다음과 같이 생겼다.</p>
<pre>
size 1:    size 2:    size 3:
                         1
              1         1 1
   1         1 1       1   1
              1         1 1
                         1
</pre>
<p>다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하는 프로그램을 작성하시오.</p>
<pre class="sampledata" id="sample-input-1">5 5
01100
01011
11111
01111
11111
</pre>
<pre class="sampledata" id="sample-output-1">3
</pre>
<pre class="sampledata" id="sample-input-2">5 5
01100
00011
11111
01111
11111
</pre>
<pre class="sampledata" id="sample-output-2">2
</pre>
<pre class="sampledata" id="sample-input-3">4 4
0000
0000
0000
0000
</pre>
<pre class="sampledata" id="sample-output-3">0
</pre>
<pre class="sampledata" id="sample-input-4">3 6
111000
101111
111111
</pre>
<pre class="sampledata" id="sample-output-4">2
</pre>
<img class="pull-right startlink-logo" src="https://www.acmicpc.net/https://d2gd6pc034wcta.cloudfront.net/logo/startlink-logo-white-only.png"/>
<img height="1" src="https://www.acmicpc.net/https://www.facebook.com/tr?id=1670563073163149&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
<hr/>

### 입력
<p>첫째 줄에 R과 C가 주어진다. R과 C는 750보다 작거나 같은 자연수이다. 둘째 줄부터 R개의 줄에는 다이아몬드 광산의 모양이 주어진다.</p>
<hr/>

### 출력
<p>첫째 줄에 다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력한다. 만약 다이아몬드가 없을 때는 0을 출력한다.</p>
<hr/>

### 입력 예시 1
5 5
01100
01011
11111
01111
11111

### 출력 예시 1
3

<hr/>

### 입력 예시 2
5 5
01100
00011
11111
01111
11111

### 출력 예시 2
2

<hr/>

### 입력 예시 3
4 4
0000
0000
0000
0000

### 출력 예시 3
0

<hr/>

### 입력 예시 4
3 6
111000
101111
111111

### 출력 예시 4
2

<hr/>

