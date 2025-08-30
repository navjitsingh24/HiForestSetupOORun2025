Last login: Sat Aug 23 14:26:55 on ttys009
navjitsingh@Navjits-MacBook-Pro ~ % ssh nasingh@lxplus.cern.ch
(nasingh@lxplus.cern.ch) Password: 
* ********************************************************************
* Welcome to lxplus996.cern.ch, Red Hat Enterprise Linux release 9.6 (Plow)
* Archive of news is available in /etc/motd-archive
* Reminder: you have agreed to the CERN
*   computing rules, in particular OC5. CERN implements
*   the measures necessary to ensure compliance.
*   https://cern.ch/ComputingRules
* Puppet environment: production, Roger state: production
* Foreman hostgroup: lxplus/nodes/login
* Availability zone: cern-geneva-a
* LXPLUS Public Login Service - http://lxplusdoc.web.cern.ch/
* Please read LXPLUS Privacy Notice in http://cern.ch/go/TpV7
* ********************************************************************
* /!\ LxPlus will require 2fa from September 2nd 2025 /!\
*  Test your access from now https://cern.ch/otg0152605
*  All details for 2FA enforcing on https://cern.ch/otg0156449

[nasingh@lxplus996 ~]$ ls
CMSSW_15_0_11  CMSSW_8_0_36_patch2  listofforestfiles.txt  out.txt  pPb_eff  private  pthat80_part1.txt  public  Skimming  Tracking_group  UIC
[nasingh@lxplus996 ~]$ cd CMSSW_15_0_11/src/
[nasingh@lxplus996 src]$ cmsenv
[nasingh@lxplus996 src]$ ls
HeavyIonsAnalysis  HiForestSetupOORun2025
[nasingh@lxplus996 src]$ cd HiForestSetupOORun2025/
[nasingh@lxplus996 HiForestSetupOORun2025]$ ls -ltr
total 2388
-rw-r--r--. 1 nasingh zh 2397935 Aug 30 08:31 emap_2025_full.txt
-rw-r--r--. 1 nasingh zh    6750 Aug 30 08:31 README.md
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 OO_Reco_v1
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 ForestConfigArchive
-rw-r--r--. 1 nasingh zh     154 Aug 30 08:31 submitScript.sh
-rw-r--r--. 1 nasingh zh    1256 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_filelist_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    7033 Aug 30 08:31 forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:39 forest_CRABConfig_Run3_OXY_DATA_NEW.py
-rw-r--r--. 1 nasingh zh    9860 Aug 30 09:05 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD.py
-rw-r--r--. 1 nasingh zh    9504 Aug 30 09:18 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
-rw-r--r--. 1 nasingh zh      63 Aug 30 09:18 HiForestMiniAOD.root
[nasingh@lxplus996 HiForestSetupOORun2025]$ rm HiForestMiniAOD.root
[nasingh@lxplus996 HiForestSetupOORun2025]$ voms-proxy-init -rfc -voms cms
Enter GRID pass phrase:
Your identity: /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=nasingh/CN=862393/CN=Navjit Singh
Creating temporary proxy .......................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... Done
Contacting  voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms" Done
Creating proxy ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... Done

