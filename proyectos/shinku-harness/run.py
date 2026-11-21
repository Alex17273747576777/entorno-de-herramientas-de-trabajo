#!/usr/bin/env python3
"""Compile the actual decoder with synthetic models; no Android integration is implied."""
from pathlib import Path
import hashlib
import os
import subprocess
import sys
import tempfile
import urllib.request

HERE = Path(__file__).resolve().parent
DECODER = (Path(sys.argv[1]) if len(sys.argv) == 2 else
           HERE.parents[2] / 'shinku/app/src/main/java/com/shinku/reader/data/backup/BackupStreamDecoder.kt')
ARTIFACTS = [
 ('org/jetbrains', 'annotations', '13.0'),
 ('org/jetbrains/kotlin', 'kotlin-compiler-embeddable', '1.9.24'),
 ('org/jetbrains/kotlin', 'kotlin-reflect', '1.6.10'),
 ('org/jetbrains/kotlin', 'kotlin-script-runtime', '1.9.24'),
 ('org/jetbrains/kotlin', 'kotlin-serialization-compiler-plugin-embeddable', '1.9.24'),
 ('org/jetbrains/kotlin', 'kotlin-stdlib', '1.9.24'),
 ('org/jetbrains/kotlinx', 'kotlinx-serialization-core-jvm', '1.6.3'),
 ('org/jetbrains/kotlinx', 'kotlinx-serialization-protobuf-jvm', '1.6.3'),
 ('com/squareup/okio', 'okio-jvm', '3.9.0'),
 ('org/jetbrains/intellij/deps', 'trove4j', '1.0.20200330'),
]

def main():
    if not DECODER.is_file():
        raise SystemExit('Pass the path to BackupStreamDecoder.kt as the sole argument')
    expected = dict(line.split() for line in (HERE / 'dependencies.sha256').read_text().splitlines())
    expected = {name: digest for digest, name in expected.items()}
    with tempfile.TemporaryDirectory(prefix='shinku-test-') as temp:
        tmp = Path(temp)
        jars = []
        for group, artifact, version in ARTIFACTS:
            name = f'{artifact}-{version}.jar'
            url = f'https://repo.maven.apache.org/maven2/{group}/{artifact}/{version}/{name}'
            data = urllib.request.urlopen(url, timeout=90).read()
            if hashlib.sha256(data).hexdigest() != expected[name]:
                raise ValueError(f'Unexpected hash for {name}; aborting')
            jar = tmp / name
            jar.write_bytes(data)
            jars.append(jar)
        cp = os.pathsep.join(map(str, jars))
        output = tmp / 'check.jar'
        plugin = tmp / 'kotlin-serialization-compiler-plugin-embeddable-1.9.24.jar'
        subprocess.run(['java', '-cp', cp, 'org.jetbrains.kotlin.cli.jvm.K2JVMCompiler',
                        '-no-stdlib', '-no-reflect', '-classpath', cp, f'-Xplugin={plugin}',
                        '-d', str(output), str(HERE / 'Models.kt'), str(HERE / 'Test.kt'),
                        str(DECODER)], check=True)
        subprocess.run(['java', '-cp', str(output) + os.pathsep + cp,
                        'com.shinku.reader.data.backup.TestKt'], check=True)

if __name__ == '__main__':
    main()
