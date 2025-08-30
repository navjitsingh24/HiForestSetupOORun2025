### HiForest CMSSW Configuration
# Collisions: Oxygen-Oxygen
# Input: miniAOD
# Type: data

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_2025_OXY_cff import Run3_2025_OXY
process = cms.Process('HiForest', Run3_2025_OXY)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 150X, data")

# import subprocess, os
# version = subprocess.check_output(
#     ['git', '-C', os.path.expandvars('$CMSSW_BASE/src'), 'describe', '--tags'])
# if version == '':
#     version = 'no git info'
# process.HiForestInfo.HiForestVersion = cms.string(version)

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
         '/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
    )
)

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_Prompt_v3', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

###############################################################################

# Define centrality binning
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#     )
# )

# process.output_path = cms.EndPath(process.output)
###############################################################################

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('L1Trigger.L1TNtuples.l1MetFilterRecoTree_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
process.particleFlowAnalyser.ptMin = cms.double(0.)
process.particleFlowAnalyser.absEtaMax = cms.double(6.)
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.hiEvtAnalyzer.doHFfilters = cms.bool(False)
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.hltobject.triggerNames = cms.vstring()
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')
# process.hiEvtAnalyzer.doCentrality = cms.bool(False) # for UPC
################################
# electrons, photons, muons
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = cms.bool(False)
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.ggHiNtuplizer.useValMapIso = cms.bool(False) # True here causes seg fault
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.ak4PFJetSequence_ppref_data_cff')
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
process.ppTracks.dedxEstimators = cms.VInputTag(["dedxEstimator:dedxAllLikelihood", "dedxEstimator:dedxPixelLikelihood", "dedxEstimator:dedxStripLikelihood"])
# muons
###############################################################################

#########################
# ZDC RecHit Producer && Analyzer
#########################
# to prevent crash related to HcalSeverityLevelComputerRcd record
process.load("RecoLocalCalo.HcalRecAlgos.hcalRecAlgoESProd_cfi")
process.load('HeavyIonsAnalysis.ZDCAnalysis.ZDCAnalyzersPbPb_cff')

# =============================================================================
# ==================== modification needed for the fsc data ===================
from CondCore.CondDB.CondDB_cfi import *
process.es_pool = cms.ESSource("PoolDBESSource",
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string("HcalElectronicsMapRcd"),
            tag = cms.string("HcalElectronicsMap_v10.0_offline")
        )
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
)
process.es_prefer = cms.ESPrefer('HcalTextCalibrations', 'es_ascii')
process.es_ascii = cms.ESSource(
    'HcalTextCalibrations',
    input = cms.VPSet(
        cms.PSet(
            object = cms.string('ElectronicsMap'),
            file = cms.FileInPath("/afs/cern.ch/user/n/nasingh/CMSSW_15_0_11/src/HiForestSetupOORun2025/emap_2025_full.txt")
        )
    )
)
# =============================================================================

###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    process.centralityBin +
    process.hltanalysis +
   # process.hltobject +
    process.l1object +
    process.l1MetFilterRecoTree +
    process.trackSequencePP +
   process.particleFlowAnalyser +
    process.hiEvtAnalyzer +
  #  process.zdcSequencePbPb +
   # process.fscSequence +
   # process.ppsSequence +
    process.ggHiNtuplizer
  #  process.jetanalyzer
   # process.unpackedMuons +
   # process.muonAnalyzer
)

#####################################################################################
# Select the types of jets filled
matchJets = True             # Enables q/g and heavy flavor jet identification in MC
jetPtMin = 15
jetAbsEtaMax = 2.5

# Choose which additional information is added to jet trees
doHIJetID = True             # Fill jet ID and composition information branches
doWTARecluster = True        # Add jet phi and eta for WTA axis
doBtagging  =  False         # Note that setting to True increases computing time a lot

# 0 means use original mini-AOD jets, otherwise use R value, e.g., 3,4,8
# Add all the values you want to process to the list
jetLabels = ["4"]

# add candidate tagging for all selected jet radii
from HeavyIonsAnalysis.JetAnalysis.setupJets_ppRef_cff import candidateBtaggingMiniAOD

for jetLabel in jetLabels:
    candidateBtaggingMiniAOD(process, isMC = False, jetPtMin = jetPtMin, jetCorrLevels = ['L2Relative', 'L3Absolute'], doBtagging = doBtagging, labelR = jetLabel)

    # setup jet analyzer
    setattr(process,"ak"+jetLabel+"PFJetAnalyzer",process.ak4PFJetAnalyzer.clone())
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").jetTag = "selectedUpdatedPatJetsAK"+jetLabel+"PFCHSBtag"
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").jetName = 'ak'+jetLabel+'PF'
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").matchJets = matchJets
   getattr(process,"ak"+jetLabel+"PFJetAnalyzer").matchTag = 'patJetsAK'+jetLabel+'PFUnsubJets'
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").doBtagging = doBtagging
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").doHiJetID = doHIJetID
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").doWTARecluster = doWTARecluster
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").jetPtMin = jetPtMin
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").jetAbsEtaMax = cms.untracked.double(jetAbsEtaMax)
    getattr(process,"ak"+jetLabel+"PFJetAnalyzer").rParam = 0.4 if jetLabel=='0' else float(jetLabel)*0.1
    if doBtagging:
        getattr(process,"ak"+jetLabel+"PFJetAnalyzer").pfJetProbabilityBJetTag = cms.untracked.string("pfJetProbabilityBJetTagsAK"+jetLabel+"PFCHSBtag")
        getattr(process,"ak"+jetLabel+"PFJetAnalyzer").pfUnifiedParticleTransformerAK4JetTags = cms.untracked.string("pfUnifiedParticleTransformerAK4JetTagsAK"+jetLabel+"PFCHSBtag")
    process.forest += getattr(process,"ak"+jetLabel+"PFJetAnalyzer")

#########################
# Event Selection -> add the needed filters here
#########################

process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.load('HeavyIonsAnalysis.EventAnalysis.hffilterPF_cfi')
process.pAna = cms.EndPath(process.skimanalysis)

process.HFAdcana = cms.EDAnalyzer("HFAdcToGeV",
    digiLabel = cms.untracked.InputTag("hcalDigis"),
    #digiLabel = cms.untracked.InputTag("simHcalUnsuppressedDigis","HFQIE10DigiCollection"),
    minimized = cms.untracked.bool(True),
    fillhf = cms.bool(False) # only turn this on when you have or know how to produce "towerMaker"
)
process.hfadc = cms.Path(process.HFAdcana)

process.MessageLogger.cerr.FwkReport.reportEvery = 100
