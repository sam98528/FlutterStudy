## Lifting State ##

- StatefulWidget 안에 StateLessWidget이 있는데, child Widget에서 StatefulWidget의 State를 변경하는 방법
- statefulWidget처럼 똑같이 만들되, 함수를 widget 인자로 전달 (Constructor 활용)
- StateLessWidget에서는 `final void Function() temp;` 로 받음
- 버튼 클릭하면 해당 함수 호출 
- 단 문제는 UI를 그리는 State 인경우, variable이 생성되는 시점이 너무 빠르면, UI그리는데 이상이 생김, 따라서 InitState() 함수에서 Initial State를 선언

```Dart

// Parent Widget? 상위 Widget

class _QuizState extends State<Quiz> {
	// Widget activeScreen = StartContainer(switchScreen) X
	// activeScrren이 생성되는 시점과 SwitchScreen이 생성되는 시점이 거의 동시라서, 
	// 에러가 발생함
	Widget? activeScreen;
@override
	void initState() {
		activeScreen = StartContainer(switchScreen); // 함수로 전달
		super.initState();
	}
	void switchScreen() {
		setState(() {
		activeScreen = const QuestionsScreen();
		});
	}
@override
Widget build(BuildContext context) {
	return MaterialApp(
		home: Scaffold(
		body: Container(
		'''
		'''
		child: activeScreen)),
	);
}

//StartContainer 하위 Widget
class StartContainer extends StatelessWidget {
	const StartContainer(this.startQuiz, {super.key}); // Constructor 인자로 받고
	final void Function() startQuiz; // Final void Function()으로 저장
@override
	Widget build(BuildContext context) {
		return Container(
		'''
		'''
		child: OutlinedButton(onPressed: startQuiz, xxx)
```)
		)
```

Refers to : [[StatelessWidget vs StatefulWidget]]