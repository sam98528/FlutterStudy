## StatelessWidget vs StatefulWidget ##

- Stateless 말그대로 정적, Stateful 동적
- State에 따라서 변하냐 안변하냐

|                   | StateLessWidget        | StatefulWidget      |
| ----------------- | ---------------------- | ------------------- |
| **Definition**    | 정적, UI변경 없음            | State에 따라서 UI업데이트   |
| **Update <br>시점** | Parent Widget이 업데이트 하면 | State가 변할때마다 UI업데이트 |
| **사용처**           | 제일 많이 사용됨              | UI 변동이 필요한 경우       |

```Dart
// StateLessWidget
class CustomText extends StatelessWidget {
	const CustomText(this.text, {super.key});
	final String text;
@override
	Widget build(BuildContext context) {
		return Text(
			text,
			style: const TextStyle(fontSize: 28.0, color: Colors.white),
		);
	}
}

//StatefulWidget
class DiceRoller extends StatefulWidget {
	const DiceRoller({super.key});
@override
	State<StatefulWidget> createState() {
		return _DiceRollerState();
		// State를 관리하는 StateClass를 호출
	}
}

class _DiceRollerState extends State<DiceRoller> { 
// _DiceRollerState, UnderBar -> Private
	var activeDiceImage = "assets/images/dice-6.png"; 
	
	void rollDice() {
		setState(() {
		// setState 말그대로 State를 변경하니
		// UI를 다시 그려달라고 하는 함수
		// Notify the framework that the internal state of this object has changed.
		activeDiceImage = "assets/images/dice-4.png";
		});
	}
@override
	Widget build(BuildContext context) { // StateLessWidget이랑 똑같이 Build
		return Column(
			mainAxisSize: MainAxisSize.min,
			children: [
				Image.asset(
					activeDiceImage,
					width: 200,
				),
			const SizedBox(
				height: 20,
			),
			TextButton(
				onPressed: rollDice,
				style: TextButton.styleFrom(
				padding: const EdgeInsets.all(20),
				foregroundColor: Colors.white,
				textStyle: const TextStyle(fontSize: 28)),
					child: const Text("Roll Dice"))
			],
		);
	}
}
```

Refers to: [[StatefulWidget]]