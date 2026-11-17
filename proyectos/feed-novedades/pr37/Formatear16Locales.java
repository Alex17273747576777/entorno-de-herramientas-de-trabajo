import java.nio.file.*; import java.util.*;
public class Prueba {
  public static void main(String[] a) throws Exception {
    String json = Files.readString(Path.of("/tmp/cadenas.json"));
    int fallos = 0, ok = 0;
    // parseo mínimo del JSON plano {"tag":"cadena", ...}
    java.util.regex.Matcher m = java.util.regex.Pattern
        .compile("\"([^\"]+)\":\\s*\"((?:[^\"\\\\]|\\\\.)*)\"", java.util.regex.Pattern.DOTALL).matcher(json);
    while (m.find()) {
      String tag = m.group(1);
      String cad = m.group(2).replace("\\n","\n").replace("\\\"","\"").replace("\\\\","\\");
      Locale loc = Locale.forLanguageTag(tag);
      int tope = 25;
      String salida;
      try { salida = String.format(loc, cad, tope); }
      catch (Exception e) { System.out.println("  FALLO al formatear " + tag + ": " + e); fallos++; continue; }
      // el número formateado en ese locale, para comparar con lo que debe aparecer
      String esperado = String.format(loc, "%d", tope);
      boolean bien = !salida.contains("%1$d") && salida.contains(esperado);
      if (!bien) fallos++; else ok++;
      System.out.printf("  %s %-6s %s%n      → %s%n", bien ? "OK  " : "FALLO", tag, esperado, salida);
    }
    System.out.printf("%nRESULTADO: %d cadenas forman bien el número, %d fallos%n", ok, fallos);
    System.exit(fallos == 0 ? 0 : 1);
  }
}
