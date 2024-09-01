## Dialog ##

- 간단한 Controller 같은 느낌
- `AlertDialog`, `SimpleDialog`

```dart
showDialog(
	context: context,
	builder: (ctx) {
		return AlertDialog(
			title: const Text('123'),
			content: const Text('PLEASE!@#'),
			actions: [
				TextButton( 
				onPressed: () => Navigator.pop(ctx);,
				child: const Text('Cancel')),
			],
		);
	}
);
```