package com.bosch.mat;

import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Table;
import org.eclipse.swt.widgets.TableColumn;
import org.eclipse.ui.ISelectionListener;
import org.eclipse.ui.IWorkbenchPart;
import org.eclipse.ui.part.ViewPart;

public class TableViewPart extends ViewPart implements ISelectionListener{

	TableViewer tbviewer;
	public TableViewPart() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public void createPartControl(Composite parent) {
		tbviewer= new TableViewer(parent,SWT.MULTI|SWT.H_SCROLL|SWT.V_SCROLL|SWT.FULL_SELECTION|SWT.BORDER);
		
		final Table tb = tbviewer.getTable();
		tb.setHeaderVisible(true);
		tb.setLinesVisible(true);
		tb.setVisible(true);
		
//		TableColumn fieldCol = new TableColumn(tb, SWT.NONE);
//		fieldCol.setWidth(100);
//		fieldCol.setText("Field");
		
		TableColumn valueCol = new TableColumn(tb, SWT.NONE);
		valueCol.setWidth(100);
		
		valueCol.setText("Value");
		
		tbviewer.setContentProvider(new TableViewContentProvider());
		tbviewer.setLabelProvider(new TableViewLabelProvider());
	
		getSite().getPage().addSelectionListener(this);
		
	}

	@Override
	public void setFocus() {
		// TODO Auto-generated method stub

	}
	@Override
	public void selectionChanged(IWorkbenchPart part, ISelection selection) {
		
		if(selection instanceof IStructuredSelection){
			Object firstElement = ((IStructuredSelection) selection).getFirstElement();
			
			if (firstElement instanceof String)
			{			
				tbviewer.setInput(firstElement);
				
			}					
		}
		

}}
