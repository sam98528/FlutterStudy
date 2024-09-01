## Future ##

- Dart에서 future는 말그대로 지금은 없지만 미래에 요청한 데이터 혹은 에러가 담길 변수 타입이라서 생각하면 된다. 
- 싱글스레드 환경에서 비동기처리를 위해 존재한다. 
```dart
showDatePicker( // Type을 보면 Future?로 되어 있다. 
	barrierColor: Colors.blue,
	context: context,
	initialDate: now,
	firstDate: DateTime(now.year - 1),
	lastDate: DateTime(now.year + 1)
);

//Then 방법
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
//Async Await
void _presentDatePicker async {
	final pickedDate = await showDatePicker(
		barrierColor: Colors.blue,
		context: context,
		initialDate: now,
		firstDate: DateTime(now.year - 1),
		lastDate: DateTime(now.year + 1)
	);
	print(showDatePicker); 
	// Await를 위에 걸었기 때문에,
	//Print문은 pickedDate의 값이 정해져야지만 호출이됨. 
}

```
Refers to : [[Then]] , [[Async & Await]]
