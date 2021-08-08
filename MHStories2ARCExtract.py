import zlib
import os
import struct
import sys
from Crypto.Cipher import Blowfish

fileExts = dict()

key = b"QZHaM;-5:)dV#"
cipher = Blowfish.new(key,Blowfish.MODE_ECB)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def endianness_reversal(data):
    return b''.join(map(lambda x: x[::-1],chunks(data, 4)))

def readUShort(file):
    return struct.unpack("H",file.read(2))[0]

def writeUShort(file,val):
    file.write(struct.pack("H",val))

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def jamcrc(string):
    return (zlib.crc32(str(string).encode()) ^ 0xffffffff) & 0x7fffffff

def removeNulls(array):
    arr = bytearray()
    for i in range(len(array)):
        if array[i] != 0x00:
            arr.append(array[i])
    return bytes(arr)

#this is why this needs a non-Python solution

fileExts[jamcrc("rBattleBinary")] = ".btb"
fileExts[jamcrc("rBattleCutCmdData")] = ".bccmd"
fileExts[jamcrc("rBattleSelectSetData")] = ".bsset"
fileExts[jamcrc("rAgingFieldPatrolDataNative")] = ".afpd"
fileExts[jamcrc("rTalkDemoCut")] = ".cut"
fileExts[jamcrc("rTalkDemoSound")] = ".tsnd"
fileExts[jamcrc("rTalkDemoWorkOriginInfo")] = ".work"
fileExts[jamcrc("rTalkDemoObjInitPos")] = ".pos"
fileExts[jamcrc("rFieldEnemyDefaultAifsmDataNaitive")] = ".fedad"
fileExts[jamcrc("rFieldConnectionInfoNative")] = ".fci"
fileExts[jamcrc("rFieldPartsInfoNative")] = ".fpi"
fileExts[jamcrc("rFieldPartsLayoutNative")] = ".fpl"
fileExts[jamcrc("rTraceSonarNative")] = ".ts"
fileExts[jamcrc("rFieldPlacementObjectSetNative")] = ".fpos"
fileExts[jamcrc("rFieldCamOption")] = ".fco"
fileExts[jamcrc("rDungeonInfoListNative")] = ".dai"
fileExts[jamcrc("rFieldNpcNekoTaxiList")] = ".fntl"
fileExts[jamcrc("rFieldObjectList")] = ".fol"
fileExts[jamcrc("rFieldCamera")] = ".fcr"
fileExts[jamcrc("rOccluder2Native")] = ".occ2"
fileExts[jamcrc("rInstanceDrawDistance")] = ".idd"
fileExts[jamcrc("rIDColor")] = ".idcol"
fileExts[jamcrc("rInstancePlacement")] = ".ipr"
fileExts[jamcrc("rPlayerMoveConfigData")] = ".pmc"
fileExts[jamcrc("rSoundGuiSe")] = ".sgs"
fileExts[jamcrc("rSoundParamOffsetControl")] = ".spoc"
fileExts[jamcrc("rSoundPelTiedSe")] = ".pts"
fileExts[jamcrc("rSoundAreaReverb")] = ".sar"
fileExts[jamcrc("rSoundSystemSetting")] = ".sss"
fileExts[jamcrc("rSoundPronounceList")] = ".sptl"
fileExts[jamcrc("rEnaJoinProgressDataNative")] = ".ejpd"
fileExts[jamcrc("rKizunaLvProgressDataNative")] = ".klpd"
fileExts[jamcrc("rReusJoinProgressDataNative")] = ".rjpd"
fileExts[jamcrc("rFieldDirectionInfoNative")] = ".fdi"
fileExts[jamcrc("rAgingBtlBuddyTableNative")] = ".abbt"
fileExts[jamcrc("rAgingBtlEnemySetTableNative")] = ".abest"
fileExts[jamcrc("rAgingBtlStageTableNative")] = ".abst"
fileExts[jamcrc("rAgingCheckBuddyNative")] = ".acb"
fileExts[jamcrc("rAgingCheckEnaLayArmorNative")] = ".acela"
fileExts[jamcrc("rAgingCheckNaviAccesoryNative")] = ".acna"
fileExts[jamcrc("rAgingCheckPlArmorNative")] = ".acpa"
fileExts[jamcrc("rAgingCheckWeaponNative")] = ".acwp"
fileExts[jamcrc("rAgingFieldTableNative")] = ".aft"
fileExts[jamcrc("rCheatCheckTableItemBattleNative")] = ".cctib"
fileExts[jamcrc("rCheatCheckTableWeaponBowNative")] = ".cctbw"
fileExts[jamcrc("rCheatCheckTableWeaponGunNative")] = ".cctgn"
fileExts[jamcrc("rDoubleKizunaCameraOffsetNative")] = ".bdkc"
fileExts[jamcrc("rDoubleKizunaMonsterConditionNative")] = ".bdkmc"
fileExts[jamcrc("rDoubleKizunaMonsterOffsetNative")] = ".bdkm"
fileExts[jamcrc("rDoubleKizunaSchedulerPathNative")] = ".bdkd"
fileExts[jamcrc("rActionCommandDelayTimeDataNative")] = ".acdd"
fileExts[jamcrc("rAnimationSecondParamNative")] = ".asp"
fileExts[jamcrc("rGuiClearedDungeonItemParamNative")] = ".cdi"
fileExts[jamcrc("rGuiColorDataNative")] = ".gcol"
fileExts[jamcrc("rGuiFadeDataNative")] = ".gfad"
fileExts[jamcrc("rGuiHatchBabyParamNative")] = ".ghbp"
fileExts[jamcrc("rGuiModelDrawCameraParamNative")] = ".gmdc"
fileExts[jamcrc("rGuiModelDrawWindowParamNative")] = ".gmdw"
fileExts[jamcrc("rGuiMonsterModelParamNative")] = ".gmmp"
fileExts[jamcrc("rGuiMultiVsPlayerParamNative")] = ".gmvp"
fileExts[jamcrc("rGuiNpcModelParamNative")] = ".gnpc"
fileExts[jamcrc("rGuiParamNative")] = ".gpm"
fileExts[jamcrc("rGuiRiderCardBuddyParamNative")] = ".grcb"
fileExts[jamcrc("rGuiStatusPlayerParamNative")] = ".gspp"
fileExts[jamcrc("rGuiTraditionBuddyParamNative")] = ".gtbp"
fileExts[jamcrc("rGuiWeaponModelParamNative")] = ".gwmp"
fileExts[jamcrc("rAchievementIconNative")] = ".aic"
fileExts[jamcrc("rCommandIconNative")] = ".cic"
fileExts[jamcrc("rIconStatusDataNative")] = ".isd"
fileExts[jamcrc("rItemIconNative")] = ".iic"
fileExts[jamcrc("rMonsterIconNative")] = ".mic"
fileExts[jamcrc("rSkillIconNative")] = ".sic"
fileExts[jamcrc("rDramaMessageDataNative")] = ".drmd"
fileExts[jamcrc("rFieldCommonMessageDataNative")] = ".fcmd"
fileExts[jamcrc("rGameMessageDataNative")] = ".grmd"
fileExts[jamcrc("rNpcMessageDataNative")] = ".ntlkd"
fileExts[jamcrc("rTalkMessageDataNative")] = ".tlkd"
fileExts[jamcrc("rOptionKeyConfigButtonDataNative")] = ".okbd"
fileExts[jamcrc("rOptionKeyConfigDataNative")] = ".okd"
fileExts[jamcrc("rOptionKeyConfigKeyboardDataNative")] = ".okkd"
fileExts[jamcrc("rOptionLanguageDataNative")] = ".lad"
fileExts[jamcrc("rOptionParamDataNative")] = ".opd"
fileExts[jamcrc("rOptionSettingDataNative")] = ".osd"
fileExts[jamcrc("rAmiiboGiftNative")] = ".agt"
fileExts[jamcrc("rBattleBuddyConditionDataNative")] = ".bbcnd"
fileExts[jamcrc("rBattleCmdCameraDataNative")] = ".bccam"
fileExts[jamcrc("rBattleCmdIgnoreEnemyDataNative")] = ".bcige"
fileExts[jamcrc("rBattleEffHitInfoDataNative")] = ".behi"
fileExts[jamcrc("rBattleEnemyMCTblNative")] = ".bemct"
fileExts[jamcrc("rBattleEventResourceDataNative")] = ".bert"
fileExts[jamcrc("rBattleEventResultDataNative")] = ".berd"
fileExts[jamcrc("rBattleEventTblNative")] = ".bet"
fileExts[jamcrc("rBattleMorphChangeDataNative")] = ".bmcd"
fileExts[jamcrc("rBattleMorphConditionDataNative")] = ".bmcnd"
fileExts[jamcrc("rBattleNavirouFsmTableNative")] = ".bnft"
fileExts[jamcrc("rBattleNavirouMessageNative")] = ".bnmt"
fileExts[jamcrc("rBattleNavirouSetTableNative")] = ".bnst"
fileExts[jamcrc("rBattleNavirouUniqueNative")] = ".bnut"
fileExts[jamcrc("rBattlePartsConditionDataNative")] = ".bptcnd"
fileExts[jamcrc("rBCATAppDataNative")] = ".bcatData"
fileExts[jamcrc("rBingoBonusCategoryNative")] = ".bbc"
fileExts[jamcrc("rBreakFieldObjectDataNative")] = ".bfofd"
fileExts[jamcrc("rBuddyBtlMCDataNative")] = ".bdbcm"
fileExts[jamcrc("rCharaCustomLogDataNative")] = ".chcl"
fileExts[jamcrc("rCharaRemakeTicketDataNative")] = ".crd"
fileExts[jamcrc("rDemoGalleryDataNative")] = ".dgd"
fileExts[jamcrc("rDifficultyConvertCountNative")] = ".dcc"
fileExts[jamcrc("rDifficultyConvertGameFlagNative")] = ".dcgf"
fileExts[jamcrc("rDLCAppDataNative")] = ".dlcData"
fileExts[jamcrc("rDLCViewDataNative")] = ".dlcView"
fileExts[jamcrc("rDungeonChestLotTableNative")] = ".dclt"
fileExts[jamcrc("rDungeonContainsDataNative")] = ".dcd"
fileExts[jamcrc("rDungeonCreatePatternNative")] = ".dcp"
fileExts[jamcrc("rDungeonEggMonsterDataNative")] = ".demd"
fileExts[jamcrc("rDungeonEnemyFixedDataNative")] = ".defd"
fileExts[jamcrc("rDungeonEnemyHomingDataNative")] = ".deh"
fileExts[jamcrc("rDungeonEnemyLocatorDataNative")] = ".deloc"
fileExts[jamcrc("rDungeonEnemyLotDataNative")] = ".deld"
fileExts[jamcrc("rDungeonNestRarenessDataNative")] = ".dnrd"
fileExts[jamcrc("rEggUniquePatternDataNative")] = ".eup"
fileExts[jamcrc("rEnvCreatureDataNative")] = ".ecr"
fileExts[jamcrc("rExpeditionFieldDataNative")] = ".exfd"
fileExts[jamcrc("rExpeditionPolicyDataNative")] = ".expl"
fileExts[jamcrc("rExpeditionSlotNumDataNative")] = ".esd"
fileExts[jamcrc("rFieldAmbientDataNative")] = ".fldamb"
fileExts[jamcrc("rFieldPartsDataNative")] = ".fpd"
fileExts[jamcrc("rFieldPartsNameDataNative")] = ".fldpn"
fileExts[jamcrc("rFieldSkyDataNative")] = ".fldsky"
fileExts[jamcrc("rFieldSpotDataNative")] = ".flds"
fileExts[jamcrc("rFixedDungeonConfigDataNative")] = ".fdcd"
fileExts[jamcrc("rFortuneGiftNative")] = ".fgt"
fileExts[jamcrc("rGeneRandomSetNative")] = ".grset"
fileExts[jamcrc("rGiftBuddyTableNative")] = ".tgb"
fileExts[jamcrc("rGiftEggTableNative")] = ".tge"
fileExts[jamcrc("rGuiFontDataNative")] = ".fnd"
fileExts[jamcrc("rGuiFontLanguageDataNative")] = ".gfld"
fileExts[jamcrc("rGuiLocalizeTextureDataNative")] = ".ltd"
fileExts[jamcrc("rGuiMessageDataNative")] = ".msgm"
fileExts[jamcrc("rGuiWorldMapNative")] = ".gwm"
fileExts[jamcrc("rHabitatDataNative")] = ".hbt"
fileExts[jamcrc("rHardDungeonUIDataNative")] = ".hdu"
fileExts[jamcrc("rHatchEggBonusDataNative")] = ".heb"
fileExts[jamcrc("rEditCameraDataNative")] = ".ecd"
fileExts[jamcrc("rEditColorPresetDataNative")] = ".ecp"
fileExts[jamcrc("rEditEyeShapeDataNative")] = ".eed"
fileExts[jamcrc("rEditFaceShapeDataNative")] = ".efd"
fileExts[jamcrc("rEditHairstyleDataNative")] = ".ehd"
fileExts[jamcrc("rEditMakeupTypeDataNative")] = ".emad"
fileExts[jamcrc("rEditMouthShapeDataNative")] = ".emod"
fileExts[jamcrc("rEditParamDataNative")] = ".epd"
fileExts[jamcrc("rEditVoiceTypeDataNative")] = ".evd"
fileExts[jamcrc("rLinkedDungeonDataNative")] = ".ldd"
fileExts[jamcrc("rMelynxShopAccessoryDataNative")] = ".macd"
fileExts[jamcrc("rMelynxShopArmorDataNative")] = ".mard"
fileExts[jamcrc("rMelynxShopDataNative")] = ".msp"
fileExts[jamcrc("rMelynxShopWeaponDataNative")] = ".mwd"
fileExts[jamcrc("rMenuRiderNoteDataNative")] = ".mrnd"
fileExts[jamcrc("rModTextureNoScaleDataNative")] = ".mtnscl"
fileExts[jamcrc("rMonsterAdditionalShowTableNative")] = ".mas"
fileExts[jamcrc("rMonsterBaseInfoDataNative")] = ".mbi"
fileExts[jamcrc("rMHSoundEmitter")] = ".ses"
fileExts[jamcrc("rMHSoundSequence")] = ".mss"
fileExts[jamcrc("rSoundAttributeSe")] = ".aser"
fileExts[jamcrc("rSoundEngine")] = ".engr"
fileExts[jamcrc("rSoundEngineXml")] = ".engr.xml"
fileExts[jamcrc("rSoundEngineValue")] = ".egvr"
fileExts[jamcrc("rSoundMotionSe")] = ".mser"
fileExts[jamcrc("rSoundSequenceSe")] = ".ssqr"
fileExts[jamcrc("rSoundSimpleCurve")] = ".sscr"
fileExts[jamcrc("rSoundSubMixerXml")] = ".smxr.xml"
fileExts[jamcrc("rSoundSubMixer")] = ".smxr"
fileExts[jamcrc("uSoundSubMixer::CurrentSubMixer")] = ".smxr"
fileExts[jamcrc("rMonsterPartsTableNative")] = ".mpt"
fileExts[jamcrc("rNavirouGuideDataNative")] = ".ngt"
fileExts[jamcrc("rNpc2dFaceTexTableNative")] = ".nft"
fileExts[jamcrc("rNpcAirouSetMotionDataNative")] = ".nasmd"
fileExts[jamcrc("rNpcLayeredArmorDataNative")] = ".nlad"
fileExts[jamcrc("rNpcSetMotionDataNative")] = ".nsmd"
fileExts[jamcrc("rNpcTalkResourceDataNative")] = ".ntrp"
fileExts[jamcrc("rNpcTalkZoneNative")] = ".ntz"
fileExts[jamcrc("rPotEffectDataNative")] = ".pte"
fileExts[jamcrc("rPotLevelDataNative")] = ".ptl"
fileExts[jamcrc("rPotOfferingDataNative")] = ".pto"
fileExts[jamcrc("rPotPrayingDataNative")] = ".ptp"
fileExts[jamcrc("rPresetParamCharaCustomNative")] = ".tppcc"
fileExts[jamcrc("rPresetParamLearningSkillSetNative")] = ".tppls"
fileExts[jamcrc("rPresetParamOtomonNative")] = ".tppo"
fileExts[jamcrc("rPresetParamOtomonGeneNative")] = ".tppog"
fileExts[jamcrc("rRiderNoteDataRushNative")] = ".rndr"
fileExts[jamcrc("rRideSkillTableNative")] = ".rst"
fileExts[jamcrc("rSkillCalcNative")] = ".skc"
fileExts[jamcrc("rSkillSetDataNative")] = ".wss"
fileExts[jamcrc("rStableCapacityDataNative")] = ".scd"
fileExts[jamcrc("rStatusChangeFlagsNative")] = ".scf"
fileExts[jamcrc("rStatusDataNative")] = ".sdt"
fileExts[jamcrc("rStoryQuestDataNative")] = ".sqd"
fileExts[jamcrc("rStoryQuestDefineNative")] = ".sqdf"
fileExts[jamcrc("rSubQuestConditionDataNative")] = ".sqccd"
fileExts[jamcrc("rSubQuestDataRenewNative")] = ".suqd"
fileExts[jamcrc("rSubQuestVeilDataNative")] = ".svd"
fileExts[jamcrc("rSubstituteNpcTblNative")] = ".sntt"
fileExts[jamcrc("rSummaryDataNative")] = ".smr"
fileExts[jamcrc("rTalkDemoDefineDataNative")] = ".tdmspk"
fileExts[jamcrc("rTrialCleanNativeDataNative")] = ".tcn"
fileExts[jamcrc("rTutorialArrowDataNative")] = ".tad"
fileExts[jamcrc("rTutorialLockDataNative")] = ".tld"
fileExts[jamcrc("rVsItemSetDataNative")] = ".vsitemset"
fileExts[jamcrc("rVsPrizeDataNative")] = ".vsprize"
fileExts[jamcrc("rVsRuleDataNative")] = ".vsrule"
fileExts[jamcrc("rSoundDemoControlNative")] = ".sdc"
fileExts[jamcrc("rSoundDemoEnvControlNative")] = ".sdec"
fileExts[jamcrc("rSoundDemoSeControlNative")] = ".sdsc"
fileExts[jamcrc("rSoundGuiOperationNative")] = ".sgo"
fileExts[jamcrc("rSoundInfoSeNative")] = ".siet"
fileExts[jamcrc("rSoundInfoStreamNative")] = ".siets"
fileExts[jamcrc("rSoundArchiveDataNative")] = ".samd"
fileExts[jamcrc("rSoundArmorDataNative")] = ".sad"
fileExts[jamcrc("rSoundBattleStageDataNative")] = ".sbsd"
fileExts[jamcrc("rSoundBattleStageDefineNative")] = ".sbsdef"
fileExts[jamcrc("rSoundBgmMonsterDataNative")] = ".sbmd"
fileExts[jamcrc("rSoundFootstepDataNative")] = ".sftd"
fileExts[jamcrc("rSoundFSMCommandBgmDataNative")] = ".sfcbd"
fileExts[jamcrc("rSoundFSMCommandSeDataNative")] = ".sfcsd"
fileExts[jamcrc("rSoundMonsterDataNative")] = ".smd"
fileExts[jamcrc("rSoundMonsterEnvironmentalDataNative")] = ".smed"
fileExts[jamcrc("rSoundMonsterKizunaDataNative")] = ".smkd"
fileExts[jamcrc("rSoundNpcAirouDataNative")] = ".snad"
fileExts[jamcrc("rSoundNpcDataNative")] = ".snd"
fileExts[jamcrc("rSoundObjectDataNative")] = ".sod"
fileExts[jamcrc("rSoundSceneVolumeNative")] = ".ssv"
fileExts[jamcrc("rSoundWeaponDataNative")] = ".swd"
fileExts[jamcrc("rSoundNpcVoicePathDataNative")] = ".snvpd"
fileExts[jamcrc("rSoundPlayerVoicePathDataNative")] = ".spvpd"
fileExts[jamcrc("rUnlockMixDataNative")] = ".ulm"
fileExts[jamcrc("rUnlockProgressDataNative")] = ".ulp"
fileExts[jamcrc("rUnlockScriptDataNative")] = ".uls"
fileExts[jamcrc("rFacialPartsComboNative")] = ".fpc"
fileExts[jamcrc("rFacialPartsControl")] = ".fpctl"
fileExts[jamcrc("rObjectModelAttachGroupNative")] = ".omg"
fileExts[jamcrc("rObjectModelAttachInfoNative")] = ".omi"
fileExts[jamcrc("rObjectModelAttachSetData")] = ".omas"
fileExts[jamcrc("rMonsterLookAtParamNative")] = ".mlka"
fileExts[jamcrc("rKizunaStoneOfsNative")] = ".kofb"
fileExts[jamcrc("rWeaponKindOfsNative")] = ".wko"
fileExts[jamcrc("uSceneCapture::rCaptureTexture")] = ".tex"
fileExts[jamcrc("cInstancingResource")] = ".ext"
fileExts[jamcrc("rCheatCheckTableAccSkillNative")] = ".cctas"
fileExts[jamcrc("rCheatCheckTableArmorNative")] = ".ccta"
fileExts[jamcrc("rCheatCheckTableBuddyNative")] = ".cctb"
fileExts[jamcrc("rCheatCheckTableBuddyFlagNative")] = ".cctbf"
fileExts[jamcrc("rCheatCheckTableGeneNative")] = ".cctg"
fileExts[jamcrc("rCheatCheckTableNaviAccNative")] = ".cctna"
fileExts[jamcrc("rCheatCheckTableRangeNative")] = ".cctr"
fileExts[jamcrc("rCheatCheckTableWeaponHamNative")] = ".ccthm"
fileExts[jamcrc("rCheatCheckTableWeaponHueNative")] = ".ccthu"
fileExts[jamcrc("rCheatCheckTableWeaponOneNative")] = ".cctwo"
fileExts[jamcrc("rCheatCheckTableWeaponTwoNative")] = ".cctwt"
fileExts[jamcrc("rBattleArenaDLCTableNative")] = ".badt"
fileExts[jamcrc("rBattleArenaTrialTableNative")] = ".batt"
fileExts[jamcrc("rBattleNaviTextEventNative")] = ".bte"
fileExts[jamcrc("rBattleStatusEffectNative")] = ".bseff"
fileExts[jamcrc("rBattleVsPorchPresetNative")] = ".bvspp"
fileExts[jamcrc("rDLCItemTableNative")] = ".ditemp"
fileExts[jamcrc("rDLCRegionTnmntTableNative")] = ".dtnmt"
fileExts[jamcrc("rDLCSubQuestDataNative")] = ".dsuqd"
fileExts[jamcrc("rDLCVsRuleTableNative")] = ".dvsrule"
fileExts[jamcrc("rEnemyCameraParamNative")] = ".ecpd"
fileExts[jamcrc("rLimitedShopDataNative")] = ".lshpd"
fileExts[jamcrc("rLimitedShopPlaceDataNative")] = ".lshppd"
fileExts[jamcrc("rLinkPrizeDataNative")] = ".lpd"
fileExts[jamcrc("rMedalCompRewardNative")] = ".mcr"
fileExts[jamcrc("rMonsterEnumConversionTableNative")] = ".mectd"
fileExts[jamcrc("rNavirouAccessoryDataNative")] = ".nad"
fileExts[jamcrc("rNestEggReviewANative")] = ".nstera"
fileExts[jamcrc("rNestEggReviewBNative")] = ".nsterb"
fileExts[jamcrc("rNestMessageNative")] = ".nstmsg"
fileExts[jamcrc("rOtomonCameraParamNative")] = ".ocpd"
fileExts[jamcrc("rPostmanRewardDataNative")] = ".pmrd"
fileExts[jamcrc("rStaffRollCutDataNative")] = ".srcd"
fileExts[jamcrc("rWorldMapMaskDataNative")] = ".wmmd"
fileExts[jamcrc("rTalkDemoViewSpriteDataNative")] = ".tdvs"
fileExts[jamcrc("rArmorParamNative")] = ".arp"
fileExts[jamcrc("rDLCTableNative")] = ".dlc"
fileExts[jamcrc("rMedalDataListNative")] = ".mdl"
fileExts[jamcrc("rMyhouseBoxCameraDataNative")] = ".mbcd"
fileExts[jamcrc("rStoryTalkBalloonNative")] = ".stb"
fileExts[jamcrc("rWeaponParamNative")] = ".wpp"
fileExts[jamcrc("rBattleEnemyFileNative")] = ".bef"
fileExts[jamcrc("rConditionPriorityDataNative")] = ".cndp"
fileExts[jamcrc("rGatherLevelTableNative")] = ".ghlt"
fileExts[jamcrc("rLimitedShopNpcList")] = ".lsnl"
fileExts[jamcrc("rMonsterBookDataNative")] = ".mbd"
fileExts[jamcrc("rPresetParamNative")] = ".tpp"
fileExts[jamcrc("rPresetParamEquipNative")] = ".tppe"
fileExts[jamcrc("rPresetParamItemNative")] = ".tppi"
fileExts[jamcrc("rPresetParamPlayerNative")] = ".tppp"
fileExts[jamcrc("rSkillFlagNative")] = ".skf"
fileExts[jamcrc("rAppMovie")] = ".dat"
fileExts[jamcrc("rAppMovieIntermediate")] = ".wmv"
fileExts[jamcrc("rCardPose")] = ".cps"
fileExts[jamcrc("rRideParamNative")] = ".rdp"
fileExts[jamcrc("rSequenceCameraList")] = ".scl"
fileExts[jamcrc("rResourceNameForDevNative")] = ".rnmd"
fileExts[jamcrc("rChestItemTableDataNative")] = ".cfid"
fileExts[jamcrc("rGatherSetTableDataNative")] = ".gstd"
fileExts[jamcrc("rFldPlParam_ARNative")] = ".fppar"
fileExts[jamcrc("rFldPlParam_GRNative")] = ".fppgr"
fileExts[jamcrc("rFldPlParam_NRNative")] = ".fppnr"
fileExts[jamcrc("rFldPlParam_WRNative")] = ".fppwr"
fileExts[jamcrc("rAccessoryDataNative")] = ".acd"
fileExts[jamcrc("rAccessoryRareNative")] = ".acr"
fileExts[jamcrc("rAccessorySkillNative")] = ".acs"
fileExts[jamcrc("rArmorDataNative")] = ".ard"
fileExts[jamcrc("rBattleArenaTableNative")] = ".bat"
fileExts[jamcrc("rBattleCommonResourceNative")] = ".bcmr"
fileExts[jamcrc("rBattleEnemySetNative")] = ".bes"
fileExts[jamcrc("rBattleEnemyTblNative")] = ".bemt"
fileExts[jamcrc("rBattleEnemyTblPlanNative")] = ".bemtp"
fileExts[jamcrc("rBattleNpcTblNative")] = ".bnt"
fileExts[jamcrc("rBattlePlayerTblNative")] = ".bplt"
fileExts[jamcrc("rBattleResultBonusNative")] = ".brsb"
fileExts[jamcrc("rBattleStageResourceNative")] = ".bstr"
fileExts[jamcrc("rBattleWeaponTblNative")] = ".bwpt"
fileExts[jamcrc("rBroilerFlavorDataNative")] = ".bfd"
fileExts[jamcrc("rBuddyPathDataNative")] = ".bdypa"
fileExts[jamcrc("rBuddyPlanDataNative")] = ".bdypl"
fileExts[jamcrc("rCallingEncountDataNative")] = ".sce"
fileExts[jamcrc("rConditionNameDataNative")] = ".cnd"
fileExts[jamcrc("rDemoDataNative")] = ".dmd"
fileExts[jamcrc("rDemoFlagDataNative")] = ".dfd"
fileExts[jamcrc("rEggBaseColorDataNative")] = ".ebc"
fileExts[jamcrc("rEncntEnemyPartyNative")] = ".eepd"
fileExts[jamcrc("rEquiprShopDataNative")] = ".eshd"
fileExts[jamcrc("rFieldAISetActNative")] = ".fasa"
fileExts[jamcrc("rFieldAISetKindNative")] = ".fask"
fileExts[jamcrc("rFieldEnemyPathDataNative")] = ".fedpa"
fileExts[jamcrc("rFieldEnemyPlanDataNative")] = ".fedpl"
fileExts[jamcrc("rFieldHuntingDataNative")] = ".fhd"
fileExts[jamcrc("rFieldMotionPackageDataNative")] = ".fmpd"
fileExts[jamcrc("rFieldNpcMotionNative")] = ".fnmd"
fileExts[jamcrc("rFieldPlayerMotionDataNative")] = ".fpm"
fileExts[jamcrc("rFieldSetFlagDataNative")] = ".fsfd"
fileExts[jamcrc("rFurattoFieldDataNative")] = ".fofd"
fileExts[jamcrc("rFurattoTrendDataNative")] = ".fotd"
fileExts[jamcrc("rGalleryFlagDataNative")] = ".gfd"
fileExts[jamcrc("rGatherCommentDataNative")] = ".gcd"
fileExts[jamcrc("rGeneEditNative")] = ".ged"
fileExts[jamcrc("rGeneLottingNative")] = ".glt"
fileExts[jamcrc("rGeneralCountDataNative")] = ".gcd"
fileExts[jamcrc("rGeneralFlagDataNative")] = ".gfd"
fileExts[jamcrc("rGeneTableNative")] = ".gtb"
fileExts[jamcrc("rItemDataNative")] = ".itm"
fileExts[jamcrc("rItemMixNative")] = ".mix"
fileExts[jamcrc("rMainQuestDataNative")] = ".mqsd"
fileExts[jamcrc("rMapMarkerNative")] = ".mmk"
fileExts[jamcrc("rMarkerDataNative")] = ".mkr"
fileExts[jamcrc("rMaterialDataNative")] = ".matd"
fileExts[jamcrc("rMergeStreamDataNative")] = ".asd"
fileExts[jamcrc("rMixFlagNative")] = ".mxf"
fileExts[jamcrc("rMonsterRankTableNative")] = ".mrt"
fileExts[jamcrc("rNekoTaxiStationDataNative")] = ".nsd"
fileExts[jamcrc("rNestHappeningNative")] = ".nhap"
fileExts[jamcrc("rNestHappeningProbNative")] = ".nhapp"
fileExts[jamcrc("rNpcAirouSetResourceLogDataNative")] = ".nasl"
fileExts[jamcrc("rNpcSetResourceLogDataNative")] = ".npsl"
fileExts[jamcrc("rReactionCommentDataNative")] = ".rcd"
fileExts[jamcrc("rRiderNoteDataNative")] = ".rnd"
fileExts[jamcrc("rRiderNoteLargeCategoryDataNative")] = ".rnld"
fileExts[jamcrc("rRiderNotePageDataNative")] = ".rnpd"
fileExts[jamcrc("rRiderNoteSmallCategoryDataNative")] = ".rnsd"
fileExts[jamcrc("rRiderNoteThumbnailDataNative")] = ".rntd"
fileExts[jamcrc("rShortDemoDataNative")] = ".sdm"
fileExts[jamcrc("rSkillTableNative")] = ".skt"
fileExts[jamcrc("rStChapDataNative")] = ".schd"
fileExts[jamcrc("rStEpiDataNative")] = ".sed"
fileExts[jamcrc("rStoryCountDataNative")] = ".scod"
fileExts[jamcrc("rStoryDataNative")] = ".std"
fileExts[jamcrc("rStoryFlagDataNative")] = ".stfd"
fileExts[jamcrc("rStPrComDataNative")] = ".spcd"
fileExts[jamcrc("rSubQuestCountDataNative")] = ".sqcd"
fileExts[jamcrc("rSubQuestFlagDataNative")] = ".sqfd"
fileExts[jamcrc("rSubStEpiDataNative")] = ".ssed"
fileExts[jamcrc("rSystemCountDataNative")] = ".sycd"
fileExts[jamcrc("rTalkDemoActorDataNative")] = ".tdmact"
fileExts[jamcrc("rTalkDemoCommandDataNative")] = ".tdmcmd"
fileExts[jamcrc("rTalkDemoDataNative")] = ".tdmd"
fileExts[jamcrc("rTalkDemoEffectDataNative")] = ".tdmeff"
fileExts[jamcrc("rTalkDemoFaceDataNative")] = ".tdmfc"
fileExts[jamcrc("rTalkDemoMotionDataNative")] = ".tdmmot"
fileExts[jamcrc("rTalkDemoPoseDataNative")] = ".tdmpos"
fileExts[jamcrc("rTalkDemoScript")] = ".tdms"
fileExts[jamcrc("rTalkInfoDataNative")] = ".tid"
fileExts[jamcrc("rTalkMsgDataNative")] = ".tmd"
fileExts[jamcrc("rTalkSelectDataNative")] = ".tstd"
fileExts[jamcrc("rWeaponDataNative")] = ".wpd"
fileExts[jamcrc("rFieldGateDataNative")] = ".fgd"
fileExts[jamcrc("rMHFSMList")] = ".fslm"
fileExts[jamcrc("rWipeData")] = ".wpdt"
fileExts[jamcrc("rBattleAtkNative")] = ".btat"
fileExts[jamcrc("rFieldBuddyMotionDataNative")] = ".fbd"
fileExts[jamcrc("rFieldDataNative")] = ".fld"
fileExts[jamcrc("rFieldEnemySetDataNative")] = ".fesd"
fileExts[jamcrc("rFieldIngredientSetDataNative")] = ".fisd"
fileExts[jamcrc("rFieldMotionDataNative")] = ".fmd"
fileExts[jamcrc("rFieldOrnamentSetDataNative")] = ".fosd"
fileExts[jamcrc("rFieldPredatorDataNative")] = ".fprd"
fileExts[jamcrc("rFieldSchedulerSetDataNative")] = ".fssd"
fileExts[jamcrc("rMonsterRaceDataNative")] = ".mrd"
fileExts[jamcrc("rNpcTalkNative")] = ".ntk"
fileExts[jamcrc("rShopDataNative")] = ".shp"
fileExts[jamcrc("rSystemFlagDataNative")] = ".sfd"
fileExts[jamcrc("rTalkDataNative")] = ".tlk"
fileExts[jamcrc("rProofEffectColorControl")] = ".pec"
fileExts[jamcrc("rProofEffectList")] = ".pel"
fileExts[jamcrc("rProofEffectMotSequenceList")] = ".psl"
fileExts[jamcrc("rProofEffectParamScript")] = ".pep"
fileExts[jamcrc("rCameraData")] = ".cmdt"
fileExts[jamcrc("rColorLinkColor")] = ".clc"
fileExts[jamcrc("rColorLinkInfo")] = ".cli"
fileExts[jamcrc("rConditionChangeInfo")] = ".ccinfo"
fileExts[jamcrc("rDollPartsDisp")] = ".dpd"
fileExts[jamcrc("rGroundAdjustment")] = ".gar"
fileExts[jamcrc("rModelEasyAnime")] = ".mea"
fileExts[jamcrc("rModelInPath")] = ".mip"
fileExts[jamcrc("rMonsterPartsDisp")] = ".mpd"
fileExts[jamcrc("rNavirouPartsDisp")] = ".npd"
fileExts[jamcrc("rPartsVisibleInfo")] = ".pvi"
fileExts[jamcrc("rSchedulerPreLoadList")] = ".spll"
fileExts[jamcrc("rShadowParamNative")] = ".swp"
fileExts[jamcrc("rVirtualJoint")] = ".vjr"
fileExts[jamcrc("rWeaponGimmickInfo")] = ".wgi"
fileExts[jamcrc("rWeaponOfsForBodyNative")] = ".wofb"
fileExts[jamcrc("cResource")] = ".ext"
fileExts[jamcrc("rModel")] = ".mod"
fileExts[jamcrc("rMotionList")] = ".lmt"
fileExts[jamcrc("rTexture")] = ".tex"
fileExts[jamcrc("rCollision")] = ".sbc"
fileExts[jamcrc("rAIWayPointGraph")] = ".gway"
fileExts[jamcrc("rScheduler")] = ".sdl"
fileExts[jamcrc("rArchive")] = ".arc"
fileExts[jamcrc("rCnsTinyChain")] = ".ctc"
fileExts[jamcrc("rChain")] = ".chn"
fileExts[jamcrc("rChainCol")] = ".ccl"
fileExts[jamcrc("rAIFSM")] = ".fsm"
fileExts[jamcrc("rAIFSMList")] = ".fsl"
fileExts[jamcrc("rAIConditionTree")] = ".cdt"
fileExts[jamcrc("rCameraList")] = ".lcm"
fileExts[jamcrc("rGUI")] = ".gui"
fileExts[jamcrc("rRenderTargetTexture")] = ".rtex"
fileExts[jamcrc("rEffect2D")] = ".e2d"
fileExts[jamcrc("rGUIFont")] = ".gfd"
fileExts[jamcrc("rGUIIconInfo")] = ".gii"
fileExts[jamcrc("rGUIStyle")] = ".gst"
fileExts[jamcrc("rGUIMessage")] = ".gmd"
fileExts[jamcrc("rDeformWeightMap")] = ".dwm"
fileExts[jamcrc("rSwingModel")] = ".swm"
fileExts[jamcrc("rVibration")] = ".vib"
fileExts[jamcrc("rSoundRequest")] = ".srqr"
fileExts[jamcrc("rSoundStreamRequest")] = ".stqr"
fileExts[jamcrc("rSoundCurveSet")] = ".scsr"
fileExts[jamcrc("rSoundDirectionalSet")] = ".sdsr"
fileExts[jamcrc("rSoundEQ")] = ".equr"
fileExts[jamcrc("rSoundReverb")] = ".revr"
fileExts[jamcrc("rSoundCurveXml")] = ".scvr.xml"
fileExts[jamcrc("rSoundDirectionalCurveXml")] = ".sdcr.xml"
fileExts[jamcrc("rSoundBank")] = ".sbkr"
fileExts[jamcrc("rSoundPhysicsRigidBody")] = ".sprr"
fileExts[jamcrc("rSoundPhysicsSoftBody")] = ".spsr"
fileExts[jamcrc("rSoundPhysicsJoint")] = ".spjr"
fileExts[jamcrc("rShader2")] = ".mfx"
fileExts[jamcrc("rImplicitSurface")] = ".is"
fileExts[jamcrc("rMovie")] = ".ext"
fileExts[jamcrc("rMovieOnMemory")] = ".mem.wmv"
fileExts[jamcrc("rMovieOnDisk")] = ".wmvd"
fileExts[jamcrc("rMovieOnMemoryInterMediate")] = ".mem.wmv"
fileExts[jamcrc("rMovieOnDiskInterMediate")] = ".wmvd"
fileExts[jamcrc("rSceneTexture")] = ".stex"
fileExts[jamcrc("rGrass2")] = ".gr2"
fileExts[jamcrc("rGrass2Setting")] = ".gr2s"
fileExts[jamcrc("rOccluder")] = ".occ"
fileExts[jamcrc("rISC")] = ".isc"
fileExts[jamcrc("rSky")] = ".sky"
fileExts[jamcrc("rStarCatalog")] = ".stc"
fileExts[jamcrc("rCloud")] = ".cld"
fileExts[jamcrc("rSoundSourcePC")] = ".ext"
fileExts[jamcrc("rSoundSourceMSADPCM")] = ".xsew"
fileExts[jamcrc("rSoundSourceOggVorbis")] = ".sngw"
fileExts[jamcrc("rEffectList")] = ".efl"
fileExts[jamcrc("rCollisionHeightField")] = ".sbch"
fileExts[jamcrc("rCnsIK")] = ".ik"
fileExts[jamcrc("rShaderPackage")] = ".spkg"
fileExts[jamcrc("rShaderCache")] = ".sch"
fileExts[jamcrc("rMaterial")] = ".mrl"
fileExts[jamcrc("rSoundSpeakerSetXml")] = ".sssr.xml"
fileExts[jamcrc("rCollisionObj")] = ".obc"
fileExts[jamcrc("rGrass")] = ".grs"
fileExts[jamcrc("rConstraint")] = ".ext"
fileExts[jamcrc("rCnsLookAt")] = ".lat"
fileExts[jamcrc("rEffectAnim")] = ".ean"
fileExts[jamcrc("rEffectStrip")] = ".efs"
fileExts[jamcrc("rVertices")] = ".vts"
fileExts[jamcrc("rNulls")] = ".nls"
fileExts[jamcrc("rAI")] = ".ais"
fileExts[jamcrc("rSoundPhysicsList")] = ".splr"
fileExts[jamcrc("rFacialAnimation")] = ".fca"
fileExts[jamcrc("rMetaSet")] = ".mst"
fileExts[jamcrc("rMetaSetXml")] = ".mst.xml"
fileExts[jamcrc("rCnsTinyIK")] = ".tik"
fileExts[jamcrc("rCnsScaleNormalize")] = ".scnl"
fileExts[jamcrc("rCnsRotateLimit")] = ".lim"
fileExts[jamcrc("rCnsMatrix")] = ".mtx"
fileExts[jamcrc("rCnsJointOffset")] = ".jof"
fileExts[jamcrc("rCnsParent")] = ".par"
fileExts[jamcrc("rCnsParentN")] = ".pan"
fileExts[jamcrc("rCnsLookAtEyeball")] = ".eye"
fileExts[jamcrc("rGraphPatch")] = ".gpt"
fileExts[jamcrc("rGrassWind")] = ".grw"
fileExts[jamcrc("rConvexHull")] = ".hul"
fileExts[jamcrc("rGeometry2")] = ".geo2"
fileExts[jamcrc("rGeometry3")] = ".geo3"
fileExts[jamcrc("rSerial")] = ".srt"
fileExts[jamcrc("rDynamicSbc")] = ".dsc"
fileExts[jamcrc("rGeometry2Group")] = ".geog"


