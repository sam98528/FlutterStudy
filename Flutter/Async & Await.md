## Async & Await ##

- await 키워드를 사용한 함수는 무조건 async 함수이어야 함.
- async 함수는 무조건 Future를 반환해야 함.
- await 을 만나면 함수를 잠시 멈추고 함수를 호출한 곳에 Future 를 return 함.
- await 가 붙은 동작이 완료되기 전까지 함수를 더 이상 진행하지 않음.
- return 을 통해 2번에서 주었던 Future 에서 return 값 반환.

```dart
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

Refers to : [[Then]] , [[Future]]
