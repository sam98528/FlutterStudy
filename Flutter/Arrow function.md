## Arrow function ##

- 함수안에 한줄밖에 없다면, Swift에서도 줄일수 있는것 처럼 Dart도 가능하다
- `=>`

```dart
//한줄밖에 없는경우
final numCorrectQuestions = summaryData.where((data) {
	return data['correct_answer'] == data['user_answer'];
}).length;
// 이렇게 변경이 가능하다
final numCorrectQuestions = summaryData
	.where(
	(data) => data['correct_answer'] == data['user_answer'];
).length;
```