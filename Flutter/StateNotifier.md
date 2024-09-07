## StateNotifier ##
- **상태 관리 (State Management)**:
	- StateNotifier는 특정 타입의 상태를 관리하는 클래스로, 이를 통해 애플리케이션 내에서 상태를 변경하거나 유지할 수 있습니다.
	- 상태는 불변(immutable)이어야 하며, StateNotifier는 상태를 직접적으로 수정하지 않고 항상 새로운 상태 객체를 생성하여 교체합니다.

- **상태의 불변성 (Immutability)**:
	- Flutter에서는 상태가 불변적이어야 하는데, 이는 상태를 변경할 때 기존 상태를 직접 수정하는 대신 새로운 상태를 생성하여 변경된 데이터를 반영한다는 의미입니다.
	- StateNotifier는 이러한 불변성 규칙을 준수하면서 상태를 관리할 수 있도록 설계되었습니다.

 - **상태 변경 알림 (State Updates)**:
	- StateNotifier는 상태가 변경될 때 이를 자동으로 감지하고, 상태가 변경되었음을 구독자들에게 알립니다.
	- 이로 인해 UI는 상태가 변경될 때마다 자동으로 다시 빌드되어 최신 상태를 반영할 수 있습니다.

- **리액티브 프로그래밍 지원 (Reactive Programming)**:
	- StateNotifier는 리액티브하게 상태를 관리할 수 있게 해줍니다. 구독된 UI나 다른 로직이 상태 변경을 감지하고 적절하게 반응합니다.

```dart
class FavoriteMealsNotifier extends StateNotifier<List<Meal>> {
  FavoriteMealsNotifier() : super([]); 
  // Set the Initial Data

  bool toggleMealFavoriteStatus(Meal meal) {
    // Not Allowed to edit an Existing Value in memory.
    // Must ALWAYS Create a New One

    final isExisting = state.contains(meal);
    // State가 해당 클래스 입력으로 받는 데이터 "<List<Meal>>"
    if (isExisting) {
      state = state
          .where(
            (element) => element != meal,
          )
          .toList();
      return false;
    } else {
      state = [...state, meal];
      return true;
    }
  }
}
```

Refers to: [[Riverpod]],