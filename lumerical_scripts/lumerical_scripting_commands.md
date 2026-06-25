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

## Far field projections
### FDTD, MODE
* `farfieldsettings` : Sets the parameters available in the Far field settings window for far field calculations.
* `farfieldfilter` : Sets or gets the filter width for far field filter which is used to remove ripples in the far field projection due to clipping of the near fields.
* `farfield2d` : Projects fields from a given power or field profile monitor or a rectilinear dataset to the far field in a 2D simulation. E intensity is returned.
* `farfieldvector2d` : Farfieldvector2d is identical to farfield2d, however E field components in Cartesian coordinates (Ex, Ey and Ez) are returned.
* `farfieldpolar2d` : Farfieldpolar2d is identical to farfield2d, however E field components in cylindrical coordinates (Er, Eθ and Ez) are returned.
* `farfieldangle` : Returns the vector of angles, in degrees, corresponding to the data from farfield2d for a 2D simulation.
* `farfield3d` : Projects a given power or field profile monitor or a rectilinear dataset to the far field in a 3D simulation. E intensity is returned.
* `farfieldvector3d` : Farfieldvector3d is identical to farfield3d, however E field components in Cartesian coordinates (Ex, Ey and Ez) are returned.
* `farfieldpolar3d` : Farfieldpolar3d is identical to farfield3d, however E field components in spherical coordinates (Er, Eθ and Eϕ) are returned.
* `farfieldux` : Returns the matrix of ux corresponding to the far field data from farfield3d for a 3D simulation.
* `farfielduy` : Returns the matrix of uy corresponding to the far field data from farfield3d for a 3D simulation.
* `farfieldspherical` : Interpolates far field projection data from Cartensian to spherical coordinates: E(ux,uy) to E(θ,ϕ).
* `farfieldexact2d` : Calculates the far field over a specified grid of positions.
* `farfieldexact3d` : Calculates the far field at any specified grid of positions.
* `farfieldexact` : Similar to farfieldexact2d and farfieldexact3d, however the far field is only evaluated at positions explicitly specified by the vector list.
* `farfield2dintegrate` : Calculates the integral of the far field projection over some range of theta in 2D simulation.
* `farfield3dintegrate` : Calculates the integral of the far field projection over a specified cone in 3D simulation.

### DGTD
* `near2far` : Calculates the far field at the specified points using the provided near field monitor data.
* `createsphericalsurface` : Creates a triangulated spherical surface or a segmented circular arc.

## Grating projections
### FDTD, MODE
* `grating` : Returns the fraction of transmitted power to each physical grating orders for a given simulation.
* `gratingn` : Returns a vector of the grating order numbers.
* `gratingm` : Returns a vector of the grating order numbers.
* `gratingpolar` : Returns the relative strength of all physical grating orders in spherical coordinates.
* `gratingvector` : Returns the relative strength of all physical grating orders in cartesian coordinates.
* `gratingperiod1` : Returns grating period a 1 .
* `gratingperiod2` : Returns grating period a 2 .
* `gratingbloch1` : Returns bloch vector (k in_1 ).
* `gratingbloch2` : Returns bloch vector (k in_2 ).
* `gratingu1` : Returns first component of the unit vector u 1 .
* `gratingu2` : Returns second component of the unit vector u 2 .
* `gratingangle` : Returns the angle of each order.
* `gratingordercount` : Returns the total number of supported grating numbers.

### DGTD
* `getperiodicity` : Returns the periodicity vector(s) associated with the active periodic boundary conditions in the specified solver.
* `getsourcedirection` : Returns a unit vector in the direction of the specified source wave vector.
* `gratingorders` : Returns a matrix data set with the propagating grating orders and and their corresponding grating angles.
* `gratingprojection` : Returns a matrix data set with the propagating grating orders, grating angles and the relative power into each grating order.

## Visualizing data
Line and image plots are supported. These figures can be exported to jpeg images.

### Plotting functions
* `plot` : Makes line plots.
* `plotxy` : Makes line plots, when data sets are sampled at different position vectors.
* `polar` : Makes polar plots.
* `polar2` : Makes polar plots, when data sets are sampled at different position vectors.
* `polarimage` : Makes a 2D polar image plot.
* `smithchart` : Makes an impedance Smith chart.
* `histc` : Makes a histogram plot.
* `bar` : Makes a bar chart.
* `legend` : Adds a legend to a figure with line plots.
* `image` : Makes 2D image plots.
* `setplot` : Sets figure properties.
* `visualize` : Sends data to the visualizer.
* `add2visualizer` : Adds data to an existing visualizer
* `vectorplot` : Makes vector plots.
* `holdon` : Switches on the mode to hold multiple mathematical functions on the same figure.
* `holdoff` : Switches off the mode to hold multiple mathematical functions on the same figure.

