## Getter ##

- Getter를 특별하게 선언할 수 있음
``` Dart
List<Map<String, Object>> getSummaryData() { // 함수
	final List<Map<String, Object>> summary = [];
	for (int i = 0; i < selectedAnswer.length; i++) {
		summary.add({
			'question_index': i,
			'question': questions[i].text,
			'correct_answer': questions[i].answers[0],
			'user_answer': selectedAnswer[i]
		});
	}
return summary;
}

List<Map<String, Object>> get summaryData{ // 변수 Getter
	final List<Map<String, Object>> summary = [];
	for (int i = 0; i < selectedAnswer.length; i++) {
		summary.add({
			'question_index': i,
			'question': questions[i].text,
			'correct_answer': questions[i].answers[0],
			'user_answer': selectedAnswer[i]
		});
	}
return summary;
}
```