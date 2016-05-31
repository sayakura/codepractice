import java.util.List;
import java.util.ArrayList;
public class SparseArray
{
	private int numRows;
	private int numCols;

	private List<SparseArrayEntry> entries;

	public SparseArray()
	{
		entries = new ArrayList<SparseArrayEntry>();
	}

	public int getNumRows(){
		return numRows;
	}
	public int getNumCols(){
		return numCols;
	}
	public int getValueAt(int row, int col){
		for (int i = 0;i < entries.size() ;i++ ) {
			if((row == entries.get(i).getRow()) && (col == entries.get(i).getCol())){
				return entries.get(i).getValue();
			}
		}
		return 0;
	}
	public int removeColumn(){
		return 0;
	}

}