### Miscellaneous plotting functions
* `selectfigure` : Selects a figure.
* `exportfigure` : Exports a figure.
* `closeall` : Closes all figure windows. 

## INTERCONNECT
### Element library
* `library` : Returns a list of elements available in the currently installed element libraries, including custom elements.
* `addtolibrary` : Adds an element to the currently selected custom library.
* `customlibrary` : Returns the path of the custom library.
* `saveelement` : Saves an element to file.
* `loadelement` : Loads an element from file.
* `probe` : Places a probe analyzer at a specified port.
* `loadcustom` : Redirects the location of the element library ‘Custom’ folder and reloads the contents of the folder.
* `replacelibrary` : Replaces all instances of the current library in the Element Library.
* `hideproperty` : Hides the ‘property’ of a given ‘element’.
* `protectproperty` : Protects the 'property' of a given 'element'.
* `hidecategory` : Hides all properties of a given ‘category' of a given ‘element’.
* `annotateproperty` : Enables ‘property’ annotation on a given ‘element’.
* `ispropertyactive` : Returns true if the property ‘property’ from element ‘element’ is active.
* `parsebackannotation` : Parses the waveguide back annotation.
* `parsewaveguidebackannotation` : Parses the waveguide back annotation at a given temperature in Celsius.

### Design Kit Commands
* `loaddesignkit` : Loads a design kit and directs its contents to a user defined path.
* `enabledesignkit` : Enables a design kit in the Design Kits folder.
* `disabledesignkit` : Disables a design kit in the Design Kits folder.
* `removedesignkit` : Removes a design kit from the element library ‘Design kits’ folder.
* `reloaddesignkit` : Reloads the contents of a design kit from the element library ‘Design kits’ folder.
* `packagedesignkit` : Creates a design kit file from a Custom folder.
* `installdesignkit` : Installs a design kit file to the Design Kits folder.
* `uninstalldesignkit` : Uninstalls a design kit from the Design Kits folder.
* `importlib` : Imports the .lib file for a CML in the Custom folder.
* `exportlib` : Exports the .lib file for a CML in the Custom folder.
* `renameport` : Renames the port name for a Compound or Scripted element.
* `removecustom` : Removes a folder in the Custom folder in Element Library.

### Measurements
These commands allow users to validate/retrieve results from analyzers.
* `validate` : Reruns the analysis of an analyzer.
* `validateall` : Reruns the analysis of all analyzers in the simulation.

These commands allow users to set the result for scripted elements and compound elements.
* `setresult` : Sets the result of a Scripted or a Compound element.

These commands allow users to get internal value for edacosimulation elements and N Port S-Parameter element.
* `getresultdata` : Gets results from an analyzer as matrices.
* `getvalue` : Gets an internal value for an ‘element’ internal ‘parameter’.
* `setvalue` : Sets an internal value for an element internal parameter.

These commands are used for creating scripted elements/ S-parameter element.
* `popportdata`: Extracts the fist available data value from the input port.
* `pushportdata` : Sends the data to the output port.
* `cloneportdata` : Clones an existing data value.
* `popportframe` : Returns a frame structure containing the input signal for a given input port.
* `pushportframe` : Writes a frame structure containing the output signal for a given output port.
* `getmonitorframe` : Reads the available frames from an analyzer input port.
* `getmonitorwaveform` : Returns a structure containing a waveform from an analyzer input port.
* `portdatasize` : Returns the number of data values available at the input port.
* `setsparameter` : Sets the s-parameter between output and input port.
* `importsparameter`: Imports the S-parameter data in the Script workspace to the S-parameter elements.
* `setfir` : Initializes a FIR filter using the current s-parameters.
* `seriir` : Initializes a IIR filter using the current s-parameters.
* `getports` : Returns a list of ports in an element.

These commands allow users to create user defined settings
* `setsetting` : Sets the value a user defined setting.
* `getsetting` : returns the value a user defined setting.

