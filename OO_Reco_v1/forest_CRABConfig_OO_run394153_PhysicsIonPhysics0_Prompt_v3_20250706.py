from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsername
username = getUsername()

###############################################################################
# INPUT/OUTPUT SETTINGS

jobTag = 'OO_394153_PhysicsIonPhysics0_Prompt_v3'
inputFilelist = 'filelist_' + jobTag + '.txt'

output = '/store/group/phys_heavyions/' + username + '/Run3_OO_2025Data_QuickForest/'
outputServer = 'T2_CH_CERN'

###############################################################################

config = config()

config.General.requestName = jobTag
config.General.workArea = 'CrabWorkArea'
config.General.transferOutputs = True

config.JobType.psetName = 'forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_v1.py'
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 5000
config.JobType.pyCfgParams = ['noprint']
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = jobTag
config.Data.userInputFiles = open(inputFilelist).readlines()
config.Data.outLFNDirBase = output
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.allowNonValidInputDataset = True

#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = outputServer
