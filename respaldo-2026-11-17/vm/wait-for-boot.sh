#!/usr/bin/env bash
set -u
source /home/user/work/vm/env.sh
OUT=/home/user/work/vm/evidence/arranque.txt
: > "$OUT"
for i in $(seq 1 120); do
  ESTADO=$(adb get-state 2>&1 || true)
  BOOT=$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r' || true)
  ANIM=$(adb shell getprop init.svc.bootanim 2>/dev/null | tr -d '\r' || true)
  printf '%s · intento %s · state=%s · boot_completed=%s · bootanim=%s\n' "$(date -Is)" "$i" "$ESTADO" "${BOOT:-?}" "${ANIM:-?}" | tee -a "$OUT"
  if [ "$BOOT" = "1" ]; then
    {
      echo 'ARRANQUE_VM_COMPLETO'
      adb shell getprop ro.build.version.release
      adb shell getprop ro.build.version.sdk
      adb shell getprop ro.product.cpu.abi
      adb shell getprop ro.product.model
      adb shell cat /proc/meminfo | head -n 3
    } | tee -a "$OUT"
    exit 0
  fi
  sleep 10
done
echo 'ARRANQUE_VM_NO_COMPLETADO_EN_20_MINUTOS' | tee -a "$OUT"
exit 1
