import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.jface.wizard.WizardDialog;

import com.bosch.wizards.MatFileImportWizard;


public class ImportFileHandler extends AbstractHandler {
	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {

		
		
			MatFileImportWizard ncw= new MatFileImportWizard();
			
			WizardDialog dialog= new WizardDialog(ncw.getShell(),ncw);
			dialog.setTitle("Import");
			return dialog.open();
		
	}
}
