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

## Manipulating objects
Physical structures, sources, monitors, and the simulation volume itself are considered objects. Objects generally have properties that can be modified.

### Selecting and deleting objects
* `groupscope` : Changes the group scope.
* `deleteall` : Deletes all objects in the current group scope.
* `delete` : Deletes the selected objects.
* `selectall` : Selects all objects in the current group scope.
* `unselectall` : Unselect all objects.
* `select` : Selects objects with a given name in the current group scope.
* `selectpartial` : Selects any objects where partialname can be found in the name.
* `shiftselect` : The same as select("name"); but does not unselect currently selected objects. Can be used to select multiple objects.
* `shiftselectpartial` : The same as selectpartial("partialname"); but does not unselect currently selected objects. Can be used to select multiple objects.

### Moving and copying objects
* `move` : Move an object.
* `copy` : Copy an object.
* `addtogroup` : Add an object/objects into a group.

### Object properties
* `adduserprop` : Add a user property to a structure group.
* `addanalysisprop` : Adds a analysis property to a selected object group.
* `addanalysisresult` : Adds a new result to an analysis group.
* `boundingbox`: Returns a cell array containing the bounding box for an object(s) in SI units with an optional argument to first make a hypothetical transformed copy.
* `set` : Set a property of selected objects.
* `setnamed` : Set a property of any objects with a given name.
* `setglobalmonitor` : Set global monitor properties.
* `setglobalsource` : Set global source properties.
* `setposition` : Set an element's vertical and horizontal positions.
* `setrectangle` : Set width and height of an element rectangle.
* `setactivesolver` : Set the specified solver as the active solver.
* `getactivesolver` : Get the active solver.
* `runsetup` : Force group setup scripts to run.
* `get` : Get a property of selected objects.
* `getnumber` : Get the number of selected objects.
* `getnamed` : Get a property of any objects with a given name.
* `getnamednumber` : Get the number of objects with a given name.
* `getglobalmonitor` : Get global monitor properties.
* `getglobalsource` : Get global source properties.
* `getposition` : Get current horizontal or vertical position of an element.
* `getrectangle` : Get the width or height of an element rectangle.
* `haveproperty` : Returns the number of selected objects with a particular property.
* `importsurface` : Import surface data from a file. Only applies to import primitives.
* `importsurface2` : Import surface data from script variables. Only applies to import primitives.
* `importnk` : Import n and k data from a file. Only applies to import primitives.
* `importnk2` : Import n and k data from script variables. Only applies to import primitives.
* `setsourcesignal` : Set a custom source time signal.
* `updatesourcemode` : Updates the mode for a mode source.
* `clearsourcedata` : Clears source data for an imported source, or the selected mode for a mode source.
* `setexpansion` : Associates a DFT monitor with a mode expansion monitor.
* `removeexpansion` : Removes a DFT monitor from a mode expansion monitor.
* `getname` : Returns the dataset name of the variable selected.
* `setname` : Sets the dataset name of the variable selected.
* `importdataset` : Imports an unstructured dataset named 'charge' to an 'eh Density' grid attribute.
* `cleardataset` : Clear the dataset from any current grid attribute.
* `getcelllist` : Returns the list of cells associated with the loaded gds file.
* `getlayer`: Retrieves the properties of the specified layer in the selected layer builder object.
* `getlayerlist` : Returns the list of layers associated with the loaded gds file.
* `setlayer` : Sets the properties of a specified layer of the selected layer builder object.
* `loadgdsfile` : Loads specified gds file into the layer builder object.
* `loadprocessfile`: Loads the specified process file in a layer builder object.
* `geteigensolver` : Sets the properties of the eigensolver in the mode source, mode expansion monitor or port.
* `seteigensolver` : Sets the properties of the eigensolver in the mode source, mode expansion monitor or port.
* `updateportmodes` : Selects the specified modes in the selected port object. Modes are specified by the mode number in the eigensolver's mode list.
* `clearportmodedata` : Clears mode data from selected port.
* `readnportsparameterat` : Interpolates the S-Parameter sweep file with the specified parameter values.
* `convertnportsparametersweep` : Converts the textual S-Parameter sweep file to a binary file.

