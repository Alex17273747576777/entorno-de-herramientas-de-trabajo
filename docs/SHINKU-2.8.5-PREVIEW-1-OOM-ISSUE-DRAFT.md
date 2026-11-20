# Bug report — OOM validating a large backup before restoration

**Publicado y verificado:** https://github.com/Harrys-HQ/ShinKu/issues/40

## Suggested title
OutOfMemoryError in ProtobufDecoder while validating a large backup (512 MiB heap limit)

## Environment
- Affected app: ShinKu.
- Exact affected version/build: not yet confirmed. Investigation target: v2.8.5-preview.1, a478592cb040e644f0e222d1fec9b20feba9ff18; do not assume this is the crashing binary.
- Android, device model, physical RAM: not provided. Reporter emphasizes low-end hardware.
- Process heap growth limit in supplied trace: 536870912 bytes (512 MiB); this is NOT device physical RAM.
- Previously reported backup: Mihon format, >110 MB, several years of library/history. Exact compressed/uncompressed sizes and counts unconfirmed.

## Reproduction (reporter supplied; not independently reproduced)
1. Open backup restore in ShinKu.
2. Select the large backup for import.
3. The supplied trace shows failure in RestoreBackupScreenModel validation, before BackupRestorer is entered on this call path.

A previous account mentioned approximately 10% progress; this trace does not establish that restoration had reached 10% or that it represents the same execution. Please distinguish validation from database restoration in progress reporting.

## Expected
Validation/import should remain usable on constrained devices. Either complete safely or return an actionable error without terminating the app. Show the actual phase and accurate partial-result semantics. Optimize memory and measure latency rather than promising a speedup without benchmarks.

## Actual and supplied crash evidence
The reporter supplied a longer trace; this is a shortened excerpt preserving the relevant call chain (R8 map IDs and repetitive serialization frames omitted):

```text
java.lang.Throwable: java.lang.OutOfMemoryError: Failed to allocate a 64 byte allocation with 263136 free bytes and 256KB until OOM, target footprint 536870912, growth limit 536870912; giving up on allocation because <1% of heap free after GC.
    at kotlinx.serialization.protobuf.internal.ProtobufDecoder.populateCache
    at kotlinx.serialization.protobuf.internal.ProtobufDecoder.<init>
    at kotlinx.serialization.protobuf.internal.ProtobufDecoder.beginStructure
    at com.shinku.reader.data.backup.models.BackupChapter$$serializer.deserialize
    ... collection decoding ...
    at com.shinku.reader.data.backup.models.BackupManga$$serializer.deserialize
    ... collection decoding ...
    at com.shinku.reader.data.backup.models.Backup$$serializer.deserialize
    at kotlinx.serialization.protobuf.ProtoBuf.decodeFromByteArray
    at com.shinku.reader.data.backup.BackupDecoder.decode
    at com.shinku.reader.data.backup.BackupFileValidator.validate
    at com.shinku.reader.presentation.more.settings.screen.data.RestoreBackupScreenModel$validate$results$1.invokeSuspend
```

The reported log subsequently contains GlobalExceptionHandler$ThrowableSerializer.deserialize, Json.decodeFromString and CrashActivity.onCreate. These later crash-report reconstruction frames should not be mistaken for the original allocation-failure site.

## What this evidence establishes / does not establish
- The managed heap is exhausted during protobuf deserialization of chapters within library entries, called by pre-restore validation.
- A 64-byte allocation is the final failed allocation, not the total backup size or a claim that 64 bytes caused the problem.
- GC left less than 1% free. The trace does not prove a memory leak, corrupt backup, physical RAM size, or an intrinsically faulty populateCache implementation.
- A heap profile is needed to attribute retained bytes among serialized payload, decoded objects, chapter collections, caches and other app state.

## Source observations at the investigation ref
BackupDecoder reads the entire decompressed input into a byte array, then calls ProtoBuf.decodeFromByteArray. BackupFileValidator fully decodes it for inspection; BackupRestorer decodes again when restoration starts. This creates avoidable full-payload allocation and repeated work, but the two calls do not prove that both object graphs coexist.

Source: https://github.com/Harrys-HQ/ShinKu/tree/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/data/backup

## Requested engineering work / acceptance checks
1. Profile validation and restoration separately on a 512 MiB heap and representative low-end devices, using synthetic backups with many entries and chapter-heavy single entries.
2. Avoid full decompressed readByteArray allocation; use bounded parsing. Streaming input alone is insufficient if the complete decoded Backup is still retained.
3. Make validation incremental (summary/source/tracker collection without retaining all chapters). Assess a bounded staging or batch-import path for restoration; preserve mappings, cancellation and duplicate/merge semantics.
4. Bound record sizes and decompression/resource usage. Reject oversized/malformed records before payload allocation when feasible. Do not rely on catching OOM or forcing GC as the solution.
5. Avoid redundant decoding where safe; do not trade away output integrity checks without replacing them appropriately.
6. Report validation/import phases and accurate errors. Do not promise rollback or zero modifications unless guaranteed for the failing phase.
7. Test gzip/raw, unknown fields, malformed/truncated data, oversized individual records and huge chapter lists. Record peak heap, elapsed time and imported counts against baseline.

## Local experimental mitigation — not a released fix
A working-tree prototype decodes top-level records incrementally and caps an individual record, but still constructs the full Backup. An isolated JVM harness using real backup models and external stubs passed parser tests and a synthetic >150 MiB case; this is not Android integration/device validation or a comparable speed measurement. The Android build did not reach app compilation (Gradle daemon disappeared). The crash reported here and build-environment failures are separate observations.

## Duplicate check
Reviewed the repository's first 100 all-state issue/PR results. No dedicated matching report was identified there. #21 concerns NoSuchMethodError during browsing/migration after import, not this protobuf OOM. Broad roadmap issues #12/#13 are not substitutes for a focused reproducible bug report. This is not an exhaustive review of every discussion/comment.

No private backup, library contents, credentials or account data is attached.
