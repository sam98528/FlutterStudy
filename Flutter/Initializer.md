## Initializer ##

- Class Constructor 에서 initializer를 함께 구현할 수 있다.
```dart
class Expense {
	final String id;
	final String title;
	final double amount;
	final DateTime date;

	Expense(
		{required this.title, 
		required this.amount, 
		required this.date})
		: id = uuid.v4(); // Initializer
}

```