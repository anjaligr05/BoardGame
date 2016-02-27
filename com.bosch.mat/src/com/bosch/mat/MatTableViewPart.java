package com.bosch.mat;


import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.part.ViewPart;


public class MatTableViewPart extends ViewPart {

	TreeViewer tree;
	public MatTableViewPart() {
		// TODO Auto-generated constructor stub
	}

	public TreeViewer getTree() {
		return tree;
	}

	

	@Override
	public void createPartControl(Composite parent) {
		 tree= new TreeViewer(parent);
		
		MatViewContentProvider cp = new MatViewContentProvider();
		MatViewLabelProvider lp= new MatViewLabelProvider();
	
			tree.setContentProvider(cp);
		    tree.setLabelProvider(lp);

		    getSite().setSelectionProvider(tree);
	}

	@Override
	public void setFocus() {
		// TODO Auto-generated method stub

	}

	
}