Your proxy is valid until Sat Aug 30 21:20:38 2025
[nasingh@lxplus996 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus996 HiForestSetupOORun2025]$ cmsRun forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
30-Aug-2025 09:21:28 CEST  Initiating request to open file root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:21:29 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov1213xrootd.unl.edu&xrdcl.requuid=8495ba38-7a28-49fe-9183-ad146c65bb42.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:21:29 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov1213xrootd.unl.edu,&xrdcl.requuid=d79c04e7-7658-4384-a3be-446d6f6775e1.
%MSG
----- Begin Fatal Exception 30-Aug-2025 09:21:29 CEST-----------------------
An exception of category 'FileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
   Additional Info:
      [a] Input file root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened.
      [b] XrdCl::File::Open(name='root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [c] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov1213xrootd.unl.edu,&xrdcl.requuid=d79c04e7-7658-4384-a3be-446d6f6775e1
      [d] Problematic data server: cms-xrd-global.cern.ch:1094
      [e] Disabled source: cms-xrd-global.cern.ch:1094
----- End Fatal Exception -------------------------------------------------
[nasingh@lxplus996 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus996 HiForestSetupOORun2025]$ cmsRun forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
30-Aug-2025 09:22:11 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:22:12 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?xrdcl.requuid=fb4fb7ae-268d-4de7-804a-2e40c8cb628b.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:22:12 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=ec3c894a-2a55-413d-900f-9ff841d9dab4.
%MSG
30-Aug-2025 09:22:12 CEST  Initiating request to open file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:22:13 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it&xrdcl.requuid=56327aa4-3728-4529-8683-08a67ec90c5d.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:22:13 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=2ae200ba-6bfd-45ca-bb4d-f6430e452527.
%MSG
%MSG-w RootInputFileSequence:  file_open 30-Aug-2025 09:22:13 CEST pre-events
Input file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened, and fallback was attempted.
Additional information:
  [a] Disabled source: eoscms.cern.ch:1094
  [b] Problematic data server: eoscms.cern.ch:1094
  [c] Last URL tried: root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=ec3c894a-2a55-413d-900f-9ff841d9dab4
  [d] XrdCl::File::Open(name='root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] Unable to open file /eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root; No such file or directory
' (errno=3011, code=400). No additional data servers were found.

%MSG
----- Begin Fatal Exception 30-Aug-2025 09:22:13 CEST-----------------------
An exception of category 'FallbackFileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
      [b] Input file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened.
      [c] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [d] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=2ae200ba-6bfd-45ca-bb4d-f6430e452527
      [e] Problematic data server: cms-xrd-global.cern.ch:1094
      [f] Disabled source: cms-xrd-global.cern.ch:1094
----- End Fatal Exception -------------------------------------------------
[nasingh@lxplus996 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus996 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus996 HiForestSetupOORun2025]$ cmsRun forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
30-Aug-2025 09:28:08 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:28:09 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?xrdcl.requuid=9479e906-dbc7-4693-baf8-04ad46c65f79.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:28:09 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=7bbdf8f2-7060-4f26-9481-e374f73b503b.
%MSG
30-Aug-2025 09:28:09 CEST  Initiating request to open file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:28:10 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-cms-redir-int.cr.cnaf.infn.it&xrdcl.requuid=ff2d0920-5a68-4b87-99c8-6a0091bb626c.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:28:10 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-cms-redir-int.cr.cnaf.infn.it,&xrdcl.requuid=ea951968-54d6-40e2-bdb9-7abd1699618d.
%MSG
%MSG-w RootInputFileSequence:  file_open 30-Aug-2025 09:28:10 CEST pre-events
Input file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened, and fallback was attempted.
Additional information:
  [a] Disabled source: eoscms.cern.ch:1094
  [b] Problematic data server: eoscms.cern.ch:1094
  [c] Last URL tried: root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=7bbdf8f2-7060-4f26-9481-e374f73b503b
  [d] XrdCl::File::Open(name='root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] Unable to open file /eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root; No such file or directory
' (errno=3011, code=400). No additional data servers were found.

%MSG
----- Begin Fatal Exception 30-Aug-2025 09:28:10 CEST-----------------------
An exception of category 'FallbackFileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
      [b] Input file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened.
      [c] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [d] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-cms-redir-int.cr.cnaf.infn.it,&xrdcl.requuid=ea951968-54d6-40e2-bdb9-7abd1699618d
      [e] Problematic data server: cms-xrd-global.cern.ch:1094
      [f] Disabled source: cms-xrd-global.cern.ch:1094
----- End Fatal Exception -------------------------------------------------
[nasingh@lxplus996 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus996 HiForestSetupOORun2025]$ cmsRun forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
30-Aug-2025 09:29:39 CEST  Initiating request to open file root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:29:40 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov&xrdcl.requuid=12e1787f-1bb9-4f21-8007-c04843e5a4cb.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 30-Aug-2025 09:29:40 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov,&xrdcl.requuid=a5032138-3783-4286-bed7-d19bb38bc3b0.
%MSG
----- Begin Fatal Exception 30-Aug-2025 09:29:40 CEST-----------------------
An exception of category 'FileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
   Additional Info:
      [a] Input file root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened.
      [b] XrdCl::File::Open(name='root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [c] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213cmsxrootd2.fnal.gov,&xrdcl.requuid=a5032138-3783-4286-bed7-d19bb38bc3b0
      [d] Problematic data server: cms-xrd-global.cern.ch:1094
      [e] Disabled source: cms-xrd-global.cern.ch:1094
----- End Fatal Exception -------------------------------------------------
[nasingh@lxplus996 HiForestSetupOORun2025]$ dasgoclient -query="file=/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root"
/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
[nasingh@lxplus996 HiForestSetupOORun2025]$ xrdcp root://cmsxrootd-site.fnal.gov//store/.../0521af1f-18a9-402a-b6e3-82cb07916fdd.root .
^C
[nasingh@lxplus996 HiForestSetupOORun2025]$ xrdcp root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
xrdcp: Destination not specified.

Usage:   xrdcp [<options>] <src> [<src> [. . .]] <dest>

Options: [--allow-http] [--cksum <args>] [--coerce] [--continue]
         [--debug <lvl>] [--dynamic-src] [--force] [--help]
         [--infiles <fn>] [--license] [--nopbar] [--notlsok]
         [--parallel <n>] [--posc] [--proxy <host>:<port>]
         [--recursive] [--retry <n>] [--retry-policy <force|continue>]
         [--rm-bad-cksum] [--server] [--silent] [--sources <n>]
         [--streams <n>] [--tlsmetalink] [--tlsnodata]
         [--tpc [delegate] {first|only}] [--verbose] [--version]
         [--xattr] [--xrate <rate>] [--xrate-threshold <rate>]
         [--zip <file>] [--zip-append] [--zip-mtln-cksum]

<src>:   [[x]root[s]://<host>[:<port>]/]<path> | -
<dest>:  [[x]root[s]://<host>[:<port>]/]<path> | -
[nasingh@lxplus996 HiForestSetupOORun2025]$ xrdcp root://cmsxrootd.fnal.gov//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root .
[0B/0B][100%][==================================================][0B/s]  
Run: [ERROR] Server responded with an error: [3011] No servers are available to read the file. (source)

[nasingh@lxplus996 HiForestSetupOORun2025]$ exit 
logout
Connection to lxplus.cern.ch closed.
navjitsingh@Navjits-MacBook-Pro ~ % ssh nasingh@lxplus.cern.ch
(nasingh@lxplus.cern.ch) Password: 
* ********************************************************************
* Welcome to lxplus916.cern.ch, Red Hat Enterprise Linux release 9.6 (Plow)
* Archive of news is available in /etc/motd-archive
* Reminder: you have agreed to the CERN
*   computing rules, in particular OC5. CERN implements
*   the measures necessary to ensure compliance.
*   https://cern.ch/ComputingRules
* Puppet environment: qa, Roger state: production
* Foreman hostgroup: lxplus/nodes/login
* Availability zone: cern-geneva-c
* LXPLUS Public Login Service - http://lxplusdoc.web.cern.ch/
* Please read LXPLUS Privacy Notice in http://cern.ch/go/TpV7
* ********************************************************************
* /!\ LxPlus will require 2fa from September 2nd 2025 /!\
*  Test your access from now https://cern.ch/otg0152605
*  All details for 2FA enforcing on https://cern.ch/otg0156449

Last failed login: Thu Aug 21 09:55:28 CEST 2025 from 2601:644:8186:1d0:b897:80ee:69c5:6d13 on ssh:notty
There was 1 failed login attempt since the last successful login.
[nasingh@lxplus916 ~]$ ls
CMSSW_15_0_11  CMSSW_8_0_36_patch2  listofforestfiles.txt  out.txt  pPb_eff  private  pthat80_part1.txt  public  Skimming  Tracking_group  UIC
[nasingh@lxplus916 ~]$ cd CMSSW_15_0_11/src/
[nasingh@lxplus916 src]$ cmsenv
[nasingh@lxplus916 src]$ ls
HeavyIonsAnalysis  HiForestSetupOORun2025
[nasingh@lxplus916 src]$ cd HiForestSetupOORun2025/
[nasingh@lxplus916 HiForestSetupOORun2025]$ ls
ForestConfigArchive   README.md                                    forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py  forest_CRABConfig_Run3_OXY_DATA_TEMPLATE.py
HiForestMiniAOD.root  emap_2025_full.txt                           forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py         forest_CRABConfig_Run3_OXY_DATA_filelist_TEMPLATE.py
OO_Reco_v1            forest_CMSSWConfig_Run3_OXY_DATA_miniAOD.py  forest_CRABConfig_Run3_OXY_DATA_NEW.py            submitScript.sh
[nasingh@lxplus916 HiForestSetupOORun2025]$ voms-proxy-init -rfc -voms cms
Enter GRID pass phrase:
Your identity: /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=nasingh/CN=862393/CN=Navjit Singh
Creating temporary proxy ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... Done
Contacting  voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms" Done
Creating proxy ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................ Done

Your proxy is valid until Sun Aug 31 13:28:36 2025
[nasingh@lxplus916 HiForestSetupOORun2025]$ ls -ltr
total 2388
-rw-r--r--. 1 nasingh zh 2397935 Aug 30 08:31 emap_2025_full.txt
-rw-r--r--. 1 nasingh zh    6750 Aug 30 08:31 README.md
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 OO_Reco_v1
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 ForestConfigArchive
-rw-r--r--. 1 nasingh zh     154 Aug 30 08:31 submitScript.sh
-rw-r--r--. 1 nasingh zh    1256 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_filelist_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    7033 Aug 30 08:31 forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:39 forest_CRABConfig_Run3_OXY_DATA_NEW.py
-rw-r--r--. 1 nasingh zh    9860 Aug 30 09:05 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD.py
-rw-r--r--. 1 nasingh zh    9498 Aug 30 09:29 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
-rw-r--r--. 1 nasingh zh     485 Aug 30 09:29 HiForestMiniAOD.root
[nasingh@lxplus916 HiForestSetupOORun2025]$ rm HiForestMiniAOD.root 
[nasingh@lxplus916 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus916 HiForestSetupOORun2025]$ cmsRun forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
31-Aug-2025 01:29:18 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 31-Aug-2025 01:29:19 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?xrdcl.requuid=6b69b1ec-bd67-44a6-bf95-191c2e6aacf4.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 31-Aug-2025 01:29:19 CEST pre-events
Failed to open file at URL root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=1d035c85-3ab4-4402-a4e2-5f21c2fb1fcf.
%MSG
31-Aug-2025 01:29:19 CEST  Initiating request to open file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
%MSG-w XrdAdaptorInternal:  file_open 31-Aug-2025 01:30:25 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it&xrdcl.requuid=24941177-753e-4b8b-954d-4c6aff45c872.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 31-Aug-2025 01:30:25 CEST pre-events
Failed to open file at URL root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=3d48ebbd-5a27-44a6-b834-8de8e4d7be63.
%MSG
%MSG-w RootInputFileSequence:  file_open 31-Aug-2025 01:30:25 CEST pre-events
Input file root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened, and fallback was attempted.
Additional information:
  [a] Disabled source: eoscms.cern.ch:1094
  [b] Problematic data server: eoscms.cern.ch:1094
  [c] Last URL tried: root://eoscms.cern.ch:1094//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=&xrdcl.requuid=1d035c85-3ab4-4402-a4e2-5f21c2fb1fcf
  [d] XrdCl::File::Open(name='root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] Unable to open file /eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root; No such file or directory
' (errno=3011, code=400). No additional data servers were found.

%MSG
----- Begin Fatal Exception 31-Aug-2025 01:30:25 CEST-----------------------
An exception of category 'FallbackFileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   [3] Calling StorageFactory::open()
   [4] Calling XrdFile::open()
Exception Message:
Failed to open the file 'root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root'
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root
      [b] Input file root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root could not be opened.
      [c] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=', flags=0x10, permissions=0660) => error '[ERROR] Server responded with an error: [3011] No servers are available to read the file.
' (errno=3011, code=400). No additional data servers were found.
      [d] Last URL tried: root://cms-xrd-global.cern.ch:1094//store/hidata/OORun2025/IonPhysics0/RAW/v1/000/394/075/00000/0521af1f-18a9-402a-b6e3-82cb07916fdd.root?tried=+1213xrootd-redic.pi.infn.it,&xrdcl.requuid=3d48ebbd-5a27-44a6-b834-8de8e4d7be63
      [e] Problematic data server: cms-xrd-global.cern.ch:1094
      [f] Disabled source: cms-xrd-global.cern.ch:1094
----- End Fatal Exception -------------------------------------------------
[nasingh@lxplus916 HiForestSetupOORun2025]$ ls -ltr
total 2388
-rw-r--r--. 1 nasingh zh 2397935 Aug 30 08:31 emap_2025_full.txt
-rw-r--r--. 1 nasingh zh    6750 Aug 30 08:31 README.md
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 OO_Reco_v1
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 ForestConfigArchive
-rw-r--r--. 1 nasingh zh     154 Aug 30 08:31 submitScript.sh
-rw-r--r--. 1 nasingh zh    1256 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_filelist_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    7033 Aug 30 08:31 forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:39 forest_CRABConfig_Run3_OXY_DATA_NEW.py
-rw-r--r--. 1 nasingh zh    9860 Aug 30 09:05 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD.py
-rw-r--r--. 1 nasingh zh    9472 Aug 31 01:29 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
-rw-r--r--. 1 nasingh zh     485 Aug 31 01:30 HiForestMiniAOD.root
[nasingh@lxplus916 HiForestSetupOORun2025]$ rm HiForestMiniAOD.root 
[nasingh@lxplus916 HiForestSetupOORun2025]$ ls -ltr
total 2387
-rw-r--r--. 1 nasingh zh 2397935 Aug 30 08:31 emap_2025_full.txt
-rw-r--r--. 1 nasingh zh    6750 Aug 30 08:31 README.md
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 OO_Reco_v1
drwxr-xr-x. 2 nasingh zh    2048 Aug 30 08:31 ForestConfigArchive
-rw-r--r--. 1 nasingh zh     154 Aug 30 08:31 submitScript.sh
-rw-r--r--. 1 nasingh zh    1256 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_filelist_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:31 forest_CRABConfig_Run3_OXY_DATA_TEMPLATE.py
-rw-r--r--. 1 nasingh zh    7033 Aug 30 08:31 forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py
-rw-r--r--. 1 nasingh zh    1229 Aug 30 08:39 forest_CRABConfig_Run3_OXY_DATA_NEW.py
-rw-r--r--. 1 nasingh zh    9860 Aug 30 09:05 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD.py
-rw-r--r--. 1 nasingh zh    9472 Aug 31 01:29 forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py
[nasingh@lxplus916 HiForestSetupOORun2025]$ vim forest_CMSSWConfig_Run3_OXY_DATA_miniAOD_test.py

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
