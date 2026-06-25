# Ansys Optics Scripting Language - Command Lists

Lumerical's scripting language allows you to automate tasks and analysis such as manipulating simulation objects, launching simulations, and analyzing results. Script commands can be entered directly into the script prompt, run from a saved script file (.lsf), or used within some simulation objects.

## Categories

* Adding objects
* Manipulating objects
* Material database
* Running simulations
* Accessing data
* Analyzing data
* Far field projections
* Grating projections
* Visualizing data
* INTERCONNECT
* Variables
* Functions
* Operators
* Loop and conditional statements
* System
* File formats
* User-defined GUI
* Interoperability

## Adding objects

The following commands can be used to add objects. Objects are always added to the location specified by the groupscope variable. 

### Simulation environment
* `switchtolayout` : Closes the analysis window, deletes current simulation data and allows you to manipulate simulation objects for a new simulation.
* `layoutmode` : Used to determine if the simulation file is open in layout or in analysis mode.
* `groupscope` : Changes the group scope.
* `addgroup` : Adds a container group to the simulation environment.
* `addanalysisgroup` : Add an analysis group.
* `addobject` : Add an object from the object library.
* `addgridattribute` : Add a grid attribute object.
* `importcsvlc` : Add LC grid attribute and optionally LC structure from CSV file.
* `addport` : Adds a port object to the ports group in the FDTD solver region object.

### Structures
* `addcircle` : Add a circle primitive.
* `addcustom` : Add a custom primitive.
* `addfieldregion` : Add a field region object.
* `addimport` : Add an import primitive.
* `addpyramid` : Add a pyramid primitive.
* `addpoly` : Add a polygon primitive
* `addrect` : Add a rectangle primitive.
* `addring` : Add a ring primitive.
* `addsphere` : Add a sphere primitive.
* `addsurface` : Add a surface primitive.
* `addstructuregroup` : Add a structure group.
* `addlayer` : Adds a layer to the layer builder object.
* `addlayerbuilder` : Adds a layer builder object.
* `addplanarsolid` : Adds a planar solid object.
* `stlimport` : Adds an STL import object.
* `stepimport` : Adds a CAD import object
* `cadimport`: Adds a CAD import object, identical to stepimport
* `add2drect` : Adds a 2D rectangle in the simulation space.
* `add2dpoly` : Adds a 2D polygon in the simulation space.
* `addwaveguide` : Adds a waveguide in the simulation space.

### Simulation region
* `addeme` : Adds an Eigenmode Expansion (EME) solver region.
* `addfdtd` : Adds an FDTD simulation area.
* `addrcwa` : Adds an RCWA solver region.
* `addfde` : Adds an Finite Difference Eigenmode (FDE) solver region.
* `addmesh` : Adds a mesh override region.
* `addsimulationregion` : Adds a simulation region to the Finite Element IDE design environment.
* `adddevice` : Adds an electrical (CHARGE) simulation
* `addvarfdtd` : Adds a 2.5D varFDTD simulation region.
* `addchargesolver` : Adds an electrical (charge transport) simulation region in Finite Element IDE.
* `addheatsolver` : Adds a thermal (heat transport) simulation region in Finite Element IDE.
* `addchargemesh` : Adds a mesh override region to the 'CHARGE' simulation environment.
* `addheatmesh` : Adds a mesh override region to the 'HEAT' simulation environment.
* `adddgtdsolver` : Adds an optical 'DGTD' solver simulation region.
* `adddgtdmesh` : Adds a mesh override region to the 'DGTD' simulation environment.
* `addfeemsolver` : Adds a 'FEEM' solver simulation region.
* `addfeemmesh` : Adds a mesh override region to the 'FEEM' simulation environment.

### Sources
* `adddipole` : Adds a dipole source.
* `addgaussian` : Adds a Gaussian source.
* `addplane` : Adds a plane source.
* `addmode` : Adds a mode source in FDTD.
* `addmodesource` : Adds a mode source to the 2.5D varFDTD simulation environment.
* `addtfsf` : Adds a TFSF source.
* `addimportedsource` : Adds an imported source.

