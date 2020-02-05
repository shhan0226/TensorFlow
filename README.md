# TensorFlow-Basics



## Introduction
기본적인 머신러닝/딥러닝 연습 및 예제

## Installation
1. 텐서플로우가 지원하는 파이선 버전 확인 <br>
https://www.tensorflow.org/install/source_windows?hl=ko.

2. 인터넷--> Python Releases for Windows
(dowload --> release 64bit executable installer--> install now)

3. 파이선 설치 시작해서 인스터올 선택, add PaTH 체크

4. MS Visual Studio 2015 c++ 패키지 설치

5. pip install --upgrade tensorflow <br>
pip install --ignore-installed --upgrade tensorflow==1.6.0 <br>
https://www.tensorflow.org/install/gpu?hl=ko ==> 여기서 설치 

6. 실행하기 IDE 켜서 실행해보기<br>
import tensorflow as tf  <br>
hello=tf.constant("Hello World!") <br>
sess = tf.Session() <br>
print(sess.run(hello)) <br>

7. warning 발생시 <br>
pip show numpy <br>
pip uninstall numpy (till you uninstall all versions) <br>
pip install numpy==1.16.4 <br>

8. pip3 install -U pip virtualenv

9. pip install --upgrade tensorflow-gpu

10. GPU 필요 파일 받기 <br>
CUDA® Toolkitopen_in_new - TensorFlow는 CUDA 10.0을 지원합니다(TensorFlow 1.13.0 이상). 
cuDNN SDKopen_in_new(7.4.1 이상) ==> 내부 파일 이동하기 <br>
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin;%PATH% <br>
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64;%PATH% <br>
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include;%PATH% <br>

11. [matplotlib](https://matplotlib.org/) 설치 <br>
python -m pip install -U pip <br>
python -m pip install -U matplotlib <br>

## Reference
* [모두를 위한 머신러닝/딥러닝 - 김성훈](http://hunkim.github.io/ml/)
  * 예제 : https://github.com/hunkim/DeepLearningZeroToAll

* [파이썬 텐서플로우 & 머신러닝 기초 - 나동빈](https://www.youtube.com/watch?v=qxUD7fOseBQ&list=PLRx0vPvlEmdAbnmLH9yh03cw9UQU_o7PO)

