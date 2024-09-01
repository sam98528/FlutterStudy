## Button ##

- TextButton, ElevatedButton 등등
- onPressed : Function을 넘겨줘야함
```dart
TextButton(onPressed: (){}, chile, Text("ROLL")); // Annoymous 함수
```

- Button 에다가 [[Icon]]을 넣는 방법
```dart
OutlineButton.icon(
	icon : const Icon(Icon.xxxx)
	label: Text("HEELO") // 이제 Child 대신 Label  사용
); // icon을 넣는 Constructor

```

- Button Radius, Padding 넣는법
```dart 
ElevatedButton(
	onPressed: onTap,
	style: ElevatedButton.styleFrom(
	backgroundColor: const Color.fromRGBO(255, 255, 255, 0.9),
	foregroundColor: const Color.fromRGBO(0, 0, 0, 1),
	shape:
		RoundedRectangleBorder(borderRadius: BorderRadius.circular(40)),
	padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 40)),
	child: Text(text));
```