## Column & Rows ##

- 기존에는 Widget에 하나의 Child만 갖는데, Column, Rows를 활용할 수 있다.
- Column -> Vertical Axis
- Row -> Horizontal Axis
```Dart
Column(
	mainAxisSize: MainAxisSize.min
	// 기본 Max, 전체를 다 차지, min은 필요한 요소들로만 사이즈 구성 
	mainAxisAlignment: MainAxisAlignment.center
	// 기본 Start, Center로 하면 좌우가 중앙으로 
	crossAxisAlignment: CrossAxisAlignment.stretch,
	// 대각선으로 Stretch
	children: []
	//위젯 List
)
```
