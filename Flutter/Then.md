## Then ##

- Future 타입의 값이나 에러가 결정되면 호출되는 코드블록
- Then은 Async/Await랑 다르게 
```dart
void _presentDatePicker(){
	showDatePicker( // Type을 보면 Future?로 되어 있다. 
		barrierColor: Colors.blue,
		context: context,
		initialDate: now,
		firstDate: DateTime(now.year - 1),
		lastDate: DateTime(now.year + 1)
	).then((value){ // Show DatePicker에서 값이나 에러가 결정이 되면
		print(value); // Print 해라.
	});
	print("HELLO"); // Then이 호출되지 않아도, 코드가 멈추지 않고 계속 진행됨.
}

```

Refers to : [[Future]], [[Async & Await]]