### Controlling the view
* `redraw` : Redraw graphics.
* `redrawoff` : Turn automatic redraw off.
* `redrawon` : Turn automatic redraw on.
* `redrawmode` : Get the current status of automatic redrawing; turn it off or on
* `setview` : Control how the graphics are drawn in the Layout Editor
* `getview` : Get the current view control properties from the Layout Editor.
* `orbit` : A built in function to do an orbit of the perspective view with option of creating a movie.
* `framerate` : Measure graphics performance of your computer.

### Element/connection properties
* `set` : Set a property of selected element.
* `setnamed` : Set a property of any element with a given name.
* `get` : Get a property of selected element.
* `getnamed` : Get a property of any element with a given name.
* `addport` : Add a port to a compound/scripted element.
* `removeport` : Remove a port from a compound/scripted element.
* `connect` : Connects one element to another via the specified ports.
* `disconnect` : Removed a specific connection between two elements.
* `gnddisconnectedelectricalports`: Automatically grounds all disconnected input and bidirectional electrical ports in the current group scope.
* `autoarrange` : Arranges port positions and dimensions of compound or scripted elements automatically
* `createcompound` : Creates a compound element with the currently selected elements.
* `addproperty` : Adds a property to a compound or to a scripted element.
* `setexpression` : Sets the selected element's specified property to the mentioned expression.
* `flipelement` : Flips an element in the schematic editor.
* `rotateelement` : Rotates an element in the schematic editor.
* `seticon` : Set a user defined icon for an element.

### Undo and redo commands
* `undo` : Undo last modify object command.
* `redo` : Redo command after an undo.
* `historyon` : Enables taking snapshots (history) for the current schematic for undo redo functionality.
* `historyoff` : Disables taking snapshots (history) of the current schematic for undo redo functionality.

## Material database
The following commands are used to add or copy materials in the material database, as well as to set any material property and verify the resulting complex index of a given material at any frequency.

* `addmaterial` : Adds a new material into the material database.
* `copymaterial` : Creates a copy of an existing material in the material database.
* `setmaterial` : Sets any property of an existing material in the material database.
* `getmaterial` : Returns properties of a material in the material database.
* `importmaterialdb` : Imports the material database from a .mdf file.
* `exportmaterialdb` : Exports the material database to a .mdf file.
* `getindex` : Returns the complex refractive index of a material.
* `getfdtdindex` : Returns the material refractive index from the material fit which is used in an FDTD simulation.
* `getdgtdindex` : Returns the material refractive index from the material fit which is used in a DGTD simulation.
* `getmodeindex` : Returns the material refractive index from the material fit which is used in a MODE simulation.
* `getnumericalpermittivity` : Returns permittivity, taking into account the effect of finite size of dt in an FDTD simulation.
* `deletematerial` : Deletes a material from the material database.
* `materialexists` : Returns a boolean to indicate whether a material exists in the material database.
* `getsurfaceconductivity` : Returns surface conductivity of specified material which uses the surface conductivity model.
* `getfdtdsurfaceconductivity` : Returns surface conductivity of specified material which uses the surface conductivity model as will be used in a simulation.

## Running simulations
### Moving between tabs
* `switchtolayout` : Closes the analysis window and allows you to manipulate simulation objects for a new simulation.
* `layoutmode` : Used to determine if the simulation file is open in layout or in analysis mode.

### Running Simulations
* `run` : Launch the simulation. (Options available)
* `runparallel` : Launch the simulation in parallel mode.
* `addjob` : Add a simulation to the job queue.
* `runjobs` : Run all simulations in the job queue.
* `clearjobs` : Remove all simulations from the job queue.
* `runsweep` : Runs a parameter sweep or optimization task.
* `runsystemcheck` : Runs check for simulation requirements.

