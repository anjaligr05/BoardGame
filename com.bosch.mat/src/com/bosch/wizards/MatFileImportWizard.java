package com.bosch.wizards;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;
import java.util.Set;

import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.wizard.Wizard;
import org.eclipse.ui.IImportWizard;
import org.eclipse.ui.IViewPart;
import org.eclipse.ui.IViewReference;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.IWorkbenchPage;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.PlatformUI;

import com.bosch.mat.MatTableViewPart;
import com.jmatio.io.MatFileReader;
import com.jmatio.types.MLArray;



public class MatFileImportWizard extends Wizard implements IImportWizard {

	MatFileImportWizardPage ncw=new MatFileImportWizardPage("Import", "Import", null);
	public static String filepath;
	public MatFileImportWizard() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public void init(IWorkbench workbench, IStructuredSelection selection) {
		// TODO Auto-generated method stub

	}

	@Override
	public boolean performFinish() {
		filepath= ncw.getTxt();
		 ArrayList<Set> list= new ArrayList<Set>();
		try {
			MatFileReader matFileReader = new MatFileReader(filepath);
			
			Map<String, MLArray> content = matFileReader.getContent();

		
		  

		   Set<String> str= content.keySet();
		   list.add( str);
		   System.out.println(list);


		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		MatTableViewPart treeView = null; 

		IWorkbenchPage page = 
		PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage(); 

		IViewReference viewReference = page.findViewReference("com.bosch.mat.MatTableview"); 
		if (viewReference != null) { 
		try { 
		IViewPart viewPart = page.showView("com.bosch.mat.MatTableview"); 
		page.activate(viewPart); 
		treeView = (MatTableViewPart) viewPart; 
		} catch (PartInitException e) { 
		} 
		} 
		
		treeView.getTree().setInput(filepath);
		return true;
	}

	@Override
	public void addPages() {

				addPage(ncw);
		super.addPages();
	}
		
}
