## Theme ##

- 각 Component별로 Theme을 설정할 수 있음
- Copywith를 안쓰면 새로운 Themedata로 만들어져서 Default설정들 조차 없어짐.

```dart
ColorScheme kColorScheme = ColorScheme.fromSeed(seedColor: const Color.fromARGB(220, 128, 216, 215));

ColorScheme kDarkColorScheme = ColorScheme.fromSeed(
	brightness: Brightness.dark,
	seedColor: const Color.fromARGB(220, 128, 216, 215)
	);

// ColorScheme을 알아서 만들어줌.


void main() {
	runApp(MaterialApp(
		darkTheme: ThemeData().copyWith(
		colorScheme: kDarkColorScheme,
		'''
		'''
		//Dark Mode로 하게 되면 아래 적용했던것들도 전부 리셋해서
		// 따로 또 적용해줘야함.
		),
		theme: ThemeData().copyWith(
			colorScheme: kColorScheme,
			appBarTheme: const AppBarTheme().copyWith(
				backgroundColor: kColorScheme.onPrimaryContainer,
				foregroundColor: kColorScheme.primaryContainer,
			),
			cardTheme: const CardTheme().copyWith(
				color: kColorScheme.secondaryContainer,
				margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
			),
			elevatedButtonTheme: ElevatedButtonThemeData(
				style: ElevatedButton.styleFrom(
				backgroundColor: kColorScheme.primaryContainer),
			),
			textTheme: ThemeData().textTheme.copyWith(
				titleLarge: TextStyle(
					fontWeight: FontWeight.bold,
					color: kColorScheme.onSecondaryContainer,
					fontSize: 14,
				)
			)
		),
	home: const Expenses(),
	));
}

//Override 하고 싶을땐


Theme.of(context). // 여기서 접근 및 수정
```