### Resource Configuration
* `addresource` : Adds a resource to the list of available resources in resource manager.
* `deleteresource` : Removes the selected resource from the list of available resources in resource manager.
* `getresource` : Returns the current setting for properties of the available resources in resource manager for the specified solver.
* `getdevice` : Returns the type of device (GPU/CPU) used to run the simulation in the FDTD solver.
* `setresource` : Sets properties of the available resources in resource manager for the specified solver.
* `setdevice` : Sets the type of device (GPU/CPU) used to run the simulation in FDTD solver.
* `setpersistcheckouts` : Sets whether persistent license checkout is enabled.
* `gpuspecs` : Obtain current system GPU specifications.

### License type and consumption
* `islicensestandard` : Returns if the current license is standard licensing.
* `getlicenseestimate` : Returns number of licenses required for a given resource.
* `getlicenseestimateallactiveresources` : Returns number of licenses required to run a parameter sweep on all active resources.

### Checking out licenses
* `checkout` : Checks out a licensed feature.

## Accessing data

* `getresult` : Gets results from simulation objects.
* `getdata` : Gets raw data from simulation objects.
* `getelectric` : Gets raw |E| 2 data matrix from monitor
* `getmagnetic` : Gets raw |H| 2 data matrix from monitor
* `runanalysis` : Runs the analysis script in analysis objects
* `clearanalysis` : Clears d-card data obtained by running analysis scripts.
* `havedata` : Used to see if there is any available data stored within an object.
* `haveresult` : Used to see if there are any available results within an object.
* `getvariable` : Returns the value of a workspace variable, if the value is not found it returns a ‘default’ value.
* `copydcard` : Creates a copy of a d-card.
* `cleardcard` : Clears a d-card.
* `lswmexport`: Exports RCWA engine grating characterization data to a JSON file.
* `lmapexport`: Creates a mapping information file (.lmap) for a metalens or a grating with spatial variation.
* `mcfit` : Runs the multi-coefficient fitting for a file containing multiple frequency dependent transmission values.
* `mczfit` : Fits a variable gain filter to a family of gain curve data, where each curve in the family corresponds to a value of carrier density, producing a file of gain filter coefficients to be used by the TWLM element.
* `simulationdiverged` : In layout mode, check whether the simulation reached the divergence checking auto shutoff threshold.
* `tdecq` : Calculates the figure of merit (fom) of PAM-4 tranmitters knows as Transmitter and Dispersion Eye Closure Quaternary (TDECQ) as defined in IEEE Standard 802.3 2018.
* `outeroma` : Returns the quantity OMAouter as specified in IEEE Standard 802.3 2018 for the given signal.

Parameter sweep, optimization, yield analysis, and S-parameter sweep data:

* `getsweepdata` : Gets raw data from parameter sweeps, optimizations, yield analysis, and S-parameter sweeps.
* `getsweepresult` : Gets results from parameter sweeps, optimizations, and S-parameter sweeps.
* `havesweepdata` : Used to check if parameter sweep and optimizations have data.
* `havesweepresult` : Used to check if parameter sweep and optimizations have results.
* `loadsweep` : Loads previously generated sweep result
* `savesweep` : Saves the generated sweep result
* `copysweep` : Copies a parameter sweep/yield/optimization/S-parameter sweep analysis item to clipboard.
* `pastesweep` : Pastes a parameter sweep/yield/optimization/S-parameter sweep analysis item from clipboard.
* `addsweep` : Adds a parameter sweep/yield/optimization/S-parameter sweep item as the top-most item.
* `insertsweep` : Inserts a parameter sweep/yield/optimization item as a child to a parent item.
* `getsweep` : Gets a property from a parameter sweep/yield/optimization/S-parameter sweep item.
* `setsweep` : Sets a property in a parameter sweep/yield/optimization/S-parameter sweep item.
* `deletesweep` : Deletes a specified parameter sweep, optimization, yield task, or S-parameter sweep.
* `addsweepparameter` : Adds a parameter to a parameter sweep/yield/optimization/S-parameter sweep item.
* `addsweepresult` : Adds a result to a parameter sweep/yield/optimization item.
* `removesweepparameter` : Removes a parameter from a parameter sweep/yield/optimization/S-parameter sweep item.
* `removesweepresult` : Removes a result from a parameter sweep/yield/optimization item.
* `exportsweep` : Exports S-parameter results from an S-parameter sweep task to a .dat file which has a format that can be loaded by the Optical N-Port S-parameter element in INTERCONNECT.

