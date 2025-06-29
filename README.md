# 2025 CMS Small Systems Run - Foresting

1. Setup
2. Processing Forests
3. Quick Reference
    - CMSSW 
    - CRAB
    - VOMS Certificate Setup

--------------------------------------------------------------------------------

## 1) Setup

> [!WARNING]
> To use CRAB for foresting, you will need to work from **lxplus8**.
> ```bash
> ssh <your_cern_id>@lxplus8.cern.ch
> ```

### 1.1) Install CMSSW
```bash
cmsrel CMSSW_15_0_9
cd CMSSW_15_0_9/src
cmsenv
```

### 1.2) Add CMS Heavy Ion foresting tools
```bash
git cms-merge-topic CmsHI:forest_CMSSW_15_0_X
scram build -j4
```

> [!TIP] 
> You can add CMSHI as a remote git reference in case of updates:
> ```bash
> git remote add cmshi git@github.com:CmsHI/cmssw.git
> ```

### 1.3) Clone this repository
```bash
git clone git@github.com:jdlang/HiForestSetupOORun2025.git
cd HiForestSetupOORun2025/
```

### 1.4) Download ZDC emap and copy into `CMSSW_15_0_9/src/HeavyIonsAnalysis/Configuration/data/`
```bash
wget https://github.com/hjbossi/ZDCOnlineMonitoring/blob/main/Conditions/emap/emap_2025_full.txt
cp emap_2025_full.txt HeavyIonsAnalysis/Configuration/data/
```

--------------------------------------------------------------------------------

## 2) Processing Forests

### 2.0) Edit CRABConfig settings
Make a **copy** of the CRABConfig file with an appropriate name:
```bash
cp forest_CRABConfig_Run3_OO_DATA_TEMPLATE.py forest_CRABConfig_Run3_OO_DATA_<your_label>.py
```
> [!TIP]
> If you want to process over a local file or a list of files, use
> `forest_CRABConfig_Run3_OO_DATA_filelist_TEMPLATE.py` as your template
> instead. Save your file(s) to a `.txt` file using a command like:
> ```bash
> ls /path/to/files/*.root > filelist.txt
> ```

Modify the input and output paths in the config (example shown below):
```Python
# INPUT/OUTPUT SETTINGS

jobTag = 'Run3_OO_IonPhysics_runXXXXXX'
input = '/DAS/Path/'
inputDatabase = 'phys03'
output = '/store/group/phys_heavyions/' + username + '/Run3_OO_2025Data_QuickForest/'
outputServer = 'T2_CH_CERN'
```
Explanation of variables:
- `jobTag` is a personal label for differentiating samples.
- `input` is the miniAOD path on [CMS DAS](https://cmsweb.cern.ch/das/).
- `inputDatabase` is the DAS "dbs instance" that contains the files
  (typically `'global'` or `'phys03'`).
- `output` is the path on the output server. Forested files are saved here.
- `outputServer` is the CMS T2 server where data will be stored.

### 2.1) Initialize VOMS proxy
```bash
voms-proxy-init -rfc -voms cms
```
> [!TIP] 
> Add an alias for this to `~/.bash_profile` to make VOMS easier:
> ```bash
> alias proxy='voms-proxy-init -rfc -voms cms; cp/tmp/x509up_u'$(id -u)' ~/'
> ```
> This will let you initialize VOMS just by running the command: `proxy`

### 2.2) Submit CRAB jobs
```bash
crab submit -c forest_CRABConfig_Run3_OO_DATA_<your_label>.py
```

### 2.3) Track status of CRAB jobs
You can view the status of a job with:
```bash
crab status -d CrabWorkArea/crab_<your job tag>/
```
> [!TIP]
> Always check job status ~2-3 minutes after submitting to make sure the job
> has been accepted! If you see the status `SUBMITREFUSED` you will need to fix
> the config(s) and delete the job folder from `CrabWorkArea/` before
> submitting it again.

When you (inevitably) have failed jobs, you can resubmit them with:
```bash
crab resubmit -d CrabWorkArea/crab_<your job tag>/
```
Optionally you can also change the requested memory or runtime for jobs when
you resubmit:
```bash
crab resubmit --maxmemory 2500 --maxruntime 300 -d CrabWorkArea/crab_<your job tag>/
```
> [!WARNING]
> Requesting more than the maximum allowed memory or runtime will result in
> your job being refused and **you will be unable to __resubmit__ any failed jobs
> for that CRAB submission!** 
> * `maxmemory` **must not exceed 5000** (MB)!
> * `maxruntime` **must not exceed 900** (minutes)!

If you need to stop a job before it finishes, use:
```bash
crab kill -d CrabWorkArea/crab_<your job tag>/
```



--------------------------------------------------------------------------------

# 3) Quick Reference

## CMSSW
```bash
# Run CMSSWConfig LOCALLY:
cmsRun forest_CMSSWConfig_XXXX.py
```


## CRAB
```bash
# Submit job:
crab submit -c <CRAB_config_file.py>

# Check job status:
crab status -d <path/to/crab_status_directory/>

# Kill a job (WARNING: this is irreversible!):
crab kill -d <path/to/crab_status_directory/>

# Resubmit failed jobs:
crab resubmit -d <path/to/crab_status_directory/>
# Resubmit with max memory and max runtime
crab resubmit --maxmemory 3000 --maxruntime 450 -d <path/to/crab_status_directory/>
```


## VOMS Certificate Setup

### Obtaining Certificates

https://ca.cern.ch/ca/user/Request.aspx?template=ee2user

Use the “New Grid User Certificate” tab to get a new CERN grid. You should set a password for this, and will need to remember it.

### Linux/Unix Installation

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid#BasicGrid

To **setup the certificate** in your remote workspace, you should:
1. Export the certificate from your browser to a file in p12 format. You can 
give any name to your p12 file (in the example below the name is `mycert.p12`).

2. Place the p12 certificate file in the `.globus` directory of your home area. 
If the `.globus` directory doesn't exist, create it.
```bash
cd ~
mkdir .globus
cd ~/.globus
mv /path/to/mycert.p12 .
```

3. Execute the following shell commands:
```bash
rm -f usercert.pem
rm -f userkey.pem
openssl pkcs12 -in mycert.p12 -clcerts -nokeys -out usercert.pem
openssl pkcs12 -in mycert.p12 -nocerts -out userkey.pem
chmod 400 userkey.pem
chmod 400 usercert.pem
```
> [!WARNING]
> **If you are new to VOMS, you will need to sign the Acceptable Usage Policy 
> (AUP)** before you are able to access files, tools, and servers secured by
> certificate access. Just follow instructions here to sign the CMS AUP:
> https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideLcgAccess#AUP
