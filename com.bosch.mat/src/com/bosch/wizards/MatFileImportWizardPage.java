package com.bosch.wizards;

import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.jface.wizard.WizardPage;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.MouseEvent;
import org.eclipse.swt.events.MouseListener;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;

public class MatFileImportWizardPage extends WizardPage {

	Text txt;
	
	Label file;
	protected MatFileImportWizardPage(String pageName, String title,
			ImageDescriptor titleImage) {
		super(pageName, title, titleImage);
		// TODO Auto-generated constructor stub
	}

	public String getTxt() {
		return txt.getText();
	}

	

	@Override
	public void createControl(Composite parent) {

		
		setPageComplete(false);
		 final Composite composite = new Composite(parent, SWT.NONE);
		GridLayout layout = new GridLayout(3, false);
		composite.setLayout(layout);
		GridData data = new GridData();
		data.grabExcessHorizontalSpace = true;
		data.grabExcessVerticalSpace = false;
		data.horizontalAlignment = SWT.FILL;
		data.verticalAlignment = SWT.FILL;

		composite.setLayoutData(data);

		 file= new Label(composite, 1);
		 file.setText("File :");
		
		
		txt= new Text(composite, 0);
		 txt.setLayoutData(data);
		 
		 
		
		 Button browse= new Button(composite, 0);
		
		
			browse.setText("Browse");
		
			
		browse.addMouseListener(new MouseListener(){

			@Override
			public void mouseDoubleClick(MouseEvent e) {
				
					
			}

			@Override
			public void mouseDown(MouseEvent e) {

				 FileDialog fd= new FileDialog(composite.getShell());
					String path= fd.open();
					if(path!=null)
					txt.setText(path);
					if(txt.getText().contains(".mat"))
					{
						
						setPageComplete(true);
						setErrorMessage(null);
					}
					
					else
					{
					setErrorMessage("Please select a mat file");
						setPageComplete(false);
					}
			}

			@Override
			public void mouseUp(MouseEvent e) {
				// TODO Auto-generated method stub
				
			}
			
		});
		setControl(composite);
			
		

	}

	

}
