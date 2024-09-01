## Dismissible ##

- The [key] argument is required because [Dismissible]s are commonly used in lists and removed from the list when dismissed. Without keys, the default behavior is to sync widgets based on their index in the list, which means the item after the dismissed item would be synced with the state of the dismissed item. Using keys causes the widgets to sync according to their keys and avoids this pitfall.


```dart
//Swipeable Listview Dismissiable
ListView.builder(
	itemCount: expenses.length,
	itemBuilder: (ctx, index) => 
	Dismissible(
		onDismissed: (direction) { // 방향에 따라서
			removeExpense(expenses[index]);
		},
		key: ValueKey(expenses[index]),
		child: ExpenseItem(expenses[index])
	),
);
```
Refers to : [[ListView]]