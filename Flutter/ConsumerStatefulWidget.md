## ConsumerStatefulWidget ##
- **상태 관리**: 
	- ConsumerStatefulWidget은 상태를 관리하는 일반적인 StatefulWidget의 기능을 모두 제공합니다.
	- Local State!!

- **Riverpod 상태 구독**: 
	- ConsumerStatefulWidget은 Riverpod의 Provider로 제공된 상태를 쉽게 구독하고, 상태가 변경될 때 이를 UI에서 반영할 수 있도록 도와줍니다.

- **리액티브 UI**: 
	- 상태가 변경되면 UI가 자동으로 다시 빌드되어 최신 상태를 반영할 수 있습니다.

```dart
class CounterScreen extends ConsumerStatefulWidget {
  @override
  _CounterScreenState createState() => _CounterScreenState();
}

class _CounterScreenState extends ConsumerState<CounterScreen> {
  @override
  Widget build(BuildContext context) {
    // Riverpod 상태 구독
    final counter = ref.watch(counterProvider);
	'''
	'''
}
```


Refers to: [[Riverpod]], [[StatefulWidget]], [[ConsumerWidget]] , [[Provider]], [[StateNotifierProvider]], 