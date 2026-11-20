package com.shinku.reader.data.backup.models
import kotlinx.serialization.Serializable
import kotlinx.serialization.protobuf.ProtoNumber
@Serializable data class Backup(
 @ProtoNumber(1) val backupManga:List<BackupManga> = emptyList(),
 @ProtoNumber(2) val backupCategories:List<BackupCategory> = emptyList(),
 @ProtoNumber(101) val backupSources:List<BackupSource> = emptyList(),
 @ProtoNumber(104) val backupPreferences:List<BackupPreference> = emptyList(),
 @ProtoNumber(105) val backupSourcePreferences:List<BackupSourcePreferences> = emptyList(),
 @ProtoNumber(106) val backupExtensionRepo:List<BackupExtensionRepos> = emptyList(),
 @ProtoNumber(600) val backupSavedSearches:List<BackupSavedSearch> = emptyList())
@Serializable data class BackupManga(val title:String="")
@Serializable data class BackupCategory(val title:String="")
@Serializable data class BackupSource(val title:String="")
@Serializable data class BackupPreference(val title:String="")
@Serializable data class BackupSourcePreferences(val title:String="")
@Serializable data class BackupExtensionRepos(val title:String="")
@Serializable data class BackupSavedSearch(val title:String="")
