## ref ##
- ref.는 **Riverpod**에서 중요한 역할을 하는 객체로, **provider를 구독하고 상태를 읽고, 상태를 변경하는 등의 작업을 수행**할 수 있게 해줍니다.

**ref의 주요 사용 패턴**

- `ref.watch(StateNotifierProvider:)`: 
	- 상태를 구독하고, 상태가 변경될 때마다 UI를 자동으로 다시 빌드합니다.
- `ref.read(StateNotifierProvider:):` 
	- 상태를 읽지만 구독하지 않으며, 주로 이벤트 핸들러에서 사용됩니다.
- `ref.listen(StateNotifierProvider:)`: 
	- 상태 변화에 반응해 리스너를 실행하지만, UI는 다시 빌드되지 않습니다.
- `ref.invalidate(StateNotifierProvider:)`: 
	- provider 상태를 무효화하고 다시 생성할 수 있게 만듭니다.
- `ref.refresh(StateNotifierProvider:)`: 
	- provider의 상태를 즉시 새로고침하고 새로운 상태를 반환합니다.


Refers to: [[Riverpod]], [[ConsumerWidget]], [[ConsumerStatefulWidget]], [[ConsumerWidget vs. ConsumerStatefulWidget]], [[Provider]], [[StateNotifier]], [[StateNotifierProvider]]