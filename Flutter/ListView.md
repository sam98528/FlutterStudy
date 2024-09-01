## ListView ##

- 기본적으로는 Scroll이 가능한 List를 보여주는 Widget
- Column은 해당 위젯이 생성되는 시점에 모든 List를 한번에 다 그리기 때문에, List의 수가 정확하지 않고 늘어날수 있다면, Listview를 사용하는것이 맞다.

```dart
ListView(children : [xxxxx]); // 이렇게 하면 Column같이 한번에 렌더림됨, 단 스크롤 가능

Widget build(BuildContext context) {
	return ListView.builder(
	itemCount: expenses.length, // itemCount가 아래 index로 전달됨
	itemBuilder: (ctx, index) => Text(expenses[index].title),
	); 
}

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

Refers to: [[ListView vs ListView.builder vs Column]], [[Column & Rows]]

The [key] argument is required because [Dismissible]s are commonly used in lists and removed from the list when dismissed. Without keys, the default behavior is to sync widgets based on their index in the list, which means the item after the dismissed item would be synced with the state of the dismissed item. Using keys causes the widgets to sync according to their keys and avoids this pitfall.