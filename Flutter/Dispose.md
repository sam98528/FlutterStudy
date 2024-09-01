## Dispose ##

- iOS로 치면 ViewdidUnload 같은 개념
- TextEditingController가 메모리를 계속 잡아먹으니, Dispose를 수동으로 하는 코드
- dispose는 State에서만 존재한다. 
```dart
class _NewExpenseState extends State<NewExpense> {
	final _titleController = TextEditingController();
@override
	void dispose() {
		_titleController.dispose();
		super.dispose();
	}
```

Refers to : [[LifeCycle]]