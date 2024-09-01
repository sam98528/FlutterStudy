## TextField ##

```dart 
class _NewExpenseState extends State<NewExpense> {

// Onchanged 사용하는 방법
var _enteredTitle = '';
void _saveTitleInput(String inputValue) {
	_enteredTitle = inputValue;
}
TextField(
	onChanged: _saveTitleInput,
	maxLength: 50,
	keyboardType: TextInputType.text,
	decoration: const InputDecoration(label: Text("Title")),
),

//TextEditingController

final _titleController = TextEditingController();
@override
	void dispose() { //State Class에서만 사용가능 
		_titleController.dispose();
		super.dispose();
	}
TextField(
	controller: _titleController,
	maxLength: 50,
	keyboardType: TextInputType.text,
	decoration: const InputDecoration(label: Text("Title")),
),

print(_titleController.text);
```

Refers to : [[LifeCycle]], [[StatefulWidget]]