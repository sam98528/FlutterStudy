## StatefulWidget ##

- State에 값을 전달하는 방법
- StatelessWidget은 State를 관리하는 Class가 없지만, StatefulWidget은 따로 있다. 
- 예를 들어서 StateLessWidget에서 StatefulWidget한테 Constructor를 통해 값을 전달하는 경우
	- StateLessWidget -> StatefulWidget ->? StateClass

```Dart
class QuestionsScreen extends StatefulWidget {
	const QuestionsScreen(this.onSelectAnswer, {super.key});
	final void Function(String answer) onSelectAnswer; 
	// 위 Function을 State에 전달해야함
@override
	State<StatefulWidget> createState() {
		return _QuestionScreenState();
	}
}

class _QuestionScreenState extends State<QuestionsScreen> {
	var currentQuestionIndex = 0;
	void answerQuestions(String selectedAnswer) {
		widget.onSelectAnswer(selectedAnswer);
		// widget. 으로 StatefulWidget에 접근할 수 있다.
		setState(() {
			currentQuestionIndex += 1;
		});
	}
@override
Widget build(BuildContext context) {
'''
'''
}
```