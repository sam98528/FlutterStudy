## StateNotifierProvider ##
- StateNotifierProvider는 StateNotifier가 관리하는 상태를 **전역적으로** 제공하고, 그 상태에 접근할 수 있는 방법을 제공하는 역할을 합니다.
  
- **상태 제공**: 
	- StateNotifierProvider는 StateNotifier를 생성하고, 그 상태를 Riverpod의 다른 부분에서 사용할 수 있도록 제공합니다.

- **상태 구독**: 
	- StateNotifierProvider는 StateNotifier가 관리하는 상태를 구독하여 UI와 같은 소비자가 상태를 자동으로 감지하고 반응할 수 있게 합니다.

- **전역적으로 상태 공유**: 
	- StateNotifierProvider를 통해 다른 위젯이나 클래스가 전역적으로 상태를 읽고, 변경할 수 있는 방법을 제공합니다.

```dart
final favoriteMealsProvider =
	StateNotifierProvider<FavoriteMealsNotifier, List<Meal>>((ref) {
		return FavoriteMealsNotifier();
});
```

Refers to: [[Riverpod]], [[StateNotifier]]