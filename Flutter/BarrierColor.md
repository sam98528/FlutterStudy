## BarrierColor ##

- Modal 이나 특정 위젯을 보여줄때 뒤에 배경이 흐릿해지는 색깔 변경
```dart
showDatePicker(
	barrierColor: Colors.blue, 
	// Alpha 값을 조정해서 더 세세하게 바꿀수 있음.
	context: context,
	initialDate: now,
	firstDate: DateTime(now.year - 1),
	lastDate: DateTime(now.year + 1));
}
```

Refers to: [[Modal]], [[DateTime]]
