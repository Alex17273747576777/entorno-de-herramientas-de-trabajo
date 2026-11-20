# Feature request — evaluate Kotatsu/Usagi/Kototoro backup migration and parser support

**Publicado y verificado:** https://github.com/Harrys-HQ/ShinKu/issues/41

## Suggested title
Evaluate Kotatsu, Usagi and Kototoro backup import, with a separate feasibility study for parser JARs

## Request
Offer an explicit import/migration path for backups from Kotatsu, Usagi and Kototoro, and evaluate parser packages published at https://github.com/Shebyyy/kotatsu-multi-parsers/releases.

## Important compatibility distinction
A backup is user data; a parser JAR is executable code. Importing a backup does not install its sources, and loading parsers does not convert a backup. File suffix changes do not create compatibility. Do not silently execute JARs found in a backup.

The linked repository README says it automatically builds parser JARs from multiple Kotatsu-based repositories. It lists Kotatsu-Redo.jar, Gekkoushi.jar, glitch-228.jar, hany18h.jar and skepsun.jar (the latter from kototoro-parsers). This establishes availability of artifacts, not ShinKu ABI compatibility or backup support. It does not identify a Usagi backup schema.

Sources:
- https://github.com/Shebyyy/kotatsu-multi-parsers
- https://raw.githubusercontent.com/Shebyyy/kotatsu-multi-parsers/main/README.md
- https://github.com/Shebyyy/kotatsu-multi-parsers/releases

## Phase A: backup import feasibility
- Identify exact repository, app version and backup schema for each app, particularly the intended Usagi fork; obtain small synthetic fixtures, not private libraries.
- Detect actual container/schema/version before import. Reject unsupported versions with an actionable explanation.
- Map library entries, canonical URLs/source identities, categories, read/bookmark state, reading progress and history where representable. Explicitly list unsupported settings/content rather than claiming lossless migration.
- Source identifiers may differ; preserve unresolved entries and offer a source mapping/migration UI. Do not match by title alone.
- Preview counts and conflicts; define merge/idempotency rules so a repeated import does not duplicate or erase data.
- Use bounded decompression/parsing/staging and batch persistence to avoid reproducing the large-backup OOM. Include cancellation and accurate partial-result reporting.
- For archives, reject path traversal and impose entry-count, decompressed-size and compression-ratio protections.

## Phase B: parser JAR feasibility (separate engineering/security decision)
- Inspect actual artifact contents before choosing a runtime path. A JAR may contain JVM bytecode or Android-compatible dex; its extension alone does not establish loadability.
- Compare parser interfaces, dependency versions, entry points, source metadata and Android runtime requirements with ShinKu's current source-extension contracts.
- Evaluate an adapter or build-time conversion/packaging only if APIs and licenses permit. Ordinary JVM class files are not automatically Android dex extensions.
- Require explicit trust decisions and provenance verification. A hash published alongside an artifact helps integrity checking but does not alone establish a trusted publisher.
- A ClassLoader is not a security sandbox. Do not grant arbitrary untrusted parser code access by treating it as passive library data.
- Document network permissions, dependency conflicts, updates, source-ID collisions and failure isolation.

## Acceptance criteria
1. Publish a versioned compatibility matrix: supported / partial / unsupported, with reasons.
2. Successful synthetic fixture imports for each claimed app/version, including unresolved sources and repeated imports.
3. Report every omitted/converted field before user confirmation.
4. Demonstrate bounded-memory handling on constrained hardware and verify database results.
5. Keep backup import independently usable if JAR loading is infeasible or rejected.

No compatibility implementation, device validation, or speedup is claimed by this request. Existing broad roadmap issues #12/#13 should be cross-referenced by maintainers if relevant rather than assumed to implement this request.