These commands allow users to run optimization under user defined settings.
* `runoptimization` : Runs optimization of a property from a chosen element under specified condition.

These commands allow users to export the image of the current circuit schematic.
* `exportimage` : Exports an image of the current circuit schematic.

These commands allow users to construct a symmetric coding generator matrix.
* `constructgeneratormatrix` : Constructs a symmetric coding generator matrix.

These commands allow users to import a temperature map from Icepak simulation to the INTERCONNECT schematic design.
* `importtemperaturemap`: Imports an Icepak data file to an INTERCONNECT schematic design.

## Variables
The following commands are used to create and access variables.
* `=` : Assignment operator.
* `:` : Array operator.
* `[]` : Create matrix.
* `%` : Create variable with space in the name
* `linspace` : Creates a linear spaced array.
* `matrix` : Creates a matrix filled with zeros.
* `ones` : Creates a matrix filled with ones.
* `zeros` : Creates a matrix filled with zeros.
* `randmatrix` : Creates a matrix with all elements randomly set between 0 and 1
* `randnmatrix` : Creates a matrix with all elements randomly distributed with mean 0 and standard distribution 1.
* `histogram` : Create a matrix containing the histogram count of a yield analysis result.
* `meshgridx` : Create a 2D meshgrid in x direction.
* `meshgridy` : Create a 2D meshgrid in y direction.
* `meshgrid3dx` : Create a 3D meshgrid in x direction.
* `meshgrid3dy` : Create a 3D meshgrid in y direction.
* `meshgrid3dz` : Create a 3D meshgrid in z direction.
* `meshgrid4d` : Create a 4D meshgrid in any direction
* `clear` : Clears all stored script variables from memory.
* `clearfunctions` : Clears all stored functions.
* `clearexcept` : Clears all workspace variables except the specified ones.
* `print` : Prints a string.
* `workspace` : Returns a string of all the currently defined scripting variables.
* `Matrix elements` : How to assign and access matrix elements.
* `Pre-defined constants` : List of pre-defined constants.
* `eye` : Creates identity matrix
* `struct` : Creates unstructured dataset
* `cell` : Creates cell array variable

The following commands are used to create, access and manipulate datasets. For an introduction to datasets, see the dataset introduction page.
* `rectilineardataset` : Creates an empty rectilinear dataset associated with the coordinates x/y/z.
* `matrixdataset` : Creates an empty matrix dataset.
* `unstructureddataset` : Creates an empty unstructured dataset associated with the coordinates x/y/z and the connectivity matrix
* `addparameter` : Adds a parameter to an existing dataset.
* `addattribute` : Adds an attribute to an existing dataset.
* `getresult` : Gets the dataset results from a monitor or analyzer.
* `getparameter` : Get a parameter from an existing dataset.
* `getattribute` : Get an attribute from an existing dataset.
* `deleteattribute` : Deletes an attribute from an existing dataset.
* `getmeshcontours` : Get information about the contours between different domains in an unstructured (finite-element) dataset.
* `cscsparsediff` : Determine the sparse differences between two rectilinear Lumerical datasets.

The following commands are INTERCONNECT specific.
* `global` : Returns the value of a global variable specified. Global variables are root element properties.
* `simulation` : Returns bandwidth and channel related simulation properties.

## Functions
Standard mathematical and matrix functions are listed in this page. Users have also the option to define their own custom functions using user defined functions

### Trigonometric and complex
* `sin` : Trigonometric sin function.
* `cos` : Trigonometric cos function.
* `tan` : Trigonometric tan function.
* `asin` : Inverse trigonometric sin function.
* `acos` : Inverse trigonometric cos function.
* `atan` : Inverse trigonometric tan function.
* `atan2` : Same as atan, but returns angle in correct quadrant.
* `real` : Returns the real part of variable
* `imag` : Returns the imaginary part of variable
* `conj` : Complex conjugate
* `abs` : Absolute value
* `angle` : Phase of a complex number.
* `unwrap` : Removes phase difference of more than 2π.

### Logarithmic, exponential and power
* `log` : The natural logarithm. Input can be complex or negative.
* `log10` : The log, base 10. Input can be complex or negative.
* `sqrt` : The square root.
* `exp` : The exponential.

