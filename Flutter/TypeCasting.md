## TypeCasting ##

- Dart 에서 TypeCasting은 `as` 를 쓴다
```dart
final List<Map<String, Object>> summaryData = getSummaryData()

List<Map<String, Object>> getSummaryData() {
	final List<Map<String, Object>> summary = [];
	for (int i = 0; i < selectedAnswer.length; i++){
		summary.add({
			'question_index' : i,
			'question': questions[i],
			'correct_answer' : questions[i].answers[0],
			'user_answer' : selectedAnswer[i]
		});
	}
return summary;
}

summaryData['question_index'] // object
summaryData['question_index'] as int // Int
summaryData['correct_answer'] as String // String
```


Refers to: [[Map]], [[Type-Safe Language]], [[As String vs toString()]]