### Monitors
* `addindex` : Adds an index monitor.
* `addeffectiveindex` : Adds an effective index monitor.
* `addtime` : Adds a time monitor.
* `addmovie` : Adds a movie monitor.
* `adddftmonitor`: Adds a frequency domain monitor
* `addmodeexpansion` : Adds a mode expansion monitor.
* `addbandstructuremonitor` : Adds a band structure monitor.
* `addjfluxmonitor` : Adds a current flux monitor.
* `addchargemonitor` : Adds a charge monitor
* `addefieldmonitor` : Adds an electric field monitor
* `addemeindex` : Adds an index monitor for an EME solver region.
* `addemeprofile` : Adds a profile monitor for an EME solver region.
* `addheatfluxmonitor` : Adds a heat flux monitor
* `addtemperaturemonitor` : Adds a temperature monitor
* `addemfieldmonitor` : Adds an Electromagnetic field monitor to a DGTD solver
* `addemfieldtimemonitor` : Adds an Electromagnetic time monitor to a DGTD solver
* `addemabsorptionmonitor` : Adds an Electromagnetic absorption monitor to a DGTD solver

### Create objects in Deck
* `createbeam` : Creates a new Gaussian beam that is accessible from the deck.

### Simulation environment (INTERCONNECT)
* `switchtolayout` : Closes the analysis window, deletes current simulation data and allows you to manipulate simulation objects for a new simulation.
* `switchtodesign` : Switches INTERCONNECT to design mode.
* `layoutmode` : Used to determine if the simulation file is open in design (layout) or in analysis mode.
* `designmode` : Returns true if the simulation is currently in design mode.
* `groupscope` : Changes the group scope.

### Adding Elements
* `addelement` : Adds an element from the INTERCONNECT element library.

### Adding materials and properties to the Material Group in Finite Element IDE
* `addmodelmaterial` : Adds an empty material model to the 'materials' folder in the objects tree
* `addmaterialproperties` : Adds a (material) property to the selected material model
* `addemmaterialproperty` : Adds a new optical material property to the selected material model
* `addctmaterialproperty` : Adds a new electrical material property to the selected material model or the selected binary alloy
* `addhtmaterialproperty` : Adds a new thermal material property to the selected material model or the selected solid alloy
* `addsemiconductorfromalloy` : Converts an Alloy material to a Semiconductor material at a fixed mole fraction and adds its electrothermal material properties to the selected material model in the object tree.

### Adding Boundary Conditions in Finite Element IDE
* `addelectricalcontact` : Adds an electrical contact boundary condition to CHARGE
* `addsurfacerecombinationbc` : Adds a surface recombination boundary condition to CHARGE
* `addtemperaturebc` : Adds a temperature boundary condition to CHARGE or HEAT
* `addconvectionbc` : Adds a convection boundary condition to CHARGE or HEAT
* `addradiationbc` : Adds a radiation boundary condition to CHARGE or HEAT
* `addthermalpowerbc` : Adds a thermal boundary condition to CHARGE or HEAT
* `addheatfluxbc` : Adds a heat flux boundary condition to CHARGE or HEAT
* `addthermalinsulatingbc` : Adds a thermal insulating boundary condition to CHARGE or HEAT
* `addvoltagebc` : Adds a voltage boundary condition to HEAT
* `addpml` : Adds a PML boundary condition to DGTD
* `addabsorbing` : Adds a absorbing boundary condition to DGTD
* `addperiodic` : Adds a periodic (or Bloch) boundary condition to DGTD
* `addpec` : Adds a PEC boundary condition to DGTD
* `addpmc` : Adds a PMC boundary condition to DGTD

### Adding simulation objects
* `addemeport` : Adds a port to the active EME solver region.
* `adddope` : Adds a constant doping region.
* `adddopinglayer` : Adds a doping layer to the layer builder object.
* `adddiffusion` : Adds a diffusion region.
* `addimplant` : Adds a implant doping region.
* `addbulkgen` : Adds a bulk generation region.
* `adddeltachargesource` : Adds a point generation source
* `addimportdope` : Adds an import primitive for a doping region.
* `addimportgen` : Adds an import primitive for a generation region.
* `adduniformheat` : Adds a constant heat source.
* `addimportheat` : Adds an import primitive for a heat source.
* `addimporttemperature` : Adds an import temperature source to the CHARGE solver
* `addimportnk` : Adds an import primitive for a spatially varying nk material.

### Activating import wizards
* `drivewziard`: Activates specific wizards with a settings structure
* `getwizardinputs`: Obtains the structure of inputs to specific wizards