### Matrix functions
* `size` : Returns the dimensions of a matrix.
* `length` : Returns the total number of elements in a matrix.
* `pinch` : Remove singleton dimensions from a matrix.
* `sum` : The sum of a matrix.
* `prod` : The product of elements in a matrix.
* `max` : The max value in a matrix.
* `min` : The min value in a matrix.
* `amax` : The maximum value in a specified dimension of a matrix.
* `amin` : The minimum value in a specified dimension of a matrix.
* `dot` : The dot product of two vectors.
* `cross` : The cross product of two vectors.
* `flip` : Flip a matrix in one dimension.
* `interp` : Linear interpolation function.
* `spline` : Cubic spline interpolation.
* `polyfit` : Polynomial fit.
* `normpdf` : Evaluate the normal (Gaussian) probability density function (PDF)
* `pearson4pdf` : Evaluate the Pearson IV probability density function (PDF)
* `lorentzpdf`: Evaluate the Lorentz (Cauchy) probability density function (PDF)
* `fitnormpdf` : Fit to the normal (Gaussian) probability density function (PDF)
* `fitpearson4pdf` : Fit to the Pearson IV probability density function (PDF)
* `fitlorentzpdf`: Fit to the Lorentz (Cauchy) probability density function (PDF).
* `integrate` : Integrate a matrix.
* `integrate2` : Integrate a matrix, ignore singleton dimensions.
* `find` : Find values that satisfy a condition in a matrix.
* `findpeaks` : Find peaks in a matrix.
* `findresonances` : Find the frequency, decay constant and Q-factor of resonances extracted from the time trace of a signal.
* `transpose` : Transpose a matrix.
* `ctranspose` : Transpose a matrix, and do complex conjugate.
* `mult` : Perform matrix multiplication of two or more matrices.
* `reshape` : Reshape the matrix to have different dimensions conserving the overall product of the dimensions.
* `eig` : Calculate the eigenvalues and/or eigenvectors of a matrix.
* `permute` : Rearrange the dimensions of a matrix.
* `inv` : Calculate the inverse of a matrix.
* `solve` : Solve a system of linear equations.
* `mean` : Return the mean value of a matrix.
* `var` : Returns the variance.
* `std` : Returns the standard deviance.
* `mapfind` : Returns a string value associated to specified point, given a file containing a map of values to a string.
* `svd` : Returns a 3-cell array for the decomposition.
* `chol` : Returns the lower triangular matrix.
* `norm` : Returns the matrix y to the L2-norm.
* `cov` : Calculates the covariance matrix.
* `corrcoef` : Calculates the correlation matrix.
* `scorrcoef` : Generates a spatial correlation matrix.
* `crosscorrelation`: Calculates the cross-correlation of time domain signal.
* `corrtransf` : Calculates the transformation matrix.
* `chpts` : Samples function on a Chebyshev grid.
* `chebin` : Returns Chebyshev interpolation of a sampled function.
* `chebpol` : Chebpol is similar to chebin command, but it offers additional control over the interpolation process as it allows to specify the polynomial order.
* `chebpol1` : Returns the first derivative of Chebyshev polynomials of a function sampled on the Chebyshev grid.
* `sort` : Sorts a matrix in ascending or descending order.
* `sortmap` : Sorts matrices in more complex ways than simply ascending or descending order of the array.
* `conv2` : Convolves two 2-dimensional arrays.

### String functions
* `num2str` : Convert number to a string.
* `str2num` : Convert a string into a floating point number.
* `eval` : Execute string containing Lumerical scripting language.
* `feval` : Run a Lumerical script file.
* `length` : Returns the total length of the string.
* `substring` : Returns a substring of a string, as a specified position and length.
* `findstring` : Returns the position of a substring in a string.
* `replace` : Replaces a part of a string with another, at a specified position.
* `replacestring` : Replaces all instances of a substring with another string.
* `splitstring` : Split a single long string into a cell (string) array based on a delimiting character.
* `upper` : Convert a string to upper case.
* `lower` : Convert a string to lower case.
* `toscript` : Returns a string containing the equivalent script of a generate variable.

### Frequency and time-domain
* `fft` : Fast Fourier transform.
* `fftw` : Returns the angular frequency vector.
* `fftk` : Returns the spatial wavevector kx.
* `invfft` : Inverse fft.
* `czt` : Chirped z-transform.
* `sroughness` : Returns a matrix containing a rough surface characterized by an RMS amplitude.

