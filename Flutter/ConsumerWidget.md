## ConsumerWidget ##
- **상태 구독**: 
	- ConsumerWidget은 Riverpod의 상태를 쉽게 구독할 수 있도록 해줍니다. ref.watch를 통해 Riverpod에서 제공하는 상태를 구독하고 UI에서 사용할 수 있습니다.

- **UI 업데이트**: 
	- 상태가 변경될 때마다 UI가 자동으로 다시 빌드됩니다. Riverpod은 상태 변화를 감지하고, 해당 상태를 사용하는 ConsumerWidget이 최신 상태를 반영하도록 자동으로 다시 빌드됩니다.

- **상태 변경 로직 제공**: 
	- ref.read를 사용하여 Riverpod의 상태를 변경하는 로직을 호출할 수 있습니다.
- **상태 관리가 필요 없는 위젯에 적합**: 
	- ConsumerWidget은 StatelessWidget처럼 상태가 필요 없고, 단순히 전역 상태를 구독하고 화면에 반영할 때 적합합니다.

Refers to: [[Riverpod]], [[StatelessWidget vs StatefulWidget]],[[ConsumerStatefulWidget]] ,[[Provider]], [[StateNotifierProvider]], 