def getExtension(hash):
    if hash in fileExts:
        return fileExts[hash]
    else:
        return "." + str(hex(hash)[2:])

class Entry:
    def __init__(self,name,extHash,compSize,decompSize,offset):
        self.name = name
        self.extHash = extHash
        self.compSize = compSize
        self.decompSize = decompSize
        self.offset = offset

def extractARC(inFile,fileCount):
    basePath = inFile.name.split('.')[0]+'/'
    os.makedirs(basePath,exist_ok=True)
    logFile = open(basePath+"orderlog.txt",'w')
    entries = []
    for _ in range(fileCount):
        nameArray = inFile.read(128)
        nameArray = removeNulls(nameArray)
        eName = nameArray.decode("utf-8")
        eExt = readUInt(inFile)
        eComp = readUInt(inFile)
        eUncomp = readUInt(inFile)
        eOffset = readUInt(inFile)
        entries.append(Entry(eName,eExt,eComp,eUncomp,eOffset))
    for entry in entries:
        #deal with compression first
        inFile.seek(entry.offset)
        cFile = inFile.read(entry.compSize)
        dFile = zlib.decompress(cFile)
        #create name
        dirPath = os.path.split(entry.name)[0]
        #print(dirPath, 1)
        if(dirPath != ''):
            os.makedirs(basePath+dirPath,exist_ok=True)
        logFile.write(entry.name+getExtension(entry.extHash)+"\n")
        finalName = basePath + entry.name + getExtension(entry.extHash)
        oFile = open(finalName,'wb')
        oFile.write(dFile)
        oFile.close()

def readARCC(inFile,fileCount):
    encFile = inFile.read()
    decFile = endianness_reversal(cipher.decrypt(endianness_reversal(encFile)))
    outFile = open(inFile.name+"-decrypt.arc",'wb')
    outFile.write(b"ARC\x00")
    writeUShort(outFile,7)
    writeUShort(outFile,fileCount)
    outFile.write(decFile)
    decName = outFile.name
    outFile.close()
    nFile = open(decName,'rb')
    nFile.seek(8)
    extractARC(nFile,fileCount)

def readARC(inFile):
    magic = inFile.read(4)
    assert readUShort(inFile) == 7
    fileCount = readUShort(inFile)
    if magic == b"ARCC":
        readARCC(inFile,fileCount)
    elif magic == b"ARC\x00":
        extractARC(inFile,fileCount)

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            readARC(open(arg,'rb'))