### Line and polygon functions
* `polyarea` : Returns the area of a polygon.
* `centroid` : Returns the center of mass of a polygon.
* `polyintersect` : Determines if two polygons intersect.
* `inpoly` : Determines if a series of points are inside our outside a polygon.
* `polyclean`: Return a simplified version of a polygon.
* `polygrow` : Expands or shrinks a polygon by a specified amount.
* `polyand` : Combines two polygons into one with an and operation.
* `polyor` : Combines two polygons into one with an or operation.
* `polydiff` : Combines two polygons into one by taking the difference.
* `polystencil`: Returns the vertices of polygons formed by intersection of structures and specified z-normal planes
* `polyxor` : Combines two polygons into one with a xor operation.
* `lineintersect` : Returns the intersection of line segments.
* `linecross` : Determines if line segments cross each other.

### Colorimetry
* `colormatchfunction` : Returns a set of color matching functions.
* `colormatch` : Calculates the X, Y, Z tristimulus values for a set of color matching functions.
* `colormatchxy` : Calculates the x, y chromaticity values for a set of color matching functions.
* `colormatchuv` : Calculates the u, v chromaticity values for a set of color matching functions.

### Multilayer stack calculations
* `stackrt` : Calculates the reflection and transmission of a plane wave through a multi-layer stack using the analytic transfer matrix method.
* `stackfield` : Calculates the fields within a multilayer stack illuminated from below by a plane wave using the analytic transfer matrix method.
* `stackdipole` : Analytically calculates the dipole emission for a multilayer stack.
* `stackpurcell`: Analytically calculates the Purcell factor and far-field emission power density for a multilayer stack

### Multi-quantum well calculations
* `mqwgain` : Calculates gain and spontaneous emission in multiple quantum well structures
* `mqwindex` : Calculates complex index, gain, and spontaneous emission in multiple quantum well structures
* `buildmqwmaterial` : Returns material properties of the type and format required by mqwgain and mqwindex

### Ion implant doping calculations
* `implantrange` : Calculates the range of the doping profile from ion implant.
* `implantstraggle` : Calculates the straggle of the doping profile from ion implant.
* `implantskewness` : Calculates the skewness of the doping profile from ion implant.
* `implantkurtosis` : Calculates the kurtosis of the doping profile from ion implant.
* `implantlateralscatter` : Calculates the lateral scatter of the doping profile from ion implant.

### Miscellaneous
* `ceil` : Round up.
* `floor` : Round down.
* `mod` : Modulus after division.
* `round` : Rounds to the nearest integer.
* `rand` : Returns a uniformly distributed random number between 0 and 1.
* `lognrnd` : Returns a lognormal distributed random number.
* `randn` : Returns a normally distributed random number.
* `randreset` : Resets the random number seed.
* `randpearson4` : Generates random number based on Pearson type IV distribution.
* `finite` : Determines if a number is finite or NaN.
* `solar` : Returns the solar power spectrum
* `all` : Returns 1 if all of the specified matrix entries are nonzero and returns 0 otherwise.
* `any` : Returns 1 if any of the specified matrix entries are nonzero and returns 0 otherwise.
* `interptri` : Interpolates a data set from a triangular to a rectilinear grid.
* `interptet` : Interpolates a data set in 3D from a tetrahedral to a rectangular grid.
* `quadtri` : Returns approximated integration (first order quadrature) of data on a 2D finite element mesh.
* `quadtet` : Returns approximated integration of data on a 3D finite element mesh.
* `precision` : Returns truncated value to a user specified precision.
* `erf` : Returns the error function.
* `erfc` : Returns the complementary error function.
* `erfinv` : Returns the inverse error function.
* `erfcinv` : Returns the inverse complementary error function.
* `unique` : Returns an array containing all unique values in a given matrix.
* `uniquevertices` : Given a matrix of vertices, returns a matrix of unique vertices with differences in values larger than a specified tolerance.
* `icht` : Takes the Chebyshev interpolation coefficients and returns the corresponding function samples
* `dcht` : Returns the Chebyshev interpolation coefficients
* `besselj` : Bessel function of the first kind
* `bessely` : Bessel function of the second kind
* `besseli` : Modified Bessel function of the first kind
* `besselk` : Modified Bessel function of the second kind
* `mie3d` : Analytically calculates scattering, absorption, and extinction coefficients of a spherical particle.
* `mie3ds12` : Analytically calculates scattered farfield functions of a spherical particle.
