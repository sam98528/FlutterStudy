## Riverpod ##
- State를 관리하는 유용한 써드 파티 패키지
- 말이 Third지, 대부분 쓴다. 
- 사용방법:

```dart

//New Dart File
final xxxProvider = Provider((ref) { // Static 한 데이터를 사용할떄는 이걸씀
	return SOMEDATA;
};

//사용하는 제일 상위 Widget를 ProviderScope 위젯 하위로 구현한다.
void main() {
	runApp(
		const ProviderScope( // 이런식으로
			child: App(),
		),
	);
}
// StateFul Widget 인 경우
							 
class TabsScreen extends ConsumerStatefulWidget {
	const TabsScreen({super.key});
	@override
	ConsumerState<TabsScreen> createState() {
		return _TabsScreenState();
	}
}

class _TabsScreenState extends ConsumerState<TabsScreen> {
		'''
		'''
	Widget build(BuildContext context) {
		final meals = ref.watch(mealsProvider); 
		// 해당 Provider의 변화를 Watch하고, 변화가 있을때마다 Build를 새로 호출함
		// 또한 Watch는 반환괎이 해당 Provider가 return하는 데이터
		// print(meals); == print(SOMEDATA);
		
}
```


Refers to: [[Lifting State]], [[StatefulWidget]], [[StatelessWidget vs StatefulWidget]],
