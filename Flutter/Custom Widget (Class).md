## Custom Widget (Class) ##

 ```Dart
class GradientContainer extends StatelessWidget {
	const GradientContainer({super.key}); // Constructor
@override
	Widget build(BuildContext context) {
		return Container('''''');
	}
}


class CustomText extends StatelessWidget {
	const CustomText(this.text, {super.key}) 
	// Constructor this.text 
	// ==> this.text = text
	final String text;
@override
	Widget build(BuildContext context) {
		return const Text(
			text,
			style: 
			TextStyle(
			fontSize: 28.0, 
			color: Colors.white),
		);
	}
}

// Class이름 (PoistionArgument, {NamedArgument, required this.변수})
// required 는 말그대로 필수로 받아야 하는 OPtional이 아닌 경우, 
// Class의 Variable가 안받으면 Null인데, this.gradientColors인 경우 , 
// gradientColors가 Null이면 안되서
1. const GradientContainer( {super.key, required this.gradientColors});
2. const GradientContainer(this.gradientColors, {super.key});

1 -> 
GradientContainer(gradientColors:[
	Color.fromRGBO(207, 26, 26, 1), 
	Color.fromRGBO(179, 96, 96, 1)]
				 ),

2 -> GradientContainer([
	Color.fromRGBO(207, 26, 26, 1), 
	Color.fromRGBO(179, 96, 96, 1)]
					),

```