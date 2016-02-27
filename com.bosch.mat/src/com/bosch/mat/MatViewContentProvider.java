package com.bosch.mat;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.swt.widgets.List;
import org.eclipse.ui.PlatformUI;

import com.jmatio.io.MatFileReader;
import com.jmatio.types.MLArray;
import com.jmatio.types.MLCell;

public class MatViewContentProvider implements ITreeContentProvider{

	@Override
	public void dispose() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void inputChanged(Viewer viewer, Object oldInput, Object newInput) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public Object[] getElements(Object inputElement) {
		
		 String filepath= (String) inputElement;
		ArrayList<String> list= new ArrayList<String>();
		try {
			MatFileReader matFileReader = new MatFileReader(filepath);
			
			Map<String, MLArray> content = matFileReader.getContent();
			
		
			for(String str:content.keySet())
			{
				list.add(str);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return list.toArray();
	}

	@Override
	public Object[] getChildren(Object parentElement) {
	
		return null;
	}

	@Override
	public Object getParent(Object element) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean hasChildren(Object element) {
	
		return false;
	}

}
