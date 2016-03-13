public class Puzzle{
	public String word;

	Puzzle(String word){
		this.word = word.toUpperCase();
	}

	public String getHint(String guess){
		guess = word.toUpperCase();
		String output = "";
		for (int i = 0; i < guess.length() ;i++ ) {
			if(word.charAt(i) == guess.charAt(i)){
				output += word.charAt(i);
			}else{
				if(word.indexOf(guess.charAt(i)) != -1){
					output += "+";
				}else{
					output += "*";
				}
			}
		}
		return output;
	}

	public static void main(String[] args) {
		Puzzle pz = new Puzzle("KURA");
		System.out.println(pz.getHint("kura"));
	}
}