Ansys Cloud Burst Compute™:
* `burstrecentids`: Returns the ID of the last 8 jobs submitted via Ansys Cloud Burst Compute™.
* `burstjobstatus`: Returns the status of a given Ansys Cloud Burst Compute™ job, given its job ID.
* `burstresultsquery`: Returns a struct containing the files available for a given Ansys Cloud Burst Compute™ job.
* `burstresultsdownload`: Downloads simulation result for a given Ansys Cloud Burst Compute™ job, with optional file filtering.

## Analyzing data
### EME solver analysis
* `setemeanalysis` : Sets properties in EME analysis window.
* `getemeanalysis` : Gets properties in EME analysis window.
* `emesweep` : Runs EME analysis propagation sweep tool.
* `emepropagate` : Propagates fields and s-matrix results with EME solver.
* `getemesweep` : Gets the user s-matrix result from an EME propagation sweep.
* `exportemesweep` : Exports the EME analysis wavelength sweep result.

### FDE solver analysis
* `setanalysis` : Sets calculation parameters in MODE' FDE and Finite Element IDE analysis window.
* `getanalysis` : Sets calculation parameters in MODE' FDE and Finite Element IDE analysis window.
* `analysis` : Opens the MODE analysis window corresponding to the active solver (FDE or EME).
* `mesh` : Meshes the physical structures.
* `findmodes` : Calculates the modes supported by the structure.
* `nummodes` : Returns the number of modes found.
* `selectmode` : Selects a mode from the mode list.
* `frequencysweep` : Performs a frequency sweep.
* `coupling` : Calculates the complex coupling coefficient.
* `overlap` : Calculates the overlap and power coupling between two modes.
* `bestoverlap` : Determines which mode has the largest overlap with another mode.
* `bestoverlap2` : Similar to bestoverlap.
* `propagate` : Propagates an arbitrary mode down a waveguide.
* `optimizeposition` : Calculates the x shift, y shift, and z shift resulting in maximum overlap between the specified mode and d-card when using the FDE solver.

### FDTD measurements
* `transmission` : Returns the power transmission through a monitor.
* `transmission_avg` : Returns the total spectral average power through a monitor surface, normalized to the total spectral average of the source.
* `transmission_pavg` : Returns the partial spectral average power through a monitor surface, normalized to the partial spectral average of the source.
* `getsourceangle` : Get source angle.

### FDTD normalization
* `nonorm` : Use no normalization.
* `cwnorm` : Use CW normalization.
* `sourcenorm` : Returns the normalization used in the cwnorm state.
* `sourcenorm2_avg` : Returns the source normalization spectrum used to normalize data in the cwnorm state for the total spectral averaged quantities
* `sourcenorm2_pavg` : Returns the source normalization spectrum used to normalize data in the cwnorm state for the partial spectral averaged quantities
* `dipolepower` : Returns the power injected into the simulation by a dipole source.
* `sourcepower` : Returns the source power.
* `sourcepower_avg` : Returns the total spectral average power injected into the simulation by the source.
* `sourcepower_pavg` : Returns the partial spectral average power injected into the simulation by the source.
* `sourceintensity` : Returns the source intensity.
* `sourceintensity_avg` : Returns the total spectral average intensity injected into the simulation by the source.
* `sourceintensity_pavg` : Returns the partial spectral average intensity injected into the simulation by the source.

### FEEM & DGTD measurements
* `modeexpansion`: Returns the mode expansion coefficients with respect to two FEEM solver results, or a FEEM solver result and a DGTD 2D frequency monitor result. 
* `modeoverlap`: Returns the overlap between the respective mode profiles (modes) of two FEEM calculations, if given two FEEM solver result structs.
