# AbaqusDataAnalysis
For Analysis of Abaqus Nodal Data and Translation into HeatMaps

Step name MUST be "Step-1"
You MUST have a node-set created for the contact surface called "CONTACT", created on the "TOTALBONE" side.
You MUST have CPRESS outputs created for the CONTACT nodeset equivalent, and those must be calculated at the nodes. 
You MUST have COORD outputs in addition to any global outputs like U, S, or E (outputted for the entire model)

e.g. your .inp file should look like this (this is not a copy-paste, just an example of what should be included)

--------------------------------- ... ----------------------------

** STEP: Step-1
** 
*Step, name=Step-1, nlgeom=YES, solver=ITERATIVE
*Static
1., 1., 1e-05, 1.

--------------------------------- ... ----------------------------

** FIELD OUTPUT: CONTACT
** 
*Output, field, frequency=99999
*Contact Output, nset=totalbone-1.<CONTACT>
CDISP, CFORCE, CNAREA, CSTATUS, CSTRESS
** 
** HISTORY OUTPUT: H-Output-1
** 
*Output, history, frequency=99999
*Contact Output, nset=totalbone-1.<CONTACT>
CSTRESS, 
*End Step

