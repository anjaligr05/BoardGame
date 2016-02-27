package com.bosch.mat;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;

import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;

import com.bosch.wizards.MatFileImportWizard;
import com.jmatio.io.MatFileReader;
import com.jmatio.types.MLArray;
import com.jmatio.types.MLCell;
import com.jmatio.types.MLDouble;

public class TableViewContentProvider implements ITreeContentProvider {

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
		  ArrayList<String> list= new ArrayList<String>();
		if(inputElement instanceof String)
		{
			String filename=MatFileImportWizard.filepath;
			try {
				MatFileReader matFileReader = new MatFileReader(filename);
				
				Map<String, MLArray> content = matFileReader.getContent();
		
			 
			   MLArray mlArray = content.get(inputElement);
				if (mlArray.isDouble()) {
					MLDouble mlCell = ((MLDouble) mlArray);
					for (int i = 0; i < mlArray.getN(); i++) {
						list.add(mlCell.get(i).toString());
					}
				}
				else if (mlArray.isCell()) {
					MLCell mlCell = ((MLCell) mlArray);
					for (int i = 0; i < mlArray.getN(); i++) {
						list.add(mlCell.get(i).contentToString());
					}
				}
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
		}
		return list.toArray();
	}

	@Override
	public Object[] getChildren(Object parentElement) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Object getParent(Object element) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean hasChildren(Object element) {
		// TODO Auto-generated method stub
		return false;
	}



}
