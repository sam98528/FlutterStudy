## Color ##

- Colors -> 기본 색상 제공
- Color.fromRGBO(r,g,b,o) -> RGB + Opacity
- 이미지 색상 및 Opacity도 설정할 수 있음 
```Dart
Image.asset('assets/images/quiz-logo.png',
			width: 300,
			color: const Color.fromRGBO(255, 255, 255, 0.8),
);
```