## Orientation ##

- 디바이스 방향 정하는 방법
- `WidgetsFlutterBinding.ensureInitialized();` 초기화 작업이 올바르게 완료되었는지 확인하는 코드입니다. 이 메서드는 일반적으로 runApp() 전에 호출되며, 특히 비동기 초기화 작업을 수행하거나 Flutter 프레임워크에 의존하는 초기화 작업을 실행하기 전에 사용됩니다.

```dart
import 'package:flutter/services.dart';
void main() {
	WidgetsFlutterBinding.ensureInitialized();
	SystemChrome.setPreferredOrientations([ // Orientation Lock
	DeviceOrientation.portraitUp
	]).then((fn) {
		runApp();
			'''
			'''
	}
}

// Orientation이 바뀌어도 자동으로 Layout이 바뀌게끔 하는 방법
final width = MediaQuery.of(context).size.width; // 화면의 가로를 구함
// 가로가 아니라 실제 디바이스의 Orientation을 구하는 방법도 있음

'''
'''
body : width < 600 ? Column() : Row() // 이런식으로 구현할 수 있음. 
```