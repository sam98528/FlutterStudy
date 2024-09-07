## ConsumerWidget vs. ConsumerStatefulWidget ##
#### ConsumerWidget ####

- **전역 상태 구독**: 
	- ConsumerWidget은 **Riverpod**의 상태 관리 시스템을 사용하여 **전역적으로 관리되는 상태**를 ref.watch()를 통해 구독합니다.
- **StatelessWidget처럼 작동**: 
	- 자체적으로는 상태를 관리하지 않지만, **Riverpod** 상태가 변경될 때마다 UI가 자동으로 업데이트됩니다. 따라서 **전역 상태**를 사용하면서도 StatefulWidget처럼 리액티브한 동작을 할 수 있습니다.
- **주요 용도**: 
	- 자체적인 로컬 상태가 필요 없고, 단순히 **전역 상태**를 구독하여 UI를 업데이트해야 할 때 사용합니다.

--- 

#### ConsumerStatefulWidget ####

- **전역 상태 구독 + 로컬 상태 관리**: 
	- ConsumerStatefulWidget은 ConsumerWidget과 같이 **전역 상태를 구독**하면서, 동시에 **StatefulWidget**의 기능(예: initState(), dispose(), 로컬 상태)을 가집니다.
- **StatefulWidget의 기능 추가**: 
	- 전역 상태를 구독하면서도 **로컬 상태**나 UI의 특정 **임시 상태**를 관리할 수 있습니다. 예를 들어, 텍스트 필드의 값, 애니메이션, 탭 컨트롤러 등 화면에 국한된 상태를 로컬 상태로 유지하고, 필요할 때 전역 상태를 조작할 수 있습니다.
- **주요 용도**: 
	- **로컬 상태**(UI와 관련된 일시적인 상태)를 관리해야 하면서도 **전역 상태**를 구독하고 변경해야 하는 경우에 사용됩니다.

  

**비유로 설명하자면:**

• **ConsumerWidget**: 전역적으로 상태를 관리하는 **StatelessWidget**처럼 동작한다고 볼 수 있습니다. UI에서 전역 상태를 구독하고, 상태가 변할 때 UI를 자동으로 갱신할 수 있습니다. 하지만 위젯 자체에서 로컬 상태는 관리하지 않습니다.

• **ConsumerStatefulWidget**: ConsumerWidget의 기능에 더해, 자체적으로 **로컬 상태도 관리**할 수 있는 **StatefulWidget**처럼 동작합니다. 즉, **전역 상태**와 **로컬 상태**를 모두 관리할 수 있기 때문에, 더 복잡한 UI 상호작용이나 일시적인 상태 처리가 필요한 경우에 적합합니다.

Refers to: [[Riverpod]], [[StatefulWidget]], [[ConsumerWidget]] , [[Provider]], [[StateNotifierProvider]], [[StatelessWidget vs StatefulWidget]],[[ConsumerStatefulWidget]] ,