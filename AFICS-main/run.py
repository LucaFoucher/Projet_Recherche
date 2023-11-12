import rmsdv2

#outputFile = 'Cr-results' #Name of prefix for output files 
#traj = rmsdv2.Trajectory(ionID='Cr', elements=['O'], boxSize=12.42, framesForRMSD=100, binSize=0.02, startFrame=1, endFrame=10000) #MD trajectory model information 
#traj.getAtoms('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/examples/Cr-aqua/Cr-aqua.xyz') #Name of MD trajectory xyz file

outputFile = 'EDTA' #Name of prefix for output files 
traj = rmsdv2.Trajectory(ionID='Eu', elements=['O','N'], boxSize=17.5, framesForRMSD=1000, binSize=0.02, startFrame=1, endFrame=10000)

traj.getAtoms('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/examples/Eu-EDTA/Eu-EDTA.xyz') #Name of MD trajectory xyz file


traj.getIonNum()
if (traj.ionNum > 1): 
    traj.getWhichIon() 
traj.getRDF() 
traj.getDist()
traj.getMaxR()
traj.printRDF(outputFile)
traj.checkWithUser() #This may be commented out if user does not wish to be prompted to confirm/reject predicted RDF maximum, first shell threshold, and coordination number
traj.getThresholdAtoms()
traj.getADF()
traj.printADF(outputFile)
traj.getIdealGeos()
traj.getRMSDs()
traj.printRMSDs(outputFile)
traj.outputIdealGeometries('') #Location name may be entered in string if user desires geometries to be written to subfolder instead of working directory 
