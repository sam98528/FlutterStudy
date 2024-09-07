## Provider ##
- **데이터 제공**:
	- Provider는 간단한 데이터를 생성하고, 해당 데이터를 다른 위젯에서 사용할 수 있도록 제공합니다.
	- 보통 상태가 변하지 않는 값, 또는 앱 전역에서 공유되는 서비스 객체 등을 제공할 때 사용합니다.

- **상태 관리 없음**:
	- Provider는 상태를 직접적으로 관리하지 않습니다. 상태를 관리하는 기능은 StateNotifier, ChangeNotifier, 또는 다른 복잡한 상태 관리 클래스에 의해 수행되며, Provider는 그런 상태 관리 클래스를 사용하지 않고 단순히 데이터를 제공합니다.
	
- **비즈니스 로직 없음**:
	- Provider 자체에는 비즈니스 로직이 없고, 데이터 생성에 관한 로직을 제공합니다. 하지만 상태 변경이나 복잡한 로직을 구현하는 데 적합하지 않습니다.

```dart
final greetingProvider = Provider<String>((ref) {
  return "Hello, Riverpod!";  // 단순한 문자열 데이터를 제공
});
```

Refers to: [[Riverpod]], [[StateNotifierProvider]]
