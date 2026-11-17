#!/usr/bin/env bash
set -euo pipefail
EVID=/home/user/work/vm/evidence
SDK=/home/user/.local/share/cerox-android-sdk
DL=/home/user/.local/share/cerox-vm-downloads
export ANDROID_AVD_HOME=/home/user/.local/share/cerox-avd
export ANDROID_USER_HOME=/home/user/.local/share/cerox-android-user
mkdir -p "$EVID" "$SDK/cmdline-tools" "$DL" "$ANDROID_AVD_HOME" "$ANDROID_USER_HOME"
{
  date -Is
  uname -a
  if [ -e /dev/kvm ]; then ls -l /dev/kvm; else echo '/dev/kvm: NO EXISTE'; fi
  printf 'flags vmx/svm: '; (grep -oE '\b(vmx|svm)\b' /proc/cpuinfo || true) | sort -u | wc -l
  free -h
  df -h /home/user
} | tee "$EVID/hardware-antes.txt"

echo '== Instalar QEMU, ADB, JDK y utilidades =='
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get install -y --no-install-recommends qemu-system-x86 qemu-utils adb openjdk-21-jdk-headless curl unzip xz-utils util-linux libpulse0 libgl1 libegl1 libx11-6 libxcb1 libxext6 libxrender1 libxtst6 libxi6 libfreetype6 libfontconfig1 libnss3 libxkbcommon0 libxkbfile1
qemu-system-x86_64 --version | tee "$EVID/qemu-version.txt"
adb --version | tee "$EVID/adb-version.txt"

if ! sudo swapon --show=NAME --noheadings | grep -qx '/swapfile-cerox'; then
  echo '== Crear y activar 3 GiB de swap =='
  if [ ! -f /swapfile-cerox ]; then
    sudo fallocate -l 3G /swapfile-cerox || sudo dd if=/dev/zero of=/swapfile-cerox bs=1M count=3072 status=progress
    sudo chmod 600 /swapfile-cerox
    sudo mkswap /swapfile-cerox
  fi
  sudo swapon /swapfile-cerox
fi
free -h | tee "$EVID/memoria-con-swap.txt"
sudo swapon --show | tee "$EVID/swap-activo.txt"

export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export ANDROID_HOME="$SDK"
export PATH="$JAVA_HOME/bin:$SDK/cmdline-tools/latest/bin:$SDK/platform-tools:$SDK/emulator:$PATH"
java -version 2>&1 | tee "$EVID/java-version.txt"

if [ ! -x "$SDK/cmdline-tools/latest/bin/sdkmanager" ]; then
  echo '== Descargar Android command-line tools =='
  curl -fL --retry 3 'https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip' -o "$DL/android-cli.zip"
  rm -rf "$SDK/cmdline-tools/extract" "$SDK/cmdline-tools/latest"
  mkdir -p "$SDK/cmdline-tools/extract"
  unzip -q "$DL/android-cli.zip" -d "$SDK/cmdline-tools/extract"
  mv "$SDK/cmdline-tools/extract/cmdline-tools" "$SDK/cmdline-tools/latest"
fi

echo '== Instalar emulador e imagen Android 12 x86_64 =='
yes | sdkmanager --licenses >/dev/null || true
sdkmanager 'platform-tools' 'emulator' 'platforms;android-31' 'system-images;android-31;google_apis;x86_64'
emulator -version 2>&1 | tee "$EVID/emulator-version.txt"

if ! avdmanager list avd -c | grep -qx 'cerox_api31_x86_64'; then
  echo '== Crear AVD =='
  echo no | avdmanager create avd --force --name 'cerox_api31_x86_64' --package 'system-images;android-31;google_apis;x86_64' --device 'pixel_4'
fi
avdmanager list avd | tee "$EVID/avd-creado.txt"
cat > /home/user/work/vm/env.sh <<EOF
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export ANDROID_HOME=$SDK
export ANDROID_AVD_HOME=$ANDROID_AVD_HOME
export ANDROID_USER_HOME=$ANDROID_USER_HOME
export PATH=\"\$JAVA_HOME/bin:\$ANDROID_HOME/cmdline-tools/latest/bin:\$ANDROID_HOME/platform-tools:\$ANDROID_HOME/emulator:\$PATH\"
EOF

echo 'INSTALACION_VM_COMPLETA' | tee "$EVID/instalacion-completa.txt"
