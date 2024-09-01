## Modal ##

```Dart
void _openAddExpenseOverlay() {
	showModalBottomSheet(
		useSafeArea: true, // SafeArea를 알아서
		context: context, //Context
		builder: (ctx) { // BuildContext
			return const Text("qwe"); // Widget
		});
}
```

Refers to : [[Context]]
